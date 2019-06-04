# construct_thesaurus

软件工程课设分词分类部分，语料爬取部分详见[words_spider](https://github.com/ETZhangSX/words_spider)

目前完成分词部分，分词器使用jieba库进行分词

## 环境部署

`Dump20190531.sql`为数据库迁移文件，在语料爬取部分数据库的基础上，新建表`thesaurus`，并导入了[清华大学中文语料库](http://thuocl.thunlp.org)作为基础词库

```bash
mysql -uroot -p < Dump20190531.sql
```

如不需要次基础词库，可修改迁移文件只导入数据库结构，再自行导入其他基础词库，导入方式可以参考我写的脚本`word.py`

安装相应python包
```bash
pip install -r requirements.txt
```
安装本项目并运行（目前仅分词、训练词向量模型）
```bash
python setup.py install
python main.py
```
