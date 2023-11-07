import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from a .env file
load_dotenv("config.env")

client = OpenAI()

# Set your OpenAI API key from an environment variable
client.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo-1106", temperature=0):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that translates English to French."},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    print(response)
    # Extract the message content from the response
    message_content = response['choices'][0]['message']['content']
    return message_content

prompt = "Translate the following : 'Hello, how are you?'"
response = get_completion(prompt)
print(response)
