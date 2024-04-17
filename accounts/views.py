import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import ProfileForm, UserForm
from .models import Profile

logger = logging.getLogger(__name__)


def register_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 and password2 and password1 != password2:
            messages.error(request, "Пароли не совпадают")
            return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form})

        if user_form.is_valid() and profile_form.is_valid():
            try:
                user = User(
                    username=user_form.cleaned_data['username'], email=user_form.cleaned_data['email'])
                user.set_password(password1)
                user.save()

                profile = Profile(user=user, image=profile_form.cleaned_data['image'],
                                company_name=profile_form.cleaned_data['company_name'],
                                phone=profile_form.cleaned_data['phone'], birth_date=profile_form.cleaned_data['birth_date'],
                                about=profile_form.cleaned_data['about'])
                profile.save()

                messages.success(
                    request, f'Аккаунт для {user.username} был успешно создан! Теперь вы можете войти.')
                return redirect('login')
            except Exception as e:
                logger.error(f"Error occurred while saving user: {e}")
                messages.error(
                    request, "Произошла ошибка при создании вашего аккаунта. Пожалуйста, попробуйте снова.")
        else:
            messages.warning(
                request, "Пожалуйста, исправьте ошибки в форме регистрации.")
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Добро пожаловать, {username}!")
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
    return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect("/")