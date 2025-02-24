import g4f

# Your G4F code here
# For example:
from g4f.client import Client

client = Client()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test"
        }
    ]
    # Add any other necessary parameters
)

print(response.choices[0].message.content)
