from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm

# Create your views here.

def student_list(request):
    students = Student.objects.all().order_by('rno')
    return render(request, 'student/student_list.html', {'students': students})

#create a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully.')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student/student_form.html', {'form': form,'title': 'Create Student'}) 

#object to update a student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/student_form.html', {'form': form,'title': 'Update Student'})  

#object to delete a student
def student_delete(request, pk):

    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully.')
        return redirect('student_list')
    return render(request, 'student/students_confirm_delete.html', {'student': student})    