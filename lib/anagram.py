# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, potential_anagrams):
        sorted_word = sorted(self.word)

        matches = []

        for possible in potential_anagrams:
            sorted_possible = sorted(possible.lower())

            if sorted_possible == sorted_word and possible.lower() != self.word:
                matches.append(possible)

        return matches


listen = Anagram("listen")
matches = listen.match(["enlists", "google", "inlets", "banana"])
print(matches)