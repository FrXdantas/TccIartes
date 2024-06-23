import torch
from captum.attr import Saliency
import numpy as np
import cv2
import config

class SaliencyMapGenerator:
    
    def __init__(self, model):
        self.model = model

    def forward_func(self, inputs):
        output = self.model.vision_model(pixel_values=inputs)
        return output.last_hidden_state[:, 0, :]

    def generate_saliency_map(self, image_tensor):
        try:
            saliency = Saliency(self.forward_func)
            image_tensor.requires_grad_()
            attributions = saliency.attribute(image_tensor, target=config.TARGET)
            return attributions
        except Exception as e:
            print(f"Erro ao gerar mapa de saliência: {e}")
            return None

    def process_saliency_map(self, saliency_map, image_tensor):
        saliency_map = saliency_map.squeeze().cpu().detach().numpy()
        saliency_map = np.abs(saliency_map).sum(axis=0)
        saliency_map = (saliency_map - saliency_map.min()) / (saliency_map.max() - saliency_map.min())
        saliency_map = cv2.resize(saliency_map, (image_tensor.shape[-1], image_tensor.shape[-2]))
        return saliency_map

    def calculate_saliency_percentage(self, saliency_map, threshold=config.THRESHOLD):
        significant_points = np.sum(saliency_map > threshold)
        total_points = saliency_map.size
        percentage = (significant_points / total_points) * 100
        return percentage

    def calculate_attention_per_word(self, saliency_map, words):
        if len(words) == saliency_map.shape[0]:
            attention_per_word = {word: saliency_map[i] for i, word in enumerate(words)}
            
            # Normalizar e criar a escala de 0 a 10
            max_val = max(attention_per_word.values())
            min_val = min(attention_per_word.values())
            scale = {word: int((attention_per_word[word] - min_val) / (max_val - min_val) * 10) for word in attention_per_word}
            
            return scale
        else:
            return {word: "N/A" for word in words}
