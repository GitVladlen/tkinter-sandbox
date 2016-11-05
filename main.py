from Tkinter import *
from math import *

def main():
    # model
    words = ["start", "stay", "word", "way", "hello", "hi", "helicopter"]

    def matches(pattern, sequence):
        result = []
        for elem in sequence:
            if elem == pattern:
                break
            if elem.find(pattern) == 0:
                result.append(elem)
        return result

    # tk creating
    root = Tk()
    lb = Listbox(root)
    var = StringVar()
    ent = Entry(root, textvariable=var)
    
    # tk binding
    def cb(*args):
        lb.delete(0, END)

        text = var.get()
        if len(text) == 0:
            return
        
        suggestions = matches(text, words)

        for suggestion in suggestions:
            lb.insert(END, suggestion)

    var.trace("w", cb)

    # tk packing
    ent.pack()
    ent.focus_set()
    lb.pack()

    # start
    root.mainloop()
    pass

if __name__ == "__main__":
    main()
    pass