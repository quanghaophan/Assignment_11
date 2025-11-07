"""
Assignment 11: AI Agent for Weather & Search Queries
Building a Langchain-based AI agent that handles real-time weather and web search queries.

Author: HaoPQ1
Date: November 6, 2025

Requirements:
- pip install langchain-openai langchain-community langchain-tavily langgraph pyowm

APIs Required:
- Azure OpenAI API
- OpenWeatherMap API
- Tavily Search API
"""

import os
from langchain.tools import tool
from langchain_openai import AzureChatOpenAI
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent

def setup_environment():
    """
    Setup API keys and environment variables.
    Replace empty strings with your actual API keys.
    """
    # Azure OpenAI Configuration
    os.environ["AZURE_OPENAI_ENDPOINT"] = ""  # Replace with your Azure OpenAI endpoint
    os.environ["AZURE_OPENAI_API_KEY"] = ""   # Replace with your Azure OpenAI API key
    os.environ["AZURE_DEPLOYMENT_NAME"] = "GPT-4o-mini"  # Replace with your deployment name
    
    # OpenWeatherMap API Configuration
    os.environ["OPENWEATHERMAP_API_KEY"] = ""  # Replace with your OpenWeatherMap API key
    
    # Tavily Search API Configuration
    os.environ["TAVILY_API_KEY"] = ""  # Replace with your Tavily API key
    
    print("Environment variables configured successfully!")

@tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a given city using OpenWeatherMap API.
    
    Args:
        city (str): The name of the city to get the weather for.
        
    Returns:
        str: A string describing the current weather in the specified city.
    """
    print(f"Get_weather tool calling: Getting weather for {city}")
    
    try:
        weather = OpenWeatherMapAPIWrapper()
        weather_info = weather.run(city)
        return f"Weather in {city}: {weather_info}"
    except Exception as e:
        return f"Sorry, I couldn't get the weather information for {city}. Error: {str(e)}"

def initialize_llm():
    """
    Initialize Azure OpenAI LLM with configuration.
    
    Returns:
        AzureChatOpenAI: Configured Azure OpenAI instance
    """
    try:
        llm = AzureChatOpenAI(
            azure_deployment=os.getenv("AZURE_DEPLOYMENT_NAME"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version="2024-07-01-preview",
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        )
        print("Azure OpenAI LLM initialized successfully!")
        return llm
    except Exception as e:
        print(f"Error initializing Azure OpenAI: {str(e)}")
        return None

def initialize_tavily_search():
    """
    Initialize Tavily search tool for web searches.
    
    Returns:
        TavilySearch: Configured Tavily search instance
    """
    try:
        tavily_search_tool = TavilySearch(
            max_results=3,  # Increased for better search results
            topic="general",
        )
        print("Tavily Search tool initialized successfully!")
        return tavily_search_tool
    except Exception as e:
        print(f"Error initializing Tavily Search: {str(e)}")
        return None

def create_ai_agent(llm, tools):
    """
    Create a Langchain agent with the provided LLM and tools.
    
    Args:
        llm: The language model instance
        tools: List of tools available to the agent
        
    Returns:
        Agent: Configured Langchain agent
    """
    try:
        agent = create_react_agent(
            model=llm,
            tools=tools,
        )
        print("AI Agent created successfully!")
        return agent
    except Exception as e:
        print(f"Error creating AI agent: {str(e)}")
        return None

def run_conversation_simulation():
    """
    Main function to run the AI agent conversation simulation.
    """
    print("=" * 60)
    print("Starting AI Agent for Weather & Search Queries")
    print("=" * 60)
    
    # Step 1: Setup environment
    setup_environment()
    print()
    
    # Step 2: Initialize LLM
    llm = initialize_llm()
    if not llm:
        print("Cannot proceed without LLM. Please check your Azure OpenAI configuration.")
        return
    print()
    
    # Step 3: Initialize Tavily search tool
    tavily_search_tool = initialize_tavily_search()
    if not tavily_search_tool:
        print("Warning: Tavily search tool not available. Only weather queries will work.")
        tools = [get_weather]
    else:
        tools = [get_weather, tavily_search_tool]
    print()
    
    # Step 4: Create AI agent
    agent = create_ai_agent(llm, tools)
    if not agent:
        print("Cannot proceed without agent. Please check your configuration.")
        return
    print()
    
    # Step 5: Run conversation simulation
    print("Welcome to the AI Assistant!")
    print("This agent can help you with:")
    print("- Weather information for any city")
    print("- Web searches for current information")
    print("-" * 40)
    
    # Mock user questions for automatic input (as requested - no manual input)
    mock_questions = [
        "What's the weather in Hanoi?",
        "What's the weather in Quy Nhon tonight?",
        "Tell me about the latest news in AI.",
        "Search for the latest developments in machine learning.",
        "Who won the last World Cup?",
        "What's the current weather in New York?",
        "exit",
    ]
    
    messages = []
    
    try:
        for i, user_input in enumerate(mock_questions, 1):
            print(f"\nQuery {i}:")
            print(f"User: {user_input}")
            
            if user_input.lower() == "exit":
                print("Goodbye! Thank you for using the AI Assistant!")
                break
            
            # Add user message to conversation history
            messages.append({"role": "user", "content": user_input})
            
            try:
                # Get agent response
                print("AI is thinking...")
                response = agent.invoke({"messages": messages})
                
                # Extract and display AI response
                ai_response = response["messages"][-1].content
                messages.append({"role": "assistant", "content": ai_response})
                
                print(f"AI: {ai_response}")
                
            except Exception as e:
                error_message = f"Sorry, I encountered an error processing your request: {str(e)}"
                print(f"AI: {error_message}")
                messages.append({"role": "assistant", "content": error_message})
            
            print("-" * 50)
            
    except KeyboardInterrupt:
        print("\n\nSession interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")

def print_setup_instructions():
    """
    Print setup instructions for the user.
    """
    print("\n" + "=" * 60)
    print("SETUP INSTRUCTIONS")
    print("=" * 60)
    print("Before running this script, you need to:")
    print()
    print("1. Install required packages:")
    print("   pip install langchain-openai langchain-community langchain-tavily langgraph pyowm")
    print()
    print("2. Get API keys from:")
    print("   - Azure OpenAI: https://azure.microsoft.com/en-us/products/ai-services/openai-service")
    print("   - OpenWeatherMap: https://openweathermap.org/api")
    print("   - Tavily: https://app.tavily.com/")
    print()
    print("3. Set your API keys in the setup_environment() function")
    print()
    print("4. Run the script: python Assignment_11.py")
    print("=" * 60)

if __name__ == "__main__":
    # Print setup instructions
    # print_setup_instructions()

    # Run the main conversation simulation
    run_conversation_simulation()
    
    print("\n" + "=" * 60)
    print("Key Features Implemented:")
    print("   - Langchain-based AI agent")
    print("   - OpenWeather API integration")
    print("   - Tavily Search API integration")
    print("   - Tool routing and decision-making")
    print("   - Conversation simulation with automatic input")
    print("   - Error handling and user-friendly responses")
    print("=" * 60)