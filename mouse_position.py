import pyautogui
import time

def print_mouse_position():
    try:
        while True:
            # 현재 마우스 좌표 가져오기
            x, y = pyautogui.position()
            position_str = f"X: {x} Y: {y}"
            print(position_str, end='\r')  # 같은 줄에 출력
            time.sleep(0.1)  # 0.1초마다 업데이트
    except KeyboardInterrupt:
        print("\n프로그램 종료")

if __name__ == "__main__":
    print("마우스 좌표를 얻으려면 마우스를 이동하세요. 종료하려면 Ctrl+C를 누르세요.")
    print_mouse_position()
