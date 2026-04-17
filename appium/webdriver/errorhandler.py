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

import json
from typing import Any, Dict, List, Sequence, Type, Union

import selenium.common.exceptions as sel_exceptions
from selenium.webdriver.remote import errorhandler

import appium.common.exceptions as appium_exceptions

ERROR_TO_EXC_MAPPING: Dict[str, Type[sel_exceptions.WebDriverException]] = {
    'element click intercepted': sel_exceptions.ElementClickInterceptedException,
    'element not interactable': sel_exceptions.ElementNotInteractableException,
    'insecure certificate': sel_exceptions.InsecureCertificateException,
    'invalid argument': sel_exceptions.InvalidArgumentException,
    'invalid cookie domain': sel_exceptions.InvalidCookieDomainException,
    'invalid element state': sel_exceptions.InvalidElementStateException,
    'invalid selector': sel_exceptions.InvalidSelectorException,
    'invalid session id': sel_exceptions.InvalidSessionIdException,
    'javascript error': sel_exceptions.JavascriptException,
    'move target out of bounds': sel_exceptions.MoveTargetOutOfBoundsException,
    'no such alert': sel_exceptions.NoAlertPresentException,
    'no such cookie': sel_exceptions.NoSuchCookieException,
    'no such element': sel_exceptions.NoSuchElementException,
    'no such frame': sel_exceptions.NoSuchFrameException,
    'no such window': sel_exceptions.NoSuchWindowException,
    'no such shadow root': sel_exceptions.NoSuchShadowRootException,
    'script timeout': sel_exceptions.TimeoutException,
    'session not created': sel_exceptions.SessionNotCreatedException,
    'stale element reference': sel_exceptions.StaleElementReferenceException,
    'detached shadow root': sel_exceptions.NoSuchShadowRootException,
    'timeout': sel_exceptions.TimeoutException,
    'unable to set cookie': sel_exceptions.UnableToSetCookieException,
    'unable to capture screen': sel_exceptions.ScreenshotException,
    'unexpected alert open': sel_exceptions.UnexpectedAlertPresentException,
    'unknown command': sel_exceptions.UnknownMethodException,
    'unknown error': sel_exceptions.WebDriverException,
    'unknown method': sel_exceptions.UnknownMethodException,
    'unsupported operation': sel_exceptions.UnknownMethodException,
    'element not visible': sel_exceptions.ElementNotVisibleException,
    'element not selectable': sel_exceptions.ElementNotSelectableException,
    'invalid coordinates': sel_exceptions.InvalidCoordinatesException,
}




class MobileErrorHandler(errorhandler.ErrorHandler):
    def check_response(self, response: Dict[str, Any]) -> None:
        """
        https://www.w3.org/TR/webdriver/#errors
        """
        pass
