from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ScheduleForm, SupportForm, UnifiedDeliveryForm
from .models import Delivery, News, Schedule_of_road_transport, Support


@login_required(login_url='login')
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user.is_authenticated:
        delivery_history = Delivery.objects.filter(user=request.user)
    else:
        delivery_history = None

    contex = {
        'delivery_history': delivery_history,
        'profile_detail': user
    }
    return render(request, 'accounts/profile.html', context=contex)


@login_required(login_url='login')
def news_list(request):
    news = News.objects.all().order_by('-published_date')
    return render(request, 'main/news_list.html', {'news': news})


@login_required(login_url='login')
def news_detail(request, news_id):
    new = get_object_or_404(News, id=news_id)
    return render(request, 'main/news_detail.html', {'news_item': new})


@login_required(login_url='login')
def exemple_delivery(request):
    return render(request, 'main/exemple_delivery.html')


@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        delivery_history = Delivery.objects.filter(user=request.user)
    else:
        delivery_history = None
    return render(request, 'main/index.html', {'delivery_history': delivery_history})


@login_required(login_url='login')
def index_detail(request, delivery_id):
    delivery_detail = get_object_or_404(Delivery, id=delivery_id)
    return render(request, 'main/index_detail.html', {"delivery": delivery_detail})


@login_required(login_url='login')
@staff_member_required
def admin_dashboard(request):
    deliveries = Delivery.objects.all()
    return render(request, 'admin/admin_dashboard.html', {'deliveries': deliveries})


@login_required(login_url='login')
@staff_member_required
def delivery_detail(request, delivery_id):
    delivery = get_object_or_404(Delivery, id=delivery_id)
    return render(request, 'admin/delivery_detail.html', {'delivery': delivery})


@login_required(login_url='login')
@staff_member_required
def users_view_admin(request):
    users = User.objects.all()
    return render(request, 'admin/users_view_admin.html', {'all_users': users})


