from openai import OpenAI
import os


def get_GPT_response(EM: int, PE: int, LC: int, AC: int, CS: int):
    client = OpenAI()

    # os.environ["OPENAI_API_KEY"] = os.getenv["OPENAI_API_KEY"] # hitsuyoukadoukawakaranai

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "prompt is in English, but you output response in Japanese",
            },
            {
                "role": "user",
                "content": """
                    Please Comment My 
                    My Score is below.
                    [
                        "EM": {EM},
                        "PE": {PE},
                        "LC": {LC},
                        "AC": {AC},
                        "CS": {CS},
                    ]
                """,
            },
        ],
    )

    return response.choices[0].message.content
