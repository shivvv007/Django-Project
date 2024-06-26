from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
from .models import Vendor


def home(request):
	records = Vendor.objects.all()
	# Check to see if logged in
	if request.method == 'POST':
		username = request.POST ['username']
		password = request.POST ['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You have been logged in")
			return redirect('home')
		else: 
			messages.success(request, "There was an error while logging in, please try again...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records})






#def home(request):
	#records = Record.objects.all()
	# Check to see if logged in
	#if request.method == 'POST':
		#username = request.POST ['username']
		#password = request.POST ['password']
		# Authenticate
		#user = authenticate(request, username=username, password=password)
		#if user is not None:
			#login(request, user)
			#messages.success(request, "You have been logged in")
			#return redirect('home')
		#else: 
			#messages.success(request, "There was an error while logging in, please try again...")
			#return redirect('home')
	#else:
		#return render(request, 'home.html', {'records':records})


def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out...")
	return redirect('home')



def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Aunthenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You have registered successfully!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})
	return render(request, 'register.html', {'form':form})



def vendor_record(request, pk):
	if request.user.is_authenticated:
		# Check for record
		vendor_record = Vendor.objects.get(id=pk)
		return render(request, 'record.html', {'vendor_record':vendor_record})
	else:
		messages.success(request, "You Need to Login to View Vendor Records")
		return redirect('home')