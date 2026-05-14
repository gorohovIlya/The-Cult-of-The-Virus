init python:
    # Git puzzle
    win_order = ['pbw branch', 'pbw switch helen_alive', 
        'pbw restore --staged helen.life', 'pbw restore helen.life']

    all_items = ['pbw branch', 'pbw switch helen_alive', 
        'pbw restore --staged helen.life', 'pbw restore helen.life', 'pbw add .', 
            'pbw push origin main', 'pbw reset HEAD emma.life']

    player_results = [None, None, None, None]

    def item_dragged(drags, drop):
        drag = drags[0]
        drag_id = drag.drag_name
        
        source_slot_index = -1
        if drag_id in player_results:
            source_slot_index = player_results.index(drag_id)

        if not drop:
            if source_slot_index != -1:
                player_results[source_slot_index] = None
                renpy.restart_interaction()
            return

        if drop.drag_name.startswith("slot_"):
            target_slot_index = int(drop.drag_name.split("_")[1])
            occupant_id = player_results[target_slot_index]

            if occupant_id is not None:
                if source_slot_index != -1:
                    player_results[source_slot_index] = occupant_id
            else:
                if source_slot_index != -1:
                    player_results[source_slot_index] = None

            player_results[target_slot_index] = drag_id
            renpy.restart_interaction()