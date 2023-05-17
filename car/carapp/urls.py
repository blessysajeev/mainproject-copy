from django.urls import path, include
from carapp import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('packages/',views.packages,name='packages'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    # path('home/',views.home,name='home'),
    path('testdrive/',views.testdrive,name='testdrive'),
    path('cars/<int:id>',views.cars,name='cars'),
    path('testview/' , views.testview,name='testview'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('staffhome',views.staffhome,name='staffhome'),
    path('stafflogin',views.stafflogin,name="stafflogin"),
    path('staffregister',views.staffregister,name="staffregister"),
    # path('staff_assignments',views.staff_assignments,name="staff_assignments"),
    path('customer_details/<int:id>', views.customer_details, name='customer_details'),
    path('showroomvisit',views.showroomvisit,name="showroomvisit"),
    path('job',views.job,name="job"),
    path('visit_delete/<int:id>',views.visit_delete,name='visit_delete'),
    path('car_loan_emi', views.car_loan_emi, name='car_loan_emi'),
    path('calculate_emi', views.calculate_emi, name='calculate_emi'),
    path('emi', views.car_loan_emi, name='emi'),
    path('predict_price/', views.predict_price, name='predict_price'),
    path('predict', views.predict, name='predict'),
    path('result', views.predict_price, name='result'),
    path('book/<int:id>',views.book,name='book'),
    path('paydone',views.paydone,name='paydone'),
    path('profile',views.profile,name='profile'),
    path('download_invoice/<int:id>', views.download_invoice, name='download_invoice'),
    path('apply_leave/', views.apply_leave, name='apply_leave'),
    path('leavestatus/', views.leavestatus, name='leavestatus'),



    path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change_password/', views.change_password, name='change_password'),

]