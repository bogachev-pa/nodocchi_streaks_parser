# Tenhou win/lose streaks parser

Parser for json files from nodocchi.moe that finds best streaks of a player.

## How to run it

Download json:

`wget -O data/<player_name>.json https://nodocchi.moe/api/listuser.php?name=<player_name>`

Run:

`python nodocchi_json_streaks.py -p <player_name>`

## Sample output

```
Max streaks for player Legenda:
1st: 5
2nd: 5
3rd: 5
4th: 4
1st or 2nd: 15
Without 4th: 15
3rd or 4th: 9
```
