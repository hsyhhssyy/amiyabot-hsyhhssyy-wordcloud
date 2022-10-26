import asyncio
import sqlite3
import os
import re

from wordcloud import WordCloud
from amiyabot import AmiyaBot, Message, Chain, log , PluginInstance

curr_dir = os.path.dirname(__file__)

#初始化停用词
stop_words = []
file_object2 = open(f"{curr_dir}/resource/word_cloud_stop_words_cn.txt",'r')
try:
    lines = file_object2.readlines()
    for line in lines:
        stop_words.append(line.strip())
finally:
    file_object2.close()

log.info(f'WordCloud stop words loaded total {len(stop_words)} words')

async def any_talk(data: Message):
    
    # log.info('AnyTalk Collect Word Cloud')

    #收集好分词后的群友句子
    words = data.text_words

    #以Sqlite的形式存到fileStorage下面
    if os.path.exists(f'{curr_dir}/../../resource/word_cloud.db'):
        conn = sqlite3.connect(f'{curr_dir}/../../resource/word_cloud.db')
    else:        
        conn = sqlite3.connect(f'{curr_dir}/../../resource/word_cloud.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE WORD_CLOUD
            (WORD           TEXT    NOT NULL,
            USER_ID         INT     NOT NULL,
            QUANTITY        INT     NOT NULL);''')
        conn.commit()
    
    user_id = data.user_id

    c = conn.cursor()
    for word in words:
        # 获取当前Quantity
        c.execute("select QUANTITY from WORD_CLOUD where USER_ID = ? and WORD = ?",(user_id,word))
        if len(c.fetchall()) <=0 :
            c.execute('INSERT INTO WORD_CLOUD (USER_ID,WORD,QUANTITY) values (?,?,1)' ,(user_id,word))
        else:
            c.execute('UPDATE WORD_CLOUD SET QUANTITY = QUANTITY +1 where USER_ID = ? and WORD = ?' ,(user_id,word))

    conn.commit()

    return False,0

class WordCloudPluginInstance(PluginInstance):
    def install(self):
        if not os.path.exists(f'{curr_dir}/../../resource/word_cloud'):
            os.makedirs(f'{curr_dir}/../../resource/word_cloud')

bot = WordCloudPluginInstance(
    name='词云统计',
    version='1.0',
    plugin_id='amiyabot-hsyhhssyy-wordcloud',
    plugin_type='official',
    description='让兔兔可以统计群用户的词云',
    document=f'{curr_dir}/README.md'
)

@bot.on_message(verify=any_talk, check_prefix=False)
async def _(data: Message):
    return

@bot.on_message(keywords=['查看词云','查询词云'], level = 5)
async def check_wordcloud(data: Message):

    # log.info('Create Word Cloud')

    if not os.path.exists(f'{curr_dir}/../../resource/word_cloud.db'):
        return Chain(data).text('词云功能没有开放。')
    
    user_id = data.user_id

    conn = sqlite3.connect(f'{curr_dir}/../../resource/word_cloud.db')
    c = conn.cursor()
    c.execute(f"select QUANTITY,WORD from WORD_CLOUD where USER_ID = '{user_id}'")

    frequencies = {}
    for row in c:
        if f'{row[1]}' not in stop_words:
            frequencies[row[1]]=row[0]

    if len(frequencies) <=0 :
        return Chain(data).text('还没有收集到您的记录，请让我多听一会儿。')

    # wordcloud = WordCloud(font_path =  "fileStorage/GenJyuuGothic-Normal-2.ttf").generate_from_frequencies(frequencies)    
    wordcloud = WordCloud(font_path =  f'{curr_dir}/resource/msyh.ttf').generate_from_frequencies(frequencies)
    wordcloud.to_file(f'{curr_dir}/../../resource/word_cloud/word_cloud_{data.user_id}.jpg')

    return Chain(data).text('你的词云是：').image(f'{curr_dir}/../../resource/word_cloud/word_cloud_{data.user_id}.jpg')