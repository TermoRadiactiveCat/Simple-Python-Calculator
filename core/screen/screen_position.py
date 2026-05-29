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

from screeninfo import get_monitors

from typing import Optional, Tuple

from PyQt5.QtWidgets import QMainWindow

class ScreenPosition:
    """
        The class of centralization the application window.
    """
    def __init__(self) -> None:
        pass

    def center_window(self, window: Optional[QMainWindow] = None, 
            width: int = 0, height: int = 0
        ) -> None:
            """
                Centralizes the application window on the monitor.

                Args:
                    window (Optional[QMainWindow]): The link to the application window.
                    width (int): The width of the window.
                    height (int): The height of the window.
            """
            try:
                monitor_width, monitor_height = self.get_monitor_size()
                window_x = max(0, (monitor_width // 2) - (width // 2))
                window_y = max(0, (monitor_height // 2) - (height // 2))
                window.setGeometry(window_x, window_y, width, height)
            except Exception:
                pass

    def get_monitor_size(self) -> Tuple[int]:
        """
            Returns the tuple with the monitor size.

            Returns:
                Tuple[int]: The tuple of the monitor size.
        """
        try:
            monitor = get_monitors()[0]
            monitor_width = monitor.width
            monitor_height = monitor.height
            return monitor_width, monitor_height
        except Exception:
            pass
