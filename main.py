from ast import operator
from lib2to3.pgen2.tokenize import tokenize
from ntpath import join
from turtle import pos
import animelyric
import json
import operator
import re
from functools import partial
from janome.tokenizer import Tokenizer
import requests
import openpyxl
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QPushButton
from PyQt5.QtCore import Qt
import ast
import pprint
import config

# Add webscrape button
# Add use backup lyrics button
# For now add text box that has all the playlists
# Add playlist where you can scroll around and see song names, and can click on them


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        #Preparing openpyxl workbooks
        self.lyricspath = 'datasets/lyricstest.xlsx'
        self.vocabpath = 'datasets/vocab.xlsx'
        self.lyricswb = openpyxl.load_workbook(self.lyricspath)
        self.vocabwb = openpyxl.load_workbook(self.vocabpath)
        self.sheet_lyrics = self.lyricswb.active
        self.sheet_vocab = self.vocabwb.active
        
        #Vocab Columns
        self.vocabCol = 'A'
        self.vocabRomajiCol = 'B'
        self.vocabDefCol = 'C'
        self.vocabSongCol = 'D'
        self.vocabCountPos = 'E2'

        #Lyrics Columns
        self.songNameColumn = 'A'
        self.lyricsColumn = 'B'

        self.lyricsCountPos = 'F2'
        self.lyricsCount = int(self.sheet_lyrics[self.lyricsCountPos].value)

        self.vocabCountPos = 'E2'
        self.vocabCount = int(self.sheet_vocab[self.vocabCountPos].value)
        # Take counts from Excel
        
        
    
        self.lyricsdf = pd.read_excel('datasets/lyricstest.xlsx')
        self.vocabdf = pd.read_excel('datasets/vocab.xlsx')
        

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(780, 710)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 140, 760, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 758, 359))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Skia")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 301, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding-left:40px;\n"
"border-radius:10px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 26, 31, 31))
        self.label_4.setStyleSheet("opacity:0.5;")
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -1, 781, 131))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(38, 0, 55, 255), stop:1 rgba(214, 57, 150, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 100, 781, 591))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(12, 410, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-width:2px;\n"
"color: rgb(0,0,0);")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(355, 433, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"color:rgb(108, 108, 108);\n"
"border:none;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(698, 540, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(0, 109, 255);\n"
"color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(12, 440, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-width:2px;\n"
"color: rgb(0,0,0);")
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 400, 380, 131))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(389, 400, 381, 131))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(391, 410, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-width:2px;\n"
"color: rgb(0,0,0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(391, 440, 351, 61))
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(391, 460, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-width:2px;\n"
"color: rgb(0,0,0);")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border-width:2px;\n"
"color: rgb(0,0,0);")
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_9")
        self.frame_3.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_7.raise_()
        self.frame_4.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 80, 1200, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-width:2px;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.frame_2.raise_()
        self.frame.raise_()
        self.scrollArea.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.buttonsLayout = QGridLayout()
        #self.hideQuery()

        self.retranslateUi(MainWindow)
        self.lineEdit.returnPressed.connect(self.checkIfInDataBase) # type: ignore
        self.pushButton.clicked.connect(self.clearQuery)
        self.pushButton_2.clicked.connect(self.save)
        #self.lineEdit.returnPressed.connect(self.unhideQuery)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "MainWindow"))
        # try:
        #     self.label_5.setText(_translate("MainWindow", self.lyricsresult))
        # except:
        self.label_5.setText(self._translate("MainWindow", "Lyrics"))
        self.label.setText(self._translate("MainWindow", "聞いて"))
        self.lineEdit.setPlaceholderText(self._translate("MainWindow", "Enter a song here!"))
        self.label_2.setText(self._translate("MainWindow", "Currently Playing:"))
        self.label_3.setText(self._translate("MainWindow", "None"))
        self.label_6.setText(self._translate("MainWindow", "Translate Query:"))
        self.pushButton.setText(self._translate("MainWindow", "✕"))
        self.pushButton_2.setText(self._translate("MainWindow", "Save"))
        self.label_7.setText(self._translate("MainWindow", ""))
        self.label_7.setWordWrap(True)
        self.label_8.setText(self._translate("MainWindow", "Translation"))
        self.label_9.setText(self._translate("MainWindow", ""))
        self.label_10.setText(self._translate("MainWindow", "temporary"))
    
    def createLyricsButtons(self):
        # Clears layout in case buttons already there
        self.clearLayout(self.buttonsLayout)

        _translate = QtCore.QCoreApplication.translate
        
        self.label_3.setText(_translate("MainWindow", self.songtitle))
        joined_tokens = ["".join(item) for item in self.newbuttons]
        
        # tokenizing lyrics
        t = Tokenizer()
        
        tokenizedlyrics = [[token for token in t.tokenize(sentence, wakati=True)]for sentence in joined_tokens]
        # text preprocessing
        tokenizedlyrics = [[space for space in sentence if space != ' '] for sentence in tokenizedlyrics]
        tokenizedlyrics = [[english for english in sentence if not re.match(r'[A-Z]+',english, re.I)] for sentence in tokenizedlyrics]
        tokenizedlyrics = [[alpha for alpha in sentence if alpha.isalpha() or sentence == []] for sentence in tokenizedlyrics]
        self.positions = {}
        self.positions = [[[tokenizedlyrics[i][j],(i,j)] for j in range(len(tokenizedlyrics[i]))] for i in range(len(tokenizedlyrics))]
        
        splitlyrics = [item.split(' ') for item in self.jplyrics]
        flattenedjplyrics = [item for sublist in splitlyrics for item in sublist]
        
        kanjiandromaji = list(zip(self.positions,flattenedjplyrics))
        print(kanjiandromaji)

        for sentence in self.positions:
            for word in sentence:
                self.button = QPushButton(word[0])
                self.button.clicked.connect(partial(self._buildQuery, self.button.text()))
                self.button.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);border:0px;}QPushButton::pressed{background-color : red;}QPushButton::hover{background-color:aqua;}")
                if word == sentence[0]:
                    self.button.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);border-top-left-radius: 5px;border-bottom-left-radius: 5px;}QPushButton::pressed{background-color : red;border-top-left-radius: 5px;border-bottom-left-radius: 5px;}QPushButton::hover{background-color:aqua;border-top-left-radius: 5px;border-bottom-left-radius: 5px;}")
                
                if word == sentence[-1]:
                    self.button.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);border-top-right-radius: 5px;border-bottom-right-radius: 5px;}QPushButton::pressed{background-color : red;border-top-left-radius: 5px;border-bottom-left-radius: 5px;}QPushButton::hover{background-color:aqua;border-top-left-radius: 5px;border-bottom-left-radius: 5px;}")
                
                if len(word[0]) >1:
                    self.button.adjustSize()
                    self.button.setMinimumHeight(25)
                else: 
                    self.button.setMinimumWidth(25)
                    self.button.setMinimumHeight(25)
                
                
                self.buttonsLayout.addWidget(self.button,word[1][0],word[1][1], alignment = Qt.AlignTop)
                self.buttonsLayout.setContentsMargins(0,0,0,0)
                self.buttonsLayout.setHorizontalSpacing(0)
                

        self.verticalLayout.addLayout(self.buttonsLayout)
    
    def buttonText(self):
        return self.button.text()

    def clearLayout(self, layout):
        if layout is not None:
         while layout.count():
             item = layout.takeAt(0)
             widget = item.widget()
             if widget is not None:
                 widget.setParent(None)
             else:
                 self.clearLayout(item.layout())
    
    def retrieveDataBase(self):

        # Retrieves Song title
        self.songtitle = self.songrow.iloc[0,0]
        # Retrieves Total lyrics
        self.lyrics = self.songrow.iloc[0,1]
        # Retrieves lyrics only without title (used for buttons)
        self.lyricsresult = self.songrow.iloc[0,2]
        # Retrieves romaji lyrics

        romaji = self.songrow.iloc[0,4]

        try:
            self.jplyrics = ast.literal_eval(romaji)
            print(self.jplyrics)
            print('successful1!')
        except:
            self.jplyrics = ast.literal_eval(romaji +'\']]')
            print(self.jplyrics)
        # Retrieves kanji lyrics
        kanjilist = self.songrow.iloc[0,3]
        
        try:
            self.newbuttons = ast.literal_eval(kanjilist)
        except:
            self.newbuttons = ast.literal_eval(kanjilist+ '\']]')
        self.label_5.setText(self._translate("MainWindow", self.lyrics))
        self.createLyricsButtons()
    
    def checkIfInDataBase(self):
        # Reloads the dataframe
        self.lyricsdf = pd.read_excel('datasets/lyricstest.xlsx')

        #
        self.query = self.lineEdit.text()
        self.songrow = self.lyricsdf.loc[self.lyricsdf['Query'] == self.query]
       
        # Checks if there's any matches, if so, will retrieve data from database
        # If not, will run search function instead
        if self.songrow.size > 0:
            self.retrieveDataBase()
        else:
            self.search()

    def clearQuery(self):
        self.label_7.setText('')
        self.query = ''
        self.label_9.setText('')
        #self.hideQuery(self)
    
    # def hideQuery(self):
    #     self.label_7.hide()
    
    # def unhideQuery(self):
    #     self.label_7.show()

    def _buildQuery(self, sub_query):
        self.query = self.label_7.text() + sub_query
        self.label_7.setText(self.query)
        translation = self.translate(self.query)
        self.label_9.setText(translation)
    
    def translate(self, query):
        # Uses MyMemory API to translate the query text
        url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"

        querystring = {"q":query,"langpair":"ja|en","onlyprivate":"0","mt":"1"}

        headers = {
            "X-RapidAPI-Key": config.api_key,
            "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        responsedict = json.loads(response.text)
        #print(responsedict["responseData"]["translatedText"])
        return responsedict["responseData"]["translatedText"]

    
    def search(self):

                
        # Runs if song name not in database:
        self.lyrics = animelyric.search_lyrics(self.query,lang="en")
        # Updates count if not already updated
        #self.lyricsCount = int(self.sheet_lyrics[self.lyricsCountPos].value)
        print(self.lyricsCount)

        self.lyricsresult = self.lyrics[0]
        self.newbuttons = self.lyrics[2]
        self.jplyrics = self.lyrics[3]
        self.songtitle = self.lyrics[1]

        # Gets first line (aka title)
        self.titleonly = self.songtitle.split("\n")[0]
        # print(self.titleonly)
        # print(self.titleonly in self.lyricsdf['Song'].unique())

        #Writes new data
        lyricstitleColumn = 'A' + str(self.lyricsCount)
        print(lyricstitleColumn)
        lyricslyricsColumn = 'B' + str(self.lyricsCount)
        print(lyricslyricsColumn)
        lyricsqueryresult = 'C' + str(self.lyricsCount)
        lyricsnewbuttonsColumn = 'D' + str(self.lyricsCount)
        lyricsjplyricsColumn = 'E' + str(self.lyricsCount)

        lyricsSongCountCol = 'G' + str(self.lyricsCount)
        lyricsfirstindexresult = 'H' + str(self.lyricsCount)

        # Updates cell values with song data
        self.sheet_lyrics[lyricstitleColumn].value = self.titleonly
        self.sheet_lyrics[lyricslyricsColumn].value = self.lyrics[1]
        stringRepOfLyrics2 = pprint.pformat(self.lyrics[2])
        self.sheet_lyrics[lyricsnewbuttonsColumn].value = stringRepOfLyrics2
        stringRepOfLyrics3 = pprint.pformat(self.lyrics[3])
        self.sheet_lyrics[lyricsjplyricsColumn].value = stringRepOfLyrics3
        stringRepOfLyrics0 = pprint.pformat(self.lyrics[0])
        self.sheet_lyrics[lyricsfirstindexresult].value = stringRepOfLyrics0
        self.sheet_lyrics[lyricsqueryresult].value = self.query

        # Increment count
        self.lyricsCount += 1
        print(self.lyricsCount)

        # Save lyric count value
        self.sheet_vocab[self.lyricsCountPos].value = self.lyricsCount
        print(self.sheet_vocab[self.lyricsCountPos].value)
        # Save song's individual count label
        self.sheet_vocab[lyricsSongCountCol].value = self.lyricsCount

        self.label_5.setText(self._translate("MainWindow", self.lyricsresult))

        self.lyricswb.save(self.lyricspath)
        self.lyricswb.close
        self.createLyricsButtons()
        # except:
        #     self.label_5.setText(_translate("MainWindow", "No Lyrics Found"))
        #     self.label_3.setText(_translate("MainWindow", "No Lyrics Found"))
    
    
    def save(self):
        # Column positions for vocab spreadsheet
        vocabkanjiColumn = 'A' + str(self.vocabCount)
        vocabromajiColumn = 'C' + str(self.vocabCount)
        vocabtitleColumn = 'D' + str(self.vocabCount)

        # Assigns kanji to A col
        self.sheet_vocab[vocabkanjiColumn].value = self.label_7.text()
        # Assigns definition to C col
        self.sheet_vocab[vocabromajiColumn].value = self.label_9.text()
        # Assigns song title to D col
        try:
            self.sheet_vocab[vocabtitleColumn].value = self.titleonly
        except:
            self.sheet_vocab[vocabtitleColumn].value = self.songtitle

        # Increment count
        self.vocabCount += 1
        print(self.vocabCount)

        # Save new count
        self.sheet_vocab[self.vocabCountPos].value = self.vocabCount

        self.vocabwb.save(self.vocabpath)
        self.lyricswb.close
        self.vocabwb.close
    
    def useBackUp(self):
        self.label_5.setText(self._translate("MainWindow", self.lyrics))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())