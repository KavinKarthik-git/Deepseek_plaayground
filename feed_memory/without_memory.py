from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import AIMessage,HumanMessage

model = OllamaLLM(model="deepseek-r1:14b")
full_ip=[]
while True:
    user_question = input("Ask something>>")
    full_ip.append(HumanMessage(user_question))
    result = model.invoke(full_ip)
    full_ip.append(AIMessage(result))


    print(result)
