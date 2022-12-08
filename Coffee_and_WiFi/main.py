from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv, pandas
from csv import writer

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_link = StringField('Location URL', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time (ex. 9 AM)', validators=[DataRequired()])
    close_time = StringField('Closing Time (ex. 8 PM)', validators=[DataRequired()])
    rating = SelectField('Coffee Rating', choices=[(1, '☕'), (2, '☕☕'), (3, '☕☕☕'), (4, '☕☕☕☕'), (5, '☕☕☕☕☕')],
                         validators=[DataRequired()])
    wifi = SelectField('WiFi Rating',
                       choices=[(0, '✘'), (1, '💪'), (2, '💪💪'), (3, '💪💪💪'), (4, '💪💪💪💪'), (5, '💪💪💪💪💪')],
                       validators=[DataRequired()])
    power = SelectField('Power Rating', choices=[(1, '🔌'), (2, '🔌' * 2), (3, '🔌' * 3), (4, '🔌' * 4), (5, '🔌' * 5)],
                        validators=[DataRequired()])

    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafes-data.csv', 'a') as csv_file:
            writer_object = writer(csv_file)
            f=[i.data for i in form]
            print([i for i in f[:4]]+[i for i in f[4:7]])
            print([i for i in f[:4]]+[i[0] for i in f[4:7]])
            writer_object.writerow([i for i in f[:4]]+[i[0] for i in f[4:7]])

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafes-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            row2=row[4:7]
            row2=[int(i) for i in row2]
            new_row=row[:4]+row2
            list_of_rows.append(new_row)
            print(new_row)

    return render_template('cafes.html', cafes=list_of_rows)



if __name__ == '__main__':
    app.run(debug=True)


