from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.
def home(request):
    response = render (request, 'home.html')
    response.set_cookie('name', 'Rahim', expires=datetime.utcnow()+timedelta(days=30))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    return render (request, 'get_cookie.html', {'name': name})

def del_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response


def set_session (request):
    data = {
        'name': 'Rahim',
        'age' : 25,
        'language': 'Bangla'
    }
    request.session.update(data)
    return render (request, 'set_session.html')

def get_session (request):
    if 'name' in request.session:
        name = request.session.get('name', 'Guest')     # if name is not available then Guest will show
        age = request.session.get('age')
        language = request.session.get('language')
        request.session.modified = True         # Reset the SESSION_COOKIE_AGE on every refresh in time

        return render (request, 'get_session.html', {'name': name, 'age': age, 'language': language})
    
    else:
        return HttpResponse('Session has been expired.')


def delete_session(request):
    # del request.session['name']     # delete a particular property
    request.session.flush()         # delete the whole session
    return render (request, 'delete_session.html')