# 📰 AI News Summarizer

An AI-powered automation workflow built using **n8n** and **Google Gemini** that collects the latest AI and Technology news from RSS feeds, generates professional summaries, and sends a formatted newsletter via email.

---

## 🚀 Project Overview

This project automates the process of collecting, summarizing, and delivering AI and Technology news.

The workflow fetches articles from multiple RSS feeds, merges and aggregates the content, uses Google's Gemini LLM to generate structured summaries, and sends the final newsletter using Gmail SMTP.

---

## ✨ Features

* Daily scheduled execution
* Fetches AI and Technology news from multiple RSS feeds
* Merges articles into a single workflow
* Aggregates news before processing
* Generates structured summaries using Gemini AI
* Formats news into a professional newsletter
* Sends automated emails using Gmail SMTP

---

## 🛠 Tech Stack

* n8n
* Google Gemini API
* Gmail SMTP
* RSS Feeds
* Prompt Engineering

---

## 🔄 Workflow

Schedule Trigger

↓

AI RSS Feed + Technology RSS Feed

↓

Merge

↓

Aggregate

↓

Basic LLM Chain

↓

Google Gemini

↓

Send Email (SMTP)

---

## 📂 Project Structure

```text
01-ai-news-summarizer/
│
├── workflow.json
├── README.md
├── prompts/
│   └── news_summary_prompt.md
└── screenshots/
    ├── workflow.png
    ├── email-output.png
     
```

---

## 📸 Screenshots

* Workflow Design
* Email Output

---

## 📚 What I Learned

* Building AI automation workflows using n8n
* Integrating external APIs
* Prompt Engineering for LLMs
* Processing RSS feeds
* Email automation with Gmail SMTP
* Workflow orchestration
* AI-powered content summarization


