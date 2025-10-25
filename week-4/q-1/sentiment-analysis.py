import httpx
import os

# AI Pipe base URL
base_url = "https://aipipe.org/openai/v1/chat/completions"

# Use your AI Pipe token here
api_key = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZHMxMDAwMDcwQGRzLnN0dWR5LmlpdG0uYWMuaW4ifQ.9N_BSNQy6-K2oyigVtotHSWZE5YeMRYyjPizkZzZQ08" 

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": api_key
}

# Messages to send
messages = [
    {
        "role": "system",
        "content": (
            "You are an AI sentiment analyzer. Analyze the sentiment of any given text "
            "and classify it strictly as GOOD, BAD, or NEUTRAL."
        )
    },
    {
        "role": "user",
        "content": "evQu 9OOUMR  Eg7qAEZoihQCW3j bQioL kLk Cbkn125O7oZ"
    }
]

# JSON payload
payload = {
    "model": "gpt-4o-mini",
    "messages": messages
}

# Send POST request
try:
    response = httpx.post(base_url, json=payload, headers=headers)
    response.raise_for_status()
    result = response.json()
    
    # Print full API response
    print("Full API Response:\n", result)

    # Extract just the sentiment
    sentiment = result["choices"][0]["message"]["content"]
    print("\nPredicted Sentiment:", sentiment)

except httpx.HTTPStatusError as e:
    print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
except Exception as e:
    print("An error occurred:", str(e))
