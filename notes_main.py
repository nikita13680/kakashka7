from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QRadioButton,QMessageBox,QGroupBox,QButtonGroup,QTextEdit,QListWidget,QHBoxLayout,QLineEdit
from random import shuffle 
from random import randint
import json
from PyQt5.QtWidgets import QInputDialog

app = QApplication([])
main_win = QWidget()
main_win.show()


field_text1 = QTextEdit()
list_tags1 = QListWidget()
list_tags2 = QListWidget()
field_text2 = QLineEdit()
button1 = QPushButton('Создать заметку')
button2 = QPushButton('Удалить заметку')
button3 = QPushButton('Сохранить заметку')
button4 = QPushButton('Добавить к заметке')
button5 = QPushButton('Открепить от заметки')
button6 = QPushButton('Искать заметк  по тегу')

with open("text.json","r") as file:
    notes = json.load(file)
    print( notes )
    zxc = list(notes.keys())
    list_tags1.addItems(zxc)

def show_results():
    name = list_tags1.selectedItems()[0].text()
    field_text1.setText(notes[name]["text"])
    list_tags2.clear()
    list_tags2.addItems(notes[name]["tegi"])
    
list_tags1.itemClicked.connect(show_results)

def add_note():
    note_name, result = QInputDialog.getText(main_win,"Добавить заметку","Название заметки:")
    if note_name != "":
        notes[note_name] = {'text':'text','tegi':[]}
        list_tags1.addItem(note_name)
        with open("text.json","w") as file:
            json.dump(notes,file)

def delete_note():
    if list_tags1.selectedItems() :
        note_name = list_tags1.selectedItems()[0].text()
        del notes[note_name]
        with open("text.json","w") as file:
            json.dump(notes,file)
        list_tags1.clear()
        list_tags1.addItems(list(notes))

def save_notes():
    if list_tags1.selectedItems() :
        note_name = list_tags1.selectedItems()[0].text()
        notes[note_name]['text'] = field_text1.toPlainText()
    with open("text.json","w") as file:
        json.dump(notes,file)

def add_tags():
    if list_tags1.selectedItems() :
        note_name = list_tags1.selectedItems()[0].text()
        tags_name = field_text2.text()
        if tags_name != "":
            if not (tags_name in notes[note_name]['tegi']):
                list_tags2.addItem(tags_name)
                notes[note_name]['tegi'].append(tags_name)
                with open("text.json","w") as file:
                    json.dump(notes,file)
                    field_text2.clear()

def delete_tags():
     if list_tags1.selectedItems() :
        if list_tags2.selectedItems() :
            note_name = list_tags1.selectedItems()[0].text()
            tags_name = list_tags2.selectedItems()[0].text()
            notes[note_name]['tegi'].remove(tags_name)
            with open("text.json","w") as file:
                json.dump(notes,file)
                list_tags2.clear()
                list_tags2.addItems(notes[note_name]['tegi'])

def find_tags():
    text_knopki = button6.text()
    if text_knopki == 'Искать заметк  по тегу':
        list_tags1.clear()
        tags_name2 = field_text2.text() 
        button6.setText('Сбросить поиск')
        for tags_name in notes:
            if tags_name2 in notes[tags_name]['tegi']:
                list_tags1.addItem(tags_name)
    else :
        list_tags1.clear()
        button6.setText('Искать заметк  по тегу')
        zxc = list(notes.keys())
        list_tags1.addItems(zxc)


#связь кнопки с функцией
button1.clicked.connect(add_note)
button2.clicked.connect(delete_note)
button3.clicked.connect(save_notes)
button4.clicked.connect(add_tags)
button5.clicked.connect(delete_tags)
button6.clicked.connect(find_tags)

h_line1 = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
v_line3 = QHBoxLayout()
v_line4 = QHBoxLayout()

h_line1.addLayout(v_line1)
h_line1.addLayout(v_line2)

#правая полоса
v_line2.addWidget(list_tags1)
v_line2.addLayout(v_line3)
v_line2.addWidget(button3)
v_line2.addWidget(list_tags2)
v_line2.addWidget(field_text2)
v_line2.addLayout(v_line4)
v_line2.addWidget(button6)

v_line1.addWidget(field_text1)

v_line3.addWidget(button1)
v_line3.addWidget(button2)

v_line4.addWidget(button4)
v_line4.addWidget(button5)

main_win.setLayout(h_line1)

app.exec_()