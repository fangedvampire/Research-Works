from spellchecker import SpellChecker
from textblob import TextBlob
from autocorrect import Speller

# Initialize tools
spellchecker = SpellChecker()
autocorrect = Speller()

# Function: pyspellchecker
def correct_pyspellchecker(text):
    return " ".join([spellchecker.correction(word) for word in text.split()])

# Function: TextBlob
def correct_textblob(text):
    return str(TextBlob(text).correct())

# Function: Autocorrect
def correct_autocorrect(text):
    return autocorrect(text)

# Test sentences (real-world noisy text)
sentences = [
    "I havv goood speling",
    "This prodct is amazng and cheep",
    "I am hapy with the servce",
    "Ths is nt wrking proprly"
]

print("\n--- Spell Checker Comparison ---\n")

for s in sentences:
    print(f"Original        : {s}")
    print(f"pyspellchecker  : {correct_pyspellchecker(s)}")
    print(f"TextBlob        : {correct_textblob(s)}")
    print(f"Autocorrect     : {correct_autocorrect(s)}")
    print("-" * 50)
