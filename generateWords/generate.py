import jieba
import pymysql
from config.database import DATABASE
from collections import Counter
from gensim.models import word2vec

db = pymysql.connect(
    DATABASE['host'],
    DATABASE['user'],
    DATABASE['password'],
    DATABASE['database']
)

dict_path = './userdict/addition_dict.txt'
words_data_path = './data/words_data.txt'
model_path = './models/word2vec_model.bin'

# 从数据库读取文章数据
def getContent():
    cursor = db.cursor()
    cursor.execute('SELECT title, content FROM articles WHERE content IS NOT NULL')
    results = cursor.fetchall()
    db.commit()
    cursor.close()
    return results


def cutContent(content):
    # words_all = list()
    # words = list()
    # 加载用户词
    jieba.load_userdict(dict_path)

    # 加载停止词
    stopwords_read = open('./userdict/stop_words.txt', 'r', encoding='utf-8').readlines()
    stopwords = ['\n', '\n\n', '\n\n\n']
    for line in stopwords_read:
        stopwords.append(line.strip())

    fp = open(words_data_path, 'w')

    # 整合读取内容
    for row in content:
        article_words = list()
        for column in row:
            article_words += jieba.lcut(column, cut_all=False)
        article_words_clear = list()
        for word in article_words:
            if len(word) > 2 and word not in stopwords:
                article_words_clear.append(word)
        fp.write(' '.join(article_words_clear) + ' ')

    # for word in words_all:
    #     if len(word) > 2 and word not in stopwords:
    #         words.append(word)
    #
    # words_vectors = Counter(words).most_common(100)
    # return words_vectors
    #
    # for word in words_vectors:
    #     print("Word: %s\t Count: %d" % (word[0], word[1]))

def train_model():
    print('加载语料文件...')
    sentences = word2vec.Text8Corpus(words_data_path)  # 加载语料
    print('模型训练中...')
    model = word2vec.Word2Vec(sentences, size=200)  # 训练skip-gram模型，默认window=5
    # 保存模型，以便重用
    print('保存模型文件中...')
    model.save(model_path)

def load_word2vec_model():
    '''
    加载训练好的模型
    '''
    print('加载模型文件...')
    return word2vec.Word2Vec.load(model_path)


def print_most_similar(words):
    '''
    测试输出最相关的20个词
    '''
    model = load_word2vec_model()
    y2 = model.most_similar(words, topn=20)  # 20个最相关的
    print ("-------------")
    print('>>> 和 {} 最相关的20个词:\n'.format(words))
    for item in y2:
        print(item[0], item[1])
    print ("-------------")