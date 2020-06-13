#frontend
from tkinter import*
import tkinter.messagebox
import stdDatabase_Backend

class Hostel:
    def __init__(self,root):
        self.root = root
        self.root.title("Hostel Management System")
        self.root.geometry("1350x7500+0+0") 
        self.root.config(bg="sky blue")

        stdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Parents = StringVar()
        DOB = StringVar()
        Age = StringVar()
        Branch = StringVar()
        Year = StringVar()
        Gender = StringVar()
        Mobile = StringVar()
        Bedno = StringVar()
        #======================================================Function================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hostel Management System", "Confirm if you want to Exit or not")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtStdID.delete(0, END)
            self.txtFna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtGna.delete(0, END)
            self.txtDOB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtBr.delete(0, END)
            self.txtyr.delete(0, END)
            self.txtgd.delete(0, END)
            self.txtMno.delete(0, END)
            self.txtBD.delete(0, END)
        
        def addData():
            if(len(stdID.get()) != 0):
                stdDatabase_Backend.addStdRec(stdID.get() , Firstname.get() , Surname.get() ,Parents.get() , DOB.get() , Age.get() ,Branch.get() , Year.get() , Gender.get() , Mobile.get() , Bedno.get() )
                studentlist.delete(0, END)
                studentlist.insert(END,(stdID.get() , Firstname.get() , Surname.get() ,Parents.get() , DOB.get() , Age.get() ,Branch.get() , Year.get() , Gender.get() , Mobile.get() , Bedno.get() ))

        def DisplayData():
            studentlist.delete(0, END)
            for row in stdDatabase_Backend.viewData():
                studentlist.insert(END, row, str(""))

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END, sd[1])
            self.txtFna.delete(0, END)
            self.txtFna.insert(END, sd[2])
            self.txtSna.delete(0, END)
            self.txtSna.insert(END, sd[3])
            self.txtGna.delete(0, END)
            self.txtGna.insert(END, sd[4])
            self.txtDOB.delete(0, END)
            self.txtDOB.insert(END, sd[5])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[6])
            self.txtBr.delete(0, END)
            self.txtBr.insert(END, sd[7])
            self.txtyr.delete(0, END)
            self.txtyr.insert(END, sd[8])
            self.txtgd.delete(0, END)
            self.txtgd.insert(END, sd[9])
            self.txtMno.delete(0, END)
            self.txtMno.insert(END, sd[10])
            self.txtBD.delete(0, END)
            self.txtBD.insert(END, sd[11])

            
        
        def DeleteData():
            if(len(stdID.get()) != 0):
                stdDatabase_Backend.deleteRec(sd[0])
                clearData()
                DeleteData()

        def searchDatabase():
            studentlist.delete(0, END)
            for row in stdDatabase_Backend.searchData(stdID.get() , Firstname.get() , Surname.get() ,Parents.get() , DOB.get() , Age.get() ,Branch.get() , Year.get() , Gender.get() , Mobile.get() , Bedno.get()):
                studentlist.insert(END, row, str(""))

        def update():
            if(len(stdID.get()) !=0):
                stdDatabase_Backend.deleteRec(sd[0])
            if(len(stdID.get()) != 0):
                stdDatabase_Backend.addStdRec(stdID.get() , Firstname.get() , Surname.get() ,Parents.get() , DOB.get() , Age.get() ,Branch.get() , Year.get() , Gender.get() , Mobile.get() , Bedno.get() )
                studentlist.delete(0, END)
                studentlist.insert(END, (stdID.get() , Firstname.get() , Surname.get() ,Parents.get() , DOB.get() , Age.get() ,Branch.get() , Year.get() , Gender.get() , Mobile.get() , Bedno.get() ) )

                




        #======================================================Frames================================================================
        MainFrame = Frame(self.root, bg="sky blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8 , bg="Ghost white", relief=RIDGE)
        TitFrame.pack(side = TOP)

        self.lblTit = Label(TitFrame, font=('areal', 47,'bold'),text='Hostel Management System', bg='ghost white')
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70,  padx=18, pady=10 , bg="Ghost white", relief=RIDGE)
        ButtonFrame.pack(side = BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400,  padx=20, pady=20 , relief=RIDGE, bg="sky blue")
        DataFrame.pack(side = BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=1000, height=600,  padx=20 , relief=RIDGE, bg="Ghost white",
                                 font=('areal', 20,'bold'), text='Student Information\n')
        DataFrameLeft.pack(side = LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1, width=450, height=300,  padx=31, pady=3 , relief=RIDGE, bg="Ghost white",
                                 font=('areal', 20,'bold'), text='Student Details\n')
        DataFrameRight.pack(side = RIGHT)
        #======================================================Label & entry================================================================
        self.lblStdID = Label(DataFrameLeft, font=('areal', 20,'bold'),text='Student ID:',  padx=2, pady=2, bg='ghost white')
        self.lblStdID.grid(row=0, column=0,)
        self.txtStdID = Entry(DataFrameLeft, font=('areal', 20,'bold'), textvariable=stdID, width = 39)
        self.txtStdID.grid(row=0, column=1)

        self.lblFna = Label(DataFrameLeft, font=('areal', 20,'bold'),text='First name:',  padx=2, pady=2, bg='ghost white')
        self.lblFna.grid(row=1, column=0,)
        self.txtFna = Entry(DataFrameLeft, font=('areal', 20,'bold'), textvariable=Firstname, width = 39)
        self.txtFna.grid(row=1, column=1)

        self.lblSna = Label(DataFrameLeft, font=('areal', 20,'bold'),text='Surname:',  padx=2, pady=2, bg='ghost white')
        self.lblSna.grid(row=2, column=0,)
        self.txtSna = Entry(DataFrameLeft, font=('areal', 20,'bold'), textvariable=Surname, width = 39)
        self.txtSna.grid(row=2, column=1)

        self.lblGna = Label(DataFrameLeft, font=('areal', 20,'bold'),text='Father/Mother Name:',  padx=2, pady=2, bg='ghost white')
        self.lblGna.grid(row=3, column=0,)
        self.txtGna = Entry(DataFrameLeft, font=('areal', 20,'bold'), textvariable=Parents, width = 39)
        self.txtGna.grid(row=3, column=1)

        self.lblDOB = Label(DataFrameLeft, font=('areal', 20,'bold'),text='DOB:',  padx=2, pady=2, bg='ghost white')
        self.lblDOB.grid(row=4, column=0,)
        self.txtDOB = Entry(DataFrameLeft, font=('areal', 20,'bold'), textvariable=DOB, width = 39)
        self.txtDOB.grid(row=4, column=1)

        self.lblAge = Label(DataFrameLeft, font=('areal', 20,'bold'),text='Age:',  padx=2, pady=2, bg='ghost white')
        self.lblAge.grid(row=5, column=0,)
        self.txtAge = Entry(DataFrameLeft, font=('areal', 20,'bold'), textvariable=Age, width = 39)
        self.txtAge.grid(row=5, column=1)

        self.lblBr = Label(DataFrameLeft, font=('areal', 20,'bold'),text='Branch:',  padx=2, pady=2, bg='ghost white')
        self.lblBr.grid(row=6, column=0,)
        self.txtBr = Entry(DataFrameLeft, font=('areal', 20,'bold'), textvariable=Branch, width = 39)
        self.txtBr.grid(row=6, column=1)

        self.lblyr = Label(DataFrameLeft, font=('areal', 20,'bold'),text='Year of Studying:',  padx=2, pady=2, bg='ghost white')
        self.lblyr.grid(row=7, column=0,)
        self.txtyr = Entry(DataFrameLeft, font=('areal', 20,'bold'), textvariable=Year, width = 39)
        self.txtyr.grid(row=7, column=1)

        self.lblgd = Label(DataFrameLeft, font=('areal', 20,'bold'),text='Gender:',  padx=2, pady=2, bg='ghost white')
        self.lblgd.grid(row=8, column=0,)
        self.txtgd = Entry(DataFrameLeft, font=('areal', 20,'bold'), textvariable=Gender, width = 39)
        self.txtgd.grid(row=8, column=1)


        self.lblMno = Label(DataFrameLeft, font=('areal', 20,'bold'),text='Mobile no.:',  padx=2, pady=2, bg='ghost white')
        self.lblMno.grid(row=9, column=0,)
        self.txtMno = Entry(DataFrameLeft, font=('areal', 20,'bold'), textvariable=Mobile, width = 39)
        self.txtMno.grid(row=9, column=1)

        self.lblBD = Label(DataFrameLeft, font=('areal', 20,'bold'),text='Bed No.:',  padx=2, pady=2, bg='ghost white')
        self.lblBD.grid(row=10, column=0,)
        self.txtBD = Entry(DataFrameLeft, font=('areal', 20,'bold'), textvariable=Bedno, width = 39)
        self.txtBD.grid(row=10, column=1)

        #======================================================List box & scroll================================================================
        scrollbar=Scrollbar(DataFrameRight)
        scrollbar.grid(row = 0, column=1, sticky='ns')

        studentlist =Listbox(DataFrameRight, width=41, height=16, font=('areal', 12,'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<LishboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = studentlist.yview)

        #=========================================================Button================================================================
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('areal', 20,'bold'), height=1,width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column=0)
        self.btnDispdata = Button(ButtonFrame, text="Display", font=('areal', 20,'bold'), height=1,width=10, bd=4, command=DisplayData)
        self.btnDispdata.grid(row=0, column=1)
        self.btnCleardata = Button(ButtonFrame, text="Clear", font=('areal', 20,'bold'), height=1,width=10, bd=4 , command=clearData)
        self.btnCleardata.grid(row=0, column=2)
        self.btnDeletedata = Button(ButtonFrame, text="Delete", font=('areal', 20,'bold'), height=1,width=10, bd=4, command= DeleteData)
        self.btnDeletedata.grid(row=0, column=3)
        self.btnSearchdata = Button(ButtonFrame, text="Search", font=('areal', 20,'bold'), height=1,width=10, bd=4, command=searchDatabase)
        self.btnSearchdata.grid(row=0, column=4)
        self.btnupdatedata = Button(ButtonFrame, text="Update", font=('areal', 20,'bold'), height=1,width=10, bd=4, command=update)
        self.btnupdatedata.grid(row=0, column=5)
        self.btnExit = Button(ButtonFrame, text="Exit", font=('areal', 20,'bold'), height=1,width=10, bd=4, command= iExit )
        self.btnExit.grid(row=0, column=6)


if __name__=='__main__':
    root = Tk()
    application = Hostel(root)
    root.mainloop()