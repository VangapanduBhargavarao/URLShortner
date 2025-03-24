from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import User,URL
import random,string

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if user already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signup')
        
        # Create new user
        User.objects.create(
            email=email,
            password=password  # Note: In production, always hash passwords!
        )
        
        # Redirect to signin page after successful signup
        return redirect('signin')
    
    return render(request, 'accounts/signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email, password=password)
            # In a real application, you would set up a session here
            return redirect('index')  # You'll need to create this view
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials')
            return redirect('signin')
    
    return render(request, 'accounts/signin.html')
"""def mainpage(request):
    if request.method=='POST':
        return redirect('signin')
    return render(request,'accounts/mainpage.html')"""

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters+string.digits,k=6))
def index(request,short_code=None):
    short_url=None
    if short_code:
        try:
            url_instance=URL.objects.get(short_code=short_code)
            return redirect(url_instance.long_url)
        except URL.DoesNotExist:
            return render(request,'accounts/mainpage.html',{'error':'Invalid short URL!'})
    if request.method=='POST':
        long_url=request.POST.get('long_url')
        url_instance,created=URL.objects.get_or_create(long_url=long_url)
        if created:
            url_instance.short_code=generate_short_code()
            url_instance.save()
        short_url=request.build_absolute_uri('/')+url_instance.short_code

    return render(request,'accounts/mainpage.html',{'short_url':short_url})
