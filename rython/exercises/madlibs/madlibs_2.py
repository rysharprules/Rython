import random

noun = input('Choose a noun... ')
verb = input('Choose a verb... ')
adjective = input('Choose a adjective... ')
adverb = input('Choose a adverb... ')

words = {'noun': noun, 'verb': verb, 'adjective': adjective, 'adverb': adverb}

phrases = [ 
    'Today I went to the zoo. I saw a {noun} jumping up and down in its tree. He {verb} {adverb} through the large tunnel that led to its {adjective}.',
    'When I go to the arcade with my {noun} there are lots of games to play. There is a game where you can {verb} {adverb} in the {adjective} level.',
    'In school, I met a really {adjective} kid. Their name is {noun}. In P.E. we {verb} which I thought was really {adverb}',
    '{noun} was invented by a {adjective} Chef who {adverb} {verb} the ingrediants into a fine paste.',
    'Last month I {adverb} went to {noun}. There were {adjective} people {verb} everywhere.'
]

print(phrases[random.randint(0, len(phrases) - 1)].format_map(words))