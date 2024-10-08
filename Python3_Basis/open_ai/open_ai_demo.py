import os
from openai import OpenAI

if __name__ == '__main__':

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("xxxxxx"),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )
