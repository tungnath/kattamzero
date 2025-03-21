import itertools

hit_list = [[1, 2, 3], [1, 4, 7], [2, 5, 8], [3, 6, 9], [7, 8, 9], [4, 5, 6], [1, 5, 9], [3, 5, 7]]


def process_player_turn(number, current_player, current_player_tiles: list[int]) -> dict:
    tmp_p1 = list(itertools.combinations(current_player_tiles, 3))

    for tmp_item in tmp_p1:
        for item in hit_list:
            if set(tmp_item) == set(item):
                win_message = f"{current_player} won it with pos {tmp_item}."
                print(win_message)
                return {'message': win_message, 'win': 1}

    return {'message': f"{current_player} clicked cell {number}", 'win': 0}


def run_game_exclusively():
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # hit_list = [[1, 2, 3], [1, 4, 7], [2, 5, 8], [3, 6, 9], [7, 8, 9], [4, 5, 6], [1, 5, 9], [3, 5, 7]]
    # rows = len(matrix)
    # cols = len(matrix[0])

    # positions used and mock positions for testing
    # pos_all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # pos_allowed_pl_1 = [2, 4, 5, 6, 8]
    # pos_allowed_pl_2 = [1, 3, 7, 9]

    pos_played_1 = []
    pos_played_2 = []

    # run it on - 2 pl iterations
    pl_turn = 1
    is_done = False
    turn_ctr = 1

    while not is_done:
        is_player_1_turn = pl_turn == 1
        std_ip = input(f"Player {'1' if is_player_1_turn else '2'}, your chance : ")

        if (std_ip.isdigit() and 0 < int(std_ip) < 10
                and (int(std_ip) not in (set(pos_played_1) | set(pos_played_2)))
                and ((is_player_1_turn and int(std_ip) not in pos_played_1) or
                     (not is_player_1_turn and int(std_ip) not in pos_played_2))):

            pos_sel = int(std_ip)
            print(f" valid input is  {pos_sel}")

            if is_player_1_turn:
                print(f"Pl 1 in turn no. {turn_ctr}")
                if turn_ctr < 9:
                    # random mock data based testing
                    # pos_sel = pos_allowed_pl_1.pop(random.randrange(len(pos_allowed_pl_1)))
                    # pos_played_1.append(pos_sel)

                    pos_played_1.append(pos_sel)

                    if len(pos_played_1) >= 3:
                        tmp_p1 = list(itertools.combinations(pos_played_1, 3))
                        for tmp_item in tmp_p1:
                            for item in hit_list:
                                if set(tmp_item) == set(item):
                                    print(f"Player 1 won it with pos {tmp_item}. Now exiting")
                                    return

                    turn_ctr = turn_ctr + 1
                    pl_turn = 2
                else:
                    is_done = True
            else:
                print(f"Pl 2 in turn no. {turn_ctr}")
                if turn_ctr < 9:
                    # random mock data based testing
                    # pos_sel = pos_allowed_pl_2.pop(random.randrange(len(pos_allowed_pl_2)))
                    # pos_played_2.append(pos_sel)

                    pos_played_2.append(pos_sel)

                    if len(pos_played_2) >= 3:
                        tmp_p1 = list(itertools.combinations(pos_played_2, 3))
                        for tmp_item in tmp_p1:
                            for item in hit_list:
                                if set(tmp_item) == set(item):
                                    print(f"Player 2 won it with pos {tmp_item}. Now exiting")
                                    return

                    turn_ctr = turn_ctr + 1

                    pl_turn = 1
                else:
                    is_done = True

        else:
            continue


