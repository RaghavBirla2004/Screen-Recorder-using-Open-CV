import cv2 as cv
import pyautogui as p
import numpy as np

rs = p.size()

fn = "E:/coding/python/Projects/4 Screen Recorder/videos/1.mp4"

output = cv.VideoWriter(fn, cv.VideoWriter_fourcc(*"DIVX"), 20, rs)



cv.namedWindow("Live Recording", cv.WINDOW_NORMAL)
cv.resizeWindow("Live Recording", (600,400))



while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv.cvtColor(f,cv.COLOR_BGR2RGB )
    output.write(f)


    if cv.waitKey(1) & 0xff == 27:
        break;

cv.destroyAllWindows()
output.release()

   


