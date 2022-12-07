import tkinter as tk
import time
import pyautogui
import random
import Constants

class pet():
    def __init__(self):
        
        # pet state
        self.state = 5
        self.state_timer = time.time()
        
        # create a window
        self.window = tk.Tk()

        # placeholder image
        self.walking_right = [tk.PhotoImage(file='pictures\walking_right.gif', format='gif -index %i' % (i)) for i in range(4)]
        self.frame_index = 0
        self.img = self.walking_right[self.frame_index]

        # timestamp to check whether to advance frame
        self.timestamp = time.time()

        # set focushighlight to black when the window does not have focus
        self.window.config(highlightbackground='black')

        # make window frameless
        self.window.overrideredirect(True)

        # make window draw over all others
        self.window.attributes('-topmost', True)

        # turn black into transparency
        self.window.wm_attributes('-transparentcolor', 'black')

        # create a label as a container for our image
        self.label = tk.Label(self.window, bd=0, bg='black')

        # create a window of size 128x128 pixels, at coordinates 0,0
        self.x = int(pyautogui.size()[0]/2)
        self.y = int(pyautogui.size()[1]/2)
        self.window.geometry('64x64+{x}+{y}'.format(x=str(self.x), y=str(self.y)))

        # add the image to our label
        self.label.configure(image=self.img)

        # give window to geometry manager (so it will appear)
        self.label.pack()

        # run self.update() after 0ms when mainloop starts
        self.window.after(0, self.update)
        self.window.mainloop()


    def update(self):
        self.doAction()

        # advance frame if 50ms have passed
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.frame_index = (self.frame_index + 1) % 4
            self.img = self.walking_right[self.frame_index]

        # create the window
        self.window.geometry('64x64+{x}+{y}'.format(x=str(self.x), y=str(self.y)))
        # add the image to our label
        self.label.configure(image=self.img)
        # give window to geometry manager (so it will appear)
        self.label.pack()

        # call update after 5ms
        self.window.after(5, self.update)
        
    def doAction(self):
        
        if time.time() > self.state_timer + 3:
            self.state = random.randint(1, 5)
            self.state_timer = time.time()
            print("State:", self.state)

        if self.state == Constants.s_idle: # idle state
            self.x += 0
            self.y += 0
            # do an idle animation
        elif self.state == Constants.s_walk_right and self.x < pyautogui.size()[0] - 70:
            self.x += 1
            self.y += 0
        elif self.state == Constants.s_walk_left and self.x > 0:
            self.x -= 1
            self.y += 0       
        elif self.state == Constants.s_walk_up and self.y > 0: 
            self.x += 0
            self.y += -1
        elif self.state == 4 and Constants.s_walk_down < pyautogui.size()[1] - 70: 
            self.x += 0
            self.y += 1
        elif self.state == Constants.s_chase_mouse: 
            #control for x dir
            if pyautogui.position()[0] > self.x:
                self.x += 1
            elif pyautogui.position()[0] < self.x:
                self.x -= 1
            else:
                self.x += 0
            
            # control for y dir
            if pyautogui.position()[1] > self.y:
                self.y += 1
            elif pyautogui.position()[1] < self.y:
                self.y -= 1
            else:
                self.y += 0 

            # if touching mouse --> drag it 
            if(pyautogui.position()[0] == self.x and pyautogui.position()[1] == self.y):
                self.x += 10
                self.y += 0
                pyautogui.moveTo(self.x, self.y) 
                self.state_timer = time.time() #resets timer, so state won't change until mouse is free


 



pet()