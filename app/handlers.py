"""
All bot handlers in one file.
"""

import logging

from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import Conversation, User, get_or_create_user_role
from app.services.openai_service import OpenAIService

logger = logging.getLogger(__name__)

# Create router
router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message, session: AsyncSession) -> None:
    """Handle /start command."""
    if not message.from_user:
        await message.answer(
            f"Hello! Welcome to {settings.project_name}, <b>Unknown</b>", parse_mode=ParseMode.HTML
        )
        return

    telegram_user = message.from_user

    # Get or create user
    stmt = select(User).where(User.telegram_id == telegram_user.id)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if user:
        # Update existing user
        user.username = telegram_user.username
        user.first_name = telegram_user.first_name
        user.last_name = telegram_user.last_name
        user.language_code = telegram_user.language_code
        logger.info(f"Updated user: {user.display_name}")
    else:
        # Create new user
        user = User(
            telegram_id=telegram_user.id,
            username=telegram_user.username,
            first_name=telegram_user.first_name,
            last_name=telegram_user.last_name,
            language_code=telegram_user.language_code,
        )
        session.add(user)
        logger.info(f"Created new user: {user.display_name}")

    await session.commit()

    # Send greeting
    greeting = f"Hello! Welcome to {settings.project_name}, 😎 <b>{user.display_name}</b>"
    await message.answer(greeting, parse_mode=ParseMode.HTML)


@router.message(Command("do"))
async def do_ai_handler(message: types.Message, session: AsyncSession) -> None:
    """Process user text through OpenAI API."""
    if not message.from_user:
        await message.reply("Authentication required")
        return

    # Extract text after /do command
    if not message.text:
        await message.reply("Usage: /do <your message>\nExample: /do Explain quantum physics")
        return

    text = message.text.replace("/do ", "", 1).strip()
    if not text:
        await message.reply("Usage: /do <your message>\nExample: /do Explain quantum physics")
        return

    # Get or create user
    telegram_user = message.from_user
    stmt = select(User).where(User.telegram_id == telegram_user.id)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        # Create new user if not exists
        user = User(
            telegram_id=telegram_user.id,
            username=telegram_user.username,
            first_name=telegram_user.first_name,
            last_name=telegram_user.last_name,
            language_code=telegram_user.language_code,
        )
        session.add(user)
        await session.commit()
        logger.info(f"Created new user for AI interaction: {user.display_name}")

    try:
        # Send typing indicator
        await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")

        # Get user role
        user_role = await get_or_create_user_role(session, user.id)

        # Initialize OpenAI service
        openai_service = OpenAIService()

        # Generate AI response
        ai_response, tokens = await openai_service.generate_response(
            user_message=text, role_prompt=user_role.role_prompt, model=settings.default_ai_model
        )

        # Save conversation to database
        conversation = Conversation(
            user_id=user.id,
            user_message=text,
            ai_response=ai_response,
            model_used=settings.default_ai_model,
            tokens_used=tokens,
            role_used=user_role.role_name,
        )
        session.add(conversation)
        await session.commit()

        # Send AI response to user
        await message.reply(ai_response, parse_mode=ParseMode.HTML)

        logger.info(f"AI response sent to {user.display_name}, tokens used: {tokens}")

    except ValueError as e:
        # User-friendly error (from our service)
        await message.reply(f"❌ {str(e)}")
        logger.warning(f"AI service error for {telegram_user.id}: {e}")

    except Exception as e:
        # Unexpected error
        await message.reply(
            "❌ Sorry, I'm having trouble processing your request. Please try again later."
        )
        logger.error(f"Unexpected error in AI handler: {e}")


@router.message(F.text)
async def default_handler(message: types.Message) -> None:
    """Handle all other text messages."""
    help_text = (
        f"Welcome to {settings.project_name}! 🤖\n\n"
        "Available commands:\n"
        "• /start - Get a greeting\n"
        "• /do <message> - Chat with AI\n\n"
        "Example: /do Explain quantum physics"
    )
    await message.answer(help_text)

    if message.from_user:
        logger.info(
            f"Received message from {message.from_user.username or message.from_user.first_name}"
        )
