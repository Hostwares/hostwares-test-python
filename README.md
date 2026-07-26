# Hostwares Test - Python Flask

A Flask 3.0 API for testing Python deployment on Hostwares.

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| APP_NAME | Display name | No |
| SECRET_KEY | Flask secret key | Yes |
| DATABASE_URL | PostgreSQL connection string | No |
| REDIS_URL | Redis connection URL | No |
| OPENAI_API_KEY | OpenAI API key (for AI features) | No |
| PORT | Server port (default: 8000) | No |

## Endpoints

- `GET /` — App info + env var status
- `GET /health` — Health check

## Deploy on Hostwares

1. Create a new site → select this repo
2. Set SECRET_KEY and any other env vars
3. Deploy! (uses Gunicorn with 2 workers)
