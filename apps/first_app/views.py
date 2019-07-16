from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print("///////////////////")
    print("Hello World!")
    return HttpResponse ("Heya!")

def index(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')
    print("///////////////////")
    print("Create route hit...... redirecting to /......")
    return redirect("/")

def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
    print("******************")
    print(f"route to delete blog {number}")
    return redirect ("/")