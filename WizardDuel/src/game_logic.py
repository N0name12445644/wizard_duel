from collections import deque
import json
import random

class Card:
     def __init__(self, name, effect_type, power, description):
         self.name = name
         self.effect_type = effect_type
         self.power = power
         self.description = description


class Deck:
    def __init__(self, path):
        self.cards = deque()
        self.discard_pile = []
        self.path = path

    def build_from_json(self, deck_size=10):
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)

        all_cards = []
        for card_dict in data:
            card = Card(
                card_dict["name"],
                card_dict["effect_type"],
                card_dict["power"],
                card_dict["description"]
            )
            all_cards.append(card)


        selected_cards = random.sample(all_cards, deck_size)


        for card in selected_cards:
            self.cards.append(card)

    def draw_card(self):

        if len(self.cards) == 0:
            if len(self.discard_pile) == 0:
                return None


            temp = list(self.discard_pile)
            self.discard_pile = []
            random.shuffle(temp)
            self.cards = deque(temp)

        return self.cards.popleft()

    def discard(self, card):

        self.discard_pile.append(card)

    def refill_from_discard(self):

        if len(self.discard_pile) == 0:
            return

        temp = list(self.discard_pile)
        random.shuffle(temp)
        self.cards = deque(temp)
        self.discard_pile = []
