from django.shortcuts import render
from .models import Student
# Create your views here.


def student_view(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request, "student.html", context) 

def update_student(request):
    if request.method == 'POST':
        sid = request.POST['student_id']
        attribute = request.POST['attribute']
        new_value = request.POST['new_value']

        my_model = Student.objects.get(student_id=sid)
        setattr(my_model, attribute, new_value)
        my_model.save()

    return render(request, 'student.html')

def delete_student(request):
    if request.method == 'POST':
        sid = request.POST['student_id']
        my_model = Student.objects.filter(student_id=sid)
        my_model.delete()

    return render(request, 'student.html')

def create_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        sex = request.POST['sex']
        major = request.POST['major']
        sid = request.POST['student_id']
        student = Student(name=name, age=age, sex=sex, major=major, student_id=sid)
        student.save()

    return render(request, 'student.html')

def query_student(request):
    if request.method == 'POST':
        sid = request.POST['student_id']
        my_model = Student.objects.filter(student_id=sid)
        context = {'student': my_model, 'student_id' : sid}
        return render(request, 'student.html', context)

    return render(request, 'student.html')
