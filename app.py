import streamlit as st
import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

st.title("My AI Foundry App")

# Load credentials from Streamlit Secrets
endpoint = st.secrets["AZURE_ENDPOINT"]
api_key = st.secrets["AZURE_API_KEY"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key)
)

user_input = st.text_input("Ask the model something:")

if st.button("Generate"):
    if user_input:
        response = client.complete(messages=[{"role": "user", "content": user_input}])
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter a prompt.")
