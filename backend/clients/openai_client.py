from openai import OpenAI
from config.settings import openai_api_key

client = OpenAI(api_key=openai_api_key)