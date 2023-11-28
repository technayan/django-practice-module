from django.shortcuts import render
import datetime

# Create your views here.
def contact (req):
    return render(req, 'app1/contact.html')

def practice (req):
    d = {
        'admin': 'Nayan',
        'age': 23,
        'courses' : [
            {'name': 'Python', 'fee': 5000},
            {'name': 'C++', 'fee': 3000},
            {'name': 'Django', 'fee': 7000}
        ],
        'nums': [1,2,3,4,5],
        'today': datetime.datetime.now(),
        'text': '',
        'marks': 45,
        'greetings': 'good morning',
        'greetings2': 'GOOD NIGHT',
        'msg': 'Learning Python is Fun',
        'fruits': ['mango', 'orange', 'berry'],
        'multi_line': 'Hello \n I am \n Learning \n Django',
        'text2': 'I loVE to lEArn',
        'publication': datetime.datetime(2023, 11, 20, 12, 00, 00),
        'count': 1,
        'count2': 3,
    }
    return render(req, 'app1/practice.html', d)