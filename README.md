🍎 Nutrition Copilot – Agentic AI Chatbot
<div align="center">






A production-ready multi-agent chatbot for personalized nutrition planning, calorie tracking, and meal pricing — powered by OpenAI’s Agents SDK.

Live Demo
 • Architecture
 • Features
 • Setup

</div>
🎯 Overview

Nutrition Copilot is an intelligent, agentic chatbot designed to deliver personalized dietary advice, calorie insights, and cost estimates.
It leverages multi-agent orchestration, Retrieval-Augmented Generation (RAG) with ChromaDB, and real-time web search through Model Context Protocol (MCP).

Key Highlights

🤖 Multi-agent workflow with intelligent handoffs

📊 RAG using ChromaDB for 8,789+ food items

🌍 Real-time data retrieval for calorie and price lookups

🧠 Persistent session memory via SQLite

⚙️ One-click GitHub Codespaces setup

🔒 Input guardrails and structured outputs

💬 Beautiful Chainlit chat interface

🏗️ Architecture

The system follows a hierarchical multi-agent structure, where specialized agents collaborate to produce context-aware responses.

Agent Workflow
🛡️ Input Guardrail Agent

Validates that inputs are food-related and safe before further processing.

🎯 Orchestrator (Main Controller)

Coordinates the workflow, routes queries, and maintains conversational memory.

🍳 Breakfast Planner Agent

Suggests nutritious breakfast options tailored to user preferences and calorie limits.

🔢 Calorie Calculator Agent

Uses RAG over ChromaDB to compute precise calorie values; falls back to web search when data is missing.

💰 Price Checker Agent

Fetches real-time prices for ingredients and provides cost-per-meal breakdowns.

⚙️ Tech Stack
Component	Technology
AI Framework	OpenAI Agents SDK (GPT-4)
Frontend	Chainlit
Vector Database	ChromaDB
Web Search	Exa Search (MCP)
Memory	SQLite
Environment	GitHub Codespaces
Deployment	Render.com
Language	Python 3.11+
Libraries	Pandas, Chainlit, OpenAI
✨ Features
🤝 Multi-Agent Collaboration

Agents communicate and delegate tasks seamlessly to ensure accurate, contextual responses.

📚 RAG-Based Knowledge Retrieval

The system indexes over 8,000 nutrition entries for efficient ingredient and calorie lookup.

🌍 Real-Time Web Augmentation

Integrates live data for ingredient prices and nutrition facts using MCP.

💬 Production-Ready Chat UI

Provides a modern Chainlit interface with real-time streaming, chat persistence, and authentication.

🛡️ Guardrails & Safety

Ensures queries are relevant, avoids hallucinations, and enforces structured, verifiable outputs.

🚀 Setup & Development (GitHub Codespaces)

Fastest way to get started — fully preconfigured development environment.

Fork this repository on GitHub.

Click the green “Code” button → Select Codespaces tab → Create codespace on main.

Wait 2–3 minutes for Codespaces to build the container and install dependencies automatically.

Create a .env file in the project root:

touch .env


Add your credentials:

OPENAI_API_KEY=your_openai_key_here
EXA_API_KEY=your_exa_key_here
CHAINLIT_USERNAME=admin
CHAINLIT_PASSWORD=your_secure_password


Initialize the ChromaDB nutrition dataset:

python chatbot/rag_setup.py


Run the application:

chainlit run chatbot/breakfast_chatbot.py --port 10000


Access the app:

Codespaces will auto-open your default browser at the forwarded port.

You can also open it manually from the “Ports” tab → Port 10000.

Log in using credentials defined in your .env.

📁 Project Structure
nutrition-copilot-agentic-chatbot/
├── chatbot/
│   ├── .chainlit/
│   │   └── config.toml              # Chainlit configuration
│   ├── public/
│   │   └── logo.png                 # Application logo
│   ├── breakfast_chatbot.py         # Main Chainlit application
│   ├── nutrition_agent.py           # Multi-agent system definitions
│   ├── rag_setup.py                 # ChromaDB initialization script
│   └── chainlit.md                  # Welcome message (optional)
├── data/
│   └── calories.csv                 # Nutrition database (8,789 items)
├── chroma/                          # Vector database storage
│   └── chroma.sqlite3               # ChromaDB persistence
├── .env                             # Environment variables (gitignored)
├── .env.example                     # Environment template
├── .gitignore                       # Git ignore rules
├── requirements.txt                 # Python dependencies
└── README.md


Codespaces Environment Includes:

Python 3.11+, Pandas, ChromaDB, Chainlit

Pre-installed VS Code extensions (Python, Jupyter, Copilot)

Port 10000 auto-forwarded for Chainlit UI

🔧 Usage Example
🍳 Breakfast Planning (User Preferences: Eggs + Fruits)
User: Plan a healthy breakfast with eggs and fruits under 400 calories.
Assistant:
[Agents: Planner → Calorie Calculator → Price Checker]

**1. Scrambled Eggs with Apple Slices** – 385 cal | ~$3.80  
• Scrambled eggs (2 large): 180 cal | $1.10  
• Apple (150g): 78 cal | $1.20  
• Whole-grain toast (1 slice): 127 cal | $1.50  
Balanced breakfast with protein, fiber, and natural sugar.

🚀 Deployment (Render.com)

Push the repository to GitHub.

Create a new Web Service on Render
.

Connect your GitHub repo.

Add environment variables (OPENAI_API_KEY, EXA_API_KEY, CHAINLIT_USERNAME, CHAINLIT_PASSWORD).

Use the following Start Command:

chainlit run chatbot/breakfast_chatbot.py --port $PORT --host 0.0.0.0


Click Deploy — your AI nutrition chatbot is live! 🎉

🧠 Key Learnings

Implementing agentic orchestration and tool handoffs

Building a RAG pipeline with ChromaDB

Integrating Model Context Protocol for external web data

Deploying Chainlit-based AI systems on Render

Designing guardrails and context retention for production AI

🤝 Contributing

Contributions are welcome!

Fork the repository

Create a new branch (git checkout -b feature/update)

Commit and push your changes

Open a Pull Request

📧 Contact

Joel Franklin
AI Engineer




<div align="center">

⭐ If you found this project useful, please give it a star!
Built with ❤️ by Joel Franklin

</div>
