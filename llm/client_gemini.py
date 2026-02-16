import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import Any
# from google.generativeai.types import HarmBlockThreshold
# from google.generativeai.types import HarmCategory
load_dotenv()

client = OpenAI(
    api_key=os.getenv("TFY_API_KEY"),
    base_url=os.getenv("TFY_BASE_URL"),
)


# def get_llm_provider_configs(model: str) -> dict[str, Any]:
#     """Return a dictionary of provider-specific configurations to be splatted (**) into the `client.chat.completions.create()`.

#     This allows centralizing model-specific parameters like safety settings
#     without affecting other models.
#     """
#     params = {}
#     if model and model.startswith("gemini"):
#         params["extra_body"] = {
#                 "safetySettings": [
#                     {"category": HarmCategory.HARM_CATEGORY_HARASSMENT.name, "threshold": HarmBlockThreshold.BLOCK_NONE.name},
#                     {"category": HarmCategory.HARM_CATEGORY_HATE_SPEECH.name, "threshold": HarmBlockThreshold.BLOCK_NONE.name},
#                     {
#                         "category": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT.name,
#                         "threshold": HarmBlockThreshold.BLOCK_NONE.name,
#                     },
#                     {
#                         "category": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT.name,
#                         "threshold": HarmBlockThreshold.BLOCK_NONE.name,
#                     },
#                 ]
#             }
#     return params

def complete_gemini(
    messages,
    model="google-vertex/gemini-2-5-pro",
    temperature=0.7,
    max_tokens=3500,
) -> str:
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        extra_headers={
            "X-TFY-METADATA": "{}",
            "X-TFY-LOGGING-CONFIG": '{"enabled": true}',
        },
        # **get_llm_provider_configs(model),
    )
    return stream.choices[0].message.content

   
    # parts: list[str] = []

    # for chunk in stream:
    #     if (
    #         chunk.choices
    #         and len(chunk.choices) > 0
    #         and chunk.choices[0].delta
    #         and chunk.choices[0].delta.content
    #     ):
    #         parts.append(chunk.choices[0].delta.content)

    # return "".join(parts).strip()
