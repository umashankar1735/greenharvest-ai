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
| LLM Backend   | [OpenAI GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5) & [Grok AI](https://x.ai/grok) |
| Agent Framework | Modular Python-based agents |
| DB            | SQLite (for user interaction logs) |
| Data Sources  | Local CSVs for farmers & market trends |
| Hosting       | Streamlit Community Cloud       |

---

## 📂 Code Structure
<pre> AgriGPT/ │ ├── agents/ │ ├── farmer_agent.py # Farmer info agent │ ├── weather_agent.py # Weather info agent │ ├── expert_agent.py # Agro expert agent │ ├── market_agent.py # Market data agent │ └── orchestrator.py # Multi-agent orchestrator │ ├── data/ │ ├── farmer_advisor_dataset.csv │ └── market_researcher_dataset.csv │ ├── utils/ │ ├── llm_utils.py # OpenAI LLM wrapper │ └── db_utils.py # SQLite DB logging │ ├── .streamlit/ │ └── secrets.toml # 🔒 OpenAI API key (not in GitHub) │ ├── app.py # Streamlit frontend UI ├── main.py # CLI for local testing ├── config.yaml # Optional future configs └── README.md # Project description </pre>


---

🧪 How to Run Locally – GreenHarvest AI
Follow these steps to set up and run the GreenHarvest AI app on your local machine.
✅ Prerequisites

- Python 3.9 or higher
- An GrokAI API key (from https://x.ai/grok)
- Git and pip installed

1️⃣ Clone the Repository

```bash
git clone https://github.com/umashankar1735/greenharvest-ai.git
cd greenharvest-ai
```

2️⃣ (Optional) Create and Activate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate         # On Windows
# OR
source venv/bin/activate       # On Mac/Linux
```

3️⃣ Install Required Dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Set Your OpenAI API Key
Create a file at `.streamlit/secrets.toml` and paste the following:
```bash
[general]
uma_shankar = "sk-your-openai-api-key"
```
⚠️ Replace with your actual API key. 🔒 Do not push this file to GitHub.

5️⃣ Run the Streamlit Web App
```bash
streamlit run app.py
```

Open the app in your browser at: http://localhost:8501

🧪 Run the CLI Version (Optional)
```bash
python main.py
```
🎬 Demo Screenshot
![image](https://github.com/user-attachments/assets/26b53ece-c926-4b31-b6e5-91b4b3c026a5)
![image](https://github.com/user-attachments/assets/6e7021ce-4103-4625-a9bc-a2a1b5e60ca3)
![image](https://github.com/user-attachments/assets/bf79e468-8ce1-428b-9db0-6dab39f1a9ea)

open in streamlit at: https://greenharvest-ai-dert6gb5xv7ajc2eoolxcc.streamlit.app/

✅ Future Enhancements
Integration with real-time APIs for weather and mandi data
Embedding-based retrieval using FAISS
Smart alert system for pest outbreaks
Mobile UI for low-bandwidth access

🤝 Contributors
Uma Shankar – AI Developer, Architect, Designer
Harshitha   – Web APP Developer, Designer
Supported by mentors and the community of Hackathon

📜 License
This project is licensed under the MIT License.
Use freely with attribution 🌱

💡 “Let’s empower farmers with AI. One field at a time.” — Team GreenHarvest AI
