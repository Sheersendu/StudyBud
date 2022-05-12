from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

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

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        received_form = RoomForm(request.POST)
        if received_form.is_valid():
            received_form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'base/room_form.html', context)

def updateRoom(request,pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        received_form = RoomForm(request.POST,instance=room)
        if received_form.is_valid():
            received_form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'base/room_form.html', context)

def deleteRoom(request,pk):
    room = Room.objects.get(id = pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})