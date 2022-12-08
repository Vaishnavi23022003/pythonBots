from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizzInterface:

    def __init__(self,quiz_brain:QuizBrain):

        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score=0
        self.score_dislay=Label(text=f"Score: {self.score}",bg=THEME_COLOR,fg="white",font=("Ariel", 10, "bold"))
        self.score_dislay.config(padx=10,pady=10)
        self.score_dislay.grid(row=0,column=1)

        self.canvas=Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.q_text=self.canvas.create_text(150, 125, text="", font=("Ariel", 20, "italic"),fill=THEME_COLOR,width=290)
        self.get_next_ques()
        self.canvas.grid(row=1, column=0, columnspan=2,pady=(20))

        self.t_img = PhotoImage(file="images/true.png")
        self.right = Button(image=self.t_img,command=self.true_ans)
        self.right.config(bg=THEME_COLOR, bd=0, highlightthickness=0, )
        self.right.grid(row=2, column=0)

        self.f_img = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.f_img,command=self.false_ans)
        self.wrong.config(bg=THEME_COLOR, bd=0, highlightthickness=0, )
        self.wrong.grid(row=2, column=1)

        self.answer="True"

        self.window.mainloop()


    def get_next_ques(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.q_text,text= self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.q_text, text=f"You have completed the quiz 🤗\nFinal Score: {self.score}")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def false_ans(self):
        if self.quiz.check_answer("False"):
            self.right_ans()
        else:
            self.wrong_ans()

    def true_ans(self):
        if self.quiz.check_answer("True"):
            self.right_ans()
        else:
            self.wrong_ans()

    def right_ans(self):
        self.score+=1
        self.score_dislay.config(text=f"Score: {self.score}")
        self.canvas.config(bg="green")
        self.window.after(1000, self.get_next_ques)


    def wrong_ans(self):
        self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_ques)


