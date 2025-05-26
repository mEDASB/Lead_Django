from django.urls import path
from . import views

urlpatterns = [
    # authentication paths
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    # path('profile/', views.profile, name='profile'),
    # path('change_password/', views.change_password, name='change_password'),
    # path('reset_password/', views.reset_password, name='reset_password'),
    # path('reset_password_confirm/<uidb64>/<token>/', views.reset_password_confirm, name='reset_password_confirm'),
    # path('reset_password_complete/', views.reset_password_complete, name='reset_password_complete'),
    # Example path
    path('home/', views.home, name='home'),
    path('all/', views.lead_list, name='lead_list'),
    path('edit_lead/<str:id>', views.edit_lead, name='edit_lead'),
    path('add_lead/', views.add_lead, name='add_lead'),
]