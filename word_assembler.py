#!/usr/bin/python
# -*- coding: UTF-8 -*-


import random
"""
TODO-LIST
fjern mellomrom før tilagt tegn - DELVIS OK
sjekk for doble tegn - tillat to ?, to !, tre . og en kombi ?!
"""
word_list = []
punctuation_list = [".", "!", "?", ",", ":", ";"]
def add_word(word):
	while word != "done":
		word_list.append(word)
		return False
	if word == "done":
		return True

def input_word():
	done = False
	print """Welcome to this word assembler. Input the word you wish to add to the sentence,
	or write 'done' to end input and receive your assembled word."""
	while not done:
		word = input("Which word would you like to add to the sentence? ")
		if add_word(word) == True:
			done = True

def insert_punctuation():
	symbol = punctuation_list[random.randint(0, len(punctuation_list) -1)]
	index = random.randint(1, len(word_list) - 3)
	print "now trying to place %s in index %d" %(symbol, index)
	print word_list[index]
	if word_list[index - 1] == "?" or word_list[index + 1] == "?" or word_list[index] == "?":
		print "FOUND ? before or after current index %d" % index
		if symbol == "?" and word_list[index - 2] != "?" and word_list[index + 2] != "?":
			word_list.insert(index, symbol)
			return True
		else:
			print "unable to place current symbol %s in current index %d" % (symbol, index)

			return False

	elif word_list[index - 1] == "!" or word_list[index + 1] == "!" or word_list[index] == "!":
		print "FOUND ! before or after  current index %d" % index
		if symbol == "!" and word_list[index - 2] != "!" and word_list[index + 2] != "!":
			word_list.insert(index, symbol)
			return True
		else:
			print "unable to place current symbol %s in current index %d" % (symbol, index)

			return False
	elif word_list[index - 1] == "." or word_list[index + 1] == "." or word_list[index] == ".":
		print "FOUND . before or after current index %d" % index
		if symbol == "." and word_list[index - 2] != "." and word_list[index - 3] != ".":
			word_list.insert(index, symbol)
			return True
		else:
			print "unable to place current symbol %s in current index %d" % (symbol, index)
			return False
	elif word_list[index - 1] == "," or word_list[index + 1 ] == "," or word_list[index] == ",":
		print "FOUND , before or after current index %d" % index
		return False
	elif word_list[index - 1] == ":" or word_list[index + 1] == ":" or word_list[index] == ":":
		print "FOUND : before, in or after current index %d" % index
		return False
	elif word_list[index - 1] == ";" or word_list[index + 1] == ";" or word_list[index] == ";":
		print "FOUND ; before, in or after current index %d" % index
		return False
	else:
		print "inserting %d %s " %(index, symbol)
		word_list.insert(index, symbol)
		return True
	return False

	#word_list.insert(random.randint(1, len(word_list) - 1), punctuation_list[random.randint(1, len(punctuation_list) - 1)])


def assemble_sentence():
	last_instance = len(word_list) - 1
	for x in range(len(word_list)):
		if x == 0:
			capitalise_letter(x)
		if check_for_punctuation(word_list[x]) and x < last_instance:
			capitalise_letter(x + 1)
	if x == last_instance:
		word_list[x] = word_list[x] + "."
	print_sentence()

def print_sentence():
	sentence = word_list[0]
	sentence = " ".join(word_list)
	sentence = sentence.replace(" ?", "?")
	sentence = sentence.replace(" .", ".")
	sentence = sentence.replace(" !", "!")
	sentence = sentence.replace(" ,", ",")
	sentence = sentence.replace(" :", ":")
	sentence = sentence.replace(" ;", ";")
	print "------------------------------------------"
	print sentence
	print "------------------------------------------"
	del word_list[:]

def capitalise_letter(x):
	word_list[x] = word_list[x][0].upper() + word_list[x][1:]


def check_for_punctuation(word):
	for x in punctuation_list:
		if x != "," and x != ":" and x != ";" and x in word:
			return True
	return False



#input_word()
#print_sentence()
