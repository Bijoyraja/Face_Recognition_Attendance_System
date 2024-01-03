from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.train_classifier()
        self.root.wm_iconbitmap("icon.ico")
        # self.root.geometry("430x190+450+250")
        # self.root.title("Alert")

        # title_lbl = Label(self.root, text = "Do you want to Train?", font = ("times new roman", 10, "bold"), fg = "black")
        # title_lbl.place(x = 0, y = 50, width = 420, height = 30)

        # b4 = Button(self.root, text = "Yes", command = self.train_classifier, bg = "white", cursor = "hand2")
        # b4.place(x = 180, y = 120, width = 60, height = 20)
    
    def train_classifier(self):
        data_dir = ("data")
        path = [ os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')   #Gray Scale Image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)




        #________________________________Train The Classifier And Save_____________________________________
        
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed")




if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
