> 让兔兔可以收集群友的消息并生成词云

- 兔兔在插件安装后，就会自动开始记录群友的聊天文本
- 发送 `兔兔查看词云` 或者 `兔兔查询词云` 就可以查看自己的词云
- 例子如下图所示：

![兔兔选助理例子](https://raw.githubusercontent.com/hsyhhssyy/amiyabot-hsyhhssyy-wordcloud/master/word_cloud_example.jpg)

> 注意，为了让该插件可以正常工作，需要安装依赖 `wordcloud~=1.8.2.2`

- 请在命令行执行 `pip install wordcloud`，插件内并不自带该依赖（因为太大了），
- 可执行文件部署的情况下，可能无法安装依赖，这种情况下无法使用本插件。
- 如果不安装该依赖，兔兔只会收集群友的聊天文本，而无法生成词云图片。
- 词云文件保存在resource文件夹下，升级插件无需备份
- 词云统计以用户为单位，因此如果一个用户同时在多个启用了本bot的群中，则展示的词云为多个群内聊天内容的合并统计。

> [项目地址:Github](https://github.com/hsyhhssyy/amiyabot-hsyhhssyy-wordcloud/)

> [遇到问题可以在这里反馈(Github)](https://github.com/hsyhhssyy/amiyabot-hsyhhssyy-wordcloud/issues/new/)

> [Logo作者:Sesern老师](https://space.bilibili.com/305550122)

|  版本   | 变更  |
|  ----  | ----  |
| 1.0  | 初版登录商店 |
| 1.1  | 适配新版插件商店 |
| 1.2  | 修复在默认字符集不是Utf-8的机器上加载会出错的问题 |
