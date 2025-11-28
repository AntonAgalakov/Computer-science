import tkinter as tk
import tkinter.messagebox as msg

window = tk.Tk()
window.title("Максим")

foods = tk.Listbox(window)
foods.pack()

foods.insert(tk.END, "Пельмени")
foods.insert(tk.END, "Рис")
foods.insert(tk.END, "Майонез")

pole = tk.Entry(window)
pole.pack()

def add():
    data = pole.get()
    if len(data) == 0:
        msg.showerror("Alarm", "Строка не должны быть пустой")
    else:
        foods.insert(tk.END, data)
        pole.delete(0, tk.END)

def remove():
    ind = foods.curselection()[0]
    foods.delete(ind)

def redak():

    novoe = tk.Toplevel(window)
    novoe.title("Редактирование")

    vvod = tk.Entry(novoe)
    vvod.pack()

    def save():
        s = vvod.get()
        ind = foods.curselection()[0]
        foods.delete(ind)
        foods.insert(ind, s)
        novoe.destroy()

    sohr = tk.Button(novoe, text="Сохранить", command=save)
    sohr.pack()


knopochka = tk.Button(window, text="Tik - tik", command=add)
knopochka.pack()

ydalenie = tk.Button(window, text="Udal", command=remove)
ydalenie.pack()

redaktor = tk.Button(window, text="редактировать", command=redak)
redaktor.pack()

window.mainloop()
