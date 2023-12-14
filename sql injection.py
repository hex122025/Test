import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Entry, Button

def check_sql_injection():
    url = entry.get()
    response = requests.get(url)
    html_content = response.text

    if "error in your SQL syntax" in html_content:
        status_label.config(text="تم العثور على ثغرة SQL injection!", fg="green")
        exploit_button.config(state="normal")
    else:
        status_label.config(text="لم يتم العثور على ثغرة SQL injection.", fg="red")
        exploit_button.config(state="disabled")

def exploit_files():
    # قم بتنفيذ استغلال الملفات الخاصة بالموقع هنا
    pass

# إنشاء نافذة التطبيق
window = Tk()
window.title("أداة فحص SQL Injection")
window.geometry("400x200")

# إضافة حقوق ملكية الأداة
copyright_label = Label(window, text="جميع الحقوق محفوظة © 2023")
copyright_label.pack()

# إضافة مدخل الرابط
url_label = Label(window, text="الرابط:")
url_label.pack()
entry = Entry(window)
entry.pack()

# إضافة زر الفحص
check_button = Button(window, text="فحص", command=check_sql_injection)
check_button.pack()

# إضافة تسمية الحالة
status_label = Label(window, text="")
status_label.pack()

# إضافة زر استغلال الملفات
exploit_button = Button(window, text="استغلال الملفات", state="disabled", command=exploit_files)
exploit_button.pack()

# تشغيل النافذة
window.mainloop()