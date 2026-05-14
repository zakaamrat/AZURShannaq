
import streamlit as st
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

st.title("My AI Foundry App")

# Load from Streamlit Secrets
endpoint = st.secrets["AZURE_ENDPOINT"]
api_key = st.secrets["AZURE_API_KEY"]
model = st.secrets["AZURE_MODEL"]  # THIS IS REQUIRED

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key),
    model=model
)

user_input = st.text_input("what is IS")

if st.button("Generate"):
    if user_input:
        try:
            response = client.complete(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input},
                ],
                max_tokens=512,
                temperature=0.7
            )
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error("Model call failed. Check configuration.")
            st.exception(e)

    else:
        st.warning("Please enter a prompt.")

