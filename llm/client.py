import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("TFY_API_KEY"),
    base_url=os.getenv("TFY_BASE_URL"),
)

def complete(
    messages,
    model="openai/gpt-4-1-mini",
    temperature=0.7,
    max_tokens=300,
) -> str:
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=True,
        extra_headers={
            "X-TFY-METADATA": "{}",
            "X-TFY-LOGGING-CONFIG": '{"enabled": true}',
        },
    )

    parts: list[str] = []

    for chunk in stream:
        if (
            chunk.choices
            and len(chunk.choices) > 0
            and chunk.choices[0].delta
            and chunk.choices[0].delta.content
        ):
            parts.append(chunk.choices[0].delta.content)

    return "".join(parts).strip()
