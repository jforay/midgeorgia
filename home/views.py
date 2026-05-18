from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            body = (
                f"New contact form submission from Mid Georgia Boat Club:\n\n"
                f"Name: {d['first_name']} {d['last_name']}\n"
                f"Email: {d['email']}\n"
                f"Phone: {d.get('phone_number', 'N/A')}\n"
f"Message:\n{d['question']}"
            )
            send_mail(
                subject=f"Contact Form - {d['first_name']} {d['last_name']}",
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.SITE_ADMIN_EMAIL],
                fail_silently=True,
            )
            messages.success(request, "Thanks! We'll be in touch soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})

def home(request):
    return render(request, 'home/home.html')

def equipment(request):
    return render(request, 'home/equipment.html')

def first_responders(request):
    return render(request, 'home/first_responders.html')

def dirty_work(request):
    return render(request, 'home/dirty_work.html')

def get_back(request):
    return render(request, 'home/get_back.html')

def amenities(request):
    return render(request, 'home/amenities.html')

def weather(request):
    return render(request, 'home/weather.html')

def faq(request):
    return render(request, 'home/faq.html')