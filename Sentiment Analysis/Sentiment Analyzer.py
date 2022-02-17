import tkinter
from textblob import TextBlob

root = tkinter.Tk()
root.title("Sentiment Analysis")
root.geometry('500x400')
root.resizable(False, False)

background_photo = tkinter.PhotoImage(file="Sentiment Analysis.png")
tkinter.Label(root, image=background_photo).place(x=-2, y=-2)

sentence = tkinter.StringVar()
answer = tkinter.StringVar()

tkinter.Label(root, text="Please type a sentence:", font=('Roboto', 9), fg='black', bg='#cb6ce6').place(x=90, y=190)
entry_box = tkinter.Entry(root, textvariable = sentence, width = 30).place(x = 230, y = 190)

tkinter.Label(root, textvariable = answer, font=('Segoe UI Black', 14), fg='black', bg='#cb6ce6').place(x=210, y=220)


def analyze():
    y = sentence.get()
    edu = TextBlob(y)
    x = edu.sentiment.polarity
    if x < 0:
        answer.set("Negative :(")
    elif x == 0:
        answer.set("Neutral :|")
    elif x > 0 and x <= 1:
        answer.set("Positive :)")

def clear():
    answer.set("")
    sentence.set("")


answer_text = tkinter.StringVar()
tkinter.Label(root, textvariable=answer_text)
tkinter.Button(text = " Analyze! ", command = analyze).place(x=200, y=265)
tkinter.Button(text = " Reset ", command = clear).place(x=275, y=265)


root.mainloop()