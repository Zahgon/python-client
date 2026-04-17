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

from selenium.common.exceptions import UnknownMethodException
from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence
from appium.webdriver.clipboard_content_type import ClipboardContentType

from ..mobilecommand import MobileCommand as Command


class Clipboard(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def set_clipboard(
        self, content: bytes, content_type: str = ClipboardContentType.PLAINTEXT, label: Optional[str] = None
    ) -> Self:
        """Set the content of the system clipboard

        Args:
            content: The content to be set as bytearray string
            content_type: One of ClipboardContentType items. Only ClipboardContentType.PLAINTEXT
                is supported on Android
            label: label argument, which only works for Android

        Returns:
            Union['WebDriver', 'Clipboard']: Self instance
        """
        pass

    def set_clipboard_text(self, text: str, label: Optional[str] = None) -> Self:
        """Copies the given text to the system clipboard

        Args:
            text: The text to be set
            label:label argument, which only works for Android

        Returns:
            Union['WebDriver', 'Clipboard']: Self instance
        """
        pass

    def get_clipboard(self, content_type: str = ClipboardContentType.PLAINTEXT) -> bytes:
        """Receives the content of the system clipboard

        Args:
            content_type: One of ClipboardContentType items. Only ClipboardContentType.PLAINTEXT
                is supported on Android

        Returns:
            Clipboard content as bytearray. Or empty bytes if the clipboard is empty
        """
        pass

    def get_clipboard_text(self) -> str:
        """Receives the text of the system clipboard

        Returns:
            The actual clipboard text or an empty string if the clipboard is empty
        """
        pass

