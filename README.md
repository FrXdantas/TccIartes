
# Iartes - Sistema para TCC - SPTCC Versão 2.0

## Descrição
Este projeto, parte do TCC Iartes - 2023, é uma ferramenta que estuda a geração de legendas de imagens, gerando mapas de saliência usando uma rede neural pré-treinada ResNet. Sua maior contribuição é a forma rápida de observar o foco de atenção de redes neurais pré-treinadas.

## Estrutura do Projeto

```plaintext
project/
│
├── main.py
├── config.py
├── caption_generator/
│   ├── __init__.py
│   ├── captioning.py
│   ├── translation.py
│   ├── saliency.py
│   ├── visualization.py
│   ├── resnet_feature_extractor.py
└── utils/
    ├── __init__.py
    ├── logger.py
    ├── file_utils.py
```

## Pré-requisitos

- Python 3.8 ou superior
- pip (Python package installer)

## Configuração do Ambiente Virtual

Para garantir um ambiente seguro e isolado, recomendamos o uso de um ambiente virtual (venv).

### Passos para criar e ativar um ambiente virtual

1. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```

2. Ative o ambiente virtual:

    - No Windows:
      ```bash
      venv\Scripts\activate
      ```

    - No macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Configuração do Projeto

1. Clone este repositório:
    ```bash
    git clone https://github.com/FrXdantas/TccIartes.git
    cd TccIartes
    ```

2. Certifique-se de que o ambiente virtual esteja ativado e instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Coloque as imagens que você deseja processar no diretório `img_entrada`.

2. Abra o arquivo `config.py` com um editor de texto e altere as configurações conforme necessário:

    ```plaintext
    MAX_LENGTH = 30
    THRESHOLD = 0.03
    TARGET = 5
    ALPHA = 1.5
    BETA = 0
    FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    FONT_SIZE = 12
    COLOR_MAP = cv2.COLORMAP_RAINBOW
    OUTPUT_BASE_DIR = "/home/project/TccIartes/img_saida/"
    ```

3. Execute o script principal:
    ```bash
    python main.py
    ```

4. As saídas, incluindo legendas originais, legendas traduzidas e mapas de saliência, serão salvas no diretório `img_saida`.

## Estrutura de Diretórios

- `img_entrada/`: Diretório onde você deve colocar as imagens a serem processadas.
- `img_saida/`: Diretório onde as imagens processadas e os arquivos de saída serão salvos.

## Autor

- Franklin Dantas - Grupo 8 - Iartes / UFAM

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.