from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys








class Window(QMainWindow):


        



    def __init__(self):
        super().__init__()

        top = 400
        left = 400
        width = 800
        height = 600

        icon = "icons/pain.png"

        self.setWindowTitle("Paint ")
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = QColor(0, 0, 0)
        self.brushStyle= Qt.SolidLine
        self.brushCap = Qt.RoundCap

        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        brushMenu = mainMenu.addMenu("Brush Size")
        brushColor = mainMenu.addMenu("Brush Color")
        brushstyle = mainMenu.addMenu("Brush Style")
        brushcap = mainMenu.addMenu("Brush Cap")
        
        openAction = QAction(QIcon("icons/Open.png"), "Open", self)
        openAction.setShortcut("Ctrl+M")
        fileMenu.addAction(openAction)
        openAction.triggered.connect(self.openAction)


        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QIcon("icons/clear.png"), "Clear", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        aboutAction = QAction(QIcon("icons/About.png"), "About", self)
        fileMenu.addAction(aboutAction)
        aboutAction.triggered.connect(self.aboutAction)

        exitAction  = QAction(QIcon("icons/Exit.png"), "Exit", self)
        exitAction.setShortcut("ALT+F4")
        fileMenu.addAction(exitAction)
        exitAction.triggered.connect(self.exitAction)

        onepxAction = QAction(QIcon("icons/onepx.png"), "1px", self)
        onepxAction.setShortcut("Ctrl+O")
        brushMenu.addAction(onepxAction)
        onepxAction.triggered.connect(self.onePx)

        threepxAction = QAction(QIcon("icons/threepx.png"), "3px", self)
        threepxAction.setShortcut("Ctrl+T")
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePx)

        fivepxAction = QAction(QIcon("icons/fivepx.png"), "5px", self)
        fivepxAction.setShortcut("Ctrl+F")
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePx)

        sevenpxAction = QAction(QIcon("icons/sevenpx.png"), "7px", self)
        sevenpxAction.setShortcut("Ctrl+S")
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPx)

        ninepxAction = QAction(QIcon("icons/ninepx.png"), "9px", self)
        ninepxAction.setShortcut("Ctrl+N")
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePx)

        elevenpxAction = QAction(QIcon("icons/ninepx.png"), "11px", self)
        elevenpxAction.setShortcut("Ctrl+E")
        brushMenu.addAction(elevenpxAction)
        elevenpxAction.triggered.connect(self.elevenPx)

        blackAction = QAction(QIcon("icons/black.png"), "Black", self)
        blackAction.setShortcut("Ctrl+B")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)

        whiteAction = QAction(QIcon("icons/white.png"), "White", self)
        whiteAction.setShortcut("Ctrl+W")
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.whiteColor)

        redAction = QAction(QIcon("icons/red.png"), "Red", self)
        redAction.setShortcut("Ctrl+R")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        greenAction = QAction(QIcon("icons/green.png"), "Green", self)
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        yellowAction = QAction(QIcon("icons/yellow.png"), "Yellow", self)
        yellowAction.setShortcut("Ctrl+Y")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)


        rgbAction = QAction(QIcon("icons/Choose.png"), "Choose", self)
        rgbAction.setShortcut("Ctrl+L")
        brushColor.addAction(rgbAction)
        rgbAction.triggered.connect(self.rgbColor)


        eraseAction = QAction(QIcon("icons/Erase.png"), "Erase", self)
        eraseAction.setShortcut("Ctrl+D")
        brushColor.addAction(eraseAction)
        eraseAction.triggered.connect(self.erase)

        dashAction = QAction(QIcon("icons/Dash.png"), "Dash", self)
        dashAction.setShortcut("Ctrl+Z")
        brushstyle.addAction(dashAction)
        dashAction.triggered.connect(self.dashAction)

        dotAction = QAction(QIcon("icons/Dot.png"), "Dot", self)
        dotAction.setShortcut("Ctrl+X")
        brushstyle.addAction(dotAction)
        dotAction.triggered.connect(self.dotAction)
        
        solidAction = QAction(QIcon("icons/Solid.png"), "Solid", self)
        solidAction.setShortcut("Ctrl+N")
        brushstyle.addAction(solidAction)
        solidAction.triggered.connect(self.solidAction)

        squarecapAction = QAction(QIcon("icons/Square.png"), "Square", self)
        squarecapAction.setShortcut("Ctrl+J")
        brushcap.addAction(squarecapAction)
        squarecapAction.triggered.connect(self.squareCapAction)

        flatcapAction = QAction(QIcon("icons/Flat.png"), "Flat", self)
        flatcapAction.setShortcut("Ctrl+B")
        brushcap.addAction(flatcapAction)
        flatcapAction.triggered.connect(self.flatCapAction)

        circleCapAction = QAction(QIcon("icons/Circle.png"), "Circle", self)
        circleCapAction.setShortcut("Ctrl+Q")
        brushcap.addAction(circleCapAction)
        circleCapAction.triggered.connect(self.circleCapAction)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, self.brushStyle, self.brushCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def openAction(self):
        filePath2, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath2 == "":
            return

        self.image = QImage()
        self.image.load(filePath2)



    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath == "":
            return

        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()
    
    def aboutAction(self):
        QMessageBox.about(self, "About", "Paint in python with pyqt5. Thank Parwiz Forogh(https://www.youtube.com/@ParwizForogh) and NicolasG31(https://github.com/NicolasG31)")

    def exitAction(self):
        sys.exit()

    def onePx(self):
        self.brushSize = 1

    def threePx(self):
        self.brushSize = 3

    def fivePx(self):
        self.brushSize = 5

    def sevenPx(self):
        self.brushSize = 7

    def ninePx(self):
        self.brushSize = 9

    def elevenPx(self):
        self.brushSize = 11

    def blackColor(self):
        self.brushColor = QColor(0, 0, 0)

    def whiteColor(self):
        self.brushColor = QColor(255, 255, 255)

    def redColor(self):
        self.brushColor = QColor(255, 0, 0)

    def greenColor(self):
        self.brushColor = QColor(0, 255, 0)

    def yellowColor(self):
        self.brushColor = QColor(255, 255, 0)

    def rgbColor(self, color):
        color = QColorDialog.getColor()
        self.brushColor = color

    def erase(self):
        self.brushColor = QColor(255, 255, 255)

    def dashAction(self):
        self.brushStyle = Qt.DashLine
    
    def dotAction(self):
        self.brushStyle = Qt.DotLine

    def solidAction(self):
        self.brushStyle = Qt.SolidLine

    def squareCapAction(self):
        self.brushCap = Qt.SquareCap

    def flatCapAction(self):
        self.brushCap = Qt.FlatCap
    
    def circleCapAction(self):
        self.brushCap = Qt.RoundCap



    







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()