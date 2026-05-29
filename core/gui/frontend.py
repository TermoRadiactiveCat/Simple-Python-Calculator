# Simple Python Calculator - with open source code.
# Copyright (c) 2026 Yaroslav.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITHESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from typing import Any, List, Optional

from PyQt5.QtWidgets import QGridLayout, QMainWindow, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget

from core.event.events import CustomLineEdit

class Frontend:
    """
        The class of the application's GUI.

        Args:
            app (Any): The main class of the application.
            parent (Optional[QMainWindow]): The main window of the application.
    """
    def __init__(self, app: Any, parent: Optional[QMainWindow] = None) -> None:
        self.app = app
        self.parent = parent

        self.numbers: List[int] = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
        self.operations: List[str] = [["+", "-"], ["*", "/"], ["//", "%"]]

    def frame_container(self) -> None:
        """
            Creates layouts for the GUI elements.
        """
        self.central = QWidget()
        self.parent.setCentralWidget(self.central)
        self.central.setStyleSheet("""
            QWidget {
                background-color: #121212; 
                border-radius: 5px;
            }
        """)

        self.main_layout = QVBoxLayout(self.central)
        self.main_layout.setContentsMargins(5, 5, 5, 5)

        self.title_frame = QHBoxLayout()
        self.title_frame.setContentsMargins(5, 5, 5, 5)

        self.display_frame = QHBoxLayout()
        self.display_frame.setContentsMargins(5, 5, 5, 5)

        self.central_frame = QHBoxLayout()
        self.central_frame.setContentsMargins(5, 5, 5, 5)

        self.numpad_frame = QGridLayout()
        self.numpad_frame.setContentsMargins(5, 5, 5, 5)

        self.operation_frame = QGridLayout()
        self.operation_frame.setContentsMargins(5, 5, 5, 5)

    def create_frontend(self, app_name: str = "Application") -> None:
        """
            Creates GUI elements of the application.
        """
        self.app_name = QLabel(app_name, self.parent)
        self.app_name.setStyleSheet("""
            QLabel {
                background-color: #121212; 
                border-radius: 5px; 
                color: #FFFFFF; 
                font-family: SegoeUI; 
                font-size: 12pt;
            }
        """)
        self.app_name.setFixedHeight(20)
        self.title_frame.addWidget(self.app_name, stretch=1)

        self.main_line = CustomLineEdit(self.parent, app=self.app)
        self.main_line.textChanged.connect(self.app.get_arguments)
        self.main_line.setStyleSheet("""
            QLineEdit {
                background-color: #121212; 
                border: 2px solid #212121; 
                border-color: #212121; 
                border-radius: 5px; 
                color: #FFFFFF; 
                font-family: SegoeUI; 
                font-size: 15pt;
            }

            QLineEdit::hover {
                border-color: #3D3D3D;
            }
        """)
        self.main_line.setFixedHeight(40)
        self.display_frame.addWidget(self.main_line, stretch=1)

        self.clear_button = QPushButton("<", self.parent)
        self.clear_button.clicked.connect(self.app.calculator.clear_input)
        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: #1E1E1E; 
                border-radius: 5px; 
                color: #FFFFFF; 
                font-family: SegoeUI; 
                font-size: 15pt;
            }

            QPushButton::hover {
                background-color: #3D3D3D;
            }
        """)
        self.clear_button.setFixedWidth(70)
        self.clear_button.setFixedHeight(50)
        self.display_frame.addWidget(self.clear_button, stretch=0)

        self.point_button = QPushButton(".", self.parent)
        self.point_button.clicked.connect(lambda: self.app.on_button_clicked("."))
        self.point_button.setStyleSheet("""
            QPushButton {
                background-color: #1E1E1E; 
                border-radius: 5px; 
                color: #FFFFFF; 
                font-family: SegoeUI; 
                font-size: 15pt;
            }

            QPushButton::hover {
                background-color: #3D3D3D;
            }
        """)
        self.point_button.setFixedWidth(50)
        self.point_button.setFixedHeight(50)
        self.display_frame.addWidget(self.point_button, stretch=0)

        for row in range(3):
            for col in range(3):
                num = self.numbers[row][col]
                button = QPushButton(str(num), self.parent)
                button.clicked.connect(lambda _, n=num: self.app.on_button_clicked(n))
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #0000FF; 
                        border-radius: 5px; 
                        color: #FFFFFF; 
                        font-family: SegoeUI; 
                        font-size: 15pt; 
                    }

                    QPushButton::hover {
                        background-color: #137FFD; 
                    }
                """)
                button.setFixedWidth(50)
                button.setFixedHeight(50)
                self.numpad_frame.addWidget(button, row, col)

        for row in range(3):
            for col in range(2):
                oper = self.operations[row][col]
                button = QPushButton(f"{self.operations[row][col]}", self.parent)
                button.clicked.connect(lambda _, op=oper: self.app.on_button_clicked(op))
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #0000FF; 
                        border-radius: 5px; 
                        color: #FFFFFF; 
                        font-family: SegoeUI; 
                        font-size: 15pt;
                    }

                    QPushButton::hover {
                        background-color: #137FFD;
                    }
                """)
                button.setFixedWidth(50)
                button.setFixedHeight(50)
                self.operation_frame.addWidget(button, row, col)

        self.zero_button = QPushButton("0", self.parent)
        self.zero_button.clicked.connect(lambda: self.app.on_button_clicked(0))
        self.zero_button.setStyleSheet("""
            QPushButton {
                background-color: #0000FF; 
                border-radius: 5px; 
                color: #FFFFFF; 
                font-family: SegoeUI; 
                font-size: 15pt;
            }

            QPushButton::hover {
                background-color: #137FFD;
            }
        """)
        self.zero_button.setFixedWidth(50)
        self.zero_button.setFixedHeight(50)
        self.numpad_frame.addWidget(self.zero_button, 4, 0)

        self.result_button = QPushButton("=", self.parent)
        self.result_button.clicked.connect(self.app.calculator.calculate)
        self.result_button.setStyleSheet("""
            QPushButton {
                background-color: #0000FF; 
                border-radius: 5px; 
                color: #FFFFFF; 
                font-family: SegoeUI; 
                font-size: 15pt;
            }

            QPushButton::hover {
                background-color: #137FFD;
            }
        """)
        self.result_button.setFixedHeight(50)
        self.numpad_frame.addWidget(self.result_button, 4, 1, 1, 2)

        self.degree_button = QPushButton("**", self.parent)
        self.degree_button.clicked.connect(lambda: self.app.on_button_clicked("**"))
        self.degree_button.setStyleSheet("""
            QPushButton {
                background-color: #0000FF; 
                border-radius: 5px; 
                color: #FFFFFF; 
                font-family: SegoeUI; 
                font-size: 15pt;
            }

            QPushButton::hover {
                background-color: #137FFD;
            }
        """)
        self.degree_button.setFixedHeight(50)
        self.operation_frame.addWidget(self.degree_button, 4, 0, 1, 2)

        self.central_frame.addLayout(self.numpad_frame)
        self.central_frame.addLayout(self.operation_frame)

        self.main_layout.addLayout(self.title_frame)
        self.main_layout.addLayout(self.display_frame)
        self.main_layout.addLayout(self.central_frame)
