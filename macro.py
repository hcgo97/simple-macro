import pyautogui
import time

def move_and_copy_paste():
    # 첫 번째 위치로 마우스 이동
    pyautogui.moveTo(1117, 220, duration=0.1)  # (x, y, 이동 시간)
    pyautogui.doubleClick()

    # 복사 (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # 복사 작업이 완료될 때까지 잠시 대기

    # 두 번째 위치로 마우스 이동
    pyautogui.moveTo(367, 980, duration=0.1)
    pyautogui.click()  # 클릭하여 포커스 설정

    # 붙여넣기 (Ctrl + V)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)  # 붙여넣기 작업이 완료될 때까지 잠시 대기

if __name__ == "__main__":
    # time.sleep(3)  # 매크로 시작 전 준비 시간을 줌
    move_and_copy_paste()
