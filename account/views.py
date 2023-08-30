from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm, UserEditForm


# Create your views here.
def user_login(request):
    if request.user.is_authenticated == True:  # if user is already logged in, redirect to home page
        return redirect('home:home')  # redirect to home page

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:home')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'account/login.html', context)


def user_register(request):
    context = {
        'errors': []
    }

    if request.user.is_authenticated:  # if user is already logged in, redirect to home page
        return redirect('home:home')  # redirect to home page

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            context['errors'].append('پسوردها با هم برابر نیستند')
            return render(request, 'account/register.html', context)

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('account:login')

    return render(request, 'account/register.html', context)


def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == 'POST':
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }
    return render(request, 'account/edit.html', context)


def user_logout(request):
    logout(request)  # logout user
    return redirect('home:home')  # redirect to home page
