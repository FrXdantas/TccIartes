"""
    Arquivo para mudanças de paramentros e ajustes,
    MAX_LENGTH (Tamanho da legenda gerada)
    THRESHOLD  (Parametro de atenção)
    TARGET     (Alvo de atenção)
    ALPHA      (Alpha do Mapa de Saliência)
    BETA       (Beta do Mapa de saliência)
    FONT_PATH  (Diretório de fontes)
    FONT_SIZE  (Tamanho da fonte da lengenda
    COLOR_MAP  (Mapa de saliência gerado)
    OUTPUT_BASE_DIR (Saídas dos arquivos processados)
    
"""

import cv2

MAX_LENGTH = 30
THRESHOLD = 0.03
TARGET = 5
ALPHA = 1.5
BETA = 0
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SIZE = 12
COLOR_MAP = cv2.COLORMAP_RAINBOW
OUTPUT_BASE_DIR = "/home/franklin-dantas/TccIartes/img_saida/"
