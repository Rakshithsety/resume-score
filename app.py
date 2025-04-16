import tkinter as tk
from tkinter import filedialog, messagebox
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

def process_docx(path):
    return docx2txt.process(path)

def calculate_similarity(jd_text, resume_text):
    content = [jd_text, resume_text]
    cv = CountVectorizer()
    matrix = cv.fit_transform(content)
    similarity_matrix = cosine_similarity(matrix)
    return round(similarity_matrix[1][0] * 100, 2)

def upload_jd():
    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if file_path:
        jd_path.set(file_path)

def upload_resume():
    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if file_path:
        resume_path.set(file_path)

def check_match():
    if not jd_path.get() or not resume_path.get():
        messagebox.showwarning("Missing Files", "Please upload both JD and Resume.")
        return

    jd_text = process_docx(jd_path.get())
    resume_text = process_docx(resume_path.get())
    score = calculate_similarity(jd_text, resume_text)
    messagebox.showinfo("Match Score", f"Resume matches the JD by {score}%")

# GUI Setup
root = tk.Tk()
root.title("Resume vs JD Matcher")
root.geometry("400x250")

jd_path = tk.StringVar()
resume_path = tk.StringVar()

tk.Label(root, text="Upload Job Description (.docx)").pack(pady=5)
tk.Button(root, text="Browse JD", command=upload_jd).pack()

tk.Label(root, text="Upload Resume (.docx)").pack(pady=10)
tk.Button(root, text="Browse Resume", command=upload_resume).pack()

tk.Button(root, text="Check Match Score", command=check_match, bg="green", fg="white").pack(pady=20)

root.mainloop()