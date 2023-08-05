from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Bookings


def Home(request):
    return render(request, "Home.html")

def Aboutpage(request):
    return render(request, "About.html")

def LogInpage(request):
    return render(request, "Login.html")

def Dashboardpage(request):
    return render(request, "dashboard.html")

def SignUppage(request):
    return render(request, "signup.html")

def contactpage(request):
    return render(request, "contact.html")

def Servicepage(request):
    return render(request, "service.html")

def Bookingpage(request):
    return render(request, "booking.html")

def Roomspage(request):
    return render(request, "rooms.html")

from django.shortcuts import render
# from .forms import BookingForm
# from .models import Booking

def Bookings(request):
    if request.method == 'POST':
        form = Bookingpage(request.POST)
        if form.is_valid():
            guest_name = form.cleaned_data['guest_name']
            mobile_number = form.cleaned_data['mobile_number']
            email = form.cleaned_data['email']
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            id_proof = form.cleaned_data['id_proof']

            new_booking = Bookings(
                guest_name=guest_name,
                mobile_number=mobile_number,
                email=email,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                id_proof=id_proof
            )
            new_booking.save()

            return render(request, 'booking.html')

    else:
        form = Bookingpage()

    return render(request, 'booking.html', {'form': form})




    