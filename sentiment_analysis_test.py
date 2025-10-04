import httpx

# Sample meaningless text
text_to_analyze = "evQu 9OOUMR  Eg7qAEZoihQCW3j bQioL kLk Cbkn125O7oZ"

# Endpoint and headers
url = "https://aipipe.org/openai/v1/chat/completions"
headers = {
    "Authorization": "Bearer YOUR_DUMMY_API_KEY",  # replace with your actual dummy key
    "Content-Type": "application/json"
}

# Request payload
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
response = httpx.post(url, json=data, headers=headers)
response.raise_for_status()
result = response.json()

# Extract the sentiment classification from the response
sentiment = result["choices"][0]["message"]["content"]

# Print it properly
print(f"Sentiment: {sentiment}")
