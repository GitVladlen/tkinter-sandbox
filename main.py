from Tkinter import *
from math import *

def main():

    master = Tk()

    ent_str = StringVar()

    group_chat = LabelFrame(master, text="All chat log", padx=5, pady=5)
    group_chat.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    scrollbar = Scrollbar(group_chat)
    text = Text(group_chat, wrap=WORD, yscrollcommand=scrollbar.set)

    group_msg = LabelFrame(master, text="Enter Message", padx=5, pady=5)
    group_msg.pack(side=TOP, fill=BOTH, padx=10, pady=10)

    btn = Button(group_msg, text="Submit")
    ent = Entry(group_msg, textvariable=ent_str)

    def onClick(event):
        if len(ent_str.get()) == 0:
            return
            pass

        text.config(state=NORMAL)
        msg = "- " + ent_str.get() + "\n"
        ent_str.set("")
        text.insert(END, msg)
        text.config(state=DISABLED)
        pass
    btn.bind("<Button-1>", onClick)
    btn.pack(side=BOTTOM, fill=BOTH)

    
    ent.pack(side=BOTTOM, fill=BOTH)
    
    text["state"] = DISABLED
    text.pack(side=LEFT, fill=BOTH)

    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=text.yview)

    mainloop()
    pass

def main_graph():

    f = raw_input('f(x):')

    root = Tk()

    canv = Canvas(root, width = 1000, height = 1000, bg = "white")
    canv.create_line(500,1000,500,0,width=2,arrow=LAST)
    canv.create_line(0,500,1000,500,width=2,arrow=LAST)

    First_x = -15;

    for i in range(1, 31):
        try:
            prev_x = First_x + (i - 1)
            cur_x = First_x + i
            prev_f = f.replace('x', str(prev_x))
            cur_f = f.replace('x', str(cur_x))
            prev_y = -eval(prev_f) + 500
            cur_y = -eval(cur_f) + 500

            prev_x += 500
            cur_x += 500

            canv.create_line(prev_x, prev_y, cur_x, cur_y, width=1)
        except:
            pass

    canv.pack()
    root.mainloop()
    pass

if __name__ == "__main__":
    # main()
    main_graph()
    pass