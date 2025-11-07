# Assignment 11: AI Agent for Weather & Search Queries

🤖 A Langchain-based AI agent that handles real-time weather and web search queries using OpenWeather and Tavily APIs.

## 🚀 Features

- **Smart Tool Routing**: Automatically routes queries to appropriate tools
- **Weather Data**: Real-time weather information via OpenWeatherMap API
- **Web Search**: Current information via Tavily Search API
- **Interactive Interface**: Both Python script and Jupyter Notebook versions
- **Conversation History**: Maintains context across interactions

## 📋 Requirements

```bash
pip install langchain-openai langchain-community langchain-tavily langgraph pyowm langchain tiktoken requests
```

## 🔑 API Keys Required

- **Azure OpenAI**: Endpoint, API key, deployment name
- **OpenWeatherMap**: API key from [openweathermap.org](https://openweathermap.org/api)
- **Tavily**: API key from [tavily.com](https://app.tavily.com/)

## 🛠️ Usage

### Python Script Version
```bash
python Assignment_11.py
```

### Jupyter Notebook Version
```bash
jupyter notebook Assignment_11.ipynb
```

## 📝 Configuration

1. Open either `Assignment_11.py` or `Assignment_11.ipynb`
2. Update the `setup_environment()` function with your API keys:
```python
os.environ["AZURE_OPENAI_ENDPOINT"] = "your_endpoint"
os.environ["AZURE_OPENAI_API_KEY"] = "your_key"
os.environ["OPENWEATHERMAP_API_KEY"] = "your_key"  
os.environ["TAVILY_API_KEY"] = "your_key"
```

## 🎯 Example Queries

- **Weather**: "What's the weather in Hanoi?"
- **Search**: "Tell me about the latest AI developments"
- **General**: "Who won the last World Cup?"

## 🏗️ Architecture

- **LangChain Agent**: ReAct pattern for tool selection
- **Custom Tools**: Weather tool with @tool decorator
- **API Integration**: OpenWeather + Tavily APIs
- **Error Handling**: Graceful failure management

## ✅ Concepts Covered

- ✅ Langchain tools and agent setup
- ✅ API integration for OpenWeather and Tavily Search  
- ✅ Tool routing and decision-making within Langchain agents
- ✅ Interactive agent loop simulation in Jupyter Notebook

---

**Author**: HaoPQ1  
**Date**: November 7, 2025