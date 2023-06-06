from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class ImageToCaption:

    def __init__(self,max_length = 16,num_beams = 4):
        self.model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning").to(device)
        self.feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.max_length = max_length
        self.num_beams = num_beams
        self.gen_kwargs = {"max_length": self.max_length, "num_beams": self.num_beams}
    
    def predict_step(self,image):
        if image.mode != "RGB":
            image = image.convert(mode="RGB")
        images = []
        images.append(image)
        print("Image converted to rgb!!")
        pixel_values = self.feature_extractor(images=images, return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(device)

        output_ids = self.model.generate(pixel_values, **self.gen_kwargs)

        preds = self.tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        preds = [pred.strip() for pred in preds]
        return preds[0]