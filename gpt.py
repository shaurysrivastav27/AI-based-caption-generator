import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.organization = os.environ["OPENAI_ORG_ID"]


def get_chatgpt_response(caption):
    message = f"""Convert the following text enclosed in ``` into a caption for social media with relevant hashtags: 
                ```{caption}```
                Give 10 relevant captions for the above text.
                Answer format : Strings sepearated by commas. 
                """
    messages = {"role":"user" , "content":message}
    max_tokens = 300
    model = 'gpt-3.5-turbo'
    response = openai.ChatCompletion.create(
        model=model,
        messages=[messages],
        temperature=0,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response['choices'][0]['message']['content']