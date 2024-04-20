import json
import requests
import os
import anthropic
from markdown import Markdown
def send(query, model):
    try:
        if model == 3:
            url = "https://llama.k8s-gosha.atlas.illinois.edu/completion" # for mistral
        elif model == 1:
            url="https://mixtral.k8s-gosha.atlas.illinois.edu/completion" # for mixtral (better version)

        myobj = {
            "prompt": "<s>[INST]"+query+"[/INST]",
            "n_predict": -1 # -1 for no limit of tokens for output
        }

        headers = {
            "Content-Type": "application/json",
            # "Authorization": "Basic YXRsYXNhaXRlYW06anhAVTJXUzhCR1Nxd3U="
            
        }

        response = requests.post(url, data=json.dumps(myobj), headers=headers, 
                                auth=('atlasaiteam', 'jx@U2WS8BGSqwu'), timeout=1000)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return response.json()

# Claude3 API
def Claude_3(query):
    client = anthropic.Anthropic(
        # api_key=os.environ["ANTHROPIC_API_KEY"],
    )
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=4000,
        messages=[
            {"role": "user", "content": query}
        ]
    )
    return message

