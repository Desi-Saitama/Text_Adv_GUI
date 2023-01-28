import api

import openai

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLineEdit)
from PySide6.QtGui import QFont

from qt_material import apply_stylesheet

story = "You wake up in a strange room. You have no idea how you got here or where you are. You are surrounded by unfamiliar objects and you feel disoriented and confused. You see a door to your left and a window to your right. You are unsure of what to do next. Do you go to the door or the window?"

openai.api_key = api.api_key1

def generate_description(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

class AiTextGame(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Text Adventure Game")
        self.setGeometry(0, 0, 800, 600)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1200, 900)

        #create a TextBox
        self.text = QTextEdit()
        self.text.setReadOnly(True)
        self.text.setFont(QFont('Times', 20))
        self.text.setText(f"{story}\n\n")

        #creating a input field
        self.input_field = QLineEdit(self)
        self.input_field.setFixedSize(800, 50)
        self.input_field.setFont(QFont('Arial', 20))

        #creating the button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setFixedSize(100, 50)
        self.submit_button.clicked.connect(self.Action)
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setFixedSize(100, 50)
        self.exit_button.clicked.connect(self.close)

        #creating the button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.exit_button)

        #creating the main layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.text)
        main_layout.addWidget(self.input_field)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    #function that creates new story
    def Action(self):
        action = self.input_field.text()
        prompt = f"You {action}."
        description = generate_description(prompt)
        self.text.append(description)
        self.input_field.setText("")

if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app, theme='dark_red.xml',)
    game = AiTextGame()
    game.show()
    app.exec()