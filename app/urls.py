from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404
from django.shortcuts import render

# Define the custom 404 view
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

# Set the handler for 404 errors
handler404 = custom_404_view


app_name = "app"

urlpatterns = [
    path('', views.Index, name="index"),
    path('degree-programme/', views.DegreeProgramme, name="degree_programme"),
    path('admission-list/', views.AdmissionList, name="admission_list"),
    path('application-instruction/', views.ApplicationInstruction, name="application_list"),
    path('booking/', views.Booking, name="booking"),
    path('our-policy/', views.OurPolicy, name="our_policy"),
    path('faq/', views.Faq, name="faq"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)

# if settings.DEBUG is False:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)