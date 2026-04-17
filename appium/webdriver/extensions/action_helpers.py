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

from typing import TYPE_CHECKING, List, Optional, Tuple, cast

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.pointer_input import PointerInput
from typing_extensions import Self

from appium.webdriver.webelement import WebElement

if TYPE_CHECKING:
    # noinspection PyUnresolvedReferences
    from appium.webdriver.webdriver import WebDriver


class ActionHelpers:
    def scroll(self, origin_el: WebElement, destination_el: WebElement, duration: Optional[int] = None) -> Self:
        """Scrolls from one element to another

        Args:
            origin_el: the element from which to begin scrolling (center of element)
            destination_el: the element to scroll to (center of element)
            duration: defines speed of scroll action when moving from originalEl to destinationEl.
                Default is 600 ms for W3C spec.

        Usage:
            driver.scroll(el1, el2)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        pass

    def drag_and_drop(self, origin_el: WebElement, destination_el: WebElement, pause: Optional[float] = None) -> Self:
        """Drag the origin element to the destination element

        Args:
            origin_el: the element to drag
            destination_el: the element to drag to
            pause: how long the action pauses before moving after the tap and hold, in float seconds.

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        pass

    def tap(self, positions: List[Tuple[int, int]], duration: Optional[int] = None) -> Self:
        """Taps on an particular place with up to five fingers, holding for a
        certain time

        Args:
            positions: an array of tuples representing the x/y coordinates of
                the fingers to tap. Length can be up to five.
            duration: length of time to tap, in ms

        Usage:
            driver.tap([(100, 20), (100, 60), (100, 100)], 500)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        pass

    def swipe(self, start_x: int, start_y: int, end_x: int, end_y: int, duration: int = 0) -> Self:
        """Swipe from one point to another point, for an optional duration.

        Args:
            start_x: x-coordinate at which to start
            start_y: y-coordinate at which to start
            end_x: x-coordinate at which to stop
            end_y: y-coordinate at which to stop
            duration: defines the swipe speed as time taken to swipe from point a to point b, in ms.

        Usage:
            driver.swipe(100, 100, 100, 400)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        pass

    def flick(self, start_x: int, start_y: int, end_x: int, end_y: int) -> Self:
        """Flick from one point to another point.

        Args:
            start_x: x-coordinate at which to start
            start_y: y-coordinate at which to start
            end_x: x-coordinate at which to stop
            end_y: y-coordinate at which to stop

        Usage:
            driver.flick(100, 100, 100, 400)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        pass
