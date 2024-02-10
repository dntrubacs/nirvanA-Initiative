# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

completion = client.chat.completions.create(
  model="local-model",  # this field is currently unused
  messages=[
    {"role": "user", "content": "Go have a nice pizza party"}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)