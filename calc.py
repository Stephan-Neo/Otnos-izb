# В программе есть проверка на ввод текста(выводит диологовое окно, если ничего не ввести), проверка на выбор языка
# (выводит диологовое окно, если не выбрать язык или выбрать другой)
# Выполнил: Казанцев Степан СМБ-101

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from math import log2
from webbrowser import open as op
from time import sleep

window: Tk = Tk()
window.geometry(f"1000x600+100+200")
window.resizable(width=False, height=False)
window.title("Калькулятор относительной избыточности")
window.iconbitmap("source/prev.ico")
window.config(bg="white")

rb_var = IntVar()
rb_var.set(0)
message = ''
language = ''

image_1 = PhotoImage(file="source/img_1.png")
image_2 = PhotoImage(file="source/img_2.png")
image_3 = PhotoImage(file="source/img_3.png")
image_4 = PhotoImage(file="source/img_4.png")

gt = PhotoImage(file="source/big_logo.png")
image_clear = PhotoImage(file="source/clear.png")

count_start_calculate = 0

alphabet_power = 0
probability_symbol = {}
entropy = 0
max_entropy = 0
relative_redundancy = 0
len_message = 0


def insertText():
    file_name = fd.askopenfilename()
    f = open(file_name)
    string = f.read()
    inputtxt.delete("1.0", "end")
    inputtxt.insert(1.0, string)
    f.close()


# check function
def check_language():
    global language, alphabet_power, probability_symbol
    if rb_var.get() == 2:
        language = "ENGLISH"
        alphabet_power = 26
        probability_symbol = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }

    elif rb_var.get() == 1:
        language = "RUSSIA"
        alphabet_power = 33
        probability_symbol = {
            'а': 0,
            'б': 0,
            'в': 0,
            'г': 0,
            'д': 0,
            'е': 0,
            'ё': 0,
            'ж': 0,
            'з': 0,
            'и': 0,
            'й': 0,
            'к': 0,
            'л': 0,
            'м': 0,
            'н': 0,
            'о': 0,
            'п': 0,
            'р': 0,
            'с': 0,
            'т': 0,
            'у': 0,
            'ф': 0,
            'х': 0,
            'ц': 0,
            'ч': 0,
            'ш': 0,
            'щ': 0,
            'ъ': 0,
            'ы': 0,
            'ь': 0,
            'э': 0,
            'ю': 0,
            'я': 0
        }


def check_warning():
    if inputtxt.get(1.0, 1.1) == '' or inputtxt.get(1.0, 1.1) == ' ':
        messagebox.showerror('Ошибка', 'Вы не ввели текст!')
    elif language == '':
        messagebox.showerror('Ошибка', 'Вы не выбрали язык!')
    else:
        return True


# draw function
def draw_radiobutton():
    Radiobutton(text="Русский", variable=rb_var, activebackground="purple", value=1,
                font=("Helvetica", 9, "bold"), relief="groove", bg="cyan", fg="black", bd=5, cursor="hand2").place(
        x=760, y=480)
    Radiobutton(text="Английский", variable=rb_var, activebackground="purple", value=2, font=("Helvetica", 9, "bold"),
                relief="groove", bg="cyan", fg="black", bd=5, cursor="hand2").place(x=850, y=480)


def draw_window_right():
    global inputtxt
    Label(window, text="Введите текст",  font=("Helvetica", 20, "bold"), bg="white").place(x=650, y=10)

    inputtxt = Text(window, height=15, width=40, bg="light cyan", pady=5, padx=5, bd=5, font=("Helvetica", 14), spacing2=5, spacing1=5, selectbackground="purple")
    inputtxt.place(x=510, y=50)


    b_open = Button(text="Выбрать", activebackground="purple", command=insertText, font=("Helvetica", 9, "bold"), relief="groove", bg="cyan", fg="black", bd=5, cursor="hand2")
    b_open.place(x=510, y=480)

    draw_radiobutton()

    b_start = Button(text="Рассчитать", width=37, command=start_calculate, activebackground="purple", font=("Helvetica", 14, "bold"), relief="groove", bg="cyan", fg="black", bd=5, cursor="hand2")
    b_start.place(x=510, y=525)


def draw_window_left():
    time_sleep = 0.5

    window.update()
    sleep(time_sleep)

    img_1 = Label(window, image=image_1, bg="white")
    img_1.place(x=0, y=45)
    window.update()
    sleep(time_sleep)

    img_2 = Label(window, image=image_2, bg="white")
    img_2.place(x=5, y=165)
    Label(window, text=round(entropy, 2), fg='cyan', font=("Helvetica", 18, "bold"), bg="white").place(x=350, y=180)
    window.update()
    sleep(time_sleep)

    img_3 = Label(window, image=image_3, bg="white")
    img_3.place(x=8, y=300)
    Label(window, text=round(max_entropy, 2), fg='cyan', font=("Helvetica", 18, "bold"), bg="white").place(x=350, y=305)
    window.update()
    sleep(time_sleep)

    img_4 = Label(window, image=image_4, bg="white")
    img_4.place(x=8, y=420)
    Label(window, text=round(relative_redundancy, 10), fg='cyan', font=("Helvetica", 18, "bold"), bg="white").place(x=280, y=423)
    window.update()
    sleep(time_sleep)

    link = Button(activebackground="white", command=open_site_gtsk, image=gt, font=("Helvetica", 14, "bold"), relief="raised", bg="white", fg="black", bd=0, cursor="hand2")
    link.place(x=10, y=550)


def open_site_gtsk():
    op('https://gtsk.pw', new=0, autoraise=True)


# calculate function
def start_calculate():
    global message, count_start_calculate
    count_start_calculate += 1
    message = inputtxt.get(1.0, 'end').lower()
    check_language()
    if count_start_calculate > 1:
        Label(window, image=image_clear, bg="white").place(x=0, y=0)

    if check_warning():
        try:
            count_element()
            calculate_probability()
            calculate_entropy()
            calculate_relative_redundancy()
            if entropy != 0:
                draw_window_left()
        except ZeroDivisionError:
            messagebox.showerror('Ошибка', 'Вы выбрали не тот язык!')


def count_element():
    global len_message
    len_message = 0
    for i in probability_symbol:
        len_message += message.count(i)


def calculate_probability():
    for i in probability_symbol:
        probability_symbol[i] = message.count(i) / len_message


def calculate_entropy():
    global entropy, max_entropy
    entropy = 0
    max_entropy = 0
    for i in probability_symbol:
        if probability_symbol[i] != 0:
            entropy += probability_symbol[i]*log2(1 / probability_symbol[i])
    max_entropy = len_message*log2(alphabet_power)


def calculate_relative_redundancy():
    global relative_redundancy, max_entropy, entropy
    relative_redundancy = (max_entropy - entropy) / max_entropy


def main():
    draw_window_right()


main()
window.mainloop()
