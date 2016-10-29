	#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
"""
TODO-LIST
sjekk for doble tegn - tillat to ?, to !, tre . og en kombi ?!
"""
debug = False
word_list = []
punctuation_dict = {"." : 0, "!" : 0, "?" : 0, "," : 0, ":" : 0, ";" : 0}

def insert_punctuation(symbol, index):
	if debug:
		print "#1 Trying to place %s in index %d" % (symbol, index)
		print "#2 Word before punctuation will be %s" % word_list[index - 1]
		print "#2 Word after punctuation will be %s" % word_list[index]
	if check_for_punctuation(word_list[index - 1], False) or check_for_punctuation(word_list[index], False):
		if debug:
			print "#3 Unable to place symbol %s in index %d" % (symbol, index)
		return False
	else:
		if debug:
			print "#3 Inserting %s in index %d" % (symbol, index)
		word_list.insert(index, symbol)
		return True

def pick_punctuation():
	symbol = punctuation_dict.keys()[random.randint(0, len(punctuation_dict) -1)]
	index = random.randint(1, len(word_list) - 3)
	return insert_punctuation(symbol, index)

def assemble_sentence(punct_qty):
	last_instance = len(word_list) - 1
	for x in range(len(word_list)):
		if x == 0:
			capitalise_letter(x)
		if check_for_punctuation(word_list[x], True) and x < last_instance:
			capitalise_letter(x + 1)
	sentence = " ".join(word_list)
	#char - character, punct - punctuation
	for char in sentence:
		for punct in punctuation_dict.keys():
			if char == punct:
				#make sure char before punct is a space
				if sentence[sentence.index(char) - 1] == " ":
					if debug:
						print "#Found '%s'" % sentence[sentence.index(char) - 1 : sentence.index(char) + 1]
						print "#Replacing with '%s'" % punct
					#remove space before punct
					sentence = sentence.replace(sentence[sentence.index(char) - 1 : sentence.index(char) + 1], punct)
	#this is end of sentence, add period
	sentence += "."
	print_sentence(punct_qty, sentence)

def print_sentence(punct_qty, sentence):
	actual_punct_qty = 0
	for x in word_list:
		for y in punctuation_dict.keys():
			if x == y:
				actual_punct_qty += 1
	number = punct_qty - actual_punct_qty
	print "--------"
	print sentence
	print "--------"
	print "%d punctuation(s) were unable to be inserted." % number
	print "------------------------------------------"
	del word_list[:]

def capitalise_letter(x):
	word_list[x] = word_list[x][0].upper() + word_list[x][1:]


def check_for_punctuation(word, capitalise):
	if capitalise:
		for x in punctuation_dict.keys():
			if x != "," and x != ":" and x != ";" and x in word:
				return True
	else:
		for x in punctuation_dict.keys():
			if x in word:
				return True

	return False
