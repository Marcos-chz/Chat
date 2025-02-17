from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
import random

# Create your views here.
ALLOWED_ROOMS = ['1', '2', '3']

def room(request, room_name):
    # Manage the existing rooms
    if room_name not in ALLOWED_ROOMS:
        raise Http404("The room does not exist")  
    
    # Generate a new nickname for the testing page, or retrieve the nickname from the session
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        nickname = f"{nickname}2"  
    else:
        nickname = request.session.get('nickname', 'Guest')  

    # Save the random color
    randomColor = random_color()

    # Return important information for chat.html to use
    return render(request, 'chat.html', {'room_name': room_name, 'nickname': nickname, 'randomColor': randomColor})

def home(request):

    # Obtain the nickname and save it in the session
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        
        if nickname:
            request.session['nickname'] = nickname  
        return redirect('menu')
    
    return render(request, 'home.html')


# Just render the menu
def menu(request):
    
    return render(request, 'menu.html')
    

# Generate a random color for the nickname display
def random_color():
    r = random.randint(0, 200)  
    g = random.randint(0, 200)
    b = random.randint(0, 200)
    
    if r > 180 and g > 180 and b > 180:
        return random_color() 
    
    return f"#{r:02x}{g:02x}{b:02x}"
