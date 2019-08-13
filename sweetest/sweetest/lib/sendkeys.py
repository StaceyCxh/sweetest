import pyautogui


def pressEnter():
    '''
    按下Enter键
    :return:
    '''
    pyautogui.press('enter')
    return 1


def pressDown():
    '''
    按下向下箭头按钮键
    :return:
    '''
    pyautogui.press('down')
    return 1