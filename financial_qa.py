import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint
from langchain import PromptTemplate, LLMChain
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Set the HuggingFace API token from the .env file
sec_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize the Streamlit application
st.title("Finance Query Assistant")

# Display an image
st.image("/Users/aameerkhan/Desktop/llm_chatbot/istockphoto-1432903655-612x612.jpg", use_column_width=True)

# Check if the token is loaded
if not sec_key:
    st.error("HuggingFace API token is not set. Please check your .env file.")
else:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = sec_key

    # Set up HuggingFaceEndpoint LLM
    repo_id = "mistralai/Mistral-Small-Instruct-2409"
    llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.7, token=sec_key, timeout=120)

    # Define the prompt template
    template = """ Question: {question}
    Answer: Let's think step by step."""
    prompt = PromptTemplate(template=template, input_variables=["question"])

    # Create LangChain object
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    # Input field for the user to ask questions
    question = st.text_input("Enter your finance-related question:")

    # List of finance-related keywords to check
    finance_keywords = [
    "finance", "investment", "stocks", "bonds", "money", "currency", 
    "budget", "loan", "interest", "credit", "debt", "tax", "savings", 
    "wealth", "insurance", "net pay", "gross pay", "salary", "income", 
    "expenses", "profit", "loss", "revenue", "cash flow", "equity", 
    "dividend", "assets", "liabilities", "capital", "retirement", 
    "pension", "mortgage", "financial planning", "cash", "valuation", 
    "portfolio", "hedge", "risk management", "ROI", "asset allocation", 
    "financial statement", "auditing", "compliance", "accounting", 
    "ledger", "balance sheet", "net worth", "financial analysis", 
    "savings account", "checking account", "investment account", 
    "mutual funds", "exchange-traded funds", "real estate", "credit score", 
    "loan approval", "interest rate", "compound interest", "simple interest",
    "payroll", "withholding tax", "deductions", "exemptions", "inflation", 
    "market trends", "economic indicators", "business cycle", "fiscal policy", 
    "monetary policy", "financial crisis", "bailout", "subsidy", 
    "public finance", "private finance", "non-profit finance", "cost-benefit analysis"
    ]

    if st.button("Ask"):
        if question:
            # Check if the question contains any finance-related keywords
            if any(keyword.lower() in question.lower() for keyword in finance_keywords):
                # Get the response from the LLM
                response = llm_chain.run(question)
                # Display the response in Streamlit
                st.write("Answer:", response)
            else:
                st.warning("Please ask a finance-related question.")
        else:
            st.write("Please enter a question.")
