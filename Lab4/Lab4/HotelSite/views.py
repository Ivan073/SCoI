import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout
from .models import Client, ClientData, Room, RoomType, Booking
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import admin
from .forms import ClientAuthenticationForm, ClientCreationForm
import requests
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

def login_view(request):
    context={"error":False}
    if request.method == "POST":
        form = ClientAuthenticationForm(request, request.POST)
        logger.warning("test")
        if form.is_valid():
            user = form.get_user()
            if user is None:
                context = {"error": True, "email": request.POST["email"]}
                return render(request, "login.html", context)
            login(request, user)
            return redirect(home_view)
        context={"error": True}
    return render(request, "login.html", context)

def signup_view(request):

    context = {"error": False}

    if request.method == "POST":
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(home_view)
        context = {"error": True,
                   "email": request.POST["email"],
                   "last_name": request.POST["last_name"],
                   "first_name": request.POST["first_name"],
                   "patronymic": request.POST["patronymic"],
                   "info": request.POST["info"]}
        if request.POST.get("has_child") is not None:
            context["has_child"] = request.POST["has_child"]

        logger.warning(form.errors.as_data())
        unprocessed_errs = form.errors.as_data()
        errors = []
        if unprocessed_errs.get("email") is not None:
            for err in unprocessed_errs.get("email"):
                logger.warning(err.code)
                if err.code == 'unique':
                    errors.append("Пользователь с этим email уже зарегистрирован")
                if err.code == 'invalid':
                    errors.append("Введите корректный email")


        if unprocessed_errs.get("password2") is not None:
            for err in unprocessed_errs.get("password2"):
                logger.warning(err.code)
                if err.code == 'password_mismatch':
                    errors.append("Пароли не совпадают")

        logger.warning(errors)
        context["errors"] = errors
    return render(request, "signup.html",context)

def home_view(request):
    rooms = Room.objects.all()
    if request.method == "POST":
        logger.warning(request.POST)
        type_name = request.POST.get("type")
        if type_name is not None and type_name != '':
            type_obj = RoomType.objects.get(name=type_name)
            rooms = rooms.filter(room_type = type_obj)

        price_filter = request.POST.get("price_filter")
        price_radio = request.POST.get("price_radio")
        if price_filter is not None and price_filter != '':
            if price_radio == 'up':
                rooms = rooms.filter(price__gt=float(price_filter))
                rooms = rooms.order_by('price')
            elif price_radio == 'down':
                rooms = rooms.filter(price__lt=float(price_filter))
                rooms = rooms.order_by('-price')
            elif price_radio is None:
                rooms = rooms.filter(price=float(price_filter))

        capacity_filter = request.POST.get("capacity_filter")
        capacity_radio = request.POST.get("capacity_radio")
        if capacity_filter is not None and capacity_filter != '':
            if capacity_radio == 'up':
                rooms = rooms.filter(capacity__gt=float(capacity_filter))
            elif capacity_radio == 'down':
                rooms = rooms.filter(capacity__lt=float(capacity_filter))
            elif capacity_radio is None:
                rooms = rooms.filter(capacity=float(capacity_filter))

        date = request.POST.get("date")

        if date is not None and date != '':
            date = datetime.strptime(date, '%Y-%m-%d')
            logger.warning(date)
            rooms = rooms.filter(free_date__lte=date)


    logger.warning(rooms)
    context={
        "user":request.user,
        "rooms":rooms,
        "amount":len(rooms),
        "tomorrow":datetime.today()+timedelta(days=1),
        "max": datetime.today() + timedelta(days=31)
    }
    return render(request, "home.html",context=context)

def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))

def geo_view(request):
    ip_response = requests.get('https://api.ipify.org/?format=json')
    ip = ip_response.json()['ip']
    logger.info('IP:'+ip)
    place_responce = requests.get('https://ipinfo.io/'+ip+'/geo')
    place = place_responce.json()
    context = {'ip':ip,
               'postal':place['postal'],
               'city':place['city']}
    logger.info(context)
    return render(request, "place.html",context=context)

def room_view(request, id):
    room = Room.objects.get(id=id)
    logger.warning(request.user)
    return render(request, 'room.html', {'room': room, "user":request.user})

@login_required
def booking_view(request, id):
    room = Room.objects.get(id=id)
    min_date = max(room.free_date,datetime.date(datetime.today()+timedelta(days=1)))
    max_date = min_date + timedelta(days=30)
    logger.warning(request.POST)
    context = {'room': room,
               "user":request.user,
               "min_date":min_date,
               "max_date":max_date}
    if request.method == "POST":
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        if start_date is not None and end_date is not None:
            start_date = datetime.date(datetime.strptime(start_date,'%Y-%m-%d'))
            end_date = datetime.date(datetime.strptime(end_date,'%Y-%m-%d'))
            if start_date <=  end_date:
                duration = (end_date-start_date).days+1
                context={"price":room.price*duration, "user":request.user,"room_id":id, "start_date":start_date,"end_date":end_date}
                request.session['price'] = float(room.price*duration)
                request.session['room_id'] = id
                request.session['start_date'] = str(start_date)
                request.session['end_date'] = str(end_date)
                logger.warning(context)
                return render(request, 'order.html', context)
            else:
                context["error"] = True
    logger.warning(context)
    return render(request, "booking.html",context)

@login_required
def payment_view(request):
    return redirect("/payment_finished")

@login_required
def payment_finsihed_view(request):
    Booking.objects.create(client=request.user,
                           room=Room.objects.get(id=request.session['room_id']),
                           entry_date=datetime.date(datetime.strptime(request.session['start_date'],'%Y-%m-%d')),
                           departure_date=datetime.date(datetime.strptime(request.session['end_date'],'%Y-%m-%d')))
    request.session.pop('price', None)
    request.session.pop('room_id', None)
    request.session.pop('start_date', None)
    request.session.pop('end_date', None)
    return render(request, "payment_successful.html")

@login_required
def bookings_view(request):
    bookings = Booking.objects.all().filter(client=request.user)
    return render(request, "bookings.html", {"user":request.user, "bookings":bookings})
