from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('blog/', views.form_view_blog, name="blog"),
    path('flexbox3_search/', views.flexbox3_search, name="flexbox3_search"),
    path('bookings/', views.form_view_booking, name="bookings"),
    #path('reservations/', views.reservations, name="reservations"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    #path('bookings/', views.bookings, name='bookings'), 
    # Add the remaining URL path configurations here
]