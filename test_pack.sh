#!/bin/sh

zip -q -r amiyabot-hsyhhssyy-wordcloud-1.1.zip *
rm -rf ../../amiya-bot-v6/plugins/amiyabot-hsyhhssyy-wordcloud-1_1
mv amiyabot-hsyhhssyy-wordcloud-1.1.zip ../../amiya-bot-v6/plugins/
docker restart amiya-bot 