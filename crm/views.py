from django.shortcuts import redirect, render, reverse
from .models import Student

def index(request):
    students = Student.objects.all()
    if request.GET.get('search'):
        students = students.filter(customer__icontains=request.GET.get('search'))  
    return render(request, 'index.html', {'students': students})

def create_student(request):
    if request.method == 'POST':
        student = Student()
        student.name = request.POST.get('name')
        student.phone = request.POST.get('phone')
        student.parent_name = request.POST.get('parent_name')
        student.parent_phone = request.POST.get('parent_phone')
        student.save()
    return redirect(reverse('index'))
