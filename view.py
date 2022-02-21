from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QLabel, QGroupBox, QPlainTextEdit
import sys
from calculator import Calculator
from rules import Rules


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.calculator = Calculator()
        self.rules = Rules()
        self.cards = {}
        for axie in self.calculator.my_axies:
            self.cards[axie.axie_class] = []
        self.enemy_class = None
        self.axie = None
        self.calculated_damage = 0
        self.is_debuffed = False
        self.enemy_buttons = []
        self.initUI()

    def select_axie(self, axie):
        print(f'selected axie: {axie.axie_class}')
        self.axie = axie

    def axie_button(self, axie, y):
        # creating a push button
        button = QPushButton(self)

        # setting geometry of button
        button.setGeometry(10, y, 120, 80)

        # adding action to a button
        button.clicked.connect(lambda: self.select_axie(axie))

        image = QIcon(axie.image)
        button.setIcon(image)
        button.setIconSize(QSize(button.width(), button.height()))

        return button

    def select_card(self, card, axie):
        print(f'selected card: {card.card_name}')
        self.cards[axie.axie_class].append(card)

    def screen_card_buttons(self, axie):
        pass

    def card_button(self, card, x, y, axie):
        # creating a push button
        button = QPushButton("", self)

        # setting geometry of button
        button.setGeometry(x, y, 80, 100)

        # adding action to a button
        button.clicked.connect(lambda: self.select_card(card, axie))
        image = QIcon(card.image)
        button.setIcon(image)
        button.setIconSize(QSize(button.width(), button.height()))

        # # setting image to the button
        button.setStyleSheet("QPushButton:hover { background-color: red }")

        return button

    def select_enemy_class(self, button, axie_class, counter):
        if self.enemy_class is None:
            self.enemy_class = axie_class
        elif self.enemy_class == axie_class:
            self.enemy_class = None
        else:
            return

        print(f'selected enemy class: {axie_class}')
        self.enemy_buttons[counter] = not self.enemy_buttons[counter]
        if self.enemy_buttons[counter]:
            button.setStyleSheet("QPushButton { background-color: green }")
        else:
            button.setStyleSheet("")

    def enemy_button(self, axie_class, x, y, counter):
        # creating a push button
        button = QPushButton(axie_class, self)

        # setting geometry of button
        button.setGeometry(x, y, 100, 50)

        # adding action to a button
        button.clicked.connect(lambda: self.select_enemy_class(button, axie_class, counter))

        return button

    def calculate_button(self, damage_label):

        # creating a push button
        button = QPushButton('Calculate', self)

        # setting geometry of button
        button.setGeometry(500, 740, 100, 50)

        # adding action to a button
        button.clicked.connect(lambda: self.calculate(damage_label))

        return button

    def reset_button(self, damage_label, debuff_button):

        # creating a push button
        button = QPushButton('Reset', self)

        # setting geometry of button
        button.setGeometry(500, 670, 100, 50)

        # adding action to a button
        button.clicked.connect(lambda: self.reset(damage_label, debuff_button))

        return button

    def calculate(self, damage_label):
        total_damage = 0

        string = ''
        for axie in self.calculator.my_axies:
            if len(self.cards[axie.axie_class]) == 0:
                string += "0\n"
            else:
                damages = self.calculator.calculates(self.enemy_class, self.cards, axie, self.is_debuffed)
                print(damages)
                for damage in damages:
                    string += f'{damage}' + "+"
                string += " = " + f'{sum(damages)}' + "\n"
                total_damage += sum(damages)
        string += f"TOTAL DAMAGE: {total_damage}"
        damage_label.setPlainText(string)

    def reset(self, damage_label, debuff_button):
        self.axie = None
        self.calculated_damage = ''
        self.is_debuffed = False
        damage_label.setPlainText(f'0')
        debuff_button.setText(f'Debuffed: {self.is_debuffed}')
        debuff_button.setStyleSheet(f"")
        self.cards = {}
        for axie in self.calculator.my_axies:
            self.cards[axie.axie_class] = []

    def is_debuffed_button(self):

        # creating a push button
        button = QPushButton(f'Debuffed: {self.is_debuffed}', self)

        # setting geometry of button
        button.setGeometry(20, 705, 100, 50)

        # adding action to a button
        button.clicked.connect(lambda: self.click_debuff(button))

        return button

    def click_debuff(self, button):
        self.is_debuffed = not self.is_debuffed
        print("Enemy debuffed:" + f'{self.is_debuffed}')
        button.setText(f'Debuffed: {self.is_debuffed}')

        if self.is_debuffed:
            button.setStyleSheet(f"background-color: blue; color:white")
        else:
            button.setStyleSheet(f"")

    def screen(self):

        dummy_buttons = []
        y = 400

        for index, axie in enumerate(self.calculator.my_axies):
            button = QPushButton(self)
            button.setGeometry(10, y + index * 80, 80, 60)
            image = QIcon(axie.image)
            button.setIcon(image)
            button.setIconSize(QSize(button.width(), button.height()))
            dummy_buttons.append(button)

    def initUI(self):
        self.setGeometry(1250, 40, 700, 1000)
        self.setWindowTitle("Axie Calculator")

        self.plant_button = self.axie_button(self.calculator.my_axies[0], 10)

        plant_cards = []
        # setting cards

        x = 100
        y = 10
        for index, card in enumerate(self.calculator.my_axies[0].cards):
            plant_cards.append(self.card_button(card, x + (index + 1) * 110, y, self.calculator.my_axies[0]))

        self.dusk_button = self.axie_button(self.calculator.my_axies[1], 140)

        dusk_cards = []

        x = 100
        y = 130
        for index, card in enumerate(self.calculator.my_axies[1].cards):
            dusk_cards.append(self.card_button(card, x + (index + 1) * 110, y, self.calculator.my_axies[1]))

        self.reptile_button = self.axie_button(self.calculator.my_axies[2], 260)

        reptile_cards = []
        x = 100
        y = 250
        for index, card in enumerate(self.calculator.my_axies[2].cards):
            reptile_cards.append(self.card_button(card, x + (index + 1) * 110, y, self.calculator.my_axies[2]))

        self.screen()

        # enemy_class
        x = 150
        y = 650

        enemy_buttons = []
        counter = 0
        for y_index, group in enumerate(self.rules.class_group):
            for x_index, class_ in enumerate(group):
                enemy_buttons.append(self.enemy_button(class_, x + x_index * 105, y + y_index * 55, counter))
                self.enemy_buttons.append(False)
                counter += 1

        damage_label = QPlainTextEdit(f'{self.calculated_damage}', self)

        # setting geometry of button
        damage_label.setGeometry(30, 840, 590, 150)
        damage_label.setFont(QFont('Arial', 20))

        debuff_button = self.is_debuffed_button()
        calculate_button = self.calculate_button(damage_label)
        reset_button = self.reset_button(damage_label, debuff_button)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
