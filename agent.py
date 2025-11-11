from google.adk.agents import Agent

agent = Agent(
    name="my_first_agent",
    model="gemini-1.5-flash",
    description="A helpful assistant for general questions.",
    instruction="Answer politely and briefly.",
)

def main():
    user_input = input("Ask your agent: ")
    response = agent.run(user_input)
    print("Agent:", response)

if __name__ == "__main__":
    main()
