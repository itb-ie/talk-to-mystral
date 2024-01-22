import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "mistral",
    "max_tokens": 500  # Set a higher value for max_tokens
}


def process_response():
    """
    Process the response to look pretty
    """
    str_list = response.text.split("\n")
    response_list = [json.loads(r) for r in str_list[:-1]]
    text = "".join([r["response"] for r in response_list])
    new_text = ""
    c = 0
    for l in text:
        c += 1
        new_text += l
        if l == " " and c > 80:
            new_text += "\n"
            c = 0
    return new_text


q = input("Hi, I am local-gpt, what do you want to know? ")
data["prompt"] = q
response = requests.post(url, data=json.dumps(data))
new_text = process_response()

print(new_text)
