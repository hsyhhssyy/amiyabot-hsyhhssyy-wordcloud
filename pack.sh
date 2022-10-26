#!/bin/sh

zip -q -r amiyabot-hsyhhssyy-wordcloud-1.0.zip *
rm -rf ../../amiya-bot-v6/plugins/amiyabot-hsyhhssyy-wordcloud-1_0
mv amiyabot-hsyhhssyy-wordcloud-1.0.zip ../../amiya-bot-v6/plugins/
docker restart amiya-bot 