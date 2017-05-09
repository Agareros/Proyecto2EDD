from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    
    url(r'^home/$', views.drive_home, name='drive_home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^registro/$', views.registro, name='registro'),
    
    

    #=========================================[DJANGO]========================================
    
    url(r'^drive/django/login$', views.loginDjango, name='loginDjango'),
    url(r'^drive/django/registrar$', views.registrarDjango, name='registrarDjango'),

    url(r'^drive/django/master$', views.masterDjango, name='masterDjango'),
    url(r'^drive/django/carpetas$', views.carpetasDjango, name='carpetasDjango'),
    url(r'^drive/django/logout$', views.logoutDjango, name='logoutDjango'),
    url(r'^drive/django/versesion$', views.verSesion, name='verSesion'),

    #=========================================[ANDROID]========================================
    url(r'^drive/android/login$', views.loginAndroid, name='loginAndroid'),
    url(r'^drive/android/registrar$', views.registroAndroid, name='registroAndroid'),


   # url(r'^drive/registrse$', views.android,name='android'),
]
