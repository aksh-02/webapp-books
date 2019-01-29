from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from blog.models import Post
from commerce.models import Product
# Create your views here.


def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			pswd = form.cleaned_data.get('password1')
			messages.success(request, f'Account successsfully created for {username}')
			messages.success(request, f'Please Update your profile')
			user = authenticate(username=username, password=pswd)
			login(request, user)
			return redirect('profile')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form' : form})

@login_required()
def profile(request):
	posts = Post.objects.filter(author=request.user).order_by('-date_posted')
	your_sells = Product.objects.filter(seller=request.user)
	context = {
		'posts' : posts,
		'y_sells' : your_sells,
	}
	return render(request, 'users/profile.html', context)


@login_required()
def edit_profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated successfully')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form':u_form,
		'p_form':p_form
	}
	return render(request, 'users/edit_profile.html', context)


@login_required()
def change_password(request):
	print('hello friends')
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, 'Your password has been updated successfully!')
			return redirect('commerce-home')
		else:
			messages.error(request, 'Error! Please try again')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'users/change_password.html', {'form': form})

