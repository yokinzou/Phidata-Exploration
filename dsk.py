from phi.agent import Agent, RunResponse
from phi.model.deepseek import DeepSeekChat

agent = Agent(model=DeepSeekChat(base_url='https://api.deepseek.com/v1'), markdown=True)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story.")
# print(run.content)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")

