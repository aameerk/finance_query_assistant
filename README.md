# Financial Query Assistant

## Overview

This project features a **Financial Query Answering Chatbot** designed to assist users with finance-related inquiries. Built using Streamlit as the front end and the Mistral-Small-Instruct-2409 model from Hugging Face, this chatbot specifically focuses on answering questions pertaining to finance while providing a warning for non-financial queries.

## Features

- **Finance Focused**: Only responds to questions related to finance.
- **User-Friendly Interface**: Built with Streamlit for an interactive experience.
- **Warning System**: Alerts users when questions outside of the finance domain are asked.
- **Extensive Knowledge Base**: Handles a variety of finance-related topics, including investments, loans, taxes, and more.

## Technologies Used

- **Python**: Programming language for building the chatbot.
- **Streamlit**: Framework for creating the web application.
- **LangChain**: Library for managing the language model interactions.
- **Hugging Face**: Model repository hosting the Mistral-Small-Instruct-2409 model.
- **dotenv**: For managing environment variables.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- An active internet connection
- A Hugging Face API token (you can obtain one by creating an account on [Hugging Face](https://huggingface.co/))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aameerk/finance_query_assistant.git
   cd finance_query_assistant
