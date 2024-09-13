import tkinter as tk
from tkinter import messagebox
import pymysql

def fetch_patient_details(patient_id):
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="gokul",
            database="medical_records"
        )
        cursor = connection.cursor()

        query = "SELECT * FROM patients WHERE patient_id = %s"
        cursor.execute(query, (patient_id,))
        result = cursor.fetchone()

        if result:
            show_patient_details(result)
        else:
            messagebox.showerror("Error", "Patient not found!")
        
        cursor.close()
        connection.close()

    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")

def show_patient_details(patient_details):
    for widget in root.winfo_children():
        widget.destroy()

    patient_id, name, age, diagnosis, contact = patient_details

    tk.Label(root, text="Patient Details", font=("Arial", 16)).pack(pady=10)
    
    details = f"""
    Patient ID: {patient_id}
    Name: {name}
    Age: {age}
    Diagnosis: {diagnosis}
    Contact: {contact}
    """
    
    tk.Label(root, text=details, font=("Arial", 12), justify="left").pack(pady=10)

    tk.Button(root, text="Back", command=start_page, font=("Arial", 12)).pack(pady=10)

def start_page():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Enter Patient ID", font=("Arial", 14)).pack(pady=20)
    
    patient_id_entry = tk.Entry(root, font=("Arial", 12))
    patient_id_entry.pack(pady=5)

    def on_enter():
        patient_id = patient_id_entry.get()
        if patient_id.isdigit():
            fetch_patient_details(patient_id)
        else:
            messagebox.showerror("Input Error", "Please enter a valid numeric patient ID.")

    tk.Button(root, text="Enter", command=on_enter, font=("Arial", 12)).pack(pady=10)

root = tk.Tk()
root.title("Medical Record Management")
root.geometry("400x300")

start_page()

root.mainloop()
