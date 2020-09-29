# AntHive.IO sample bot in *Python*

## [Import](https://github.com/new/import) this sample bot.

## Requirements
- python2 or 3
- Set your username in [ANTHIVE](ANTHIVE) file.
- Push to your Github account.
- Do not push your code to sample bot repo.
- Register your bot at https://profile.anthive.io/bots

## Debug
- git push origin master
- Register a new version of your bot from latest commits
- Start new game at https://profile.anthive.io/new-game
- Replay game step by step:
  - View logs
  - Download step payload

### Run locally (not required)
```
python run.py
```

It will start localhost server on port :7070 **Do not change port**

```
curl -X 'POST' -d @payload.json http://localhost:7070
```

### [Rules](https://anthive.io/rules/) and [Leaderboard](https://anthive.io/leaderboard/)