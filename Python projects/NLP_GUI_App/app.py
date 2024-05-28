from tkinter import *
from mydb import *
from tkinter import messagebox
from myapi import *


class NlpApp:

    def __init__(self):
        # create db object
        self.dbo = database()
        self.api = API()

        # GUI of login page
        self.root = Tk()
        self.root.title('NLP_App')
        self.root.iconbitmap('favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP_App', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='Login', width=20, height=2, command=self.perform_login)
        login_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now', command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        # clear the existing gui
        self.clear()

        heading = Label(self.root, text='NLP_App', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=20, height=2, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fetch the data from register hui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Register Successfully!')
        else:
            messagebox.showerror('Error', 'Email Already Exists...')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success', 'Login successfully!')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect email/password...')

    def home_gui(self):

        self.clear()

        heading = Label(self.root, text='NLP_App', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Name Entity Recognition', width=30, height=4, command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Analysis', width=30, height=4, command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Login Out', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP_App', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        self.label1 = Label(self.root, text='Enter The Text')
        self.label1.pack(pady=(10, 10))

        self.text_input = Entry(self.root, width=50)
        self.text_input.pack(pady=(5, 10), ipady=4)

        analyze_btn = Button(self.root, text='Analyze Sentiment', width=30, height=4, command=self.sentiment_analysis)
        analyze_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='', bg='#34495E', fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', width=30, height=4, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def sentiment_analysis(self):
        text = self.text_input.get()
        response = self.api.sentiment_analysis(text)
        self.sentiment_result.configure(text=response)

    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP_App', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Name Entity Recognition', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        self.label1 = Label(self.root, text='Enter The Text')
        self.label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        analyze_btn = Button(self.root, text='Analyze NER', width=30, height=4, command=self.ner_analysis)
        analyze_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='#34495E', fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', width=30, height=4, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def ner_analysis(self):
        text = self.ner_input.get()
        response = self.api.ner_analysis(text)
        self.ner_result.configure(text=response)

    def emotion_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP_App', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        self.label1 = Label(self.root, text='Enter The Text')
        self.label1.pack(pady=(10, 10))

        self.emotion_input = Entry(self.root, width=50)
        self.emotion_input.pack(pady=(5, 10), ipady=4)

        analyze_btn = Button(self.root, text='Analyze Emotion', width=30, height=4, command=self.emotion_analysis)
        analyze_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='', bg='#34495E', fg='white')
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', width=30, height=4, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def emotion_analysis(self):
        text = self.emotion_input.get()
        response = self.api.emotion_analysis(text)
        self.emotion_result.configure(text=response)


nlp = NlpApp()
