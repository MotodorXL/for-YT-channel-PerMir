from tkinter import *
import sys
from tkinter import messagebox as mb
#всё это собираем в .exe_шник через pip pyinstaller -w -F -i "путь к иконке" perekrestokMirovPY.py

class main_tk():
    def __init__(self):
        super().__init__()

window = Tk()
window.title("ПЕРЕКРЁСТНЫЙ ОГОНЬ")
window.geometry('360x250')
window['bg'] = '#7FFFD4' #цвет на любителя всегда можно изменить из таблицы rgb 

def calc():
    f = float(en.get()) + float(en1.get()) + float(en2.get()) + float(en3.get())
    f1 = float(en4.get()) + float(en5.get()) + float(en6.get()) + float(en7.get())
    f2 = float(en8.get()) + float(en9.get()) + float(en10.get()) + float(en11.get())
    summa = round(eval('(f + f1 + f2) *10 /4 /3 /10'), 1)
    mb.showinfo(title='ОЦНЕКА ЗА ФИЛЬМ', message=summa) 
    #модуль math() не нужен, округлил всё через стандартный round(x,[y]) где число Y это знаки после запятой
    
def deleteAll():
    en.delete(0, END)    
    en1.delete(0, END)    
    en2.delete(0, END)    
    en3.delete(0, END)
    en4.delete(0, END)    
    en5.delete(0, END)    
    en6.delete(0, END)    
    en7.delete(0, END)
    en8.delete(0, END)    
    en9.delete(0, END)    
    en10.delete(0, END)    
    en11.delete(0, END)
    
lb = Label(window, text='СЕРЖ', bg='#7FFFD4')
lb.place(x=135, y=15) 
lb1 = Label(window, text='ЛЕКС', bg='#7FFFD4')
lb1.place(x=210, y=15)
lb2 = Label(window, text='СУРЕН', bg='#7FFFD4')
lb2.place(x=275, y=15)

lb_1 = Label(window, text="СЮЖЕТ - ", bg='#7FFFD4')
lb_1.place(x=10, y=50) 
lb_2 = Label(window, text="ВИЗУАЛ - ", bg='#7FFFD4')
lb_2.place(x=10, y=80)
lb_3 = Label(window, text="АТМОСФЕРА - ", bg='#7FFFD4')
lb_3.place(x=10, y=110)
lb_4 = Label(window, text="ИГРА АКТЁРОВ - ", bg='#7FFFD4')
lb_4.place(x=10, y=140)

#x - влево\вправо
#y - вниз/вверх
en = Entry(window)
en.place(x=130, y=50, width = 50)  
en1 = Entry(window)
en1.place(x=130, y=80, width = 50) 
en2 = Entry(window)
en2.place(x=130, y=110, width = 50)
en3 = Entry(window)
en3.place(x=130, y=140, width = 50) 

en4 = Entry(window)
en4.place(x=205, y=50, width = 50) 
en5 = Entry(window)
en5.place(x=205, y=80, width = 50) 
en6 = Entry(window)
en6.place(x=205, y=110, width = 50) 
en7 = Entry(window)
en7.place(x=205, y=140, width = 50) 

en8 = Entry(window)
en8.place(x=275, y=50, width = 50) 
en9 = Entry(window)
en9.place(x=275, y=80, width = 50) 
en10 = Entry(window)
en10.place(x=275, y=110, width = 50)
en11 = Entry(window)
en11.place(x=275, y=140, width = 50)

bt1 = Button(window, text = 'ВЫВОД ОЦЕНКИ ЗА ФИЛЬМ ', bg='#F0E68C', command=calc).place(x=160, y=190)
bt2 = Button(window, text = 'ОЧИСТИТЬ ВСЁ', bg='#F0E68C', command=deleteAll).place(x=30, y=190)

window.mainloop()
#if __name__ == "__main__":
 #   main()