from tkinter import Button, Entry, Label, Tk, Listbox

from main import getCategoryCount, getClassifiedCategories


def evaluate(entry, listbox):
    listbox.delete('0', 'end')
    question = entry.get()
    category_count = getCategoryCount(question)
    categories = getClassifiedCategories(category_count)
    for index, category in enumerate(categories):
        listbox.insert(index+1, category)


master = Tk()
master.title('Questions Classifier')

Label(master, text='Question').grid(row=0, column=0)

entry = Entry(master, width=100)
entry.grid(row=0, column=1)

listbox = Listbox(master)
listbox.grid(row=2)

Button(master, text='Classify', command=lambda: evaluate(
    entry, listbox)).grid(row=1)

master.mainloop()
