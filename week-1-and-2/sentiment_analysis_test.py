import httpx

# Dummy text to analyze
text_to_analyze = "evQu 9OOUMR  Eg7qAEZoihQCW3j bQioL kLk Cbkn125O7oZ"

# API endpoint (AI Pipe)
url = "https://aipipe.org/openai/v1/chat/completions"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZHMxMDAwMDcwQGRzLnN0dWR5LmlpdG0uYWMuaW4ifQ.9N_BSNQy6-K2oyigVtotHSWZE5YeMRYyjPizkZzZQ08",  # replace with your actual key in environment
    "Content-Type": "application/json"
}

# Payload for the POST request
data = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "You are a sentiment analysis assistant. Classify any text as GOOD, BAD, or NEUTRAL."
        },
        {
            "role": "user",
            "content": text_to_analyze
        }
    ]
}

# Send POST request
with httpx.Client() as client:
    response = client.post(url, json=data, headers=headers)
    response.raise_for_status()  # Raise error if request failed
    result = response.json()

# Print the model's output
print(result)
