
import streamlit as st
from openai import OpenAI

st.title("My Azure AI Foundry App")

endpoint = st.secrets["AZURE_ENDPOINT"]     # must end with /openai/v1
api_key = st.secrets["AZURE_API_KEY"]
deployment = st.secrets["AZURE_MODEL"]

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

user_input = st.text_input("Ask the model something:")

if st.button("Generate"):
    if user_input:
        response = client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input},
            ],
        )
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter a prompt.")


