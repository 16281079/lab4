from tkinter import *
from mainlist import *


class UserInterface:
    def __init__(self, master):
        self.root = master
        self.root.geometry('420x340')
        self.varSeq = StringVar()
        self.varL = StringVar()
        self.varN = StringVar()
        self.varP = StringVar()
        self.varE = StringVar()
        self.varM = StringVar()
        self.varT = StringVar()
        self.varOPR = StringVar()
        self.varFIFO = StringVar()
        self.varLRU = StringVar()
        self.varENRU = StringVar()
        self.CreateTestingPage()

    def Calculate(self):
        r = random.random()
        Seq = int(self.varSeq.get())
        L = int(self.varL.get())
        t = float(self.varT.get())
        N = int(self.varN.get())
        p = int(self.varP.get())
        e = int(self.varE.get())
        m = int(self.varM.get())
        Sequence_String = Random_Sequence_String(p, p + e, Seq, m, N)
        if r > t:
            p = (p + 1) % N
        else:
            p = random.randrange(0, N, 1)
        print(Sequence_String)
        self.varOPR.set(Optimal_page_replacement_algorithm(Sequence_String, L) / Seq * 100)
        self.varFIFO.set(First_In_First_Out_algorithm(Sequence_String, L) / Seq * 100)
        self.varLRU.set(Least_Recently_Used_algorithm(Sequence_String, L) / Seq * 100)
        self.varENRU.set(Enhanced_Not_Recently_Used_algorithm(Sequence_String, L) / Seq * 100)

    def CreateTestingPage(self):
        self.frame_left_top = Frame(width=500, height=270)
        self.frame_right_top = Frame(width=500, height=270)
        self.frame_left = Frame(width=500, height=270)
        self.frame_right = Frame(width=500, height=270)
        self.frame_bottom = Frame(width=500, height=270)
        self.frame_bottom_left = Frame(width=500, height=270)

        ###################################The interface on the left side that can enter the parameter#########################################
        tx1 = Label(self.frame_left_top, text="   Please enter the parameter").grid(row=0, column=0, pady=10)

        sheetSeq = Entry(self.frame_bottom_left, textvariable=self.varSeq).grid(row=1, column=1, pady=10)
        sheetL = Entry(self.frame_left, textvariable=self.varL).grid(row=1, column=1, pady=10)
        sheetN = Entry(self.frame_left, textvariable=self.varN).grid(row=2, column=1, pady=10)
        sheetP = Entry(self.frame_left, textvariable=self.varP).grid(row=3, column=1, pady=10)
        sheetE = Entry(self.frame_left, textvariable=self.varE).grid(row=4, column=1, pady=10)
        sheetM = Entry(self.frame_left, textvariable=self.varM).grid(row=5, column=1, pady=10)
        sheetT = Entry(self.frame_left, textvariable=self.varT).grid(row=6, column=1, pady=10)

        labelSeq = Label(self.frame_bottom_left, text="Seq").grid(row=1, column=0)
        labelL = Label(self.frame_left, text="L").grid(row=1, column=0)
        labelN = Label(self.frame_left, text="N").grid(row=2, column=0)
        labelP = Label(self.frame_left, text="P").grid(row=3, column=0)
        labelE = Label(self.frame_left, text="E").grid(row=4, column=0)
        labelM = Label(self.frame_left, text="M").grid(row=5, column=0)
        labelT = Label(self.frame_left, text="T").grid(row=6, column=0)
        #######################################################################################################################################

        ###################################The interface on the left side that can enter the parameter#########################################
        tx2 = Label(self.frame_right_top, text="   The result are shown here").grid(row=0, column=0)

        sheetOPR = Entry(self.frame_right, textvariable=self.varOPR).grid(row=1, column=1, pady=10)
        sheetFIFO = Entry(self.frame_right, textvariable=self.varFIFO).grid(row=3, column=1, pady=10)
        sheetLRU = Entry(self.frame_right, textvariable=self.varLRU).grid(row=4, column=1, pady=10)
        sheetENRU = Entry(self.frame_right, textvariable=self.varENRU).grid(row=6, column=1, pady=10)

        labelOPR = Label(self.frame_right, text="OPR").grid(row=1, column=0)
        labelFIFO = Label(self.frame_right, text="FIFO").grid(row=3, column=0)
        labelLRU = Label(self.frame_right, text="LRU").grid(row=4, column=0)
        labelENRU = Label(self.frame_right, text="ENRU").grid(row=6, column=0)

        percent1 = Label(self.frame_right, text="%").grid(row=1, column=2)
        percent2 = Label(self.frame_right, text="%").grid(row=3, column=2)
        percent3 = Label(self.frame_right, text="%").grid(row=4, column=2)
        percent4 = Label(self.frame_right, text="%").grid(row=6, column=2)
        #######################################################################################################################################
        bottom = Button(self.frame_bottom, text="Press to calculate", command=self.Calculate).grid(row=0, column=0)

        self.frame_left_top.grid(row=0, column=0, padx=10)
        self.frame_right_top.grid(row=0, column=1, padx=10)
        self.frame_left.grid(row=1, column=0, padx=10)
        self.frame_right.grid(row=1, column=1, padx=10)
        self.frame_bottom.grid(row=2, column=1)
        self.frame_bottom_left.grid(row=2, column=0)


if __name__ == '__main__':
    root = Tk()
    root.title('Page replacement algorithm')
    UserInterface(root)
    root.mainloop()

