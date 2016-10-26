	#!/usr/bin/python
# -*- coding: UTF-8 -*-


import random
"""
TODO-LIST
fjern mellomrom før tilagt tegn - DELVIS OK
sjekk for doble tegn - tillat to ?, to !, tre . og en kombi ?!
"""
word_list = []
punctuation_dict = {"." : 1, "!" : 1, "?" : 1, "," : 0, ":" : 0, ";" : 0}
def add_word(word):
	while word != "done":
		word_list.append(word)
		return False
	if word == "done":
		return True


def insert_punctuation(symbol, index):
	debug = False
	if debug:
		print "#1 Trying to place %s in index %d" % (symbol, index)
		print "#2 Word before punctuation will be %s" % word_list[index - 1]
	if check_for_punctuation(word_list[index - 1], False) or check_for_punctuation(word_list[index + 1], False) \
		or check_for_punctuation(word_list[index], False):
		if debug:
			print "#3 Found punctuation before, after or in index %d" % index
			print "PUNCT SYMBOL WEIGHT HERE %d" % punctuation_dict[symbol]
		if punctuation_dict[symbol] > 0:
			if (check_for_punctuation(word_list[index - punctuation_dict[symbol]], False) \
				and word_list[index - punctuation_dict[symbol]] == symbol) \
				or (check_for_punctuation(word_list[index + punctuation_dict[symbol]], False) \
				and word_list[index + punctuation_dict[symbol]] == symbol):
				if debug:
					print "#4 Inserting %s in index %d" % (symbol, index)
				word_list.insert(index, symbol)
				return True
			else:
				if debug:
					print "#4 Unable to place symbol %s in index %d" % (symbol, index)
				return False
		else:
			if debug:
				print "#4.1 Unable to place symbol %s in index %d" % (symbol, index)
			return False

	else:
		if debug:
			print "#3 Inserting %s in index %d" % (symbol, index)
		word_list.insert(index, symbol)
		return True
	return False


def pick_punctuation():
	symbol = punctuation_dict.keys()[random.randint(0, len(punctuation_dict) -1)]
	index = random.randint(1, len(word_list) - 3)
	return insert_punctuation(symbol, index)


def assemble_sentence():
	last_instance = len(word_list) - 1
	for x in range(len(word_list)):
		if x == 0:
			capitalise_letter(x)
		if check_for_punctuation(word_list[x], True) and x < last_instance:
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


def check_for_punctuation(word, capitalise):
	if capitalise:
		for x in punctuation_dict.keys():
			if x != "," and x != ":" and x != ";" and x in word:
				return True
	else:
		for x in punctuation_dict.keys():
			if x in word:
				#print "SJEKK HER X ER %s" % x
				return True

	return False

print len(punctuation_dict)

#input_word()
#print_sentence()
