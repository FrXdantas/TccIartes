"""
    Sistema SPTCC - versão 2.0,
    revisão feita em 13/06/2024
    Trabalho de Conclusão de curso Iartes - UFAM

"""    
    

import os
from datetime import datetime
from caption_generator.captioning import CaptionGenerator
from caption_generator.translation import CaptionTranslator
from caption_generator.saliency import SaliencyMapGenerator
from caption_generator.visualization import Visualizer
from caption_generator.resnet_feature_extractor import ResNetFeatureExtractor
from utils.file_utils import FileUtils
from utils.logger import Logger
from tqdm import tqdm

def screen_clear():
    os.system('clear || cls')
    print("Iartes - Sistema para TCC - SPTCC Versão 1.7 ")
    print("="*44)
    
    

def main():
    #entrada de imagens
    input_directory = "/home/franklin-dantas/TccIartes/img_entrada/"
    
    #saída do processamento
    output_directory = "/home/franklin-dantas/TccIartes/img_saida/"
    output_file = f"result_captions_{datetime.now().strftime('%d-%m-%Y_%H-%M')}.txt"
    output_path = os.path.join(output_directory, output_file)
    
    screen_clear()
    #saída em tela ( logger )
    logger = Logger()
    file_utils = FileUtils()

    #objetos para geração de legenda
    caption_generator = CaptionGenerator()
    translator = CaptionTranslator(target_lang="pt-br")
    saliency_generator = SaliencyMapGenerator(caption_generator.model)
    visualizer = Visualizer()
    resnet_extractor = ResNetFeatureExtractor()

    #lista para processamento
    captions_originais = []
    captions_traduzidas = []
    attentions_per_word = []
    saliency_percentages = []

    #carregamento das imagens
    image_files = file_utils.get_image_files(input_directory)
    total_images = len(image_files)
    logger.log(f"Quantidade de imagens encontradas: {total_images}")
    

    for idx, filename in enumerate(tqdm(image_files, desc="Processando Imagens")):
        image_path = os.path.join(input_directory, filename)
        
        #extração de características usando <<ResNet>>
        resnet_features = resnet_extractor.extract_features(image_path)
        logger.log(f"Características ResNet extraídas para a imagem {filename}")

        original_caption, image_tensor = caption_generator.generate_caption(image_path)
        if original_caption and image_tensor is not None:
            translated_caption = translator.translate_caption(original_caption)
            if translated_caption:
                captions_originais.append(f"{filename}: {original_caption}")
                captions_traduzidas.append(f"{filename}: {translated_caption}")
                logger.log(f"Processando imagem {idx+1}/{total_images}: {filename}")
                saliency_map = saliency_generator.generate_saliency_map(image_tensor)
               
                if saliency_map is not None:
                    saliency_map = saliency_generator.process_saliency_map(saliency_map, image_tensor)
                    saliency_percentage = saliency_generator.calculate_saliency_percentage(saliency_map)
                    visualizer.visualize_saliency(image_path, saliency_map, translated_caption, output_directory, filename, saliency_percentage=saliency_percentage)
                    
                    #calculo de atenção por palavra ( verificar )
                    attention_per_word = saliency_generator.calculate_attention_per_word(saliency_map, original_caption.split())
                    attentions_per_word.append(f"{filename}: {attention_per_word}")
                    
                    saliency_percentages.append(f"{filename}: {saliency_percentage:.2f}%") 
                
                logger.log(f"Legenda original: {original_caption}")
                logger.log(f"Legenda traduzida: {translated_caption}")
            else:
                logger.log(f"Falhou ao traduzir legenda para imagem: {filename}")
        else:
            logger.log(f"Falhou ao gerar legenda para imagem: {filename}")

    file_utils.save_captions(output_path, captions_originais, captions_traduzidas, attentions_per_word, saliency_percentages)
    logger.log(f"Legendas originais, traduzidas e as legendas geradas foram salvas em: {output_path}")

if __name__ == "__main__":
    main()
