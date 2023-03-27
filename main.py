# This paint based on video "PyQt5 Creating Paint Application In 40 Minutes"
# Link for video: https://www.youtube.com/watch?v=qEgyGyVA1ZQ
# People whose code helped to correct errors:
# https://github.com/NicolasG31/PyPaint
# https://github.com/Khusmanda/Painting-Application


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

        icon = "icons/paint.png"


        self.setWindowTitle("PyPaint")
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.showFullScreen()

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

        fillAction = QAction(QIcon("icons/icons_file/Fill.png"), "Fill", self)
        fillAction.setShortcut("Ctrl+Q")
        fileMenu.addAction(fillAction)
        fillAction.triggered.connect(self.fillAction)
        
        openAction = QAction(QIcon("icons/icons_file/Open.png"), "Open", self)
        openAction.setShortcut("Ctrl+W")
        fileMenu.addAction(openAction)
        openAction.triggered.connect(self.openAction)

        saveAction = QAction(QIcon("icons/icons_file/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+E")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QIcon("icons/icons_file/clear.png"), "Clear", self)
        clearAction.setShortcut("Ctrl+R")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        aboutAction = QAction(QIcon("icons/icons_file/About.png"), "About", self)
        fileMenu.addAction(aboutAction)
        aboutAction.triggered.connect(self.aboutAction)

        exitAction  = QAction(QIcon("icons/icons_file/Exit.png"), "Exit", self)
        exitAction.setShortcut("ALT+F4")
        fileMenu.addAction(exitAction)
        exitAction.triggered.connect(self.exitAction)

        onepxAction = QAction(QIcon("icons/icons_px/onepx.png"), "1px", self)
        onepxAction.setShortcut("Ctrl+T")
        brushMenu.addAction(onepxAction)
        onepxAction.triggered.connect(self.onePx)

        threepxAction = QAction(QIcon("icons/icons_px/threepx.png"), "3px", self)
        threepxAction.setShortcut("Ctrl+Y")
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePx)

        fivepxAction = QAction(QIcon("icons/icons_px/fivepx.png"), "5px", self)
        fivepxAction.setShortcut("Ctrl+U")
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePx)

        sevenpxAction = QAction(QIcon("icons/icons_px/sevenpx.png"), "7px", self)
        sevenpxAction.setShortcut("Ctrl+I")
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPx)

        ninepxAction = QAction(QIcon("icons/icons_px/ninepx.png"), "9px", self)
        ninepxAction.setShortcut("Ctrl+O")
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePx)

        elevenpxAction = QAction(QIcon("icons/icons_px/elevenpx.png"), "11px", self)
        elevenpxAction.setShortcut("Ctrl+P")
        brushMenu.addAction(elevenpxAction)
        elevenpxAction.triggered.connect(self.elevenPx)

        choosepxAction = QAction(QIcon("icons/icons_px/Choosepx.png"), "Choose", self)
        choosepxAction.setShortcut("Ctrl+A")
        brushMenu.addAction(choosepxAction)
        choosepxAction.triggered.connect(self.choosesizeAction)

        blackAction = QAction(QIcon("icons/icons_color/black.png"), "Black", self)
        blackAction.setShortcut("Ctrl+S")
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)

        whiteAction = QAction(QIcon("icons/icons_color/white.png"), "White", self)
        whiteAction.setShortcut("Ctrl+D")
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.whiteColor)

        redAction = QAction(QIcon("icons/icons_color/red.png"), "Red", self)
        redAction.setShortcut("Ctrl+F")
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        greenAction = QAction(QIcon("icons/icons_color/green.png"), "Green", self)
        greenAction.setShortcut("Ctrl+G")
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        yellowAction = QAction(QIcon("icons/icons_color/yellow.png"), "Yellow", self)
        yellowAction.setShortcut("Ctrl+H")
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)

        rgbAction = QAction(QIcon("icons/icons_color/Choosecolor.png"), "Choose", self)
        rgbAction.setShortcut("Ctrl+J")
        brushColor.addAction(rgbAction)
        rgbAction.triggered.connect(self.rgbColor)

        eraseAction = QAction(QIcon("icons/icons_color/Erase.png"), "Erase", self)
        eraseAction.setShortcut("Ctrl+K")
        brushColor.addAction(eraseAction)
        eraseAction.triggered.connect(self.erase)

        dashAction = QAction(QIcon("icons/icons_style/Dash.png"), "Dash", self)
        dashAction.setShortcut("Ctrl+L")
        brushstyle.addAction(dashAction)
        dashAction.triggered.connect(self.dashAction)

        dotAction = QAction(QIcon("icons/icons_style/Dot.png"), "Dot", self)
        dotAction.setShortcut("Ctrl+Z")
        brushstyle.addAction(dotAction)
        dotAction.triggered.connect(self.dotAction)
        
        solidAction = QAction(QIcon("icons/icons_style/Solid.png"), "Solid", self)
        solidAction.setShortcut("Ctrl+X")
        brushstyle.addAction(solidAction)
        solidAction.triggered.connect(self.solidAction)

        squarecapAction = QAction(QIcon("icons/icons_cap/Square.png"), "Square", self)
        squarecapAction.setShortcut("Ctrl+C")
        brushcap.addAction(squarecapAction)
        squarecapAction.triggered.connect(self.squareCapAction)

        flatcapAction = QAction(QIcon("icons/icons_cap/flat.png"), "Flat", self)
        flatcapAction.setShortcut("Ctrl+V")
        brushcap.addAction(flatcapAction)
        flatcapAction.triggered.connect(self.flatCapAction)

        circleCapAction = QAction(QIcon("icons/icons_cap/Circle.png"), "Circle", self)
        circleCapAction.setShortcut("Ctrl+B")
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

    def resizeEvent(self, event):
        self.image = self.image.scaled(self.width(), self.height())

    def fillAction(self):
        self.image.fill(self.brushColor)

    def openAction(self):
        filePath2, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath2 == "":
            return
        with open(filePath2, 'rb') as f: 
                content = f.read()

        self.image.loadFromData(content)
        width = self.width() 
        height = self.height()
        self.image = self.image.scaled(width, height)
        self.update()

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath == "":
            return

        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()
    
    def aboutAction(self):
        QMessageBox.about(self, "About", 
        "<p>Paint in python with pyqt5.</p>"
        "<p>Thank ParwizForogh(https://www.youtube.com/@ParwizForogh)</p>"
        "<p>Thank NicolasG31(https://github.com/NicolasG31)</p>"
        "<p> Thank Khusmanda(https://github.com/Khusmanda)</p>")

    def exitAction(self):
        QApplication.exit()

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

    def choosesizeAction(self):
        choosesize, ok = QInputDialog.getInt(self, 'Choose', 'Write size brush:')
        if ok and choosesize:
            if choosesize > 2000:
                QMessageBox.about(self, "Error", "Very big size!")
            elif choosesize < 1:
                QMessageBox.about(self, "Error", "Very small size!")
            else:
                print(choosesize)
                self.brushSize = choosesize



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()