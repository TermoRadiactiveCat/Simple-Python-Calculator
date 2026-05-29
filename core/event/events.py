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

from typing import Any, Optional

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QMainWindow

class CustomLineEdit(QLineEdit):
    """
        Input protection class (disallows keyboard input for eval() calculations, except Backspace).

        Args:
            parent (Optional[QMainWindow]): The main window of the application.
            app (Any): The main class of the application.
    """
    def __init__(self, parent: Optional[QMainWindow] = None, app: Any = None) -> None:
        super().__init__(parent)
        self.app = app

    def keyPressEvent(self, event) -> None:
        """
            Controls the keyboard input (eval() protect).
        """
        if event.key() == Qt.Key_Backspace:
            if self.hasSelectedText():
                self.clear()
            else:
                cursor_pos = self.cursorPosition()
                if cursor_pos > 0:
                    self.backspace()
            return
