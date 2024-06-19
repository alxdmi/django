from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserLoginForm, ContactForm



# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('contact')  # Перенаправление на страницу записи на прием
    else:
        form = UserLoginForm()
    # Добавляем переменную form_type в контекст
    return render(request, 'login.html', {'form': form, 'form_type': 'login'})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    # Добавляем переменную form_type в контекст
    return render(request, 'login.html', {'form': form, 'form_type': 'register'})


def home(request):
    return render(request, 'home.html')

@login_required()
def contact(request):
    return render(request, 'contact.html')


def submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'submit.html')  # Перенаправление на страницу успеха
    else:
        # Если метод не POST, то перенаправляем на форму контакта
        return redirect('contact')



