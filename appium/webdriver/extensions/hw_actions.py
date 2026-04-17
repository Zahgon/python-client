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

from typing import Optional

from selenium.common.exceptions import UnknownMethodException
from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence

from ..mobilecommand import MobileCommand as Command


class HardwareActions(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def lock(self, seconds: Optional[int] = None) -> Self:
        """Lock the device. No changes are made if the device is already unlocked.

        Args:
            seconds: The duration to lock the device, in seconds.
                The device is going to be locked forever until `unlock` is called
                if it equals or is less than zero, otherwise this call blocks until
                the timeout expires and unlocks the screen automatically.

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        pass

    def unlock(self) -> Self:
        """Unlock the device. No changes are made if the device is already locked.

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        pass

    def is_locked(self) -> bool:
        """Checks whether the device is locked.

        Returns:
            `True` if the device is locked
        """
        pass

    def shake(self) -> Self:
        """Shake the device.

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        pass

    def touch_id(self, match: bool) -> Self:
        """Simulate touchId on iOS Simulator

        Args:
            match: Simulates a successful touch (`True`) or a failed touch (`False`)

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        pass

    def toggle_touch_id_enrollment(self) -> Self:
        """Toggle enroll touchId on iOS Simulator

        Returns:
            Union['WebDriver', 'HardwareActions']: Self instance
        """
        pass

    def finger_print(self, finger_id: int) -> Self:
        """Authenticate users by using their finger print scans on supported Android emulators.

        Args:
            finger_id: Finger prints stored in Android Keystore system (from 1 to 10)
        """
        pass

