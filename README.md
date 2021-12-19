# 自分用のアレ

自分用で開発しています。  
Splatoon2のステージ情報投げる奴つきですがまともに開発してません。  
  
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

- Windows 11 Home 64bit Insider Preview 10.0.22518.1012
- ArchWSL (5.10.74.3-microsoft-standard-WSL2)
- Python 3.7.3, discord.py 1.7.3

