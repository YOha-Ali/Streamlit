from agents import OpenAIChatCompletionsModel, RunConfig, AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key=os.getenv("GOOGLE_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)
