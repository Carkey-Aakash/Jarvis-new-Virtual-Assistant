from openai import OpenAI
client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis same as alexa and google cloud."},
        {
            "role": "user",
            "content": "what is content"
        }
    ]
)

print(completion.choices[0].message.content)


#this will only run because this api is paid we have to pay 5$ for this 