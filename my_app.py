from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from random import randint
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
timertwo = 45
timer = 15

def show_win2():
    main_win.hide()
    main_two.show()

def show_win3():
    result = input_result.text()
    rest = input_rest.text()
    indeks_p = QLabel(f'Индекс Руфье:{(4 * (int(result) + int(rest) + 100)-200) / 10}', main_three)
    indeks_p.move(435, 80)
    indeks_p.setFont(QFont('Times', 20, QFont.Bold))
    robotsp = QLabel('Роботоспособность сердца выше среднего', main_three)
    robotsp.move(430, 333)
    main_two.hide()
    main_three.show()



def update_timer():
    global timer
    timer -= 1
    timer_one.setText(f'00:{timer}' )

def update_timertwo():
    global timertwo
    timertwo -= 1
    timer_one.setText(f'00:{timertwo}')

def update_timerthree():
    global timer
    timer -= 1
    timer_one.setText(f'00:{timer}')
def stoptime():
    qttime.stop()
    qttimet.stop()
    qttimeq.stop()
    global timer, timertwo
    timer = 15
    timertwo = 45


app = QApplication([])
main_three = QWidget()
main_three.setWindowTitle('Результаты')
main_three.resize(1000, 700)
main_two = QWidget()
main_two.setWindowTitle('Тест Руфье')
main_two.resize(1000, 700)
main_win = QWidget()
main_win.resize(1000, 700)
main_win.setWindowTitle('Тест Руфье')
text = QLabel('Добро пожаловать в программу по определнию состояния здоровья!', main_win)
text.setFont(QFont('Times', 12, QFont.Bold))
dtext = QLabel('''Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.
Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической
У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;
затем в течение 45 секунд испытуемый выполняет 30 приседаний.
После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,
а потом - за последние 15 секунд первой минуты периода восстановления.
Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в
ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.
нагрузке.''', main_win)
text.move(270, 70)
dtext.move(200, 270)

timer_one = QLabel('00.00', main_two)
timer_one.move(700, 200)
timer_one.setFont(QFont('Times', 36, QFont.Bold))
knop = QPushButton('Начать', main_win)
knop.move(470, 500)
fio = QLabel('Введите Ф.И.О:', main_two)
fio.move(30, 30)
input_field = QLineEdit(main_two)
input_field.setPlaceholderText("Введите текст здесь...")
input_field.move(30, 59)
years = QLabel('Полных лет:', main_two)
years.move(30, 89)
input_years = QLineEdit(main_two)
input_years.setPlaceholderText("Введите текст здесь...")
input_years.move(30, 115)
textt = QLabel('''Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.
Результат запишите в соответствующее поле.''', main_two)
textt.move(30, 150)
starttest = QPushButton('Начать первый тест', main_two)
starttest.move(30, 185)
qttime = QTimer()
qttime.timeout.connect(update_timer)
starttest.clicked.connect(lambda: qttime.start(1000))
dtextt = QLabel('''Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",
чтобы запустить счетчик приседаний. ''', main_two)
dtextt.move(30, 230)
startsit = QPushButton('Начать делать приседание', main_two)
startsit.move(30, 265)
qttimet = QTimer()
qttimet.timeout.connect(update_timertwo)
startsit.clicked.connect(lambda: qttimet.start(1000))

knopt = QPushButton('Стоп', main_two)
knopt.move(300, 400)
knopt.clicked.connect(stoptime)
ddtext = QLabel('''Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.
Нажмите кнопку "Начать финальный тест", чтобы запустить таймер.
Зеленым обозначены секунды, в течение которых необходимо
проводить измерения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля. ''', main_two)
ddtext.move(30, 300)
startfinnal = QPushButton('Начать финальный тест', main_two)
startfinnal.move(30, 365)
qttimeq = QTimer()
qttimeq.timeout.connect(update_timerthree)
startfinnal.clicked.connect(lambda: qttimeq.start(1000))


input_result = QLineEdit(main_two)
input_result.setPlaceholderText("Введите текст здесь...")
input_result.move(30, 400)
input_rest = QLineEdit(main_two)
input_rest.setPlaceholderText("Введите текст здесь...")
input_rest.move(30, 435)
resultat = QPushButton('Отправить результаты', main_two)
resultat.move(325, 470)





knop.clicked.connect(show_win2)
resultat.clicked.connect(show_win3)

main_win.show()

app.exec_()