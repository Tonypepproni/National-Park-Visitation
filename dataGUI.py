from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from main import Park

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget=QWidget(self)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("Stats")
        self.setGeometry(200,200,400,500)

        ############################################################

        self.titleLabel=QLabel(self)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setText("SELECT A PARK")

        self.meanLabel=QLabel(self)
        self.medianLabel=QLabel(self)
        self.stdLabel=QLabel(self)
        self.minLabel=QLabel(self)
        self.maxLabel=QLabel(self)
        self.rangeLabel=QLabel(self)
        self.sumLabel=QLabel(self)
        self.calcLabel=QLabel(self)

        self.calcLabel.setText(f"Select a park")
        self.meanLabel.setText(f"Select Park")
        self.medianLabel.setText(f"Select Park")
        self.stdLabel.setText(f"Select Park")
        self.minLabel.setText(f"Select Park")
        self.maxLabel.setText(f"Select Park")
        self.rangeLabel.setText(f"Select Park")
        self.sumLabel.setText(f"Select Park")

        ############################################################

        self.calc=QPushButton()
        self.calc.setText("Calculate")
        self.calc.pressed.connect(self.oneParkCalc)

        self.combo=QComboBox()
        self.combo.addItem("Select One")
        self.combo.addItem("Cedar Breaks NM")

        self.dates=QComboBox()
        months=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
        for i in months:
            self.dates.addItem(i)

        ############################################################

        labelFrame=QFrame()
        labelFrame.setFrameShape(QFrame.Shape.Box)

        inputFrame=QFrame()
        inputFrame.setFrameShape(QFrame.Shape.Box)

        yearFrame=QFrame()
        yearFrame.setFrameShape(QFrame.Shape.Box)

        ############################################################

        labelFramLayout=QVBoxLayout()
        labelFramLayout.addWidget(self.calcLabel, alignment=Qt.AlignmentFlag.AlignCenter)
        labelFramLayout.addWidget(self.meanLabel)
        labelFramLayout.addWidget(self.medianLabel)
        labelFramLayout.addWidget(self.stdLabel)
        labelFramLayout.addWidget(self.minLabel)
        labelFramLayout.addWidget(self.maxLabel)
        labelFramLayout.addWidget(self.rangeLabel)
        labelFramLayout.addWidget(self.sumLabel)

        inputLayout=QHBoxLayout()
        inputLayout.addWidget(self.calc)
        inputLayout.addWidget(self.combo)
        inputLayout.addWidget(self.dates)
        inputLayout.addWidget(yearFrame)

        yearLayout=QHBoxLayout()

        layout=QVBoxLayout()
        layout.addWidget(self.titleLabel, alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(labelFrame)
        layout.addWidget(inputFrame)

        central_widget.setLayout(layout)
        labelFrame.setLayout(labelFramLayout)
        inputFrame.setLayout(inputLayout)
        yearFrame.setLayout(yearLayout)

        self.show()
    
    def oneParkCalc(self):
        index=self.combo.currentIndex()
        parks=['CedarBreaks']
        park=Park(f"data/{parks[index-1]}.csv")
        park.oneMonthStats((self.dates.currentText()).upper())

        self.calcLabel.setText(f"Stats for the month of {self.dates.currentText()}")
        self.meanLabel.setText(f"Mean: {park.oneMean:,.2f}")
        self.medianLabel.setText(f"Median: {park.oneMedian:,.2f}")
        self.stdLabel.setText(f"Standard Deviation: {park.oneSD:,.2f}")
        self.minLabel.setText(f"Min: {park.oneMin:,.2f}")
        self.maxLabel.setText(f"Max: {park.oneMax:,.2f}")
        self.rangeLabel.setText(f"Range: {park.oneRange:,.2f}")
        self.sumLabel.setText(f"Sum: {park.oneEx:,.2f}")



App = QApplication(sys.argv)

window=Window()

sys.exit(App.exec())