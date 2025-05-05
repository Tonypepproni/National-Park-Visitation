from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys

'''
Random notes from learning

A layout can only have on widget it is assifned too. It will stick with the last one it is assigned too
'''

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Creates a centreal widget, i think you can have multiple widget with different layouts
        centeral_widget=QWidget(self)
        self.setCentralWidget(centeral_widget)

        #Sets the main windows geomertry 3 and 4 number are the length and width
        self.setWindowTitle("Main Page")
        self.setGeometry(100,100,400,400)

        #Creates a label, sets the text and aligns text in center of the label
        self.label=QLabel(self)
        self.label.setText("Hello World!")
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont('Roboto',30))


        ####################

        #Creates a large frame to hold multiple frames
        frameLarge=QFrame()
        frameLarge.setFrameShape(QFrame.Shape.HLine)

        #Left Frame with box shape
        frameLeft=QFrame()
        frameLeft.setFrameShape(QFrame.Shape.Box)

        self.leftDial=QDial()
        self.leftDial.setRange(0,100)
        self.leftDial.setSingleStep(1)
        self.leftDial.setNotchesVisible(True)
        
        self.DialText=QLabel()
        self.DialText.setText(f'{self.leftDial.value()}')
        self.DialText.setFont(QFont('Arial',20))

        inLeftLayou=QVBoxLayout()
        inLeftLayou.addWidget(self.leftDial, alignment=Qt.AlignmentFlag.AlignCenter)
        inLeftLayou.addWidget(self.DialText, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom)

        frameLeft.setLayout(inLeftLayou)

        #Connect the dial to the change function
        self.leftDial.valueChanged.connect(self.value_change)

        #Right frame with a shadow
        frameright=QFrame()
        frameright.setFrameShape(QFrame.Shape.Box)
        frameright.setFrameShadow(QFrame.Shadow.Raised)

        self.LabelR=QLabel(self)
        self.LabelR.setText("I AM COMING FOR YOU")

        innerLayout=QVBoxLayout()
        innerLayout.addWidget(self.LabelR, alignment=Qt.AlignmentFlag.AlignCenter)

        frameright.setLayout(innerLayout)

        ##Sets layout to be horzontial and adds the left and right frame to it
        largeLayout=QHBoxLayout()
        largeLayout.addWidget(frameLeft)
        largeLayout.addWidget(frameright)

        #You cant directly add the layout to the central widget so you need to have a widget for it
        largeWidget=QWidget()
        largeWidget.setLayout(largeLayout)

        ####################

        #Creates a layout for a widget and says that everything in the layout is aligned to the top and center
        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(largeWidget)

        centeral_widget.setLayout(layout)

        self.show()

    def value_change(self):
        #### updates label with value of the dial in real time ####
        self.DialText.setText(f'{self.leftDial.value()}')

        

App= QApplication(sys.argv)

window=Window()

sys.exit(App.exec())