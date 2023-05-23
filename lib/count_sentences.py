#!/usr/bin/env python3
class MyString:
    """MyString in count_sentences.py"""

    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
        self.value = value

    def is_sentence(self):
        if self.value.endswith("."):
            return True
        return False

    def is_question(self):
        if self.value.endswith("?"):
            return True
        return False

    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        return False

    def count_sentences(self):
        return self.value.count(".") + self.value.count("?") + self.value.count("!")
