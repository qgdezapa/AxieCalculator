class Rules:

    def __init__(self):
        self.class_group = [
            ['reptile', 'plant', 'dusk'],
            ['aquaic', 'bird', 'dawn'],
            ['beast', 'bug', 'mech']
        ]

    def check_rules(self, ally_group, enemy_group):
        # if same class no extra damage
        if ally_group == enemy_group:
            return 0

        if ally_group == 0:
            if enemy_group == 1:
                return 1
            return -1

        if ally_group == 1:
            if enemy_group == 2:
                return 1
            return -1

        if ally_group == 2:
            if enemy_group == 0:
                return 1
            return -1

    def get_class_number(self, class_):
        for group, classes in enumerate(self.class_group):
            if class_ in classes:
                return group

    def check_axie_percentage(self, ally_class, card_class):


        if ally_class == card_class:
            return 0.10
        if ally_class == "dusk" and (card_class =="reptile" or card_class == "aquaic"):
            return 0.075

        return 0

    def check_card_percentage(self, ally_class, enemy_class):
        ally_group = self.get_class_number(ally_class)
        enemy_group = self.get_class_number(enemy_class)

        return self.check_rules(ally_group, enemy_group) * 0.15