@login_required(login_url='login')
@staff_member_required
def user_profile_detail(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    return render(request, 'admin/user_profile_detail.html', {'profile_user': profile_user})


@login_required(login_url='login')
@staff_member_required
def delete_user_view(request, user_id):
    user_to_delete = get_object_or_404(User, id=user_id)

    if request.user == user_to_delete:
        messages.error(
            request, 'Вы не можете удалить свой собственный аккаунт!')
        return redirect('user_profile_detail', user_id=user_id)

    if request.method == "POST":
        user_to_delete.delete()
        messages.success(request, 'Пользователь успешно удален!')
        return redirect('users_view_admin')


@login_required(login_url='login')
@staff_member_required
def delete_delivery_view(request, delivery_id):
    delivery_to_delete = get_object_or_404(Delivery, id=delivery_id)

    if request.method == "POST":
        delivery_to_delete.delete()

        return redirect('admin_dashboard')
    return render(request, 'admin/delivery_detail.html', {'delivery': delivery_to_delete})


@login_required(login_url='login')
@staff_member_required
def user_deliveries(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_deliveries = Delivery.objects.filter(user=user)

    context = {
        'user': user,
        'deliveries': user_deliveries
    }

    return render(request, 'admin/user_deliveries.html', context)


@login_required(login_url='login')
def create_delivery(request):
    if request.method == "POST":
        form = UnifiedDeliveryForm(request.POST, request.FILES)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.user = request.user
            delivery.save()
            messages.success(request, "Заявка на доставку успешно создана!")
            return redirect('home')
    else:
        form = UnifiedDeliveryForm()
    return render(request, 'main/create_delivery.html', {'form': form})


@login_required(login_url='login')
def support_request(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SupportForm()
    return render(request, 'main/support.html', {'form': form})


@login_required(login_url='login')
@staff_member_required
def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_view')
    else:
        form = ScheduleForm()
    return render(request, 'admin/schedule_form.html', {'form': form})


def user_in_group_GRAFIG(user):
    return user.groups.filter(name='GRAFIG').exists()


def GRAFIG_member_required(view_func):
    decorated_view_func = user_passes_test(
        user_in_group_GRAFIG,
        login_url='no_access'
    )(view_func)
    return decorated_view_func


@login_required(login_url='login')
@GRAFIG_member_required
def schedule_view(request):
    schedules = Schedule_of_road_transport.objects.all()
    return render(request, 'admin/schedule.html', {'schedules': schedules})


@login_required(login_url='login')
@GRAFIG_member_required
def schedule_of_road_transport_detail(request, file_and_photo_id):
    file_and_photo = get_object_or_404(
        Schedule_of_road_transport, id=file_and_photo_id)
    return render(request, 'admin/schedule_detail.html', {'schedule_file': file_and_photo})


def no_access(request):
    return render(request, 'admin/no_access.html')
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ScheduleForm, SupportForm, UnifiedDeliveryForm
from .models import Delivery, News, Schedule_of_road_transport, Support


@login_required(login_url='login')
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user.is_authenticated:
        delivery_history = Delivery.objects.filter(user=request.user)
    else:
        delivery_history = None

    contex = {
        'delivery_history': delivery_history,
        'profile_detail': user
    }
    return render(request, 'accounts/profile.html', context=contex)


@login_required(login_url='login')
def news_list(request):
    news = News.objects.all().order_by('-published_date')
    return render(request, 'main/news_list.html', {'news': news})


@login_required(login_url='login')
def news_detail(request, news_id):
    new = get_object_or_404(News, id=news_id)
    return render(request, 'main/news_detail.html', {'news_item': new})


@login_required(login_url='login')
def exemple_delivery(request):
    return render(request, 'main/exemple_delivery.html')


@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        delivery_history = Delivery.objects.filter(user=request.user)
    else:
        delivery_history = None
    return render(request, 'main/index.html', {'delivery_history': delivery_history})


@login_required(login_url='login')
def index_detail(request, delivery_id):
    delivery_detail = get_object_or_404(Delivery, id=delivery_id)
    return render(request, 'main/index_detail.html', {"delivery": delivery_detail})


@login_required(login_url='login')
@staff_member_required
def admin_dashboard(request):
    deliveries = Delivery.objects.all()
    return render(request, 'admin/admin_dashboard.html', {'deliveries': deliveries})


@login_required(login_url='login')
@staff_member_required
def delivery_detail(request, delivery_id):
    delivery = get_object_or_404(Delivery, id=delivery_id)
    return render(request, 'admin/delivery_detail.html', {'delivery': delivery})


@login_required(login_url='login')
@staff_member_required
def users_view_admin(request):
    users = User.objects.all()
    return render(request, 'admin/users_view_admin.html', {'all_users': users})


@login_required(login_url='login')
@staff_member_required
def user_profile_detail(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    return render(request, 'admin/user_profile_detail.html', {'profile_user': profile_user})


@login_required(login_url='login')
@staff_member_required
def delete_user_view(request, user_id):
    user_to_delete = get_object_or_404(User, id=user_id)

    if request.user == user_to_delete:
        messages.error(
            request, 'Вы не можете удалить свой собственный аккаунт!')
        return redirect('user_profile_detail', user_id=user_id)

    if request.method == "POST":
        user_to_delete.delete()
        messages.success(request, 'Пользователь успешно удален!')
        return redirect('users_view_admin')


@login_required(login_url='login')
@staff_member_required
def delete_delivery_view(request, delivery_id):
    delivery_to_delete = get_object_or_404(Delivery, id=delivery_id)

    if request.method == "POST":
        delivery_to_delete.delete()

        return redirect('admin_dashboard')
    return render(request, 'admin/delivery_detail.html', {'delivery': delivery_to_delete})


@login_required(login_url='login')
@staff_member_required
def user_deliveries(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_deliveries = Delivery.objects.filter(user=user)

    context = {
        'user': user,
        'deliveries': user_deliveries
    }

    return render(request, 'admin/user_deliveries.html', context)


@login_required(login_url='login')
def create_delivery(request):
    if request.method == "POST":
        form = UnifiedDeliveryForm(request.POST, request.FILES)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.user = request.user
            delivery.save()
            messages.success(request, "Заявка на доставку успешно создана!")
            return redirect('home')
    else:
        form = UnifiedDeliveryForm()
    return render(request, 'main/create_delivery.html', {'form': form})


@login_required(login_url='login')
def support_request(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SupportForm()
    return render(request, 'main/support.html', {'form': form})


@login_required(login_url='login')
@staff_member_required
def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_view')
    else:
        form = ScheduleForm()
    return render(request, 'admin/schedule_form.html', {'form': form})


def user_in_group_GRAFIG(user):
    return user.groups.filter(name='GRAFIG').exists()


def GRAFIG_member_required(view_func):
    decorated_view_func = user_passes_test(
        user_in_group_GRAFIG,
        login_url='no_access'
    )(view_func)
    return decorated_view_func


@login_required(login_url='login')
@GRAFIG_member_required
def schedule_view(request):
    schedules = Schedule_of_road_transport.objects.all()
    return render(request, 'admin/schedule.html', {'schedules': schedules})


@login_required(login_url='login')
@GRAFIG_member_required
def schedule_of_road_transport_detail(request, file_and_photo_id):
    file_and_photo = get_object_or_404(
        Schedule_of_road_transport, id=file_and_photo_id)
    return render(request, 'admin/schedule_detail.html', {'schedule_file': file_and_photo})


def no_access(request):
    return render(request, 'admin/no_access.html')