from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
#if we get post request, then it instantiates a user creation form with the post data, otherwise empty form
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		#conditional for if form is valid
		if form.is_valid():
			form.save() #user created if form is valid
			username = form.cleaned_data.get('username')
			#display a success message if form data is valid
			messages.success(request, f'Your account has now been created. You are now able to log in')
			#after message, redirect to home page
			return redirect ('login')

	else: 
		form = UserRegisterForm()
	#render a template that uses the form, first argument is always request, create dictionary to access form within template
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, 
								   instance = request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect ('profile')
	else: 
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.profile)
	context = {
		'u_form': u_form,
		'p_form': p_form,
	}
	return render(request, 'users/profile.html', context)



