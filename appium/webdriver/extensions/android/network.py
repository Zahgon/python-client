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


class NetSpeed:
    GSM = 'gsm'  # GSM/CSD (up: 14.4(kbps), down: 14.4(kbps))
    SCSD = 'scsd'  # HSCSD (up: 14.4, down: 57.6)
    GPRS = 'gprs'  # GPRS (up: 28.8, down: 57.6)
    EDGE = 'edge'  # EDGE/EGPRS (up: 473.6, down: 473.6)
    UMTS = 'umts'  # UMTS/3G (up: 384.0, down: 384.0)
    HSDPA = 'hsdpa'  # HSDPA (up: 5760.0, down: 13,980.0)
    LTE = 'lte'  # LTE (up: 58,000, down: 173,000)
    EVDO = 'evdo'  # EVDO (up: 75,000, down: 280,000)
    FULL = 'full'  # No limit, the default (up: 0.0, down: 0.0)


class NetworkMask:
    WIFI = 0b010
    DATA = 0b100
    AIRPLANE_MODE = 0b001


class Network(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    @property
    def network_connection(self) -> int:
        """Returns an integer bitmask specifying the network connection type.

        Android only.
        Possible values are available through the enumeration `appium.webdriver.ConnectionType`

        This API only works reliably on emulators (any version) and real devices
        since API level 31.
        """
        pass

    def set_network_connection(self, connection_type: int) -> int:
        """Sets the network connection type. Android only.

        Possible values:

            +--------------------+------+------+---------------+
            | Value (Alias)      | Data | Wifi | Airplane Mode |
            +====================+======+======+===============+
            | 0 (None)           | 0    | 0    | 0             |
            +--------------------+------+------+---------------+
            | 1 (Airplane Mode)  | 0    | 0    | 1             |
            +--------------------+------+------+---------------+
            | 2 (Wifi only)      | 0    | 1    | 0             |
            +--------------------+------+------+---------------+
            | 4 (Data only)      | 1    | 0    | 0             |
            +--------------------+------+------+---------------+
            | 6 (All network on) | 1    | 1    | 0             |
            +--------------------+------+------+---------------+

        These are available through the enumeration `appium.webdriver.ConnectionType`

        This API only works reliably on emulators (any version) and real devices
        since API level 31.

        Args:
            connection_type: a member of the enum `appium.webdriver.ConnectionType`

        Return:
            int: Set network connection type
        """
        pass

    def toggle_wifi(self) -> Self:
        """Toggle the wifi on the device, Android only.
        This API only works reliably on emulators (any version) and real devices
        since API level 31.

        Returns:
            Union['WebDriver', 'Network']: Self instance
        """
        pass

    def set_network_speed(self, speed_type: str) -> Self:
        """Set the network speed emulation.

        Android Emulator only.

        Args:
            speed_type: The network speed type.
                A member of the const appium.webdriver.extensions.android.network.NetSpeed.

        Usage:
            self.driver.set_network_speed(NetSpeed.LTE)

        Returns:
            Union['WebDriver', 'Network']: Self instance
        """
        pass

