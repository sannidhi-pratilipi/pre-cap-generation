import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("TFY_API_KEY"),
    base_url=os.getenv("TFY_BASE_URL"),
)

def complete_grok(
    messages,
    model="xai/grok-4-1-fast-reasoning",
    temperature=0.5,
    max_tokens=300,
) -> str:
    response= client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        extra_headers={
            "X-TFY-METADATA": "{}",
            "X-TFY-LOGGING-CONFIG": '{"enabled": true}',
        },
    )
    return response.choices[0].message.content
    # parts = []
    # for chunk in response:
    #     if (
    #         chunk.choices
    #         and len(chunk.choices) > 0
    #         and chunk.choices[0].delta
    #         and chunk.choices[0].delta.content
    #     ):
    #         parts.append(chunk.choices[0].delta.content)

    # return "".join(parts).strip()
