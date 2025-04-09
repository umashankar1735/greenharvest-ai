# 🌾 GreenHarvest AI – AgriGPT (Multi-Agent Farming Advisor)

GreenHarvest AI is a **GenAI-powered multi-agent system** that helps farmers make sustainable, data-driven decisions by integrating insights from weather forecasts, agro-expert systems, market trends, and LLM-generated advice.

> 🚀 **Live Demo**: [greenharvest-ai.streamlit.app](https://greenharvest-ai-dert6gb5xv7ajc2eoolxcc.streamlit.app/)  
> 📦 **GitHub Repo**: [github.com/umashankar1735/greenharvest-ai](https://github.com/umashankar1735/greenharvest-ai.git)

---

## 🧠 Key Features

- 🤖 **Multi-Agent System**: Combines farmer input, expert advice, weather data, and market insights
- 🌦️ **Weather Insights**: Provides season-based weather outlook
- 🌱 **Agro Expert Agent**: Fertilizer and irrigation recommendations by soil type and crop
- 📈 **Market Intelligence Agent**: Real-time commodity pricing & sale suggestions
- 🧾 **LLM-Based Advisory**: GPT-generated final recommendations in simple farmer-friendly language
- 💾 **SQLite DB Logging**: Tracks each interaction and logs it for transparency
- 🌐 **Streamlit Web Interface**: Easy-to-use dashboard for farmers and researchers

---

## 🔧 Tech Stack

| Layer         | Technology                      |
|---------------|----------------------------------|
| UI            | [Streamlit](https://streamlit.io)                    |
| LLM Backend   | [OpenAI GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5) [Grok AI](https://x.ai/grok) |
| Agent Framework | Modular Python-based agents |
| DB            | SQLite (for user interaction logs) |
| Data Sources  | Local CSVs for farmers & market trends |
| Hosting       | Streamlit Community Cloud       |

---

## 📂 Code Structure
<pre> AgriGPT/ │ ├── agents/ │ ├── farmer_agent.py # Farmer info agent │ ├── weather_agent.py # Weather info agent │ ├── expert_agent.py # Agro expert agent │ ├── market_agent.py # Market data agent │ └── orchestrator.py # Multi-agent orchestrator │ ├── data/ │ ├── farmer_advisor_dataset.csv │ └── market_researcher_dataset.csv │ ├── utils/ │ ├── llm_utils.py # OpenAI LLM wrapper │ └── db_utils.py # SQLite DB logging │ ├── .streamlit/ │ └── secrets.toml # 🔒 OpenAI API key (not in GitHub) │ ├── app.py # Streamlit frontend UI ├── main.py # CLI for local testing ├── config.yaml # Optional future configs └── README.md # Project description </pre>


---

## 🧪 How to Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/umashankar1735/greenharvest-ai.git
cd greenharvest-ai



