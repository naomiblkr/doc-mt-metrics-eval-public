import requests
import json


API_KEY = "**************************************"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"


def generate_answer(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=None):
    '''Get response to prompt/message from API'''

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print(response.json()["choices"][0]["message"]["content"])
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")