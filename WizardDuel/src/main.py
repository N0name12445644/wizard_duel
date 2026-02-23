from game_logic import Deck
from Player import Player
from effects import apply_effect
import random

CARDS_PATH = "data/cards.json"


def setup_game():
    print("=== Setting up the game ===")

    cat = Player("Cat", 30)
    dog = Player("Dog", 30)


    cat_deck = Deck(CARDS_PATH)
    dog_deck = Deck(CARDS_PATH)


    cat_deck.build_from_json(deck_size=10)
    dog_deck.build_from_json(deck_size=10)

    print("Decks created.\n")
    return cat, dog, cat_deck, dog_deck


def print_hand(player):
    print(f"\n{player.name}'s hand:")

    if player.hand.size == 0:
        print("  (empty)")
        return

    current = player.hand.head
    index = 1

    while True:
        card = current.card
        print(f"  {index}. {card.name}  |  {card.effect_type} ({card.power})")
        index += 1
        current = current.next

        if current is player.hand.head:
            break


def player_select_card(player):

    if player.hand.size == 0:
        print("You have no cards to play.")
        return None

    print_hand(player)

    while True:
        choice = input("Choose a card number: ")

        if not choice.isdigit():
            print("Enter a valid number.")
            continue

        choice = int(choice)

        if choice < 1 or choice > player.hand.size:
            print("Choice out of range.")
            continue


        current = player.hand.head
        for _ in range(choice - 1):
            current = current.next

        return current


def enemy_play_card(enemy):
    """Случайный выбор карты для бота."""
    if enemy.hand.size == 0:
        print(f"{enemy.name} has no cards to play.")
        return None

    steps = random.randint(0, enemy.hand.size - 1)

    current = enemy.hand.head
    for _ in range(steps):
        current = current.next

    return current


def main():
    cat, dog, cat_deck, dog_deck = setup_game()

    current_player = cat
    current_deck = cat_deck
    enemy = dog
    enemy_deck = dog_deck

    print("=== Game Start ===")


    while cat.health > 0 and dog.health > 0:

        print("\n=== New Turn ===")
        print(f"{cat.name} HP: {cat.health}")
        print(f"{dog.name} HP: {dog.health}")


        cards_to_draw = random.randint(2, 3)
        for _ in range(cards_to_draw):
            current_player.draw_from_deck(current_deck)

        print(f"{current_player.name} draws {cards_to_draw} cards.")


        removed = current_player.hand.remove_random()
        if removed:
            print(f"{current_player.name} randomly discards {removed.name}.")


        if current_player is cat:
            print("\nYour turn:")
            card_node = player_select_card(cat)
        else:
            print(f"\n{dog.name}'s turn:")
            card_node = enemy_play_card(dog)

        if card_node is not None:
            card = card_node.card


            apply_effect(card, current_player, enemy)


            current_player.hand.remove_node(card_node)


            current_deck.discard(card)


        if cat.health <= 0 or dog.health <= 0:
            break


        if current_player is cat:
            current_player = dog
            enemy = cat
            current_deck = dog_deck
            enemy_deck = cat_deck
        else:
            current_player = cat
            enemy = dog
            current_deck = cat_deck
            enemy_deck = dog_deck


    print("\n=== GAME OVER ===")
    if cat.health > 0:
        print("Cat wins!")
    else:
        print("Dog wins!")


if __name__ == "__main__":
    main()
