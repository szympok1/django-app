from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login as auth_login, logout
from app.models import Offer, Reservation, Barber
from .forms import UserLoginForm, UserRegisterForm, NewReservation


def index(request):
    offers = Offer.objects.all()
    return render(request, 'home/index.html', {'offers': offers})

def login(request):
    return render(request, 'home/login.html')

def register(request):
    return render(request, 'home/register.html')

@login_required
def user_profile(request):
    reservations = Reservation.objects.all()
    return render(request, "home/user_profile.html", {'reservations':reservations})

@login_required
def new_reservation(request):
    newreservation = NewReservation(request.POST)
    if newreservation.is_valid():
        reservation = newreservation.save() 
        reservation.Client = request.user.username
        reservation.save()
        return redirect('/home')
    context = {
        'form':newreservation
    }
    return render(request, "home/new_reservation.html", context)

@staff_member_required
def staff_profile(request):
    reservations = Reservation.objects.all()
    barbers = Barber.objects.all()
    return render(request, "home/staff_profile.html",{'reservations': reservations, 'barbers': barbers})

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        auth_login(request, user)
        if next:
            return redirect(next)
        return redirect('/home')
    context = {
        'form':form
    }
    return render(request, "home/login.html", context)

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        auth_login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/home')
    context = {
        'form':form
    }
    return render(request, "home/register.html", context)

def logout_view(request):
    logout(request)
    return redirect ('/home')

def redirect_home(request):
    return redirect('home/')
