import random

noun = input('Choose a noun... ')
verb = input('Choose a verb... ')
adjective = input('Choose a adjective... ')
adverb = input('Choose a adverb... ')

words = {'noun': noun, 'verb': verb, 'adjective': adjective, 'adverb': adverb}

phrases = list(open('phrases_1.txt'))

print(phrases[random.randint(0, len(phrases) - 1)].format_map(words))