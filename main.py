from generateWords import generate

content = generate.getContent()
words_vectors = generate.cutContent(content)

for word in words_vectors:
    print("Word: %s\t Count: %d" % (word[0], word[1]))