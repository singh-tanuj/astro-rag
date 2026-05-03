from app.rag.llm_generator import generate_llm_answer

context = "Mars in the 11th house gives gains through networks and ambition."

query = "mars in 11th house"

print(generate_llm_answer(query, context))