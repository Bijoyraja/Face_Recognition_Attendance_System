from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from collectData import Student
from learn import Train
from recognizer import Face_Recognization


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("icon.ico")


        # ____________________B A C K G R O U N D   I M A G E_________________________

        bg_img = Image.open(r"F:\Face_Recognition_Attendance_System\images\black_bg.png")
        #img = img.resize(500,130)
        self.photoimg = ImageTk.PhotoImage(bg_img)

        bg_lbl = Label(self.root, image = self.photoimg)
        bg_lbl.place(x = 0, y = 0, width = 1280, height = 750 )

        title_lbl = Label(bg_lbl, text = "FACE RECOGNITION ATTENDANCE SYSTEM", font = ("times new roman", 15, "bold"), bg = "black", fg = "white")
        title_lbl.place(x = 0, y = 0, width = 1280, height = 30)


        # ____________________T A K E   P H O T O   B U T T O N_________________________
        b1 = Button(bg_lbl, text = "ADD A NEW PERSON", command = self.student_details, bg = "yellow", cursor = "hand2")
        b1.place(x = 80, y = 200, width = 220, height = 40)

        # ____________________A T T E N D A N C E   B U T T O N_________________________
        b2 = Button(bg_lbl, text = "DETECT FACE", command = self.face_data, bg = "yellow", cursor = "hand2")
        b2.place(x = 530, y = 200, width = 220, height = 40)

        # ____________________T R A I N   B U T T O N_________________________
        b3 = Button(bg_lbl, text = "TRAINING DATA", command = self.train_classification, bg = "yellow", cursor = "hand2")
        b3.place(x = 980, y = 200, width = 220, height = 40)


        # b3 = Button(bg_lbl, text = "TRAIN DATA", bg = "yellow", cursor = "hand2")
        # b3.place(x = 530, y = 200, width = 220, height = 40)
        



#___________________________Functions Button____________________________
    
    # def student_details(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = Student(self.new_window)

    def student_details(self):
        self.student_details = tkinter.messagebox.askyesno("Alert", "Do you want to add a new person?", parent = self.root)
        if self.student_details > 0:
            self.new_window = Toplevel(self.root)
            self.app = Student(self.new_window)
        else:
            return

    

    def train_classification(self):
        self.train_classification = tkinter.messagebox.askyesno("Alert", "Do you want to train all the data?", parent = self.root)
        if self.train_classification > 0:
            self.new_window = Toplevel(self.root)
            self.app = Train(self.new_window)
        else:
            return
        
    
    def face_data(self):
        self.face_data = tkinter.messagebox.askyesno("Alert", "Do you want to open the detection window?", parent = self.root)
        if self.face_data > 0:
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognization(self.new_window)
        else:
            return
        


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()



    

