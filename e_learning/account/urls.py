from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('login/', views.user_login, name='login')
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('password-change/', auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    # reset password urls
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'), # step-1
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), #step-2
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), #step-3
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), #step-4
    path('register/', views.register, name='register'),
     path('edit/', views.edit, name='edit'),
     
]
