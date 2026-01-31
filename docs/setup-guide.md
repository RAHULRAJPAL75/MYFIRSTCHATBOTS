# Setup Guide

## Python Chatbot Setup

### 1. Simple Chatbot (No API Required)
```bash
cd python-chatbot
python chatbot.py
```

### 2. AI Chatbot (Requires OpenAI API)
1. Copy `.env.example` to `.env`
2. Add your OpenAI API key to `.env`
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python ai_chatbot.py`

## n8n Workflow Setup

### Installation
```bash
npm install -g n8n
```

### Running n8n
```bash
n8n start
```

### Importing Workflows
1. Open n8n in browser (usually http://localhost:5678)
2. Go to Workflows > Import from File
3. Select workflow JSON files from `n8n-workflows/` folder

### API Usage Examples

#### Chatbot Webhook
```bash
curl -X POST http://localhost:5678/webhook/chatbot \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, how are you?"}'
```

#### Content Creator Webhook
```bash
curl -X POST http://localhost:5678/webhook/content-creator \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "artificial intelligence",
    "content_type": "blog post",
    "audience": "developers",
    "tone": "professional"
  }'
```

## Environment Variables
Create `.env` file in `python-chatbot/` directory:
```
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```