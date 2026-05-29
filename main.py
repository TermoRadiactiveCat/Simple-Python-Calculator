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

import sys

from typing import Optional
from functools import lru_cache

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    """
        The class of the main application window.

        Args:
            main (Optional[QMainWindow]): The class of the main PyQt5 application window.
    """
    def __init__(self, main: Optional[QMainWindow] = None) -> None:
        super().__init__()

        self.main = main

        self._WIDTH: int = 300
        self._HEIGHT: int = 330

        self.screen_position.center_window(self, self._WIDTH, self._HEIGHT)

        self.application.start()

    @property
    @lru_cache(maxsize=None)
    def application(self):
        """
            Imports the main class of the application.

            Returns:
                Application: The main class of the application.
        """
        from core.app.application import Application
        return Application(parent=self)

    @property
    @lru_cache(maxsize=None)
    def screen_position(self):
        """
            Imports the class of centralization the application window.

            Returns:
                ScreenPosition: The class of centralization the application window.
        """
        from core.screen.screen_position import ScreenPosition
        return ScreenPosition()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(app)
    window.setWindowFlag(Qt.FramelessWindowHint)
    window.setAttribute(Qt.WA_TranslucentBackground)
    window.setStyleSheet("""
        QMainWindow {
            background-color: #121212;
            border-radius: 5px;
            color: #FFFFFF; 
            font-family: SegoeUI; 
            font-size: 15pt; 
        }
    """)
    window.show()

    sys.exit(app.exec())
