init python:
    import random
    # AntColonyAlgorithm puzzle
    num_ants = 10
    success_probability = 0
    ants = [f"ants_{i}" for i in range(num_ants)]
    ants_positions = {}
    ants_found = []

    def setup_ant_puzzle():
        global ants_found, ants_positions, success_probability
        ants_found.clear()
        ants_positions.clear()
        success_probability = random.uniform(0, 1)
        for ant in ants:
            ants_positions[ant] = (random.randint(100, 1500), 
                                        random.randint(600, 1000))

    def check_win():
        if len(ants_found) == num_ants:
            if 60 <= store.ants_time_left <= 90:
                renpy.jump('ant_puzzle_success')
            elif 30 <= store.ants_time_left < 60:
                store.state = 1
                renpy.jump('ant_puzzle_prob_success')
            elif 15 <= store.ants_time_left < 30:
                store.state = 2
                renpy.jump('ant_puzzle_prob_success')
            elif 5 <= store.ants_time_left < 15:
                store.state = 3
                renpy.jump('ant_puzzle_prob_success')
            else:
                renpy.jump('ant_puzzle_failure')

    def ant_clicked(ant):
        global ants_found
        ants_found.append(ant)
        check_win()

    def get_time_color():
        result = ''
        if 60 <= store.ants_time_left <= 90:
            result = '#00ff11'
        elif 30 <= store.ants_time_left < 60:
            result = '#eeff00'
        elif 15 <= store.ants_time_left < 30:
            result = '#ff6f00'
        else:
            result = '#ff0000'
        return result