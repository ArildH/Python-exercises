from word_assembler import *
import random

debug = False
def pick_random_word():

    with open("words.txt") as f:
        words = [line.rstrip() for line in f]
    return words[random.randint(0, len(words) - 1)]

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
        max_attempts = 0
        while not success and max_attempts < count + 50:
            if(pick_punctuation()):
                success = True
            max_attempts += 1
            if debug:
                print "####### NUMBER OF ATTEMPTS ARE NOW %d ##########" % max_attempts
        counter += 1



def input_counts():
    generate_words(int(input("How many words do you wish to add to the sentence? ")))
    choose_punctuation(int(input("How many instances of punctuation should the sentence contain? ")))
    assemble_sentence()

def random_sentences():
    count = int(input("How many sentences do you wish to generate? "))
    counter = 0
    while count > counter:
        word_qty = random.randint(5, 15)
        punct_qty = random.randint(0, word_qty - 5)
        print "Word quantity = %d" % word_qty
        print "Punctuation quantity = %d" % punct_qty
        generate_words(word_qty)
        choose_punctuation(punct_qty)
        assemble_sentence()
        counter += 1

def choose_operation():
    operation = str(input("""\n Please choose (input the digit) how you want to operate the word generator:
    1: Choose how many sentences to generate - the rest is automated and random.
    2: Choose the number of words and punctuation - only one sentence is generated.
    3: Close Word-generator
    NB: Due to missing support of compound words in English, a sentence may contain more words than specified.\n"""))
    if operation == "1":
        random_sentences()
    elif operation == "2":
        input_counts()
    elif operation == "3":
        print "Word-generator powering down..."
        return
    else:
        print "You must choose one of the three options by inputting the corresponding digit."
        choose_operation()



choose_operation()
