from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import login, authenticate
import users.models as users


def Login(request):
    if users.UserProfile.objects.filter(login=request.user).exists():
        return redirect('cabinet')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            frm = form.cleaned_data
            user = authenticate(login=frm['login'], password=frm['password'])
            if user is not None:
                login(request, user)
                return redirect('cabinet')
            else:
                pass
    form = LoginForm()
    return render(request, 'users/login.html', {'forms': form})


def Registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(login=user.login, email=email, password=raw_password)
            login(request, user)
            return redirect('cabinet')
    else:
        form = SignUpForm()
    return render(request, 'users/registration.html', {'forms': form})


def Cabinet(request):
    content = {}
    user = users.UserProfile.objects.get(login=request.user)
    content['login'] = user.login
    content['password'] = user.password
    content['name'] = user.name
    content['authorship'] = user.authorship
    content['date_joined'] = user.date_joined
    if request.user != 'AnonymousUser':
        avatar_path = users.UserProfile.objects.get(login=request.user).img.url
        content['avatar'] = avatar_path.split('/', 3)[3]
    else:
        content['avatar'] = 'main/img/Stoned_Fox.jpg'
    return render(request, 'users/cabinet.html', content)
