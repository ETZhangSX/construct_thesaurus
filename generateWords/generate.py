import jieba
import pymysql
from config.database import DATABASE
from collections import Counter

db = pymysql.connect(
    DATABASE['host'],
    DATABASE['user'],
    DATABASE['password'],
    DATABASE['database']
)

dict_path = './userdict/addition_dict.txt'

# 从数据库读取文章数据
def getContent():
    cursor = db.cursor()
    cursor.execute('SELECT title, content FROM articles WHERE content IS NOT NULL')
    results = cursor.fetchall()
    db.commit()
    cursor.close()
    return results


def cutContent(content):
    words_all = list()
    words = list()
    # 加载用户词
    jieba.load_userdict(dict_path)

    # 加载停止词
    stopwords_read = open('./userdict/stop_words.txt', 'r', encoding='utf-8').readlines()
    stopwords = ['\n', '\n\n', '\n\n\n']
    for line in stopwords_read:
        stopwords.append(line.strip())

    # 整合读取内容
    for row in content:
        for column in row:
            words_all += jieba.lcut(column, cut_all=False)

    for word in words_all:
        if len(word) > 2 and word not in stopwords:
            words.append(word)

    words_vectors = Counter(words).most_common(100)
    return words_vectors
    #
    # for word in words_vectors:
    #     print("Word: %s\t Count: %d" % (word[0], word[1]))