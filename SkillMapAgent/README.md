# SkillMap Agent

An AI-powered career assistant that helps students understand industry demand for a skill and discover relevant job opportunities.

## Project Overview

SkillMap Agent combines Google Gemini, Tavily Search, and JSearch to research career trends and find real-time job opportunities.

The agent can:

* Research industry demand for a specific skill
* Find current job opportunities related to that skill
* Filter job searches by location
* Provide job details and application links
* Combine research results into a readable career-focused response

## Technologies Used

* Python
* LangChain
* Google Gemini
* Tavily Search
* JSearch API
* RapidAPI
* python-dotenv
* Requests

## How It Works

User Query
↓
Google Gemini Agent
↓
Tavily → Researches skill demand and career trends
↓
JSearch → Finds relevant job openings
↓
Gemini → Combines the results into a response

## Example Query

What's the demand for generative AI in the industry and show me related job openings in India

## Environment Variables

Create a `.env` file and add your API keys:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
RAPIDAPI_KEY=your_rapidapi_key
```

Never commit the `.env` file or expose API keys publicly.

## Running the Project

Install the required packages:

```bash
pip install python-dotenv requests langchain langchain-google-genai langchain-tavily
```

Then run:

```bash
python app.py
```

## Project Goal

The goal of this project is to demonstrate how an AI agent can combine an LLM with external tools and real-world APIs to solve a practical career-related problem.

