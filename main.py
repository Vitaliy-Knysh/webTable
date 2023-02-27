from flask import Flask, render_template, url_for, request
from datetime import datetime, timedelta
import json

with open('employees.json') as f:
    employees = json.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login_form():
    print(url_for('login_check'))
    return render_template('login.html')

@app.route('/loginHandler', methods=['GET','POST'])
def login_check():
    print(request.form['username'])
    user_authorized = False
    stand_id = 0
    for doc in employees:
        if request.form['username'] == doc['username'] and request.form['password'] == doc['password']:
            user_authorized = True
            stand_id = doc['stand']
            break
    if user_authorized:
        device_id, status, bgcolors, listLen, progress = parse_dict(test_dict[f'test_stand_{stand_id}'])
        return render_template('index.html', serialNums=device_id, status=status, listLen=listLen,
                               user_authorized=user_authorized, bgcolors=bgcolors, username=request.form['username'],
                               stand_id=stand_id, progress=progress)
    else:
        return render_template('login.html')

@app.route('/table')
def display():
    return render_template('head.html')


test_dict = {
    'test_stand_1': [
        {
            'device_id': 'A1001',
            'status': 'test 3 in progress',
            'test start time': '2023-12-12 10:10:20.000000',
            'progress': 90,
            'last result': 'PASS'
        },
        {
            'device_id': 'A1002',
            'status': 'test 2 complete',
            'test start time': '2023-12-12 10:10:30.000000',
            'progress': 79,
            'last result': 'FAIL'
        },
        {
            'device_id': 'A1000',
            'status': 'test 4 complete',
            'test start time': '2023-12-12 10:10:10.000000',
            'progress': 100,
            'last result': 'PASS'
        },
        {
            'device_id': 'B2001',
            'status': 'test 3 in progress',
            'test start time': '2023-12-12 10:10:20.000000',
            'progress': 57,
            'last result': 'PASS'
        },
        {
            'device_id': 'B2002',
            'status': 'test 2 in progress',
            'test start time': '2023-12-12 10:10:30.000000',
            'progress': 33,
            'last result': 'FAIL'
        },
        {
            'device_id': 'B2000',
            'status': 'test 5 complete',
            'test start time': '2023-12-12 10:10:10.000000',
            'progress': 100,
            'last result': 'PASS'
        }
    ],
    'test_stand_2':[
        {
        'device_id': 'C1001',
        'status': 'test 1 in progress',
        'test start time': '2023-12-12 10:10:20.000000',
        'progress': 62,
        'last result': 'PASS'
        },
        {
        'device_id': 'C1002',
        'status': 'test 4 complete',
        'test start time': '2023-12-12 10:10:30.000000',
        'progress': 100,
        'last result': 'FAIL'
        },
        {
        'device_id': 'C1000',
        'status': 'test 5 complete',
        'test start time': '2023-12-12 10:10:10.000000',
        'progress': 100,
        'last result': 'PASS'
        },
        {
        'device_id': 'D2001',
        'status': 'test 2 in progress',
        'test start time': '2023-12-12 10:10:20.000000',
        'progress': 23,
        'last result': 'FAIL'
        },
        {
        'device_id': 'D2002',
        'status': 'test 4 in progress',
        'test start time': '2023-12-12 10:10:30.000000',
        'progress': 67,
        'last result': 'PASS'
        },
        {
        'device_id': 'D2000',
        'status': 'test 5 complete',
        'test start time': '2023-12-12 10:10:10.000000',
        'progress': 100,
        'last result': 'FAIL'
        }
    ]
}

def parse_dict(dict):
    device_id = [i['device_id'] for i in dict]
    status = []
    bgcolors = []
    progress = []
    for i in dict:
        str_to_append = ('Тест ' + i['status'][5])
        if i['status'][7] == 'c':
            str_to_append += ' завершён, результат: ' + i['last result']
            if i['last result'] == 'FAIL':
                bgcolors.append('#c92902')  # red
            elif i['last result'] == 'PASS':
                bgcolors.append('#16de6d')  # green
        elif i['status'][7] == 'i':
            str_to_append += ' в процессе, начат ' + str(datetime.strptime(i['test start time'], '%Y-%m-%d %H:%M:%S.%f')
                                                         - datetime.utcnow()) + ' назад'
            str_to_append.replace('days', 'дней')
            bgcolors.append('#ffffff')  # white
        status.append(str_to_append)
        progress.append(i['progress'])
    listLen = len(device_id)
    return device_id, status, bgcolors, listLen, progress

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

