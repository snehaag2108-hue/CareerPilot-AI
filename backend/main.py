from backend.workflow import career_graph

print("=" * 50)
print("CareerPilot AI")
print("=" * 50)

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    result = career_graph.invoke(
        {
            "user_input": question,
            "response": "",
            "agent": ""
        }
    )

    print("\nCareerPilot:\n")
    print(result["response"])