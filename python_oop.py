#Serial Number Generator

class SerialGenerator:
  def __init__(self, start=0):

        self.start = self.next = start

    def __repr__(self):

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):

        self.next += 1
        return self.next - 1

    def reset(self):

        self.next = self.start



#Word Finder

import random

class WordFinder:

    def __init__(self, path):

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):

        return [w.strip() for w in dict_file]

    def random(self):

        return random.choice(self.words)

#Subclass Special Word Finder

class SpecialWordFinder(WordFinder):

    def parse(self, dict_file):

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]

