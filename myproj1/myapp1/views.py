from django.shortcuts import render
from django.http import HttpResponse
from .function.functions import handle_uploaded_file
from myapp1.forms import StudentForm

def index(request):
    if request.method == 'POST':
        student = StudentForm(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("file uploaded succesfully")
    else:
        student = StudentForm()
        return render(request,"index.html",{'form':student})        