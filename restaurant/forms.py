from django.forms import ModelForm
from .models import Booking
from .models import UserComments
from .models import Menu2
from .models import Bookings


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

class CommentForm(ModelForm):
    class Meta:
        model = UserComments
        fields =  "__all__"
        

class MenuForm(ModelForm):
    class Meta:
        model = Menu2
        fields = "__all__"
        
class BookingForm(ModelForm):
    class Meta:
        model = Bookings
        fields = "__all__"