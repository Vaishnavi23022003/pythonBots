import requests, datetime, random, webbrowser
from tkinter import *

# quotes for title -----------------------------------------
quote = requests.get(url="https://type.fit/api/quotes").json()
quote = random.choice(quote)
quote = f"{quote['text']}  -{quote['author']}"

today = datetime.datetime.now()

# graph methods and variables ---------------------

GRAPH_ID = ["daily", "webandpy", "cp", "exercise"]
quantity = [0, 0, 0, 0, 0]


def show_graph():
    pixela_endpoint = "https://pixe.la/v1/users"
    USR_NAME = "killua"
    TOKEN = "sdfnjfsnsmfn2121"
    graph_endpoint = f"{pixela_endpoint}/{USR_NAME}/graphs"

    headers = {
        "X-USER-TOKEN": TOKEN
    }
    quantity_values=[sum(quantity),quantity[0]+quantity[1],quantity[2]+quantity[3],quantity[4]]
    for i in range(4):
        graph_add_endpoint = f"{graph_endpoint}/{GRAPH_ID[i]}"
        graph_add_config = {
            "date": today.strftime("%Y%m%d"),
            "quantity": str(quantity_values[i]),
        }
        res = requests.post(url=graph_add_endpoint, json=graph_add_config, headers=headers)

    for i in GRAPH_ID:
        webbrowser.open(f"https://pixe.la/v1/users/killua/graphs/{i}.html", new=1)

    window.destroy()


def w():
    quantity[0] = 5


def w2():
    quantity[1] = 5


def w3():
    quantity[2] = 10


def w4():
    quantity[3] = 10


def w5():
    quantity[4] = 5



def q():
    quantity[0] = 10


def q2():
    quantity[1] = 10


def q3():
    quantity[2] = 15


def q4():
    quantity[3] = 15


def q5():
    quantity[4] = 10




half_function_list = [w, w2, w3, w4, w5]
full_function_list = [q, q2, q3, q4, q5,]

window = Tk()
window.title("Daily Checker")
window.config(bg="#2E2837")

bg = PhotoImage(file="bg-img2.png")
canvas = Canvas(width=480 * 2, height=319, highlightthickness=0, bd=0)

canvas.create_image(240 * 2, 319 // 2, image=bg)
canvas.grid(row=0, column=0, columnspan=6)

quote_text = canvas.create_text(240 * 2, 70, text=quote, font=("Ariel", 17, "bold"), fill="#2F2D3F", width=800)

title_text = canvas.create_text(240 * 2, 230, text=f"{today.today().strftime('%A')} {today.date()}",
                                font=("Ariel", 35, "bold"), fill="white", width=700)

Tasks = ["Web Dev", "Python", "Cp-Algo", "Cp-Main", "Exercise"]
Tasks_label = []

for i in range(5):
    x = Label(font=("Ariel", 14, "bold"), fg="white", bg="#2E2837", text=Tasks[i])
    x.config(padx=10, pady=20)
    x.grid(row=1, column=i)
    Tasks_label.append(x)

Zero = ["Slept in", "Cipher", "Nahhh", "Early Bed", "Couldn't"]
zero_buttons = []
for i in range(5):
    x = Button(text=Zero[i], command="")
    x.config(bg="#2E2837", bd=0, highlightthickness=2, padx=10, fg="white", font=("Ariel", 13),
             activeforeground="#FFDDD8", activebackground="#2E2837")
    x.grid(row=2, column=i)
    zero_buttons.append(x)

Half = ["Halfway", "Fractional", "50 50", "At least tried", "      "]
half_buttons = []
for i in range(5):
    x = Button(text=Half[i], command=half_function_list[i])
    x.config(bg="#2E2837", bd=0, highlightthickness=2, padx=10, fg="white", font=("Ariel", 13),
             activeforeground="#FFDDD8", activebackground="#2E2837")
    x.grid(row=3, column=i)
    zero_buttons.append(x)

Full = ["Nailed it!", "Win - Win", "100%","Victory", "Success"]
full_buttons = []
for i in range(5):
    x = Button(text=Full[i], command=full_function_list[i])
    x.config(bg="#2E2837", bd=0, highlightthickness=2, padx=10, fg="white", font=("Ariel", 13),
             activeforeground="#FFDDD8", activebackground="#2E2837")
    x.grid(row=4, column=i)
    zero_buttons.append(x)

x = Label(font=("Ariel", 1, "bold"), fg="white", bg="#2E2837", text="  ")
x.config(padx=10, pady=20)
x.grid(row=5, column=0, columnspan=6)

endb = Button(text="", command="")
endb.config(bg="white", bd=0, highlightthickness=2, padx=0, pady=0, fg="white", font=("Ariel", 19, "bold"),
            activeforeground="white", activebackground="white", width=46)
endb.grid(row=6, column=0, columnspan=6)

end = Button(text="Done", command=show_graph)
end.config(bg="#2E2837", bd=0, highlightthickness=2, padx=0, pady=0, fg="white", font=("Ariel", 18, "bold"),
           activeforeground="white", activebackground="#2E2837", width=46)
end.grid(row=6, column=0, columnspan=6)

x2 = Label(font=("Ariel", 1, "bold"), fg="white", bg="#2E2837", text="  ")
x2.config(padx=10, pady=20)
x2.grid(row=7, column=0, columnspan=6)

window.mainloop()

# Creating a pixela account -----------------------------
#
#
# user_params={
#     "token":TOKEN,
#     "username":USR_NAME,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes",
# }
#
# rep=requests.post(url=pixela_endpoint,json=user_params)
# print(rep.text)
#
#
# Creating a graph ---------------------------------------
#
#
# GRAPH_ID="daily"
#
# graph_config={
#     "id":GRAPH_ID,
#     "name":"Full Daily Commitment",
#     "unit":"commit",
#     "type":"float",
#     "color":"kuro",
# }
#

#
# res=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(res.json())


# update_date=input("Which date to update (yyyymmdd)? ")
# new_quantity=input(f"How many coding session did you complete on {update_date[:4]} {update_date[4:6]} {update_date[6:9]} 😊? ")
#
# graph_update_endpoint=f"{graph_add_endpoint}/{update_date}"
#
# graph_update_config={
#     "quantity":new_quantity,
# }
#
# res=requests.put(url=graph_update_endpoint,json=graph_update_config,headers=headers)
# print(res.text)

# webbrowser.open("https://pixe.la/v1/users/killua/graphs/dailycoding.html", new=1)
# webbrowser.open("https://pixe.la/v1/users/killua/graphs/dailycoding", new=1)


# To delete a pixel on a particular date
#
# delete_date=input("Which date to delete (yyyymmdd)? ")
# graph_delete_endpoint=f"{graph_add_endpoint/{delete_date}"
# res=requests.delete(url=graph_delete_endpoint,headers=headers)
# print(res.text)
