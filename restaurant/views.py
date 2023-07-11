# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from .models import UserComments
from .forms import CommentForm
from django.http import JsonResponse
from .models import Menu2
from .forms import MenuForm
from datetime import datetime
from .models import Bookings
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item})

def flexbox3_search(request):
    return render(request, 'flexbox3_search.html')

def form_view_blog(request): #this is the blog
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uc = UserComments(
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                comment = cd['comment'],
            )
            uc.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'blog.html', {'form': form})

def form_view_booking(request): #this is the bookings
    form = MenuForm()
    if request.method == 'POST':
        form = MenuForm(request.POST)
        print(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            mf = Menu2(
                item_name = cd['item_name'],
                category = cd['category'],
                description = cd['description'],
            )
            mf.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'booking.html', {'form': form})

# WEEK 5
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add code for the bookings() view
def reservations(request):
    date = request.GET.get('date', datetime.today().date())
    bookings =  Bookings.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {'bookings': booking_json})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item})

""" @csrf_exempt
def booking2(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Bookings.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Bookings(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())

    bookings = Bookings.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json') """
