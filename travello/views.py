from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1= Destination()
    dest1.name= 'Dhaka'
    dest1.price= 700
    dest1.desc='City of Magic'
    dest1.img= 'destination_1.jpg'

    dest2= Destination()
    dest2.name= 'Barisal'
    dest2.price= 750
    dest2.desc='City of Beauty'
    dest2.img= 'destination_2.jpg'

    dest3= Destination()
    dest3.name= 'Khulna'
    dest3.price= 800
    dest3.desc='Lovely city to breathe'
    dest3.img= 'destination_3.jpg'

    dests=[dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})
