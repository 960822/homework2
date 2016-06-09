alphabet_list = [chr(i) for i in range(97,113)]
max_word_len = 0
max_length_word = ''

diction_file = open('/usr/share/dict/words')
for line in diction_file:
    word = line.split()[0]
    n = len(word) - 1
    count = 0
    while count <= n:
	if word[count] in alphabet_list:
	    count += 1
	else:
	    break
        if len(word) > max_word_len:
            max_word_len = len(word)
            max_length_word = word
print max_length_word

diction_file.close()
