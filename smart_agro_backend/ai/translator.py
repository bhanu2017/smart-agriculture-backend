from deep_translator import GoogleTranslator


def translate_text(text, lang):
    """
    Translate text into selected language
    """
    try:
        if lang == "en":
            return text

        translated = GoogleTranslator(
            source="auto",
            target=lang
        ).translate(text)

        return translated

    except Exception as e:
        print("Translation error:", e)
        return text