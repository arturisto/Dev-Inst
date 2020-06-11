class AnagramChecker:

    def __init__(self):

        self.file = open("words.txt", "r")
        self.words = {}

        for line in self.file:
            line = line.rstrip("\n")

            if len(line) == 2:
                self.words[line] = []
            else:
                try:
                    self.words[line[:2]].append(line)
                except:
                    self.words[line[:2]] = line

    def is_valid_word(self, word):
        if len(word) <2:
            return False
        if word in self.words[word[:2]]:
            return True
        else:
            return False

    def get_anagrams(self, word):  # main function for finding anagrams

        keys = self.get_keys(word)
        anagrams = []
        for key in keys:
            for word_to_check in self.words[key]:
                if word_to_check != word:
                    if self.check_anagram(word, word_to_check):
                        anagrams.append(word_to_check)
        return anagrams

    def get_keys(self, word):  # function to get the possible keys for the word dict

        keys = set()
        for letter in word:
            for second_letter in word:
                keys.add(letter + second_letter)
                keys.add(second_letter + letter)

        #filter keys that don't exists in the dictionary:
        all_keys = self.words.keys()
        temp_keys = keys.copy()
        for key in temp_keys:
            if key not in all_keys:
                keys.remove(key)
        return keys

    def check_anagram(self, word, word_to_check):  # check if words are anagrams

        word_dict = {}
        word_to_check_dict = {}
        for charecter in word:  # convert first word to dict of keys = charecter, value = number of occurences
            try:
                word_dict[charecter] += 1
            except:
                word_dict[charecter] = 1

        for charecter in word_to_check: # convert second word to dict of keys = charecter, value = number of occurences
            try:
                word_to_check_dict[charecter] += 1
            except:
                word_to_check_dict[charecter] = 1

        if word_dict == word_to_check_dict: #check if the dicts are equal
            return True
        else:
            return False



