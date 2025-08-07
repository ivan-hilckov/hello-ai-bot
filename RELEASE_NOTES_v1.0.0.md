# Hello AI Bot v1.0.0 - Stable Release 🎉

## 🚀 Production-Ready AI Telegram Bot

**Hello AI Bot v1.0.0** is the first stable release of a production-ready Telegram bot with full OpenAI integration. This represents the evolution from Hello Bot (HB-001) to a complete AI-powered conversational bot.

## 🎯 Key Features

### ✅ **Full OpenAI Integration**
- **GPT-3.5/GPT-4 Support**: Choose between models for cost vs quality optimization
- **`/do` Command**: Natural conversation interface with AI assistant
- **Token Tracking**: Comprehensive cost monitoring and usage analytics
- **Error Handling**: Graceful API failure management with user-friendly messages

### ✅ **Role-Based Conversations**
- **Customizable AI Personalities**: Set context and behavior for specialized use cases
- **Conversation Context**: Maintains role consistency across interactions
- **Predefined Roles**: Built-in templates for common AI assistant types

### ✅ **Production Deployment**
- **One-Command Deploy**: `git push origin main` → automatic VPS deployment
- **GitHub Actions CI/CD**: Automated testing, building, and deployment
- **Shared PostgreSQL**: Resource-optimized database architecture
- **Health Monitoring**: Automatic health checks and recovery procedures

### ✅ **Enterprise-Grade Quality**
- **Exception Handling**: Proper error chaining and comprehensive logging
- **Security**: Environment-based secrets, database isolation, input validation
- **Rate Limiting**: Built-in cost control and abuse prevention
- **Resource Optimization**: Runs efficiently on 2GB VPS (150MB per bot)

## 📊 Performance Specifications

| Metric | Specification |
|--------|---------------|
| **Memory Usage** | 150MB per bot instance |
| **Database** | 512MB shared PostgreSQL (supports 10+ bots) |
| **Response Time** | <500ms for typical AI queries |
| **Deployment** | <2 minutes via GitHub Actions |
| **VPS Requirements** | 2GB RAM supports 10+ bot instances |

## 🛠 Technology Stack

### Core Framework
- **Python 3.12+** with full async support and comprehensive type hints
- **aiogram 3.0+** modern Telegram Bot framework with Router pattern
- **OpenAI API** with tiktoken for accurate token counting and cost estimation
- **PostgreSQL 15** with SQLAlchemy 2.0 async for type-safe database operations

### Infrastructure
- **Docker + Compose** for consistent development and production environments
- **GitHub Actions** for automated CI/CD pipeline
- **FastAPI** for optional webhook mode (polling mode default)
- **Shared Database Architecture** for cost-effective multi-bot deployments

### Development Tools
- **uv** ultra-fast Python package manager
- **ruff** lightning-fast code formatting and linting
- **pytest** comprehensive testing framework
- **Pydantic** data validation and settings management

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone https://github.com/ivan-hilckov/hello-ai-bot
cd hello-ai-bot
uv sync
cp .env.example .env
```

### 2. Configure Tokens
Add to `.env`:
```env
BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=sk-your-openai-api-key-here
DB_PASSWORD=secure_dev_password
```

### 3. Start Development
```bash
docker compose -f docker-compose.dev.yml up -d
docker compose -f docker-compose.dev.yml logs -f bot-dev
```

### 4. Test Your AI Bot
- Send `/start` → get personalized greeting
- Send `/do Tell me a joke` → AI responds with humor
- Send `/do Write a Python function to reverse a string` → get code examples

## 🤖 Bot Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Initialize user and get greeting | `/start` |
| `/do <message>` | Send message to AI assistant | `/do Explain quantum physics simply` |

## 🏗 Architecture Highlights

### AI Processing Flow
```
User Message → Telegram API → aiogram Router → AI Handler
                                                    ↓
Database Session ← User Role ← OpenAI Service ← Message Processing
    ↓              ↓              ↓              ↓
Conversation Log → Token Count → AI Response → User Response
```

### Database Schema
- **`users`**: User profiles and settings
- **`user_roles`**: AI role preferences per user  
- **`conversations`**: Complete chat history with token usage tracking

## 🔧 Production Deployment

### Required GitHub Secrets
Configure in repository: **Settings → Secrets and variables → Actions**

#### VPS Connection
- `VPS_HOST` - Server IP address
- `VPS_USER` - SSH username  
- `VPS_SSH_KEY` - Private SSH key content
- `VPS_PORT` - SSH port (default: 22)

#### Docker Registry
- `DOCKERHUB_USERNAME` - Docker Hub username
- `DOCKERHUB_TOKEN` - Docker Hub access token

#### Application Secrets
- `BOT_TOKEN` - Telegram bot token from @BotFather
- `OPENAI_API_KEY` - OpenAI API key
- `DB_PASSWORD` - Database password
- `POSTGRES_ADMIN_PASSWORD` - PostgreSQL admin password

### Deploy to Production
```bash
git push origin main  # Automatic deployment to VPS
```

## 📈 Bot Evolution History

This release represents the systematic evolution from Hello Bot foundation:

- **HB-001**: [Hello Bot Template](https://github.com/ivan-hilckov/hello-bot) - Simple greeting bot with database
- **HB-002**: **Hello AI Bot v1.0.0** - Complete OpenAI integration with role system and conversation management

### Evolution Features Added
- ✅ OpenAI GPT-3.5/GPT-4 integration
- ✅ AI conversation handling via `/do` command
- ✅ Role-based conversation system
- ✅ Comprehensive conversation history with token tracking
- ✅ Production-grade exception handling with proper chaining
- ✅ Rate limiting and cost management
- ✅ Shared PostgreSQL architecture for efficiency
- ✅ Automated GitHub Actions deployment pipeline

## 🔒 Security & Best Practices

- **No Hardcoded Secrets**: All sensitive data via environment variables
- **Exception Chaining**: Proper error handling with `raise ... from e` pattern
- **Input Validation**: Pydantic models for configuration validation
- **Resource Limits**: Memory and connection limits to prevent exhaustion
- **Database Security**: Separate users and databases per bot instance

## 🎯 Use Cases

### Perfect For
- **AI Assistants**: Customer support, educational bots, creative assistants
- **Business Automation**: Query processing, content generation, data analysis
- **Learning Projects**: Understanding modern Python async patterns and AI integration
- **MVP Development**: Rapid prototyping of AI-powered Telegram applications

### Scaling Considerations
- **Small to Medium**: <1,000 daily active users per bot
- **Resource Efficient**: 10+ bots on single 2GB VPS
- **Cost Effective**: Shared infrastructure reduces operational costs
- **Growth Ready**: Can scale up with additional enterprise patterns when needed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make changes with proper exception handling
4. Ensure `uv run ruff check .` passes without errors
5. Test AI functionality thoroughly
6. Commit changes (`git commit -m 'Add amazing feature'`)
7. Push to branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🔗 Links

- **Repository**: https://github.com/ivan-hilckov/hello-ai-bot
- **Documentation**: Complete guides in `/docs` directory
- **Parent Template**: [Hello Bot (HB-001)](https://github.com/ivan-hilckov/hello-bot)
- **OpenAI Platform**: https://platform.openai.com/
- **Telegram Bot API**: https://core.telegram.org/bots/api

---

**🎉 Hello AI Bot v1.0.0 - Production-ready AI for everyone!**

*Built with ❤️ for the AI era through human-AI collaboration*
