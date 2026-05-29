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

from typing import Optional
from functools import lru_cache

from PyQt5.QtWidgets import QMainWindow

class Application:
    """
        The main class of the application.

        Args:
            parent (Optional[QMainWindow]): The main window of the application.
    """
    def __init__(self, parent: Optional[QMainWindow] = None) -> None:
        self.parent = parent

        self._APP_NAME: str = "Simple Calculator:"

    def start(self) -> None:
        """
            Initializes the application (GUI).
        """
        self.frontend.frame_container()
        self.frontend.create_frontend(self._APP_NAME)

    @property
    @lru_cache(maxsize=None)
    def frontend(self):
        """
            Imports GUI class of the application.

            Returns:
                Frontend: The class of the application's GUI.
        """
        from core.gui.frontend import Frontend
        return Frontend(app=self, parent=self.parent)

    @property
    @lru_cache(maxsize=None)
    def calculator(self):
        """
            Imports the main business logic class of the application.

            Returns:
                Calculator: The main business logic class of the application.
        """
        from core.logic.calculator import Calculator
        return Calculator(app=self)

    def on_button_clicked(self, text) -> None:
        """
            The callback method.

            Args:
                text (str): The user's input (through the buttons).
        """
        self.calculator.on_button_clicked(str(text))

    def get_arguments(self) -> None:
        """
            Checks the input for correctness. Marks the input field in red 
                if a syntax error is detected, and disables result button.
        """
        text = self.frontend.main_line.text()
        is_valid = self.calculator.is_valid_expression(text)
        self.set_input_style(is_valid)
        self.frontend.result_button.setEnabled(is_valid)

    def set_input_style(self, is_valid: bool) -> None:
        """
            Marks the input field with a color according to the situation: 
                if a syntax error was detected, the color is red.

            Args:
                is_valid (bool): The sign for change the mark color.
        """
        color = "#FFFFFF" if is_valid else "#FF0000"
        border_color = "#212121" if is_valid else "#FF0000"
        style = f"""
            QLineEdit {{
                background-color: #121212; 
                border: 2px solid {border_color}; 
                border-radius: 5px; 
                color: {color}; 
                font-family: SegoeUI; 
                font-size: 15pt;
            }}
            QLineEdit::hover {{
                border-color: #3D3D3D;
            }}
        """
        self.frontend.main_line.setStyleSheet(style)
