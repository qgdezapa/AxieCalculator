from axie import Axie
from card import Card
from rules import Rules


class Calculator:

    def __init__(self):
        self.rules = Rules()
        self.my_plant_axie = Axie(
            [
                Card("October Treat", "images/october_treat.png", 0, 110, "plant"),
                Card("Vegetal Bite", "images/vegetal_bite.png", 30, 30, "plant"),
                Card("Disguise", "images/disguise.png", 20, 20, "bug"),
                Card("Gas Unleash", "images/gas_unleash.png", 20, 20, "plant"),
            ],
            "plant",
            "images/my_plant_axie.PNG",
            31
        )

        self.my_dusk_axie = Axie(
            [
                Card("Heart Break", "images/heart_break.png", 120, 20, "bird"),
                Card("Chomp", "images/chomp.png", 75, 50, "reptile"),
                Card("Disarm", "images/disarm.png", 100, 40, "reptile"),
                Card("Allergic Reaction", "images/allergic_reaction.png", 100, 30, "bug"),
            ],
            "dusk",
            "images/my_dusk_axie.PNG",
            27
        )

        self.my_reptile_axie = Axie(
            [
                Card("Bug Splat", "images/bug_splat.png", 110, 50, "bug"),
                Card("Chomp", "images/chomp.png", 75, 50, "reptile"),
                Card("Mystic Rush", "images/mystic_rush.png", 30, 0, "bug"),
                Card("Allergic Reaction", "images/allergic_reaction.png", 100, 30, "bug"),
            ],
            "reptile",
            "images/my_reptile_axie.PNG",
            31
        )

        self.my_axies = [
            self.my_plant_axie,
            self.my_dusk_axie,
            self.my_reptile_axie,
        ]

    def calculates(self, enemy_class, cards, axie, is_debuffed):


        ally_class = axie.axie_class
        cards = cards[ally_class]

        damages = []
        combo_bonus = False
        if len(cards) > 1:
            combo_bonus = True

        for card in cards:
            print(card.card_name)
            stab = 0
            if card.card_name == "Allergic Reaction" and is_debuffed:
                print("hello")

                # stab = 0.3
                card = Card("Allergic Reaction", "images/allergic_reaction.png", 130, 30, "bug")

            if card.card_name == "Bug Splat" and enemy_class == "bug":
                stab = 0.5

            stab += self.rules.check_axie_percentage(ally_class, card.card_class)
            stab += self.rules.check_card_percentage(card.card_class, enemy_class)
            stab += 1

            combo_damage = axie.axie_skill *0.55-12.5 if combo_bonus else 0
            damage = card.damage * stab + combo_damage

            damages.append(int(damage))

        return damages
