from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("icon.ico")



        #______________________Variables___________________
        self.var_course = StringVar()
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_stdID = StringVar()
        self.var_stdName = StringVar()
        self.var_phn = StringVar()
        self.var_dob = StringVar()
        
        









        # ____________________B A C K G R O U N D   I M A G E_________________________

        bg_img = Image.open(r"F:\Face_Recognition_Attendance_System\images\white_bg.png")
        #img = img.resize(500,130)
        self.photoimg = ImageTk.PhotoImage(bg_img)

        bg_lbl = Label(self.root, image = self.photoimg)
        bg_lbl.place(x = 0, y = 0, width = 1280, height = 750 )


        title_lbl = Label(bg_lbl, text = "Add A New Person", font = ("times new roman", 18, "bold"), bg = "black", fg = "white")
        title_lbl.place(x = 0, y = 0, width = 1280, height = 30)

 
        # ____________________W H O L E   W H I T E   F R A M E_________________________
        
        frame = Frame(bg_lbl, bd = 2)
        frame.place(x = 0, y = 30, width = 1280, height = 720)


        # ____________________L E F T   F R A M E_________________________

        left_frame = LabelFrame(frame, bd = 2, relief = RIDGE, text = "Adding or Updating Information", font = ("times new roman", 13, "bold"), fg = "red")
        left_frame.place(x = 0, y = 0, width = 1272, height = 180)
       
       

        #__________________________DETAILS OF THE STUDENT_______________________________
                            #Course
        crs_label = Label(left_frame, text = "Course: ", font = ("times new roman", 12, "bold"))
        crs_label.grid(row = 0, column = 0, padx = 5, pady = 5)

        crs_combo = ttk.Combobox(left_frame, textvariable = self.var_course, font = ("times new roman", 12, "bold"), state = "readonly")
        crs_combo["values"] = ("Select Course", "B.Tech", "Computer Application", "Management")
        crs_combo.current(0)
        crs_combo.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)                    
                            
                            
                            #Department
        dep_label = Label(left_frame, text = "Department: ", font = ("times new roman", 12, "bold"))
        dep_label.grid(row = 0, column = 2, padx = 10)

        dep_combo = ttk.Combobox(left_frame, textvariable = self.var_dep, font = ("times new roman", 12, "bold"), state = "readonly")
        dep_combo["values"] = ("Select Department", "BCA", "MCA", "Mechanical", "Civil", "IT", "CSE", "ECE", "EE")
        dep_combo.current(0)
        dep_combo.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = W)

        

                            #Year
        year_label = Label(left_frame, text = "Year: ", font = ("times new roman", 12, "bold"))
        year_label.grid(row = 0, column = 4, padx = 15, pady = 5)
        
        year_combo = ttk.Combobox(left_frame, textvariable = self.var_year, font = ("times new roman", 12, "bold"), state = "readonly")
        year_combo["values"] = ("Select Year", "1", "2", "3", "4")
        year_combo.current(0)
        year_combo.grid(row = 0, column = 5, padx = 5, pady = 5, sticky = W)


                            #Semester
        semester_label = Label(left_frame, text = "Semester:", font = ("times new roman", 12, "bold"))
        semester_label.grid(row = 0, column = 6, padx = 10)
        
        semester_combo = ttk.Combobox(left_frame, textvariable = self.var_semester, font = ("times new roman", 12, "bold"), state = "readonly")
        semester_combo["values"] = ("Select Semester", "SEM-I", "SEM-II", "SEM-III", "SEM-IV", "SEM-V", "SEM-VI", "SEM-VII", "SEM-VIII")
        semester_combo.current(0)
        semester_combo.grid(row = 0, column = 7, padx = 10, pady =10, sticky = W)


        
                            #Student ID
        id_label = Label(left_frame, text = "Student ID", font = ("times new roman", 12, "bold"))
        id_label.grid(row = 1, column = 0, padx = 25)
        
        id_label_entry = ttk.Entry(left_frame, textvariable = self.var_stdID, width = 22, font = ("times new roman", 12, "bold"))
        id_label_entry.grid(row = 1, column = 1, padx = 5, pady = 0, sticky = W) 


                            #Name
        studentName_label = Label(left_frame, text = "Student Name", font = ("times new roman", 12, "bold"))
        studentName_label.grid(row = 1, column = 2, padx = 10)
        
        studentName_label_entry = ttk.Entry(left_frame, textvariable = self.var_stdName, width = 22, font = ("times new roman", 12, "bold"))
        studentName_label_entry.grid(row = 1, column = 3, padx = 5, pady = 0, sticky = W) 


                            #Contact No
        contact_label = Label(left_frame, text = "Contact No", font = ("times new roman", 12, "bold"))
        contact_label.grid(row = 1, column = 4, padx = 10)
        
        contact_label_entry = ttk.Entry(left_frame, textvariable = self.var_phn, width = 22, font = ("times new roman", 12, "bold"))
        contact_label_entry.grid(row = 1, column = 5, padx = 5, pady = 0, sticky = W) 


                            #Date Of Birth
        dob_label = Label(left_frame, text = "Date of Birth", font = ("times new roman", 12, "bold"))
        dob_label.grid(row = 1, column = 6, padx = 10)
        
        dob_label_entry = ttk.Entry(left_frame, textvariable = self.var_dob, width = 22, font = ("times new roman", 12, "bold"))
        dob_label_entry.grid(row = 1, column = 7, padx = 10, pady = 0, sticky = W) 
        

        #__________________________B U T T O N S_______________________________

        btn_frame = Frame (left_frame)
        btn_frame.place(x = 5, y = 100, width = 1259, height = 50)

        save_btn = Button(btn_frame, text = "SAVE", command = self.add_data, width = 15, font = ("times new roman", 12, "bold"), bg = "green", fg = "white", cursor = "hand2")
        save_btn.grid( row = 0, column = 0, padx = 22, pady = 6)

        update_btn = Button(btn_frame, text = "UPDATE", command = self.update_data, width = 15, font = ("times new roman", 12, "bold"), bg = "green", fg = "white", cursor = "hand2")
        update_btn.grid( row = 0, column = 1, padx = 22, pady = 6)

        delete_btn = Button(btn_frame, text = "DELETE", command = self.delete_data, width = 15, font = ("times new roman", 12, "bold"), bg = "red", fg = "white", cursor = "hand2")
        delete_btn.grid( row = 0, column = 2, padx = 22, pady = 6)

        reset_btn = Button(btn_frame, text = "RESET", command = self.reset_data, width = 15, font = ("times new roman", 12, "bold"), bg = "red", fg = "white", cursor = "hand2")
        reset_btn.grid( row = 0, column = 3, padx = 22, pady = 6)




        # btn2_frame = Frame (left_frame, bg = "white")
        # btn2_frame.place(x = 5, y = 460, width = 627, height = 120)

        take_photo_btn = Button(btn_frame, text = "TAKE PHOTO SAMPLE", command = self.generate_dataset, width = 49, font = ("times new roman", 12, "bold"), bg = "blue", fg = "white", cursor = "hand2")
        take_photo_btn.grid( row = 0, column = 4, padx  = 22, pady = 6)

        # upload_photo_btn = Button(btn_frame, text = "UPLOAD PHOTO", width = 22, font = ("times new roman", 12, "bold"), bg = "red", fg = "white", cursor = "hand2")
        # upload_photo_btn.grid( row = 0, column = 5, padx  = 18, pady = 6)





        # ____________________R I G H T   F R A M E_________________________

        search_title_lbl = Label(frame, text = "Registered Persons", font = ("times new roman", 18, "bold"), bg = "black", fg = "white")
        search_title_lbl.place(x = 0, y = 185, width = 1272, height = 30)
        
        
        
        search_frame = LabelFrame(frame, bd = 2, relief = RIDGE, text = "Details", font = ("times new roman", 13, "bold"), fg = "red")
        search_frame.place(x = 0, y = 215, width = 1272, height = 442)



        # ____________________S E A R C H   S T U D E N T_________________________
        # search_frame = LabelFrame(right_frame, bd = 2, relief = RIDGE)
        # search_frame.place(x = 0, y = 30, width = 620, height = 80)

        # search_label = Label(search_frame, text = "Search By: ", font = ("times new roman", 12, "bold"))
        # search_label.grid(row = 0, column = 0)

        # search_combo = ttk.Combobox(search_frame, width = 35, font = ("times new roman", 12, "bold"), state = "readonly")
        # search_combo["values"] = ("Select", "ID", "Name", "Phone No")
        # search_combo.current(0)
        # search_combo.grid(row = 0, column = 1, padx = 25, pady = 10, sticky = W)

        # searchEntry_label_entry = ttk.Entry(search_frame, width = 35, font = ("times new roman", 12, "bold"))
        # searchEntry_label_entry.grid(row = 0, column = 2, padx = 25, sticky = W) 


        # search_btn = Button(search_frame, text = "SEARCH", width = 20, font = ("times new roman", 12, "bold"), bg = "grey", fg = "white", cursor = "hand2")
        # search_btn.grid( row = 0, column = 3, padx = 25, pady = 10)

        # showall_btn = Button(search_frame, text = "SHOW ALL", width = 20, font = ("times new roman", 12, "bold"), bg = "grey", fg = "white", cursor = "hand2")
        # showall_btn.grid( row = 0, column = 4, padx = 25, pady = 10)



        # # ____________________P E R S O N   D E T A I L S   T A B L E_________________________
        table_frame = Frame(search_frame, bd = 2, bg = "white", relief = RIDGE)
        table_frame.place(x = 0, y = 10, width = 1268, height = 409)


        scroll_x = ttk.Scrollbar(table_frame, orient =  HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient =  VERTICAL)

        self.student_table = ttk. Treeview(table_frame, column = ("course", "dep", "year", "sem", "id","name", "phn", "dob"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side =RIGHT, fill = Y)
        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)

        self.student_table.heading("course", text = "Course")
        self.student_table.heading("dep", text = "Department")
        self.student_table.heading("year", text = "Year")
        self.student_table.heading("sem", text = "Semester")
        self.student_table.heading("id", text = "Student_Id")
        self.student_table.heading("name", text = "Name")
        self.student_table.heading("phn", text = "Phone")
        self.student_table.heading("dob", text = "DOB")

        self.student_table.column("course", width = 100)
        self.student_table.column("dep", width = 100)
        self.student_table.column("year", width = 100)
        self.student_table.column("sem", width = 100)
        self.student_table.column("id", width = 100)
        self.student_table.column("name", width = 100)
        self.student_table.column("phn", width = 100)
        self.student_table.column("dob", width = 100)

        self.student_table.pack(fill = BOTH, expand = 1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    #_________________________Function Details_____________________
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_stdName.get() == "" or self.var_stdID.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "RJ331AR7", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                    self.var_course.get(),
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_stdID.get(),
                                                                                                    self.var_stdName.get(),
                                                                                                    self.var_phn.get(),
                                                                                                    self.var_dob.get()
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Details has been added successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent = self.root)


    #________________________________Fetching Data To UI______________________________________ 
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username = "root", password = "RJ331AR7", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values = i)
            conn.commit()
        conn.close()
    

    #_______________________________Get Cursor_______________________________
    def get_cursor(self, event = ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_course.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_stdID.set(data[4]),
        self.var_stdName.set(data[5]),
        self.var_phn.set(data[6]),
        self.var_dob.set(data[7])


    #___________________________________Update Function____________________________
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_stdName.get() == "" or self.var_stdID.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            try:
                updt = messagebox.askyesno("Update", "Do you want to update?", parent = self.root)
                if updt > 0:
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = " ", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Course = %s, Dep = %s, Year = %s, Semester = %s, Name = %s, Phone = %s, DOB = %s where Student_id = %s",(
                                                                                                                                                self.var_course.get(),
                                                                                                                                                self.var_dep.get(),
                                                                                                                                                self.var_year.get(),
                                                                                                                                                self.var_semester.get(),
                                                                                                                                                self.var_stdName.get(),
                                                                                                                                                self.var_phn.get(),
                                                                                                                                                self.var_dob.get(),
                                                                                                                                                self.var_stdID.get()
                                                                                                                                             ))
                else:
                    if not updt:
                        return
                messagebox.showinfo("Success", "Details has been updated successfully", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent = self.root)


    #__________________________________Delete Function________________________________
    def delete_data(self):
        if self.var_stdID.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete the student?", parent = self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "RJ331AR7", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id = %s"
                    val = (self.var_stdID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Succesfully deleted the data", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent = self.root)



#_________________________________________Reset__________________________________________
    def reset_data(self):
        self.var_course.set("Select Course"),
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_stdID.set(""),
        self.var_stdName.set(""),
        self.var_phn.set(""),
        self.var_dob.set("")




    # __________________________________________T A K E   P H O T O   S A M P L E S_________________________________________
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_stdName.get() == "" or self.var_stdID.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "RJ331AR7", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Course = %s, Dep = %s, Year = %s, Semester = %s, Name = %s, Phone = %s, DOB = %s where Student_id = %s",(
                                                                                                                                                    self.var_course.get(),
                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                    self.var_year.get(),
                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                    self.var_stdName.get(),
                                                                                                                                                    self.var_phn.get(),
                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                    self.var_stdID.get() == id+1
                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #_________________________Load Predefined data on face frontal from opencv____________________________
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #Minimum Neighbor = 5
                    #Scaling Factor = 1.3

                    for (x,y,w,h) in faces:
                        face_cropped = img [y:y+h, x:x+w]
                        return face_cropped
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame), (450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path ="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)


                    if cv2.waitKey(1) == 13 or int(img_id) == 200:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed")
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent = self.root)











if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
