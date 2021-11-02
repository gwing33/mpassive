"""
To render HTML webpages
"""

from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth import authenticate, login


class ActivateForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password', 'required': 'required'})
    )


@login_required(login_url='/login')
def home_view(request):
    return render(request, template_name='home.html')


def activate_account(request):
    user = User.objects.first()
    # User is logged in send to home
    if request.user.is_authenticated:
        return redirect('/')

    # User exists, send to login
    if user:
        return redirect('/login')

    form = ActivateForm(data={
        'email': request.POST.get("email", ""),
        'password': request.POST.get("password", "")
    })

    if form.is_valid():
        data = form.cleaned_data
        user = User(
            email=data.get('email'),
            username=data.get('email'),
        )
        user.set_password(data.get('password'))
        user.save()
        return redirect('/login')

    context = {'activate_form': form.as_p()}

    return render(request, template_name='activate-account.html', context=context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    user = User.objects.first()
    if not user:
        return redirect('/activate')

    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=email, password=password)
    user2 = User.objects.first();
    print('user', user, user2.username == email, user2.password == password)
    if user is not None:
        login(request, user)
        return redirect('/')

    form = ActivateForm(data={
        'email': email,
        'password': '',
    })
    context = {'activate_form': form.as_p()}

    return render(request, template_name='login.html', context=context)
