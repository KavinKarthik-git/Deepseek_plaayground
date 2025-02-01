from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="deepseek-r1:14b")

while True:
    user_question = input("Ask something>>")
    result = model.invoke([user_question])
    print(result)
