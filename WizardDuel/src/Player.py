from game_logic import Card


class HandNode:
    def __init__(self, card):
        self.card = card
        self.next = None
        self.prev = None


class Hand:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_card(self, card):
        new_node = HandNode(card)

        if self.head is None:

            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:

            tail = self.head.prev

            tail.next = new_node
            new_node.prev = tail

            new_node.next = self.head
            self.head.prev = new_node

        self.size += 1

    def remove_node(self, node):
        if self.size == 0:
            return

        if self.size == 1:
            self.head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

            if node is self.head:
                self.head = node.next

        self.size -= 1

    def remove_random(self):

        if self.size == 0:
            return None

        import random
        steps = random.randint(0, self.size - 1)

        current = self.head
        for _ in range(steps):
            current = current.next

        self.remove_node(current)
        return current.card


class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.hand = Hand()
        self.skip_next_turn = False
        self.extra_turn = False

    def draw_from_deck(self, deck, max_hand_size=5):

        card = deck.draw_card()
        if card is None:
            return

        if self.hand.size >= max_hand_size:
            deck.discard(card)
            return

        self.hand.add_card(card)