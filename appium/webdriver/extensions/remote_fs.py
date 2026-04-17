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

import base64
from typing import Optional

from selenium.common.exceptions import InvalidArgumentException, UnknownMethodException
from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence

from ..mobilecommand import MobileCommand as Command


class RemoteFS(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def pull_file(self, path: str) -> str:
        """Retrieves the file at `path`.

        Args:
            path: the path to the file on the device

        Returns:
            The file's contents encoded as Base64.
        """
        pass

    def pull_folder(self, path: str) -> str:
        """Retrieves a folder at `path`.

        Args:
            path: the path to the folder on the device

        Returns:
            The folder's contents zipped and encoded as Base64.
        """
        pass

    def push_file(self, destination_path: str, base64data: Optional[str] = None, source_path: Optional[str] = None) -> Self:
        """Puts the data from the file at `source_path`, encoded as Base64, in the file specified as `path`.

        Specify either `base64data` or `source_path`, if both specified default to `source_path`

        Args:
            destination_path: the location on the device/simulator where the local file contents should be saved
            base64data: file contents, encoded as Base64, to be written
            to the file on the device/simulator
            source_path: local file path for the file to be loaded on device

        Returns:
            Union['WebDriver', 'RemoteFS']: Self instance
        """
        pass

