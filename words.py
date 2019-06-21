import pymysql
import os

filelist = os.listdir('./thesaurus/')
# print(filelist[7:-4])
# for item in filelist:
#     if item[-1] == 't':
#         print(item[7:-4])

# 链接数据库
db = pymysql.connect("localhost", "root", "19981129", "words_spider")

# 读取
cursor = db.cursor()
for item in filelist:
    if item[-1] == 't':
        word_type = item[7:-4]
        file_path = './thesaurus/' + item
        print(file_path)
        words = open(file_path, 'r', encoding='utf-8').readlines()
        for line in words:
            sql = "INSERT INTO thesaurus (word, type) VALUES ('" + line.split('\t')[0] + "', '" + word_type + "');"
            # print(line)
            # print(sql)
            cursor.execute(sql)
try:
    db.commit()
except:
    db.rollback()
db.close()
print('finished')