from django.shortcuts import render, redirect

from student.forms import Studentform
from student.models import Students


# Create your views here.
def home(request):
    form = Studentform()
    if request.method == 'POST':
        forms = Studentform(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('student:result')
    return render(request,'home.html',{'form':form})


def result(request):
    result = Students.objects.all()
    for i in result:
        name = i.name
        dob = i.dob
        physics = i.physics
        chemistry = i.chemistry
        maths = i.maths
        computer_science = i.computer_science
        marks = (i.physics,i.chemistry,i.maths,i.computer_science)
        total_mark = sum(map(int, marks))
        percentage = round((total_mark/(len(marks)*100))*100,2)
        context = {
            'name': name,
            'physics':physics,
            'chemistry':chemistry,
            'maths':maths,
            'computer_science':computer_science,
            'dob': dob,
            'percentage': percentage
        }
    return render(request,'result.html',context)