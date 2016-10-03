from Tkinter import *
from math import *

from Graph import Graph



def test_interface(master=None):

    if master is None:
        print "Master is None"
        return
        pass

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
    pass

def test_graph_plotting(root):

    root.title('Simple Plot - Version 3 - Smoothed')

    try:
        canvas = Canvas(root, width=450, height=300, bg = 'white')
        canvas.pack()
        Button(root, text='Quit', command=root.quit).pack()

        canvas.create_line(100,250,400,250, width=2)
        canvas.create_line(100,250,100,50,  width=2)

        for i in range(11):
            x = 100 + (i * 30)
            canvas.create_line(x,250,x,245, width=2)
            canvas.create_text(x,254, text='%d'% (10*i), anchor=N)

        for i in range(6):
            y = 250 - (i + 40)
            canvas.create_line(100,y,105,y, width=2)
            canvas.create_text(96,y, text='%5.1f'% (50.*i), anchor=E)

        scaled = []
        for x, y in [(12, 56), (20, 94), (33, 98), (45, 120), (61, 180),
                    (75, 160), (98, 223)]:
            scaled.append( (100 + 3*x, 250 - (4*y)/5) )

        canvas.create_line(scaled, fill='black', smooth=1)

        for xs, ys in scaled:
            canvas.create_oval(xs-6,ys-6,xs+6,ys+6, width=1,
                               outline='black', fill='SkyBlue2')
    except Exception as exception:
        print "Exception {}: {}".format(type(exception), exception)

    pass

def test_graph_class(root):

    graph = Graph(root, width=500, height=500)
    graph.addAxes(10, 100, 10, 100)
    
    graph.addLine(20, 20, 50, 60)

    graph.scaleAndCenter()

    graph.pack()
    pass

def main():
    root = Tk()

    # test_interface(root)
    # test_graph_plotting(root)
    test_graph_class(root)

    root.mainloop()
    pass

if __name__ == "__main__":
    main()
    pass