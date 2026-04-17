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

from selenium.common.exceptions import UnknownMethodException
from typing_extensions import Self

from appium.common.helper import extract_const_attributes
from appium.common.logger import logger
from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence
from appium.webdriver.mobilecommand import MobileCommand as Command


class GsmCallActions:
    CALL = 'call'
    ACCEPT = 'accept'
    CANCEL = 'cancel'
    HOLD = 'hold'


class GsmSignalStrength:
    NONE_OR_UNKNOWN = 0
    POOR = 1
    MODERATE = 2
    GOOD = 3
    GREAT = 4


class GsmVoiceState:
    UNREGISTERED = 'unregistered'
    HOME = 'home'
    ROAMING = 'roaming'
    SEARCHING = 'searching'
    DENIED = 'denied'
    OFF = 'off'
    ON = 'on'


class Gsm(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def make_gsm_call(self, phone_number: str, action: str) -> Self:
        """Make GSM call (Emulator only)

        Android only.

        Args:
            phone_number: The phone number to call to.
            action: The call action.
                A member of the const `appium.webdriver.extensions.android.gsm.GsmCallActions`

        Usage:
            self.driver.make_gsm_call('5551234567', GsmCallActions.CALL)

        Returns:
            Union['WebDriver', 'Gsm']: Self instance
        """
        pass

    def set_gsm_signal(self, strength: int) -> Self:
        """Set GSM signal strength (Emulator only)

        Android only.

        Args:
            strength: Signal strength.
                A member of the enum :obj:`appium.webdriver.extensions.android.gsm.GsmSignalStrength`

        Usage:
            self.driver.set_gsm_signal(GsmSignalStrength.GOOD)

        Returns:
            Union['WebDriver', 'Gsm']: Self instance
        """
        pass

    def set_gsm_voice(self, state: str) -> Self:
        """Set GSM voice state (Emulator only)

        Android only.

        Args:
            state: State of GSM voice.
                A member of the const `appium.webdriver.extensions.android.gsm.GsmVoiceState`

        Usage:
            self.driver.set_gsm_voice(GsmVoiceState.HOME)

        Returns:
            Union['WebDriver', 'Gsm']: Self instance
        """
        pass

