from word_assembler import *
import random

def pick_random_word():

    with open("words.txt") as f:
        words = [line.rstrip() for line in f]
    return words[random.randint(0, len(words))]

#implement method which asks for number of punctuation, insert randomly into sentence

def generate_words(count):
    i = 0
    while i < count:
        add_word(pick_random_word())
        i += 1
    add_word("done")

def choose_punctuation(count):
    counter = 0
    while count > counter:
        success = False
        while not success:
            if(insert_punctuation()):
                success = True
        counter += 1



def input_count():
    generate_words(int(input("How many words do you wish to add to the sentence? ")))

def input_punctuation():
    choose_punctuation(int(input("How many instances of punctuation should the sentence contain? ")))

def generate_sentences():
    count = int(input("How many sentences do you wish to generate? "))
    counter = 0
    while count > counter:
        punct_qty = random.randint(1,5)
        print "Punctuation quantity = %d" % punct_qty
        generate_words(random.randint(10, 13))
        choose_punctuation(punct_qty)
        assemble_sentence()
        counter += 1



generate_sentences()
