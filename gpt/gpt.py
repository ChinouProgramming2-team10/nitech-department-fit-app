import openai
import os

my_api_key = os.getenv("OPENAI_API_KEY")

# print(my_api_key) //debug


def get_GPT_response():
    openai.api_key = my_api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "prompt is in English, but you output response in Japanese",
            },
            {"role": "user", "content": "prompt"},
        ],
    )

    return response["choices"][0]["message"]["content"]
