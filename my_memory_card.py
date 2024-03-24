from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout,QGroupBox, QRadioButton, QPushButton, QLabel,QButtonGroup
from random import shuffle , randint


git удаленное добавление источника https://github.com/Alex85073/memoryCard.git
 git Branch -M main 
git push -u origin main

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

question_list = []
question_list.append(Question("Вопрос1","1","2","3","4"))
question_list.append(Question("Вопрос2","2","3","4","1"))
question_list.append(Question("Вопрос3","3","4","1","2"))
question_list.append(Question("Вопрос4","4","1","2","3"))



app=QApplication([])
btn_ok=QPushButton("Ответить")
ib_Question=QLabel("djghjc")
RadioGroupBox=QGroupBox("Варианты ответов:")

rbtn_1=QRadioButton()
rbtn_2=QRadioButton()
rbtn_3=QRadioButton()
rbtn_4=QRadioButton()

RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_1=QHBoxLayout()
layout_2=QVBoxLayout()
layout_3=QVBoxLayout()

layout_2.addWidget(rbtn_1)
layout_2.addWidget(rbtn_2)
layout_3.addWidget(rbtn_3)
layout_3.addWidget(rbtn_4)

layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)

RadioGroupBox.setLayout(layout_1)


AnsGroupBox=QGroupBox("результат теста")
ib_Result=QLabel("Прав ты или нет")
ib_Correct=QLabel("ОТвет будет тут")

layout_res=QVBoxLayout()
layout_res.addWidget(ib_Result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(ib_Correct,alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()

layout_line1.addWidget(ib_Question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok,stretch=2)
layout_line3.addStretch(1)

layout_card=QVBoxLayout()
layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Следующий вопрос")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answer=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    ib_Question.setText(q.question)
    ib_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    ib_Result.setText(res) 
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct("Правильно!Ё")
        window.score += 1
        print("Статистика:\n-Всего вопросов:",window.total, "\n-Правильных ответов:", int(window.score))
        print("Рейтинг:", str(int(window.score/window.total*100)),"%")
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct("Неверно!")
            print("Рейтинг:", str(int(window.score/window.total*100)),"%")

def next_question():
    window.total +=1
    print("Статистика:\n-Всего вопросов:",window.total, "\n-Правильных ответов:", int(window.score))
    cur_queston=randint(0,len(question_list)- 1)
    q= question_list[cur_queston]
    ask(q)
def click_ok():
    if btn_ok.text()=="Ответить":
        check_answer()
    else:
        next_question()


            




window=QWidget()
window.setLayout(layout_card)
window.setWindowTitle("Вопроситель 3000")

window.cur_queston=-1


window.score=0
window.total=0
btn_ok.clicked.connect(click_ok)
next_question()
window.resize(600,500)
window.show()
app.exec()
