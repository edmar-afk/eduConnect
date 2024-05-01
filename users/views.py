from django.shortcuts import render, redirect

# Create your views here.

def homepage(request):
    return render(request, 'index.html')


def student(request):
    return render(request, 'student.html')

def videocall(request):
    return render(request, 'videocall.html')

def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'joinroom.html')