from phi.model.google import Gemini
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
from dotenv import load_dotenv 
import os 
import phi.api 
from phi.playground import Playground, serve_playground_app
from fastapi import FastAPI

# Load environment variables
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")
print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))

# Define the agent
Research_Agentic_AI = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[DuckDuckGo(), Newspaper4k()],
    description="You are a senior NYT researcher writing an article on a topic.",
    instructions=[
        "For a given topic, search for the top 5 links.",
        "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
        "Analyse and prepare an NYT worthy article based on the information.",
    ],
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    debug_mode=True,
    use_default_system_message=False,
    handle_function_errors=True,  # New parameter to handle function errors gracefully
)

app = Playground(agents=[Research_Agentic_AI]).get_app(use_async=False)

if __name__ == "__main__":
    serve_playground_app("Reaserch_AI_Agent:app", reload=True)
