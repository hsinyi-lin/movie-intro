from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def login(request):
    if request.user.is_authenticated:
        return redirect('/movies/')

    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, '登入成功')
            return redirect('/movies/')
    return render(request, 'users/auth_form.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/login/')


def register(request):
    if request.user.is_authenticated:
        return redirect('/movies/')

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login/')
    return render(request, 'users/auth_form.html', {'form': form})




