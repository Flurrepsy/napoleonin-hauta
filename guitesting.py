import sys
import importlib
import shuffleDeck as sh
import draw_card as drwcrd
import cardChecker as cc
import playingField as pf
import os
#import mainLoop as ml

importlib.reload(cc)
importlib.reload(drwcrd)
importlib.reload(pf)
importlib.reload(sh)
#importlib.reload(ml)

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QGridLayout, QHBoxLayout, QDialog, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon

cardIcons = {
	"null": "",
	"1S": "1S.png",
	"2S": "2S.png",
	"3S": "3S.png",
	"4S": "4S.png",
	"5S": "5S.png",
	"6S": "6S.png",
	"7S": "7S.png",
	"8S": "8S.png",
	"9S": "9S.png",
	"10S": "10S.png",
	"11S": "11S.png",
	"12S": "12S.png",
	"13S": "13S.png",
	"1D": "1D.png",
	"2D": "2D.png",
	"3D": "3D.png",
	"4D": "4D.png",
	"5D": "5D.png",
	"6D": "6D.png",
	"7D": "7D.png",
	"8D": "8D.png",
	"9D": "9D.png",
	"10D": "10D.png",
	"11D": "11D.png",
	"12D": "12D.png",
	"13D": "13D.png",
	"1C": "1C.png",
	"2C": "2C.png",
	"3C": "3C.png",
	"4C": "4C.png",
	"5C": "5C.png",
	"6C": "6C.png",
	"7C": "7C.png",
	"8C": "8C.png",
	"9C": "9C.png",
	"10C": "10C.png",
	"11C": "11C.png",
	"12C": "12C.png",
	"13C": "13C.png",
	"1H": "1H.png",
	"2H": "2H.png",
	"3H": "3H.png",
	"4H": "4H.png",
	"5H": "5H.png",
	"6H": "6H.png",
	"7H": "7H.png",
	"8H": "8H.png",
	"9H": "9H.png",
	"10H": "10H.png",
	"11H": "11H.png",
	"12H": "12H.png",
	"13H": "13H.png"
	}


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Napoleonin Hauta")

		layout = QVBoxLayout()

		#Card buttons
		cardSize = QSize(100, 147)

		self.k1Button = QPushButton()
		self.k1Button.setFixedSize(cardSize)
		self.k1Button.setProperty("space", 7)
		self.k1Button.setIcon(QIcon())
		self.k1Button.setIconSize(self.k1Button.size())
		self.k1Button.clicked.connect(self.playCard)

		self.k2Button = QPushButton()
		self.k2Button.setFixedSize(cardSize)
		self.k2Button.setProperty("space", 9)
		self.k2Button.setIcon(QIcon())
		self.k2Button.setIconSize(self.k2Button.size())
		self.k2Button.clicked.connect(self.playCard)

		self.k3Button = QPushButton()
		self.k3Button.setProperty("space", 1)
		self.k3Button.setFixedSize(cardSize)
		self.k3Button.setIcon(QIcon())
		self.k3Button.setIconSize(self.k3Button.size())
		self.k3Button.clicked.connect(self.playCard)

		self.k4Button = QPushButton()
		self.k4Button.setProperty("space", 3)
		self.k4Button.setFixedSize(cardSize)
		self.k4Button.setIcon(QIcon())
		self.k4Button.setIconSize(self.k4Button.size())
		self.k4Button.clicked.connect(self.playCard)

		self.aButton = QPushButton()
		self.aButton.setProperty("space", 5)
		self.aButton.setFixedSize(cardSize)
		self.aButton.setIcon(QIcon())
		self.aButton.setIconSize(self.aButton.size())
		self.aButton.clicked.connect(self.playCard)

		self.d1Button = QPushButton()
		self.d1Button.setProperty("space", "d1")
		self.d1Button.setFixedSize(cardSize)
		self.d1Button.setIcon(QIcon())
		self.d1Button.setIconSize(self.d1Button.size())
		self.d1Button.clicked.connect(self.playCard)

		self.d2Button = QPushButton()
		self.d2Button.setProperty("space", "d2")
		self.d2Button.setFixedSize(cardSize)
		self.d2Button.setIcon(QIcon())
		self.d2Button.setIconSize(self.d2Button.size())
		self.d2Button.clicked.connect(self.playCard)

		self.d3Button = QPushButton()
		self.d3Button.setProperty("space", "d3")
		self.d3Button.setFixedSize(cardSize)
		self.d3Button.setIcon(QIcon())
		self.d3Button.setIconSize(self.d3Button.size())
		self.d3Button.clicked.connect(self.playCard)

		self.d4Button = QPushButton()
		self.d4Button.setProperty("space", "d4")
		self.d4Button.setFixedSize(cardSize)
		self.d4Button.setIcon(QIcon())
		self.d4Button.setIconSize(self.d4Button.size())
		self.d4Button.clicked.connect(self.playCard)

		self.sixButton = QPushButton()
		self.sixButton.setProperty("space", "six")
		self.sixButton.setFixedSize(cardSize)
		self.sixButton.setIcon(QIcon())
		self.sixButton.setIconSize(self.sixButton.size())
		self.sixButton.clicked.connect(self.playCard)

		#Card grid layout
		cardGrid = QGridLayout()
		cardGrid.setSpacing(0)
		cardGrid.setContentsMargins(0,0,0,0)

		cardGrid.addWidget(self.k1Button, 0, 0)
		cardGrid.addWidget(self.d1Button, 0, 1)
		cardGrid.addWidget(self.k2Button, 0, 2)
		cardGrid.addWidget(self.d4Button, 1, 0)
		cardGrid.addWidget(self.aButton, 1, 1)
		cardGrid.addWidget(self.d2Button, 1, 2)
		cardGrid.addWidget(self.k3Button, 2, 0)
		cardGrid.addWidget(self.d3Button, 2, 1)
		cardGrid.addWidget(self.k4Button, 2, 2)

		#widget.setLayout(cardGrid)
		#layout2 = QVBoxLayout()

		startButton = QPushButton("Start")
		#startButton.setCheckable(True)
		startButton.clicked.connect(self.startGame)

		self.drawButton = QPushButton()
		self.drawButton.setProperty("space", "draw")
		self.drawButton.setFixedSize(cardSize)
		self.drawButton.setIcon(QIcon())
		self.drawButton.setIconSize(self.drawButton.size())
		self.drawButton.clicked.connect(self.drawCard)

		self.discardButton = QPushButton()
		self.discardButton.setProperty("space", "disc")
		self.discardButton.setFixedSize(cardSize)
		self.discardButton.setIcon(QIcon())
		self.discardButton.setIconSize(self.discardButton.size())
		self.discardButton.clicked.connect(self.playCard)

		self.sixButton = QPushButton()
		self.sixButton.setProperty("space", "six")
		self.sixButton.setFixedSize(cardSize)
		self.sixButton.setIcon(QIcon())
		self.sixButton.setIconSize(self.sixButton.size())
		self.sixButton.clicked.connect(self.playCard)

		sixSlotGUI = QHBoxLayout()
		sixSlotGUI.addWidget(self.sixButton)

		startButG = QHBoxLayout()
		startButG.addWidget(startButton)

		drawDiscButtons = QHBoxLayout()
		drawDiscButtons.addWidget(self.drawButton)
		drawDiscButtons.addWidget(self.discardButton)

		self.setMinimumSize(QSize(1000, 900))
		self.setMaximumSize(QSize(1000, 900))


		#Set background image for playing field, find better image later
		background = QLabel("asd")
		background.setPixmap(QPixmap("table.jpg"))
		background.setScaledContents(True)
		#self.setCentralWidget(background)

		#self.setCentralWidget(startButton)
		layout.addWidget(startButton)
		layout.addWidget(background)
		#layout.addWidget(drawButton)
		#layout.addWidget(discardButton)


		bgAndButtons = QWidget()
		bgAndButtons.setLayout(layout)

		cardSlots = QWidget()
		cardSlots.setLayout(cardGrid)
		cardSlots.setParent(bgAndButtons)
		cardSlots.setGeometry(250, 150, 500, 500)
		cardSlots.raise_()

		deckSlot = QWidget()
		deckSlot.setLayout(drawDiscButtons)
		deckSlot.setParent(bgAndButtons)
		deckSlot.setGeometry(50, 650, 300, 200)
		deckSlot.raise_()

		sixGUI = QWidget()
		sixGUI.setLayout(sixSlotGUI)
		sixGUI.setParent(bgAndButtons)
		sixGUI.setGeometry(750, 650, 200, 200)
		sixGUI.raise_()

		startGUI = QWidget()
		startGUI.setLayout(startButG)
		startGUI.setParent(bgAndButtons)
		startGUI.setGeometry(100, 50, 100, 100)
		startGUI.raise_()

		self.setCentralWidget(bgAndButtons)
		self.drawnCard = [["null", 0]]
		self.shuffledDeck = [["null", 0]]
		self.turnCounter = 0
		self.discarded = None
		self.discardedFrom = None
		cardOk = False
		#self.setCentralWidget(cardSlots)


	def startGame(self):
		pf.resetField()

		self.turnCounter = 0
		self.discardedFrom = 0
		self.shuffledDeck = sh.shuffle_deck()

		self.drawButton.setIcon(QIcon("back.png"))
		self.k1Button.setIcon(QIcon())
		self.k2Button.setIcon(QIcon())
		self.k3Button.setIcon(QIcon())
		self.k4Button.setIcon(QIcon())
		self.d1Button.setIcon(QIcon())
		self.d2Button.setIcon(QIcon())
		self.d3Button.setIcon(QIcon())
		self.d4Button.setIcon(QIcon())
		self.sixButton.setIcon(QIcon())
		self.aButton.setIcon(QIcon())
		self.discardButton.setIcon(QIcon())


	def drawCard(self):
		self.drawnCard = drwcrd.draw_card(self.shuffledDeck)
		#print(self.drawnCard)
		self.drawnCardTemp = [self.drawnCard]
		print(self.drawnCardTemp)
		self.discardButton.setIcon(QIcon(cardIcons[self.drawnCardTemp[0][0]]))
		self.discarded = False
		if self.drawnCard == 0:
			self.drawButton.setIcon(QIcon())

	def playCard(self):

		pressedButton = self.sender()
		buttonSpace = pressedButton.property("space")
		if buttonSpace in ("d1", "d2", "d3", "d4", "six", "draw"):
			turnCounter, self.drawnCard, self.discarded, self.discardedFrom = pf.actionSelect(self.turnCounter, self.shuffledDeck, self.drawnCard, buttonSpace)
		elif buttonSpace in (1, 3, 5, 7, 9, "disc"):
			self.turnCounter, cardOk, self.drawnCard = pf.playCard(self.drawnCard, self.turnCounter, buttonSpace, self.shuffledDeck, self.discarded, self.discardedFrom)
			print(self.drawnCard)
		else:
			print("wat")
		self.setButtonLabels()
		vc = pf.victoryCondition()
		if vc == True:
			#victoryText = QLabel("Victory!")
			vicText = QMessageBox(self)
			vicText.setWindowTitle("Victory!")
			vicText.setText("Victory!")
			vicText.exec()
		elif vc == "totalVictory":
			vicText = QMessageBox(self)
			vicText.setWindowTitle("Victory!")
			vicText.setText("Victory! Ja vielä ristiässällä!")
			vicText.exec()

		#pf.playCard(self.drawnCard, turnCounter, buttonSpace)
	def setButtonLabels(self):
		self.k1Button.setIcon(QIcon(cardIcons[pf.objectiveSpaceK3[0][0]]))
		self.k2Button.setIcon(QIcon(cardIcons[pf.objectiveSpaceK4[0][0]]))
		self.k3Button.setIcon(QIcon(cardIcons[pf.objectiveSpaceK1[0][0]]))
		self.k4Button.setIcon(QIcon(cardIcons[pf.objectiveSpaceK2[0][0]]))
		self.d1Button.setIcon(QIcon(cardIcons[pf.discardSpace1[0][0]]))
		self.d2Button.setIcon(QIcon(cardIcons[pf.discardSpace2[0][0]]))
		self.d3Button.setIcon(QIcon(cardIcons[pf.discardSpace3[0][0]]))
		self.d4Button.setIcon(QIcon(cardIcons[pf.discardSpace4[0][0]]))
		self.sixButton.setIcon(QIcon(cardIcons[pf.storeSix[0][0]]))
		self.aButton.setIcon(QIcon(cardIcons[pf.objectiveSpaceAce[0][0]]))
		self.discardButton.setIcon(QIcon())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
