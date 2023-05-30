from django.contrib import admin
from django.urls import path,include,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Put-TwoStep_binomial',views.put_TwoStep_Binomial,name='TwoStep value'),
    path('Put-nStep_binomial',views.put_nStep_binomial,name='N-Step value'),
    path('Put-Black-Scholes',views.put_Black_Scholes,name='Black-Schole value')
]