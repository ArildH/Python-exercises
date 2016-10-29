from word_assembler import *
import random

debug = False
def pick_random_word():
    with open("words.txt") as f:
        words = [line.rstrip() for line in f]
    return words[random.randint(0, len(words) - 1)]

#implement method which asks for number of punctuation, insert randomly into sentence

def generate_words(count):
    if count < 4:
        count = 4
        print "WARNING: minimum supported sentence length is 4. Defaulting length to 4 words.\n"
    i = 0
    while i < count:
        word_list.append(pick_random_word())
        i += 1

def choose_punctuation(count):
    counter = 0
    while count > counter:
        success = False
        attempts = 0
        while not success and attempts < count + 50:
            if(pick_punctuation()):
                success = True
            attempts += 1
            if debug:
                print "##### NUMBER OF ATTEMPTS ARE NOW %d #####" % attempts
        counter += 1

def input_counts():
    generate_words(input("How many words do you wish to add to the sentence? "))
    punct_qty = input("How many instances of punctuation should the sentence contain? ")
    choose_punctuation(punct_qty)
    assemble_sentence(punct_qty)

def random_sentences():
    count = int(input("How many sentences do you wish to generate? "))
    counter = 0
    while count > counter:
        word_qty = random.randint(4, 15)
        punct_qty = random.randint(0, word_qty - 4)
        print "------------------------------------------"
        print "Word quantity = %d" % word_qty
        print "Punctuation quantity = %d" % punct_qty
        generate_words(word_qty)
        choose_punctuation(punct_qty)
        assemble_sentence(punct_qty)
        counter += 1

def choose_operation():
    print "\n Welcome to the Word Generator!"
    operation = str(input("""\n Please choose (input the digit) how you want to operate the word generator:
    1: Choose how many sentences to generate - the rest is automated and random.
    2: Choose the number of words and punctuation - only one sentence is generated.
    3: Shut down the Word Generator.
    NB: Due to missing support of compound words in English, a sentence may contain more words than specified.\n"""))
    if operation == "1":
        random_sentences()
    elif operation == "2":
        input_counts()
    elif operation == "3":
        print "Word Generator shutting down..."
        return
    else:
        print "You must choose one of the three options by inputting the corresponding digit."
        choose_operation()



choose_operation()
