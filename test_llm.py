from agents import llm_agent

question = "Explain what a banking assistant does."

print("Testing Ollama LLM...")
answer = llm_agent(question)

print("\nAI Response:")
print(answer)