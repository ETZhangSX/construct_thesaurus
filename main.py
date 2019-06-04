from generateWords import generate
#
# content = generate.getContent()
# generate.cutContent(content)
# generate.train_model()
generate.load_word2vec_model()
generate.print_most_similar('酒店')
# words_vectors = generate.cutContent(content)
#
# for word in words_vectors:
#     print("Word: %s\t Count: %d" % (word[0], word[1]))