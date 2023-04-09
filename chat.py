import requests
import json
from config import chat_url


def chat(prompt, history=[]):
    data = {
        "prompt": prompt,
        "history": history
    }
    res = requests.post(chat_url, json=data).text
    res = json.loads(res)
    return res["response"], res["history"]
