from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import config

class CaptionGenerator:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model.eval()

    def generate_caption(self, image_path):
        try:
            image = Image.open(image_path).convert("RGB")
            inputs = self.processor(images=image, return_tensors="pt")
            max_length = config.MAX_LENGTH
            out = self.model.generate(**inputs, max_length=max_length)
            caption = self.processor.decode(out[0], skip_special_tokens=True)
            return caption, inputs['pixel_values']
        except Exception as e:
            print(f"Erro ao gerar legenda para {image_path}: {e}")
            return None, None
