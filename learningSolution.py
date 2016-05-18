import win32api, win32con,os
import sys
from time import sleep

lastPosition = 1
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def autoClick(delay=1):
    """ Click at current position every [delay] seconds """
    global lastPosition
    while True:
        (x,y) = win32api.GetCursorPos()
        print lastPosition,(x,y)
        if lastPosition == (x,y):
            click(x,y)
            sleep(delay)
        else:
            break

if __name__ == '__main__':
    delay = 1
    if len(sys.argv) == 2:
        try :
            delay = int(sys.argv[1])
        except:
            print "Usage: " + sys.argv[0] + "delay (in seconds)"
    print "This program presses left mouse at an interval of %d seconds" % delay
    print "This program ends when the cursor is moved away from the original position"
    print 
    raw_input ("Bring your cursor to the desired position and then press ENTER to begin.")
    lastPosition = win32api.GetCursorPos()
    autoClick(delay)
    print 
    print "Program ends"
