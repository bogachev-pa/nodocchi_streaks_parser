#!/usr/bin/env python3

import json
import itertools
import os
import random
import time

from optparse import OptionParser


STREAK_1 = 0
STREAK_2 = 1
STREAK_3 = 2
STREAK_4 = 3
STREAK_12 = 4
STREAK_123 = 5
STREAK_34 = 6

STREAK_TYPES = 7

streak_current = [0] * STREAK_TYPES
streak_max = [0] * STREAK_TYPES


def parse_streak(game, player, places, index):
    global streak_current
    global streak_max

    streak_ok = False

    for place in places:
        if game[place] == player:
            streak_ok = True
            break

    if streak_ok:
        streak_current[index] += 1
        if streak_current[index] >= streak_max[index]:
            streak_max[index] = streak_current[index]
    else:
        streak_current[index] = 0


def find_streaks(json_data, player):
    global streak_max

    games = json_data["list"]

    for game in games:
        # parse only 4-man games
        if int(game["playernum"]) != 4:
            continue

        # parse only second dan and phoenix lobby
        if int(game["playerlevel"]) < 2:
            continue

        parse_streak(game, player, ["player1"], STREAK_1)
        parse_streak(game, player, ["player2"], STREAK_2)
        parse_streak(game, player, ["player3"], STREAK_3)
        parse_streak(game, player, ["player4"], STREAK_4)
        parse_streak(game, player, ["player1", "player2"], STREAK_12)
        parse_streak(game, player, ["player1", "player2", "player3"], STREAK_123)
        parse_streak(game, player, ["player3", "player4"], STREAK_34)

    print("Max streaks for player {}:".format(player))
    print("1st: {}".format(streak_max[STREAK_1]))
    print("2nd: {}".format(streak_max[STREAK_2]))
    print("3rd: {}".format(streak_max[STREAK_3]))
    print("4th: {}".format(streak_max[STREAK_4]))
    print("1st or 2nd: {}".format(streak_max[STREAK_12]))
    print("Without 4th: {}".format(streak_max[STREAK_123]))
    print("3rd or 4th: {}".format(streak_max[STREAK_34]))


def main():
    parser = OptionParser()

    parser.add_option('-p', '--player',
                      type='string',
                      help='Player name')

    opts, _ = parser.parse_args()
    player = opts.player

    if player == None:
        print("Please specify player with -p option")
        return

    data_file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'data',
        '{}.json'.format(player)
    )

    if not os.path.exists(data_file_path):
        print("We don't have json data for player {}".format(player))
        print("Download it from nodocchi using the following command:")
        print("wget -O data/<player_name>.json https://nodocchi.moe/api/listuser.php?name=<player_name>")
        return

    json_data = None

    with open(data_file_path, 'r') as f:
        json_data = json.load(f)

    find_streaks(json_data, player)


if __name__ == '__main__':
    main()
