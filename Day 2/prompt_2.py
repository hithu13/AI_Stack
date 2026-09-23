import ollama
response=ollama.chat(
     model="llama3.2:3b",
     messages=[
         {
           "role":"user",
           "content":"Define data science in 2 two lines and 3 types of data science define them in 2 lines with one example each in line by line."
        }
    ]
)
print(response["message"]["content"])