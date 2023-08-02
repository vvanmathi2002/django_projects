
## for user creation or register, sign-in and sign-out.
from django.shortcuts import render, redirect
from appname.forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 
 


def register(request):	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('appname:login_reg')


	context = { 'form': form }
	return render (request, 'signin/register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('appname:index')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'signin/login.html', context)

def logoutuser(request):
	logout(request)
	# return redirect('appname:login_reg')
	return redirect('appname:home')


@login_required(login_url = 'appname:login_reg')
def index(request):
	return render (request,"signin/index.html", context = {})




from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'aboutus.html')



from appname.models import Student

	
#Class based views


from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class StudentReg(CreateView):
	model = Student
	fields = '__all__'
	template_name = 'CBV/studentreg.html'
	success_url ="/"

class Studentlist(ListView):
	model = Student
	template_name = 'CBV/studentlist.html'

class Studentdetail(DetailView):
	model =Student
	template_name = 'CBV/studentdetail.html'

class StudentUpdate(UpdateView):
	model = Student
	fields = "__all__"
	template_name = 'CBV/studentupdate.html'
	success_url ="/"


class StudentDelete(DeleteView):
	model = Student
	template_name = 'CBV/studentdelete.html'
	success_url ="/"



# for get and post

def dhana(request):
	return render(request,'formmet/dhana.html')

def get1(request):
	a = int(request.GET['num1'])
	b = int(request.GET['num2'])
	c = a+b
	context = {'c': c }
	return render(request,'formmet/get.html',context)

def post1(request):
	a = int(request.POST['num1'])
	b = int(request.POST['num2'])
	c = a+b
	context = {'c': c }
	return render(request,'formmet/post.html',context)

	#### For Function based view

from django.shortcuts import render , redirect, get_object_or_404

from .models import Student
from .forms import StudentForm

### for studentlistview
def students(request):
    student = Student.objects.all()
    context = {'student':student}
    return render(request, 'student.html', context)

## for detail view
def detail(request, id):
	data = Student.objects.get(id = id)	
	context = {'data':data}
	return render(request,'FBV/detail.html', context)

##for update view
def update(request, id):
	obj = get_object_or_404(Student, id =id)
	form = StudentForm(request.POST or None, instance = obj)
	data = Student.objects.get(id = id)
	if form.is_valid():
		form.save()
		return redirect('appname:students')

	context = {'form':form, 'data':data}
	return render(request,'FBV/update.html', context )

## for delete view
def delete(request, id):
	data = Student.objects.get(id = id)
	context = {'data':data}
	if request.method =='POST':
		data.delete()
		return redirect('appname:form')
	return render(request,'FBV/delete.html', context )

## for student list and create or registration
def form(request):
    stu = Student.objects.all() 

    form = StudentForm
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appname:students')  

    context = {'stu': stu, 'form': form}
    return render(request, 'FBV/form.html', context) 


