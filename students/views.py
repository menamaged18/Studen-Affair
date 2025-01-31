from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Student
from .forms import StudentForm, StudentFormALL
from authenticationapp.views import custom_login_required

# function to check if the id is on the database or not 
# it will help me in the add student page because i can't insert a student with the same id 
def check_id(request):
    stu_id = request.GET.get('id')
    # print(f"Received ID check request for ID: {stu_id}")  # Debug print
    
    try:
        exists = Student.objects.filter(student_id=stu_id).exists()
        # print(f"ID exists: {exists}")  # Debug print
        return JsonResponse({'exists': exists})
    except Exception as e:
        # print(f"Error checking ID: {e}")  # Debug print
        return JsonResponse({'error': str(e)}, status=500)
    
@custom_login_required
def search_page(request):
    query = request.GET.get('q')
    search_by = request.GET.get('search_by')
    
    students = Student.objects.all()
    
    if query:
        if search_by == 'ID':
            students = students.filter(student_id__icontains=query)
        elif search_by == 'Name':
            students = students.filter(first_name__icontains=query) | students.filter(last_name__icontains=query)
        elif search_by == 'Level':
            students = students.filter(level__icontains=query)
        elif search_by == 'GPA':
            students = students.filter(gpa__icontains=query)
        elif search_by == 'Departement':
            students = students.filter(department__icontains=query)
    
    return render(request, 'students/Search.html', {'students': students})

@custom_login_required
# Create your views here.
def addstudent(request):
    # to make the user save the fields in the table
    if request.method == "POST":
        # first getting the values from the html page
        stu_id = request.POST.get('ID')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        PN = request.POST.get('phone')
        em = request.POST.get('email')
        level = request.POST.get('Level')
        gpa = request.POST.get('GPA')
        dof = request.POST.get('date')
        gndr = request.POST.get('Gender')
        dep = request.POST.get('Departement')
        status = request.POST.get('Status')
        
        # put the values in the table
        student_data = Student( student_id = stu_id,
                                first_name = fname,
                                last_name = lname,
                                phone_number = PN,
                                email = em,
                                level = level,
                                department = dep,
                                gpa = gpa,
                                date_of_birth = dof,
                                gender = gndr,
                                status = status)

        # saving the data in the table
        student_data.save()

    return render(request, 'students/AddStudent.html')

# delete student record
def delete_record(request, record_id):
    if request.method == 'DELETE':
        try:
            record = Student.objects.get(student_id=record_id)
            record.delete()
            return JsonResponse({'status': 'success', 'message': 'Record deleted successfully'})
        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Record not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@custom_login_required
# return pages 
def deletestudent(request):
    orderd_data = Student.objects.all().order_by('student_id').values()
    return render(request, 'students/DeleteStudent.html', {'students':orderd_data})

@custom_login_required
def departmentAssignment(request):
    return render(request, 'students/DepartementAssignmentPage.html')

@custom_login_required
def search(request):
    orderd_data = Student.objects.all().order_by('student_id').values()
    return render(request, 'students/Search.html', {'students':orderd_data})

@custom_login_required
def updatehome(request):
    orderd_data = Student.objects.all().order_by('student_id').values()
    return render(request, 'students/UpdateHomePage.html', {'students':orderd_data})

@custom_login_required
def updateinfo(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('updatehome')  # Redirect to the homepage or another page
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/UpdateInfo.html', {'form': form})

@custom_login_required
def view(request):
    orderd_data = Student.objects.all().order_by('student_id').values()
    return render(request, 'students/view.html', {'students':orderd_data})

# in view page there is a button that changes the status from active to inactive or vise versa
def change_status(request, student_id):
    if request.method == 'POST':
        try:
            # record = Student.objects.get(student_id=student_id)
            student = get_object_or_404(Student, student_id=student_id)
            if student.status == 'Active':
                student.status = 'Inactive'
            else: 
                student.status = 'Active'
            # save the changes
            student.save()

            return JsonResponse({'status': 'success', 'message': 'Student status updated successfully'})
        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Student not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
    


def edit_all_student_information(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentFormALL(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('search')  
    else:
        form = StudentFormALL(instance=student)
    return render(request, 'students/UpdateInfo.html', {'form': form})