import random

phrases = list(open('phrases_2.txt'))
phrase = phrases[random.randint(0, len(phrases) - 1)]

required_words = []
for word in phrase.split():
    if word[0] == '{':
        if word[1:word.index('}')] not in required_words:
            required_words.append(word[1:word.index('}')])

chosen_words = {}
for required_word in required_words:
    chosen_words[required_word] = input('Choose a ' + required_word[:-1] + '... ')

print(phrase.format_map(chosen_words)) 