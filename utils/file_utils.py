import os
from datetime import datetime

class FileUtils:
    def get_image_files(self, directory):
        return [f for f in os.listdir(directory) if f.endswith((".jpg", ".jpeg", ".png"))]

    def save_captions(self, output_path, captions_originais, captions_traduzidas, attentions_per_word, saliency_percentages):
        with open(output_path, "w") as file:
            file.write(f"log de teste:\n")
            file.write(f"teste gerado em: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
            file.write("com as seguintes imagens:\n")
            for caption in captions_originais:
                filename = caption.split(":")[0]
                file.write(f"\t{filename}\n")

            file.write("\ncomo resultados temos a leitura:\n")
            file.write("\nCaptions Originais e Traduzidas:\n")
            for caption in captions_originais:
                file.write(f"{caption}\n")
            for caption in captions_traduzidas:
                file.write(f"{caption}\n")

            file.write("\nAtenção por Palavra:\n")
            for attention in attentions_per_word:
                file.write(f"{attention}\n")

            file.write("\nPorcentagens de Saliência:\n")
            for percentage in saliency_percentages:
                file.write(f"{percentage}\n")
