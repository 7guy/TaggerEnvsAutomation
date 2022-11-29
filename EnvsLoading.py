import pyautogui
import webbrowser
import time
PAUSE = 2
PAUSE2 = 1


def open_sensi_timeline_chrome():
    chrome_path = 'add Chrome path here'
    url = 'add timeline url here'
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(url)
    time.sleep(PAUSE)


def set_timeline(start_time):
    pyautogui.click(600, 240)
    pyautogui.click()
    pyautogui.doubleClick()
    pyautogui.write('0.3333', interval=0.1)
    pyautogui.moveTo(520,240)
    pyautogui.click()
    pyautogui.press('backspace', presses = 5)
    pyautogui.write(f'{start_time}', )
    pyautogui.moveTo(60, 240)
    pyautogui.click()
    time.sleep(PAUSE2)


def run_environments(list, special_envs, uninstant_envs, start_time):
    open_sensi_timeline_chrome()
    time.sleep(PAUSE)
    set_timeline(start_time)
    count = 1
    for i in list:  # load all environments, 3 per tab
        if int(i) in special_envs[0]:
            if list.index(i) != 0:
                open_sensi_timeline_chrome()
                set_timeline(start_time)
            pyautogui.write(f'{i}', interval=0.2)
            pyautogui.press('enter')
            open_sensi_timeline_chrome()
            set_timeline(start_time)
            count = 1
            continue
        pyautogui.write(f'{i}', interval=0.2)
        if int(i) in uninstant_envs[0]:
            pyautogui.press('down')
        pyautogui.press('enter')
        if count % 3 == 0 and i != list[-1]:
            open_sensi_timeline_chrome()
            set_timeline(start_time)
        count += 1