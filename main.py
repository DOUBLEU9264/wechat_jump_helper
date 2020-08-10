import time, sys, win32gui, pyautogui

hld = win32gui.FindWindow(None, '跳一跳')
if hld == 0:
    print('未检测到跳一跳！')
    sys.exit()
left, top, right, bottom = win32gui.GetWindowRect(hld)
win32gui.SetForegroundWindow(hld)  # 根据句柄将窗口放在最前
print('3秒后开始')
time.sleep(3)


# 开始循环跳跃
while 1:
    a = pyautogui.locateOnScreen('1578.png', grayscale=True, confidence=0.8)
    if a:
        actor = (a[0]+15, a[1]+78)  # 主角位置
        print('主角位置', actor)
    else:
        print('未检测到主角！')
        break
    # print('3秒后获取鼠标位置')
    # time.sleep(1)
    # print('2秒后获取鼠标位置')
    # time.sleep(1)
    print('1秒后获取鼠标位置')
    # time.sleep(1)
    cursor = pyautogui.position()
    print('鼠标位置', cursor)
    distance = ((actor[0]-cursor[0])**2 + (actor[1]-cursor[1])**2) ** 0.5
    print('距离', distance)
    if distance < 55:
        during_time = distance * 0.00220
    elif distance < 85:
        during_time = distance * 0.00230
    elif distance < 95:
        during_time = distance * 0.00230
    elif distance < 105:
        during_time = distance * 0.00230
    elif distance < 115:
        during_time = distance * 0.00245
    elif distance < 125:
        during_time = distance * 0.00245
    elif distance < 135:
        during_time = distance * 0.00245
    elif distance < 145:
        during_time = distance * 0.00275
    elif distance < 155:
        during_time = distance * 0.00265
    elif distance < 165:
        during_time = distance * 0.00292
    elif distance < 180:
        during_time = distance * 0.00280
    elif distance < 600:
        during_time = distance * 0.00283
    elif distance > 600:
        during_time = distance * 0.00290
    print('按下时长', during_time)
    pyautogui.mouseDown()
    time.sleep(during_time)
    pyautogui.mouseUp()
    print('2秒后开始下一次循环\n')
    time.sleep(2)

print('Done.')