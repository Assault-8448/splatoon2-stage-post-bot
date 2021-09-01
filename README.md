# Splatoon2のステージ情報を出力するBot

自分用で開発しています。  
以下の情報をEmbedにしてコマンドが実行されたチャンネルで**APIを毎度叩き**発言します。流石にこの仕様は色々と問題があるのでそのうちどうにかします。  

- 現在のステージ情報
	- ナワバリバトル
	- ガチマッチ（モードも）
	- リーグマッチ（モードも）
	- サーモンラン（ブキも）

## どうやって使うの？

```bash
git clone git@github.com:Assault-8448/splatoon2-stage-post-bot.git
cd splatoon2-stage-post-bot
pip install -r requirements.txt
python app.py
```

で実行してください。

**初回はconfig.ymlにトークンを記述する必要があります！**

## バグあるけど？

バグを発見した際はDiscordアカウント「Assault#6639」までDMお願いします。  
あるいはIssue建てたりPull Requestしてください。

## 開発環境

- Windows 10 Home 64bit 21H1 19043.1165
- ArchWSL (5.4.72-microsoft-standard-WSL2)
- Python 3.9.6, discord.py 1.7.3

