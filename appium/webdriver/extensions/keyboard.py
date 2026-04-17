#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict, Optional

from selenium.common.exceptions import UnknownMethodException
from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence

from ..mobilecommand import MobileCommand as Command


class Keyboard(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def hide_keyboard(self, key_name: Optional[str] = None, key: Optional[str] = None, strategy: Optional[str] = None) -> Self:
        """Hides the software keyboard on the device.

        In iOS, use `key_name` to press
        a particular key, or `strategy`. In Android, no parameters are used.

        Args:
            key_name: key to press
            key:
            strategy: strategy for closing the keyboard (e.g., `tapOutside`)

        Returns:
            Union['WebDriver', 'Keyboard']: Self instance
        """
        pass

    def is_keyboard_shown(self) -> bool:
        """Attempts to detect whether a software keyboard is present

        Returns:
            `True` if keyboard is shown
        """
        pass

    def keyevent(self, keycode: int, metastate: Optional[int] = None) -> Self:
        """Sends a keycode to the device.

        Android only.
        Possible keycodes can be found in http://developer.android.com/reference/android/view/KeyEvent.html.

        Args:
            keycode: the keycode to be sent to the device
            metastate: meta information about the keycode being sent

        Returns:
            Union['WebDriver', 'Keyboard']: Self instance
        """
        pass

    def press_keycode(self, keycode: int, metastate: Optional[int] = None, flags: Optional[int] = None) -> Self:
        """Sends a keycode to the device.

        Android only. Possible keycodes can be found
        in http://developer.android.com/reference/android/view/KeyEvent.html.

        Args:
            keycode: the keycode to be sent to the device
            metastate: meta information about the keycode being sent
            flags: the set of key event flags

        Returns:
            Union['WebDriver', 'Keyboard']: Self instance
        """
        pass

    def long_press_keycode(self, keycode: int, metastate: Optional[int] = None, flags: Optional[int] = None) -> Self:
        """Sends a long press of keycode to the device.

        Android only. Possible keycodes can be found in
        http://developer.android.com/reference/android/view/KeyEvent.html.

        Args:
            keycode: the keycode to be sent to the device
            metastate: meta information about the keycode being sent
            flags: the set of key event flags

        Returns:
            Union['WebDriver', 'Keyboard']: Self instance
        """
        pass

