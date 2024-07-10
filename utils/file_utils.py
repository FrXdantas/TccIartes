import os
from datetime import datetime

class FileUtils:
    def get_image_files(self, directory):
        return [f for f in os.listdir(directory) if f.endswith((".jpg", ".jpeg", ".png"))]

    def load_predefined_captions(self, filepath):
        captions = {}
        with open(filepath, "r") as file:
            for line in file:
                parts = line.strip().split(": ")
                if len(parts) == 2:
                    captions[parts[0]] = parts[1]
        return captions

    def save_captions(self, output_path, captions_originais, attentions_per_word, saliency_percentages, comparison_results):
        with open(output_path, "w") as file:
            file.write("IARTES - UFAM\n")
            file.write(f"Teste Atenção por Saliência feito em: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
            file.write("\nCom as seguintes imagens:\n")
            for caption in captions_originais:
                filename = caption.split(":")[0]
                file.write(f"\t{filename}\n")

            file.write("\nComo resultados temos a comparação:\n")
            for result in comparison_results:
                filename, predefined_caption, original_caption, correct_words, incorrect_words, accuracy = result
                file.write(f"\nLegenda do arquivo TXT\n{filename}: {predefined_caption}\n")
                file.write(f"Legendas Geradas pela IA\n{filename}: {original_caption}\n")
                file.write(f"Temos {correct_words} acertos\n")
                file.write(f"Temos {incorrect_words} erros\n")
                file.write(f"Gerando uma acuracia de {accuracy:.2f}% entre as legendas.\n")

            file.write("\nPorcentagens de Saliência:\n")
            for percentage in saliency_percentages:
                file.write(f"{percentage}\n")
