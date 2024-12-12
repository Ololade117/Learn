from huggingface_hub import InferenceClient
import json

client = InferenceClient(api_key= "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")

messages = [
	{
		"role": "user",
		"content": input("What is the capital of France?")
	}
]

stream = client.chat.completions.create(
    model = "microsoft/Phi-3-mini-4k-instruct",
    max_tokens = 500,
    stream = True,
    messages = messages 
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="")