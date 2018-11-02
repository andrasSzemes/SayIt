import os
import re
from time import sleep
from pydub import AudioSegment

OPTIONS = ['o', 'mit', 'ez', 'ott', 'é', 'zé', 'lső', 'nt', 'gye', 'nne', 'jól', 'mbe', 'úgy']


def play(sound):
    path = os.getcwd()
    if sound in OPTIONS:
        os.system('aplay {}/sounds/{}.wav'.format(path, sound))
    elif sound == ' ':
        sleep(1/5)
    else:
        os.system('aplay {}/sounds/NOISE.wav'.format(path))


def make_wav_from(list_of_strings):
    path = os.getcwd()

    #Don't know how to make an empty start (like ''), NOSOUND was the wayout.
    combined_sounds = AudioSegment.from_wav('{}/sounds/NOSOUND.wav'.format(path))
    for string in list_of_strings:
        try:
            if string == ' ':
                sound = AudioSegment.from_wav('{}/sounds/BREAK.wav'.format(path))
            else:
                sound = AudioSegment.from_wav('{}/sounds/{}.wav'.format(path, string))
        except FileNotFoundError:
            sound = AudioSegment.from_wav('{}/sounds/NOISE.wav'.format(path))
        finally:
            combined_sounds += sound
    
    combined_sounds.export('{}/sounds/sentence.wav'.format(path), format="wav")


def words_and_spaces_of(string):
    words = string.lower().split(' ')
    words = [' ' if word == '' else word for word in words]

    words_and_spaces = words

    i = 1
    while i < len(words):
        if words_and_spaces[i - 1] != ' ':
            words_and_spaces.insert(i, ' ')
        else:
            pass
        i += 1

    return words_and_spaces


def sounds_of(sentence):
    '''Returns a list of spaces, words, subwords from the given sentence'''
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
    while True:
        sentence = input('What should I say? ')
        sounds_of_sentence = sounds_of(sentence)

        make_wav_from(sounds_of_sentence)
        path = os.getcwd()
        os.system('aplay {}/sounds/sentence.wav'.format(path))


if __name__ == '__main__':
    main()


#I will need a list of the necessary sounds to be recorded. Done
#There should be a way to replace OPTIONS, and creat it automaticallyat the start.
#   Should look up the file names in the directory.