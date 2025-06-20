from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
# from .forms import UserSignupForm, StudentSignupForm, InstructorSignupForm
from .models import *
from django.db.models import Max, Q, F
import uuid
import random
import string
import json

import os


from django.http import HttpResponse
from django.template.loader import render_to_string


from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User, auth
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict


from django.contrib import messages

# Create your views here.
def Index(request):
    return render(request, "index.html")

def DegreeProgramme(request):
    return render(request, 'programmes.html')

def AdmissionList(request):
    return render(request, 'admission_list.html')

def ApplicationInstruction(request):
    return render(request, 'application_instructor.html')

def Booking(request):
    return render(request, 'booking.html')

def OurPolicy(request):
    return render(request, 'our-policy.html')

def Faq(request):
    return render(request, 'faq.html')

def VisitUniversity(request):
    return render(request, 'visit-university.html')

def Requirements(request):
    return render(request, 'requirements.html')

def ProhibitedItems(request):
    return render(request, 'prohibited-items.html')

def Disclaimer(request):
    return render(request, 'disclaimer.html')
