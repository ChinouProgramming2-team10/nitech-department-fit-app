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
                    I take a test for getting a suitable department for university.
                    Please comment about my score.
                    My Score is below.
                    [
                        "EM": {EM},
                        "PE": {PE},
                        "LC": {LC},
                        "AC": {AC},
                        "CS": {CS},
                    ]

                    EM means Electronics.
                    PE means Phisics.
                    LC means Life Sciences.
                    AC means Sociologies.
                    CS means Computer Sciences.

                    Each max score is 80.
                """,
            },
        ],
    )

    return response.choices[0].message.content
