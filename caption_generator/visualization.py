import os
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
import config

class Visualizer:
    def visualize_saliency(self, image_path, saliency_map, caption, output_dir, filename, saliency_percentage=None):
        try:
            image = cv2.imread(image_path)
            if image.shape[:2] != saliency_map.shape[:2]:
                saliency_map = cv2.resize(saliency_map, (image.shape[1], image.shape[0]))

            heatmap = cv2.applyColorMap(np.uint8(255 * saliency_map), config.COLOR_MAP)
            heatmap = cv2.convertScaleAbs(heatmap, alpha=config.ALPHA, beta=config.BETA)
            result = cv2.addWeighted(image, 0.5, heatmap, 1.0, 0)

            combined_image = np.concatenate((image, result), axis=1)
            combined_image_pil = Image.fromarray(cv2.cvtColor(combined_image, cv2.COLOR_BGR2RGB))

            draw = ImageDraw.Draw(combined_image_pil)
            font = ImageFont.truetype(config.FONT_PATH, config.FONT_SIZE) if config.FONT_PATH else ImageFont.load_default()
            text_position = (10, combined_image_pil.height - 60)
            draw.text(text_position, caption, (255, 255, 255), font=font)

            if saliency_percentage is not None:
                saliency_text_position = (10, combined_image_pil.height - 30)
                saliency_text = f"Atenção: {saliency_percentage:.2f}%"
                draw.text(saliency_text_position, saliency_text, (255, 255, 255), font=font)

            combined_output_path = os.path.join(output_dir, f"combined_{filename}")
            combined_image_pil.save(combined_output_path)
        except Exception as e:
            print(f"Erro ao visualizar saliência para {image_path}: {e}")
