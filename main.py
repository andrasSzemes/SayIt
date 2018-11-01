import os
import re
from time import sleep

OPTIONS = ['a', 'meg', 'vagy', 'vagyok', 'van']


def play(sound):
    path = os.getcwd()
    if sound in OPTIONS:
        os.system('aplay {}/sounds/{}.wav'.format(path, sound))
    elif sound == ' ':
        sleep(1/9)
    else:
        os.system('aplay {}/sounds/NOISE.wav'.format(path))


def words_and_spaces_of(string):
    words = string.lower().split(' ')

    words_and_spaces = words
    for i in range(1, 2*len(words)-1, 2):
        words_and_spaces.insert(i, ' ')

    return words_and_spaces


def sounds_of(sentence):
    '''Creates a list of spaces, words, subwords from the given sentence'''
    sounds_of_sentence = words_and_spaces_of(sentence)

    for i, item in enumerate(sounds_of_sentence):
        there_is_sound =        item != ' '
        more_than_one_vowel =   len(vowels_in(item)) > 1

        if there_is_sound and more_than_one_vowel:
            j = 1
            for char in (vowels_in(item) + [item[-1]]):
                if item != '':
                    index = item.index(char) + 1
                else:
                    break
                sounds_of_sentence.insert(i + j, item[:index])
            
                item, j = item[index:], j+1
            del sounds_of_sentence[i]

    return sounds_of_sentence


def vowels_in(string):
    '''Returns a list containing the vowels of string'''
    return re.findall('[aáeéiíoóöőuúüű]', string)


def main():
    sentence = input('What should I say? ')
    sounds_of_sentence = sounds_of(sentence)

    for sound in sounds_of_sentence:
        play(sound)


if __name__ == '__main__':
    main()


#I will need a list of the necessary sounds to be recorded.
#There should be a way to replace OPTIONS, and creat it automaticallyat the start.
#   Should look up the file names in the directory.