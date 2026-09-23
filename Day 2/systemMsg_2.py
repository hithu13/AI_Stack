import ollama
response=ollama.chat(
     model="llama3.2:3b",
     messages=[
        {
            "role":"system",
            "content":"give answer in story format such that it is easy for a 6-year-old to understand."
        }, 
        {
           "role":"user",
           "content":"Define solar energy."
        }
    ]
)
print(response["message"]["content"])