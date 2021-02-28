import pyautogui, sys

print('종료는 컨트롤+C 입니다.')

try:
    while True:
        x, y = pyautogui.position() 
        ###position함수는 마우스 커서의 현재 위치 "x,y"를 튜플의 형태로 반환 
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')