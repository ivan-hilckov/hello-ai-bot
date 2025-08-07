# Create New Telegram Bot from Hello Bot Template

You are helping create a new Telegram bot based on the Hello Bot template. This template uses a simplified architecture (~320 lines) optimized for rapid development and AI collaboration.

## Bot Specification

**English Teacher Bot - Completed Analysis**

### Basic Information
- **Bot Name**: English Teacher Bot
- **Bot Username**: @english_teacher_bot (to be created via @BotFather)
- **Description**: AI-powered English tutor that corrects grammar/spelling errors and translates text to English with detailed explanations
- **Bot ID**: HB-003 (third bot in Hello Bot genealogy after hello-ai-bot v1.0.0)

### Core Functionality
**Primary Features** (1-3 main features):
1. **Error Correction**: Analyze English text and provide detailed correction tables with error types and explanations
2. **Translation**: Translate text from any language to natural English with language detection
3. **Learning Analytics**: Track user's correction history and English learning progress

**Commands**:
- `/start` - Welcome message explaining English teaching functionality and user registration
- `/do <text>` - Process text through AI English tutor for correction or translation
- Direct text messages - Automatically process any text for English improvement

### Technical Requirements
- **Database Tables**: User + UserRole + Conversation + CorrectionHistory (new table for tracking progress)
- **External APIs**: OpenAI GPT API for English tutoring intelligence
- **Special Dependencies**: tiktoken (token counting), openai (AI client) - already included in hello-ai-bot template
- **Deployment**: VPS alongside Hello Bot and hello-ai-bot using shared PostgreSQL architecture

## Development Roadmap

### Phase 1: Setup (30 minutes)
- [ ] Clone hello-ai-bot repository as english-teacher-bot
- [ ] Update project name to "english-teacher-bot" in all configs
- [ ] Configure English teacher-specific environment variables (SERVER_PORT=8001)
- [ ] Get new bot token from @BotFather for @english_teacher_bot
- [ ] Test basic deployment with shared PostgreSQL

### Phase 2: Core Features (2 hours)
- [ ] Add CorrectionHistory model to database.py for tracking learning progress
- [ ] Customize AI role prompt for English teaching in config.py
- [ ] Update start handler with English teacher welcome message
- [ ] Implement error correction table generation in AI responses
- [ ] Add language detection and translation functionality

### Phase 3: Enhancement (1 hour)
- [ ] Add user correction statistics and progress tracking
- [ ] Implement detailed error type classification (grammar, spelling, style)
- [ ] Optimize response formatting for correction tables
- [ ] Add comprehensive error handling for AI failures

### Phase 4: Production (30 minutes)
- [ ] Deploy to VPS with port 8001 (avoiding hello-ai-bot port 8000)
- [ ] Configure shared PostgreSQL with english-teacher-bot_db database
- [ ] Test production deployment with multiple bots running
- [ ] Update bot genealogy documentation in README

## Template Customization Checklist

### Required Changes (Must Do):
- [ ] **Project Name**: Update to "english-teacher-bot" in `app/config.py` and `.env` file
- [ ] **Repository Name**: Rename to "english-teacher-bot"
- [ ] **Bot Token**: Get new token from @BotFather for @english_teacher_bot
- [ ] **Database Name**: Update to "english-teacher-bot_db" in environment variables
- [ ] **README.md**: Update title to "English Teacher Bot", description, and features list
- [ ] **docker-compose.yml**: Update container names to english-teacher-bot and SERVER_PORT=8001

### Recommended Changes:
- [ ] **Handlers**: Update start handler with English teacher welcome message in `app/handlers.py`
- [ ] **AI Role**: Customize default_role_prompt for English tutoring in `app/config.py`
- [ ] **Models**: Add CorrectionHistory model for tracking learning progress
- [ ] **Tests**: Update tests for English correction and translation functionality

