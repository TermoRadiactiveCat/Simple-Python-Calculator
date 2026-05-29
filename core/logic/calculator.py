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

from typing import Any

class Calculator:
    """
        The main class of the application's business logic.

        Args:
            app (Any): The main class of the application.
    """
    def __init__(self, app: Any) -> None:
        self.app = app

    def is_valid_expression(self, text: str) -> bool:
        """
            Checks the input for correctness.

            Args:
                text (str): The user's input (through the buttons).

            Returns:
                bool: True if text is correct, False otherwise.
        """
        if not text:
            return True

        if text[0] in "+*/%":
            return False

        if text[-1] in "+-*/%":
            return False

        allowed_double_ops = {"**", "//", ".."}
        operators = "+-*/%."

        for i in range(len(text)-1):
            if i+1 < len(text) and text[i:i+2] in allowed_double_ops:
                continue

            if text[i] in operators and text[i+1] in operators:
                return False

        if text[-1] in operators:
            return False

        return True

    def get_validation_result(self, text: str) -> bool:
        """
            Returns boolean value.

            Args:
                text (str): The user's input (through the buttons).

            Returns:
                bool: True if text is correct, False otherwise.
        """
        return self.is_valid_expression(text)

    def on_button_clicked(self, text: str) -> None:
        """
            Inserts the pressed symbol (number/operator) to the input line.

            Args:
                text (str): The user's input (through the buttons).
        """
        self.app.frontend.main_line.insert(text)

    def calculate(self) -> None:
        """
            Returns the final result of the calculation (eval() with the keyboard protect).
        """
        expr = self.app.frontend.main_line.text()
        try:
            result = eval(expr)
            self.app.frontend.main_line.setText(str(result))
            self.app.set_input_style(True)
        except Exception:
            self.app.frontend.main_line.setText("Error")
            self.app.set_input_style(False)

    def clear_input(self) -> None:
        """
            Clears the input line.
        """
        self.app.frontend.main_line.clear()

