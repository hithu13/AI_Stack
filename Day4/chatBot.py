import ollama
msgs=[{"role":"professor","content":"Give answers in easy to understand way."}]
while True:
    question=input("You:")
    if question.lower() == "exit":
        break
    msgs.append(
        {"role":"user",
        "content":question}
    )
    response=ollama.chat(
        model="llama3.2:3b",
        messages=msgs)
    msgs.append(
        {"role":"assistant",
        "content":response["message"]["content"] }
    )
    print("AI:", response["message"]["content"])

print("----Chat History----")
for msg in msgs:
    print(msg["role"]+":",msg["content"])
    if msg["role"]=="assistant":
        print("----")    