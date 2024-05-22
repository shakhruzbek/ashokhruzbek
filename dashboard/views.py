from django.shortcuts import render

from .models import Company, Service, Staff

# Create your views here.
def home(r):
    company = Company.objects.get(id=1)
    ctx = {
        "name": company.name,
        "desc": company.short_description
    }
    return render(r, 'home.html', context=ctx)

def about(r):
    company = Company.objects.get(id=1)
    ctx = {
        "name": company.name,
        "short_desc": company.short_description,
        "long_desc": company.long_description,
    }
    return render(r, 'about.html', ctx)

def contact(r):
    company = Company.objects.get(id=1)
    ctx = {
        'socials': {
            'telegram': company.telegram,
            'instagram': company.instagram,
            'facebook': company.facebook,
        },
        'phone': company.phone
    }
    return render(r, 'contact.html', ctx)

def services(r):
    s = Service.objects.all() 
    ctx = {
        'services': s
    }
    return render(r, 'services.html', ctx)

def staff(r):
    s = Staff.objects.all() 
    ctx = {
        'staff': s
    }
    return render(r, 'staff.html', ctx)
