from django.urls import path

from . import views

urlpatterns = [
path('', views.index, name='home'),
path('user/delivery/<int:delivery_id>', views.index_detail, name="user_delivery_detail"),
path('exemple_delivery/', views.exemple_delivery, name="exemple_delivery"),
path('news/', views.news_list, name='news_list'),
path('new/<int:news_id>', views.news_detail, name="new_detail"),
path('users_view_admin', views.users_view_admin, name='users_view_admin'),
path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
path('delivery/<int:delivery_id>/', views.delivery_detail, name='view_delivery'),
path('user_deliveries/<int:user_id>/',views.user_deliveries, name='user_deliveries'),
path("profile/<int:user_id>/", views.profile, name="profile_detail"),
path('user_profile/<int:user_id>/',views.user_profile_detail, name='user_profile_detail'),
path('delete_user/<int:user_id>/',views.delete_user_view, name='delete_user'),
path('delete_delivery/<int:delivery_id>/',views.delete_delivery_view, name='delete_delivery'),
path('create_delivery/', views.create_delivery, name='create_delivery'),
path('support/', views.support_request, name='support_request'),
path('schedule/create/', views.schedule_create, name='schedule_create'),
path('schedule/', views.schedule_view, name='schedule_view'),
path('schedule/<int:file_and_photo_id>/', views.schedule_of_road_transport_detail, name='schedule_file_id'),
path('no_access', views.no_access, name='no_access'),
]
