"""
    Sistema SPTCC - versão 2.0,
    revisão feita em 13/06/2024
    Trabalho de Conclusão de curso Iartes - UFAM
"""

import os
from datetime import datetime
import matplotlib.pyplot as plt
from caption_generator.captioning import CaptionGenerator
from caption_generator.saliency import SaliencyMapGenerator
from caption_generator.visualization import Visualizer
from caption_generator.resnet_feature_extractor import ResNetFeatureExtractor
from utils.file_utils import FileUtils
from utils.logger import Logger
from tqdm import tqdm
import numpy as np

def screen_clear():
    os.system('clear || cls')
    print("Iartes - Sistema para TCC - SPTCC Versão 1.7 ")
    print("="*44)

def calculate_accuracy(generated_caption, predefined_caption):
    generated_words = generated_caption.split()
    predefined_words = predefined_caption.split()
    total_words = len(predefined_words)
    correct_words = sum(1 for word in generated_words if word in predefined_words)
    accuracy = (correct_words / total_words) * 100 if total_words > 0 else 0
    return correct_words, total_words - correct_words, accuracy

def plot_comparison(generated_caption, predefined_caption, filename, output_dir):
    generated_words = generated_caption.split()
    predefined_words = predefined_caption.split()
    total_words = len(predefined_words)
    correct_words = [word for word in generated_words if word in predefined_words]
    incorrect_words = [word for word in generated_words if word not in predefined_words]

    plt.figure(figsize=(10, 5))
    plt.bar(correct_words, [1] * len(correct_words), color='g', label='Correto')
    plt.bar(incorrect_words, [1] * len(incorrect_words), color='r', label='Errado')
    plt.xlabel('Palavras')
    plt.ylabel('Correção')
    plt.title('Comparação de Legendas')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_path = os.path.join(output_dir, f"comparison_{filename}.png")
    plt.savefig(output_path)
    plt.close()

def main():
    input_directory = "/home/franklin-dantas/TccIartes/img_entrada/"
    output_directory = "/home/franklin-dantas/TccIartes/img_saida/"
    timestamp = datetime.now().strftime('%d-%m-%Y_%H-%M')
    output_dir = os.path.join(output_directory, f"test_{timestamp}")
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"result_captions_{timestamp}.txt"
    output_path = os.path.join(output_dir, output_file)
    
    screen_clear()
    logger = Logger()
    file_utils = FileUtils()

    caption_generator = CaptionGenerator()
    saliency_generator = SaliencyMapGenerator(caption_generator.model)
    visualizer = Visualizer()
    resnet_extractor = ResNetFeatureExtractor()

    captions_originais = []
    attentions_per_word = []
    saliency_percentages = []

    image_files = file_utils.get_image_files(input_directory)
    predefined_captions = file_utils.load_predefined_captions(os.path.join(input_directory, "captions.txt"))

    total_images = len(image_files)
    logger.log(f"Quantidade de imagens encontradas: {total_images}")

    comparison_results = []

    for idx, filename in enumerate(tqdm(image_files, desc="Processando Imagens")):
        image_path = os.path.join(input_directory, filename)
        resnet_features = resnet_extractor.extract_features(image_path)
        logger.log(f"Características ResNet extraídas para a imagem {filename}")

        original_caption, image_tensor = caption_generator.generate_caption(image_path)
        predefined_caption = predefined_captions.get(filename, "")

        if original_caption and image_tensor is not None:
            captions_originais.append(f"{filename}: {original_caption}")
            logger.log(f"Processando imagem {idx+1}/{total_images}: {filename}")
            saliency_map = saliency_generator.generate_saliency_map(image_tensor)
            
            if saliency_map is not None:
                saliency_map = saliency_generator.process_saliency_map(saliency_map, image_tensor)
                saliency_percentage = saliency_generator.calculate_saliency_percentage(saliency_map)
                visualizer.visualize_saliency(image_path, saliency_map, original_caption, output_dir, filename, saliency_percentage=saliency_percentage)
                
                attention_per_word = saliency_generator.calculate_attention_per_word(saliency_map, original_caption.split())
                attentions_per_word.append(f"{filename}: {attention_per_word}")
                
                saliency_percentages.append(f"{filename}: {saliency_percentage:.2f}%") 

                correct_words, incorrect_words, accuracy = calculate_accuracy(original_caption, predefined_caption)
                comparison_results.append((filename, predefined_caption, original_caption, correct_words, incorrect_words, accuracy))
                plot_comparison(original_caption, predefined_caption, filename, output_dir)
                
                logger.log(f"Legenda original: {original_caption}")
            else:
                logger.log(f"Falhou ao gerar saliência para imagem: {filename}")
        else:
            logger.log(f"Falhou ao gerar legenda para imagem: {filename}")

    file_utils.save_captions(output_path, captions_originais, attentions_per_word, saliency_percentages, comparison_results)
    logger.log(f"Legendas originais, atenções por palavra, porcentagens de saliência e resultados de comparação foram salvos em: {output_path}")

if __name__ == "__main__":
    main()
