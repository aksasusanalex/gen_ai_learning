import os
from dotenv import load_dotenv
import requests
from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
load_dotenv()

rapidapi_key=os.getenv("RAPIDAPI_KEY")
# Step 1: Initialize the Model
model=init_chat_model("google_genai:gemini-2.5-flash")


# Step 2: Create Skill Demand Search Tool (Tavily)
skill_demand_tool =TavilySearch(
    max_results=5,
    search_depth="advanced"
)

# Step 3: Create Custom Job Search Tool
@tool
def search_jobs(skill: str, location: str) -> list:
    """Search for jobs requiring a specific skill using JSearch API from RapidAPI."""
    url = "https://jsearch.p.rapidapi.com/search"
    rapidapi_key = os.getenv("RAPIDAPI_KEY")
    headers = {
    "x-rapidapi-key": rapidapi_key,
    "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }
    params = {
    "query": skill,
    "location": location
    }
    response=requests.get(url,headers=headers,params=params)
    data=response.json()
    return data.get("data",[])


# Step 4: Define System Prompt
system_prompt = """You are a Skill-to-Career Mapping assistant that helps students understand skill demand and find matching job opportunities.
You have access to these tools:
- skill_demand_tool: Search for industry demand, salary insights, and career trends
- search_jobs: Find actual job listings requiring specific skills
Help the student by researching the skill they ask about and finding relevant opportunities. Present results in a clean, readable format with clear sections and proper spacing.
Include all job details with apply links. Don't use markdown format."""

# Step 5: Create and Run the Agent
agent=create_agent(
    model=model,
    tools=[skill_demand_tool,search_jobs],
    system_prompt=system_prompt
)
user_query = "What's the demand for generative ai in the industry and show me related job openings in India"
response = agent.invoke(
    {"messages": [{"role": "user", "content": user_query}]}
)
