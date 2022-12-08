from flask import Flask, render_template, request
import requests,smtplib

app = Flask(__name__)


@app.route("/")
def index_pg():
    return render_template("index.html",
                           blogs=requests.get("https://api.npoint.io/cf444618280ba105de77").json()["blogs"])


@app.route("/post/<int:id>")
def post_pg(id):
    blogs = requests.get("https://api.npoint.io/cf444618280ba105de77").json()["blogs"]

    for i in blogs:
        if i["id"] == id:
            blog = i

    return render_template("post.html", blog=blog)


@app.route("/contact", methods=["POST", "GET"])
def contact_pg():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        mssg=f"Name- {request.form['name']}\nEmail- {request.form['email']}\nPhone- {request.form['phone']}\nMessage- {request.form['message']}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            my_mail = "killuak722@gmail.com"
            password = "killu@9652killua"

            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail, to_addrs=my_mail, msg=mssg)
            print(mssg)
            return render_template("contact.html")


@app.route("/about")
def about_pg():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")
