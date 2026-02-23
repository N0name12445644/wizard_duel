def apply_effect(card, user, enemy):

    effect = card.effect_type

    if effect == "attack":
        enemy.health -= card.power
        print(f"{user.name} deals {card.power} damage to {enemy.name} using {card.name}!")
        return


    elif effect == "heal":
        user.health += card.power
        print(f"{user.name} gains {card.power} HP using {card.name}!")
        return


    elif effect == "skip":
        enemy.skip_next_turn = True
        print(f"{user.name} forces {enemy.name} to skip their next turn using {card.name}!")
        return


    elif effect == "steal":
        stolen_card = enemy.hand.remove_random()

        if stolen_card is None:
            print(f"{user.name} tried to steal a card from {enemy.name}, but their hand is empty!")
            return

        user.hand.add_card(stolen_card)
        print(f"{user.name} steals a card ({stolen_card.name}) from {enemy.name} using {card.name}!")
        return


    elif effect == "double_turn":
        user.extra_turn = True
        print(f"{user.name} gains an extra turn using {card.name}!")
        return


    else:
        print(f"Unknoun effect: {effect}")