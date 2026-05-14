init python:
    #Find the correct way puzzle

    all_directions = {'left': _('Налево'),
                        'left45deg': _('Налево под 45°'), 
                        'straight': _('Прямо'), 
                        'right45deg': _('Направо под 45°'),
                        'right': _('Направо')}

    winning_sequence = ['left', 'straight', 'left', 'right', 
                            'right45deg', 'straight']
    player_sequence = []

    def button_clicked(btn_name):
        global player_sequence
        player_sequence.append(btn_name)
        store.clicks_made += 1

        if store.clicks_made == 6:
            renpy.hide_screen("find_the_correct_way_puzzle")
            if player_sequence == winning_sequence:
                renpy.jump("a31")
            else:
                renpy.jump("a47")
        else:
            renpy.restart_interaction()