### Optional Changes:
- [ ] **Logging**: Add English teacher-specific log messages (corrections made, translations)
- [ ] **Error Messages**: Customize responses for language detection failures
- [ ] **Documentation**: Add English teaching methodology and correction examples

## AI Collaboration Instructions

When working with AI assistants on this bot:

### Context to Provide:
```
This is a Telegram bot built from Hello Bot template with simplified architecture:
- ~320 total lines of code across 5 main files
- Direct database operations (no service layer)
- Async SQLAlchemy 2.0 with PostgreSQL
- aiogram 3.0+ for Telegram API
- Simple middleware for database sessions
- Production deployment via Docker and GitHub Actions

Current bot purpose: AI-powered English tutor that corrects grammar errors and translates text
Target features: Error correction tables, translation, learning progress tracking
```

### Effective Prompts:
- "Generate detailed correction table showing Original | Error Type | Explanation | Correction"
- "Add language detection to translate non-English text to English"
- "Create CorrectionHistory model to track user's English learning progress"
- "Implement error type classification (grammar, spelling, style, vocabulary)"

### Architecture Constraints:
- Keep total codebase under 400 lines
- Use direct database operations in handlers
- No service layer or complex abstractions
- Simple error handling with standard logging
- One file per major component

## File Structure After Customization

```
english-teacher-bot/
├── app/
│   ├── config.py          # English teacher settings and AI role prompt
│   ├── database.py        # User + UserRole + Conversation + CorrectionHistory
│   ├── handlers.py        # English correction and translation handlers
│   ├── middleware.py      # Database middleware (unchanged)
│   ├── main.py           # Entry point with port 8001
│   └── services/
│       └── openai_service.py  # OpenAI integration (unchanged)
├── prompts/              # AI collaboration templates
├── tests/                # English correction and translation tests
├── docs/                 # English teaching methodology docs
└── README.md            # English Teacher Bot information
```

## Bot Genealogy

Add this to your new bot's README.md:

```markdown
## Bot Genealogy
- **Parent Template**: Hello AI Bot (HB-002)
- **Bot ID**: HB-003
- **Created**: 2024
- **Purpose**: AI-powered English tutor for grammar correction and translation
- **GitHub**: https://github.com/your-username/english-teacher-bot
```

## Success Criteria

Your bot is ready when:
- [ ] All tests pass (`uv run pytest tests/ -v`)
- [ ] Deploys successfully to VPS alongside hello-ai-bot (port 8001)
- [ ] English correction with detailed error tables works
- [ ] Translation from various languages to English works
- [ ] CorrectionHistory tracking saves user progress
- [ ] AI assistants can enhance English teaching features

## Example Implementation

For reference, here's how English Teacher Bot should be structured:

**Updated start handler in `app/handlers.py`:**
```python
@router.message(Command("start"))
async def start_handler(message: types.Message, session: AsyncSession) -> None:
    """English Teacher Bot welcome message."""
    greeting = (
        f"🎓 Welcome to <b>English Teacher Bot</b>, {user.display_name}!\n\n"
        f"📚 <b>What I can do:</b>\n"
        f"• Correct English grammar and spelling errors\n"
        f"• Translate text from any language to English\n"
        f"• Provide detailed error explanations\n\n"
        f"📋 <b>Commands:</b>\n"
        f"• /do <text> - Process text for correction/translation\n"
        f"• Just send any text - I'll automatically help!"
    )
    # Implementation here
```

**New model in `app/database.py`:**
```python
class CorrectionHistory(Base, TimestampMixin):
    """Track user's English correction history."""
    __tablename__ = "correction_history"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    original_text: Mapped[str] = mapped_column(Text)
    corrected_text: Mapped[str] = mapped_column(Text)
    error_count: Mapped[int] = mapped_column(Integer, default=0)
    correction_type: Mapped[str] = mapped_column(String(20))  # 'correction' or 'translation'
```

Now start building your bot! Use the other prompt templates in this directory for specific development tasks.