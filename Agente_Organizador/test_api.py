import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Responde solo con: Conexión exitosa"}
    ]
)

print(message.content[0].text)