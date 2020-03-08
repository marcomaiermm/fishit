import imagesearch
import gui
import subprocess
import time
#from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import traceback,sys


class Thread(QThread):
    def __init__(self, fn, f=False):
        super(Thread, self).__init__()
        signal = pyqtSignal(object)
        self.f=f
        self.fn=fn

    # run method gets called when we start the thread

    def run(self):
        print("starting thread")
        if self.f:
            result = self.fn(w).CheckArea()
        else:
            result = self.fn()
        

        #w.gui.catched_edit.setText(str(process.fish_count))
        #w.gui.status_edit.setText(str(process.status))
    def stop(self):
        print("thread ended")
        self.terminate()
        

class Timer:
    def __init__(self,duration):
        super(Timer, self).__init__()
        self.dur = duration
        self.elapsed_s = 0
        self.elapsed_m = 0
        self.elapsed_h = 0
        self.total=0

    def timer(self):
        while self.total<=(self.dur*60):
            if self.elapsed_m<=59:
                if self.elapsed_s<=59:
                    self.elapsed_s+=1
                else:
                    self.elapsed_s=0
                    self.elapsed_m+=1
            else:
                self.elapsed_h+=1
                self.elapsed_m=0
            time_text=str(self.elapsed_h) + ":" + str(self.elapsed_m) + ":" + str(self.elapsed_s)
            w.gui.time_edit.setText(time_text)
            self.total+=1
            time.sleep(1)
        w.Stop()

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.gui = gui.Ui_Window()
        self.gui.setupUi(self)
        self.fish_thread = Thread(imagesearch.Fishit, f=True)
        self.gui.fish_button.clicked.connect(self.FishButton)
        #self.fish_thread.signal.connect(self.gui.status_label.setText)
        #self.fish_thread.signal.connect(self.finished)
        self.gui.stop_button.clicked.connect(self.Stop)

    def FishButton(self):
        duration = int(self.gui.duration.currentText())
        self.gui.fish_button.setEnabled(False)
        self.gui.stoppedLabel.setText("")
        self.fish_thread.start()
        self.timer = Thread(Timer(duration).timer)
        self.timer.start()

    def Stop(self):
        self.gui.fish_button.setEnabled(True)
        self.gui.stoppedLabel.setText("Stopped")
        self.timer.stop()
        self.gui.time_edit.setText("0:0:0")
        self.gui.catched_edit.setText("")
        self.gui.status_edit.setText("")
        self.time=0

if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=AppWindow()
    w.show()
    app.exec_()