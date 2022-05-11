from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Room

# rooms = [
#     {'id':1, 'name':'Lets learn Python!'},
#     {'id':2, 'name':'Lets learn Django!'},
#     {'id':3, 'name':'Lets create something new!'}
# ]
def home(request):
    rooms = Room.objects.all() 
    context = {"rooms":rooms}
    return render(request, 'base/home.html', context)
    # return HttpResponse("HomePage")

def room(request, pk):
    room = Room.objects.get(id=pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room':room}
    return render(request, 'base/room.html',context)
    # return HttpResponse("Room Page")