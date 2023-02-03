from flask import Flask, render_template, flash, redirect
import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime, timedelta


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
@app.route('/', methods=['GET', 'POST'])
def display():
    user_authorized = False
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        user_authorized = True

    return render_template('index.html', serialNums=device_id, status=status, listLen=listLen,
                           user_authorized=user_authorized, form=form)



test_dict = [
    {
    'device_id': 'A1001',
    'status': 'test 3 in progress',
    'test start time': '2023-12-12 10:10:20.000000',
    'last result': 'PASS'
    },
    {
    'device_id': 'A1002',
    'status': 'test 2 complete',
    'test start time': '2023-12-12 10:10:30.000000',
    'last result': 'FAIL'
    },
    {
    'device_id': 'A1000',
    'status': 'test 4 complete',
    'test start time': '2023-12-12 10:10:10.000000',
    'last result': 'PASS'
    },
    {
    'device_id': 'B2001',
    'status': 'test 3 in progress',
    'test start time': '2023-12-12 10:10:20.000000',
    'last result': 'PASS'
    },
    {
    'device_id': 'B2002',
    'status': 'test 2 in progress',
    'test start time': '2023-12-12 10:10:30.000000',
    'last result': 'FAIL'
    },
    {
    'device_id': 'B2000',
    'status': 'test 5 complete',
    'test start time': '2023-12-12 10:10:10.000000',
    'last result': 'PASS'
    }
]

device_id = [i['device_id'] for i in test_dict]
status = []
for i in test_dict:
    str_to_append = ('Тест ' + i['status'][5])
    if i['status'][7] == 'c':
        str_to_append += ' завершён, результат: ' + i['last result']
    elif i['status'][7] == 'i':
        str_to_append += ' в процессе, начат ' + i['test start time']
    status.append(str_to_append)

listLen = len(device_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

