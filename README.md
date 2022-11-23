> 让兔兔可以收集群友的消息并生成词云

- 兔兔在插件安装后，就会自动开始记录群友的聊天文本
- 发送 `兔兔查看词云` 或者 `兔兔查询词云` 就可以查看自己的词云
- 例子如下图所示：

![兔兔查询词云例子](https://raw.githubusercontent.com/hsyhhssyy/amiyabot-hsyhhssyy-wordcloud/master/example_image/word_cloud_example.jpg)

> 注意，为了让该插件可以正常工作，需要安装依赖 `wordcloud~=1.8.2.2`，插件内并不自带该依赖（因为太大了）

- 代码部署下部署：

    - 请在命令行执行 `pip install wordcloud`
    - 完成后请重启amiyabot

- 可执行文件部署：

    - 注意，使用此方法安装依赖，需要您对windows系统的cmd命令行操作有一定了解，插件仅对该方式提供有限的支持。
    - 想要在可执行文件部署的情况下使用该插件，需要您安装python。
    - 在cmd命令行执行 `pip install wordcloud` 安装依赖文件，如果只是出现了警告，可以暂时忽略。
    - 找到site-package目录的路径，方法如下：
        - 在cmd命令行下执行 `python -c 'import site; print(site.getsitepackages())'`
        - 系统会返回多个路径，在返回的路径中找到以site-packages结尾的那个路径，比如 `C:\\Python38\\lib\\site-packages`。复制这个路径（不包含引号）
    - 在amiyabot的resource文件夹下，用记事本打开文件python_support.yaml，如果该文件不存在就新建一个。
    - 找到并编辑sitePackagePath以开头的行，改为： `sitePackagePath: '[刚刚复制的路径]'`，如果不存在则新增此行。
        - 注意，上面的冒号后面有一个空格，且路径由单引号包围
        - 修改这个路径，将两个双斜杠 `\\` 替换为一个单斜杠 `\`
    - 比如按照上面那个例子路径修改的话，文件的内容就是
        ```
        sitePackagePath: 'C:\Python38\lib\site-packages'
        ```

        ![yaml文件内容](https://raw.githubusercontent.com/hsyhhssyy/amiyabot-hsyhhssyy-wordcloud/master/example_image/yaml_file_example.jpg)

    - 确认无误后请重启amiyabot，并查看启动时是否还有错误提示。
    - （话说你都安装了python了，不试试用代码部署amiyabot吗，这样本插件或者其他需要额外依赖的插件都好弄多了。）

- 如果不安装该依赖，兔兔只会收集群友的聊天文本，而无法生成词云图片。

> 其他注意事项

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
| 1.3  | 将底色改为白色更清晰一些 |
| 1.4  | 新增可执行文件部署的相关指引 |
| 1.5  | 将几个兔兔常用指令加入词云屏蔽词 |
