import random

noun = input('Choose a noun... ')
verb = input('Choose a verb... ')
adjective = input('Choose a adjective... ')
adverb = input('Choose a adverb... ')

words = {'noun': noun, 'verb': verb, 'adjective': adjective, 'adverb': adverb}

phrases = [ 
    'Today I went to the zoo. I saw a {0} jumping up and down in its tree. He {1} {3} through the large tunnel that led to its {2}.',
    'When I go to the arcade with my {0} there are lots of games to play. There is a game where you can {1} {3} in the {2} level.',
    'In school, I met a really {2} kid. Their name is {0}. In P.E. we {1} which I thought was really {3}',
    '{0} was invented by a {2} Chef who {3} {1} the ingrediants into a fine paste.',
    'Last month I {3} went to {0}. There were {2} people {1} everywhere.'
]

phrase_to_use = phrases[random.randint(0, len(phrases) - 1)]

print(phrase_to_use.format(words['noun'], words['verb'], words['adjective'], words['adverb']))