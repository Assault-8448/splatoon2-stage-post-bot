# 飽きたので開発止まってます

そのうちどうにかします。

# 自分用のアレ

自分用で開発しています。  
Splatoon2のステージ情報投げる奴つき（というかもともとメインがこいつ）ですがまともに開発してません。  
  
投げられる情報: 

- 現在のステージ情報
	- ナワバリバトル
	- ガチマッチ（モードも）
	- リーグマッチ（モードも）
	- サーモンラン（ブキも）

## どうやって入れんのこれ

```bash
git clone git@github.com:Assault-8448/splatoon2-stage-post-bot.git
cd splatoon2-stage-post-bot
pip install -r requirements.txt
python app.py
```

**初回はconfig.ymlにトークンを記述する必要があります！**

## バグあるけど？

バグを発見した際はDiscordアカウント「Assault#1892」までDMお願いします。  
多分どうにかします。

## 開発環境

- Windows 10 Home 64bit Insider Preview 10.0.19044.1586
- Alter Linux 5.17.1-zen1-1-zen
- Python 3.7.3, discord.py 1.7.3

