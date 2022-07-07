import pyautogui
import win32clipboard
from pynput.keyboard import Key
import multiprocessing




def copy_highlighted():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')


def retrieve_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data


def outer(queue):
    def on_release(key):
        if key == Key.esc:
            exit()
        if key == Key.alt_l:
            copy_highlighted()
            data = retrieve_clipboard()
            print(data)
            queue.put(data)
        return queue
    return on_release

