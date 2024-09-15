from openai import OpenAI

client = OpenAI(
    api_key = "sk-sEKhf5c62GDTsq5b5KGxZlQ_******************************************************************",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named RoboCop skilled in task completion"},
    {"role": "user", "content": "what is the value of Pi"}
  ]
)

print(completion.choices[0].message.content)




