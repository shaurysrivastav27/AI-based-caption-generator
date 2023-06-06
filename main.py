from image_to_caption_engine import ImageToCaption
from gpt import get_chatgpt_response
from typing import Annotated
from fastapi import FastAPI, File, UploadFile
import PIL
import shutil
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = ImageToCaption()

@app.post("/uploadfile")
async def create_file(in_file: UploadFile):
    out_file_path = "./images/image1.png"
    try:
        with open(out_file_path,"wb") as buffer:
            shutil.copyfileobj(in_file.file, buffer)
    finally:
        in_file.file.close()

    image = PIL.Image.open(out_file_path).convert('RGB')
    print('Image created!!')
    captions = main(image)

    return captions

def main(image):
    caption_first = model.predict_step(image)
    print(caption_first)
    captions = get_chatgpt_response(caption_first)

    captions_list = captions.split("\n")

    return {"captions" : captions_list}

