from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QLineEdit,QGridLayout
import sys
import time
import os
import pyttsx3
import webbrowser
from PyQt5.QtCore import Qt

class Jarvis(QWidget):
    def __init__(self):
        super().__init__()
        self.sendbutton = QPushButton("Send",self)
        self.input = QLineEdit(self)
        self.message = QLabel("I AM JARVIS YOUR CHAT BOT\n",self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(550,550)
        self.sendbutton.setGeometry(100,100,80,80)
        self.setStyleSheet("""QWidget{
                           background-color:grey;}
                           QPushButton{
                           color:white;
                           border-radius:40px;
                           background-color:orange;}
                           QLineEdit{
                           background-color:white;
                           color:green;}
                           QLabel{
                           color:white;}""")
        gl = QGridLayout()
        gl.addWidget(self.input)
        gl.addWidget(self.message)
        gl.addWidget(self.sendbutton)
        self.setLayout(gl)
        self.message.setAlignment(Qt.AlignCenter)
        self.sendbutton.clicked.connect(self.brain)
        self.input.returnPressed.connect(self.brain)
        self.name = ""

    def brain(self):
        user_text = self.input.text().lower()
        if "hello" in user_text:
            reply = "Hi, how can I help you?"
        elif "how are you" in user_text:
            reply = f"i am doing good {self.name}"
        elif "your name" in user_text:
            reply = "My name is Jarvis"
        elif "who are you" in user_text:
            reply = "I am a chatbot"
        elif "time" in user_text:
            tim = time.strftime("%H:%M")
            reply = f"The time is {tim}"
        elif "open chrome" in user_text:
            reply = "Opening chrome"
            os.startfile("chrome.exe")
        elif "my name is" in user_text:
            self.name = user_text.replace("my name is", "").strip()
            reply = f"ok i will call you {self.name}"
            self.input.clear()
        elif "calculator" in user_text:
            os.startfile("calc.exe")
            reply = "opening calculator"
        elif "what is my name" in user_text:
            if self.name == "":
                reply ="sorry i don't know,\nBut if you tell me i will remember that in this conversation" 
                self.input.clear()   
            else:
                reply = f"your name is {self.name}"
                self.input.clear()
        elif "open youtube" in user_text:
            webbrowser.open("https://www.youtube.com")
            reply =  "opening youtube"
        elif "notepad" in user_text:
            os.startfile("notepad.exe")
            reply = "opening notepad"
        else:
            reply = "Sorry, I am not advanced enough yet."
        self.message.setText(reply)
        self.text_to_speech(reply)
        self.input.clear()

    def text_to_speech(self,text):
        engine = pyttsx3.init()
        engine.setProperty("rate",150)
        engine.say(text)
        engine.runAndWait()
                    
def main():
    app = QApplication(sys.argv)
    window = Jarvis()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()