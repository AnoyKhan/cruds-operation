from django.shortcuts import render, redirect
from .models import *
import os
from django.contrib import messages
# Create your views here.


def index(request):
        if request.method == 'GET':
                search = request.GET.get('src')
                if search:
                        prof = profile.objects.filter(Name__icontains = search)
                elif search == "None":
                        return redirect('home')
                else:
                        prof = profile.objects.all()
        return render(request, 'index.html', locals())

def delete(request, id):
        prof = profile.objects.get(id=id)
        if prof.image != "def.png.jpg":
                os.remove(prof.image.path)
        prof.delete()
        return redirect('index')

def create(request):
        if request.method == "POST":
                name = request.POST.get('Name')
                image = request.FILES.get('image')
                email = request.POST.get('email')
                phone_number =request.POST.get('phone_number')
                gender =request.POST.get('gender')
                address =request.POST.get('address')
                religions=request.POST.get('religions')
                blood_groop =request.POST.get('blood_groop')
                date_of_birth =request.POST.get('date_of_birth')
                is_alive =request.POST.get('is_alive')
                if profile.objects.filter(Name=name).exists():
                        messages.warning(request, "This account already exists")
                        return redirect('create')
                else:
                        if image:
                                prof = profile.objects.create(Name = name, image = image, email = email, phone_number =phone_number, gender=gender,address=address,religions =religions,  blood_groop = blood_groop,date_of_birth=date_of_birth,is_alive= is_alive )
                                prof.save()
                                messages.success(request, "Account Created")
                                return redirect('index')
                        else:
                                prof = profile.objects.create(Name = name, email = email, phone_number =phone_number, gender=gender,address=address,religions =religions,  blood_groop = blood_groop,date_of_birth=date_of_birth,is_alive= is_alive )
                                prof.save()
                                messages.success(request, "Account Created")
                                return redirect('index')

        return render(request, 'create.html')

