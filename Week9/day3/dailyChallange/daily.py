import string
import re


class Text:

    def __init__(self, path):
        with open(path, "r") as file:
            self.text = file.read().lower()

    def freq(self, input_word):

        words = self.text.split()
        counter = 0
        for word in words:
            if word.lower() == input_word:
                counter += 1
        if counter > 1:
            return counter
        else:
            return "your word wasn't found"

    def most_common(self):
        words = self.text.split()
        word_dict = {}
        max = 0
        max_word = ""
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

            if word_dict[word] > max:
                max = word_dict[word]
                max_word = word

        return max_word, max

    def unique(self):
        words = self.text.split()
        return set(words)

    @classmethod
    def from_file(cls, txt_file):
        return cls(txt_file)


class TextModification(Text):

    def no_punc(self):

        punc = string.punctuation
        print(punc)
        for punc_charecter in punc:
            self.text = self.text.replace(punc_charecter, "")

        return self.text

    def no_stopwords(self):

        stopwords = {"ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during",
                     "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours",
                     "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from",
                     "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his",
                     "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our",
                     "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at",
                     "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves",
                     "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he",
                     "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after",
                     "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how",
                     "further", "was", "here", "than"}
        for word in stopwords:
            s = rf"\b{word}\b"
            # self.text = self.text.replace(" "+word+" ", " ")
            self.text = re.sub(s, " ", self.text, 10000)
        return self.text

    def remove_special(self):

        print(re.sub("[^0-9a-zA-Z\r\n ]+", "", self.text))


def main():
    text = Text("text.txt")
    print(text.freq("has"))

    print(text.most_common())

    print(text.unique())

    new_text = Text.from_file("text.txt")

    print(new_text.freq("has"))

    text_mod = TextModification("text.txt")
    text_mod.no_punc()
    print(text_mod.no_stopwords())

    text_mod.remove_special()


if __name__ == "__main__":
    main()
