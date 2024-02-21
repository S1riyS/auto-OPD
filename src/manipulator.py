import sys
import win32gui
import win32api
import win32con
import win32ui
import re
import time
import typing as t

from src.config import KEYBOARD_KEYS
from src.types import RelativePosition
from src.exceptions import MainframeNotFoundException, MainframeIsClosedException
from src.utils.multiplicator import multiply


class MainframeManipulator:
    def __init__(self):
        mainframe_title = self.__get_mainframe_title()
        if mainframe_title is None:
            raise MainframeNotFoundException

        self.hwnd = win32gui.FindWindow(None, mainframe_title)

        self.SCREEN_SIZE: t.Tuple[int, int] = (win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))

    @staticmethod
    def __get_mainframe_title() -> t.Optional[str]:
        def enum_windows_callback(hwnd, callback_titles: t.List[str]):
            if win32gui.IsWindowVisible(hwnd):
                callback_titles.append(win32gui.GetWindowText(hwnd))

        titles = []
        regex_title_patter = re.compile(r'БЭВМ v1.\d\d.\d\d')
        win32gui.EnumWindows(enum_windows_callback, titles)

        for title in titles:
            if regex_title_patter.match(title):
                return title
        return None

    def __set_window_size(self, coefficient: float) -> None:
        win32gui.SetWindowPos(
            self.hwnd,
            None,
            0,
            0,
            multiply(self.SCREEN_SIZE[0], coefficient),
            multiply(self.SCREEN_SIZE[1], coefficient),
            win32con.SWP_SHOWWINDOW
        )
        time.sleep(0.5)

    def click(self, position: RelativePosition, clicks: int = 1, interval: float = 0.0) -> None:
        """
        Makes a left click

        Parameters
        ----------
        position : RelativePosition
            Relative position of click
        clicks : int
            Number of clicks
        interval : float
            Delay between clicks
        """
        parameters = win32api.MAKELONG(
            multiply(self.SCREEN_SIZE[0], position.x),
            multiply(self.SCREEN_SIZE[1], position.y)
        )

        for _ in range(clicks):
            win32api.PostMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, parameters)
            win32api.PostMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, parameters)
            time.sleep(interval)

    @staticmethod
    def press_key(key: str) -> None:
        key_code = KEYBOARD_KEYS[key]
        win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.02)

    def press_sequence(self, sequence: t.Sequence[str]) -> None:
        for key in sequence:
            self.press_key(key)

    def set_fullscreen_mode(self) -> None:
        self.__set_window_size(1)
        win32gui.SetForegroundWindow(self.hwnd)

    def set_normal_mode(self) -> None:
        self.__set_window_size(0.7)
