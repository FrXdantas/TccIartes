from translate import Translator as TranslateAPI

class CaptionTranslator:
    def __init__(self, target_lang="pt-br"):
        self.translator = TranslateAPI(to_lang=target_lang)

    def translate_caption(self, caption, source_lang="en"):
        try:
            translation = self.translator.translate(caption)
            return translation
        except Exception as e:
            print(f"Erro ao traduzir legenda '{caption}': {e}")
            return None

