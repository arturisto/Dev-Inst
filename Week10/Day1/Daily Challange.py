from googletrans import Translator


def main():
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
    output = {}
    translator = Translator()
    for word in french_words:
        output[word] = translator.translate(word, src="fr", dest="en").text
    print(output)


if __name__ == "__main__":
    main()
