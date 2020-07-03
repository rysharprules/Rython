import random

words = {
    'noun': input('Choose a noun... '),
    'verb': input('Choose a verb... '),
    'adjective': input('Choose a adjective... '),
    'adverb': input('Choose a adverb... ')
}

phrases = list(open('phrases.txt'))

print(phrases[random.randint(0, len(phrases) - 1)].format_map(words))