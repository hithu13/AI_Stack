import ollama
response=ollama.chat(
     model="llama3.2:3b",
     messages=[
         {
           "role":"user",
           "content":"what is data science  explain in 8 lines?"
        }
    ]
)
print(response["message"]["content"])