#!/usr/bin/env python3
class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        cleaned_value = self.value.replace("?", ".").replace("!", ".")

        # Split the cleaned value using "." as the separator and remove any empty strings
        sentences = [
            sentence for sentence in cleaned_value.split(".") if sentence.strip()
        ]

        return len(sentences)
