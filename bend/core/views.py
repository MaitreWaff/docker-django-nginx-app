from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationFrom, ProfileForm

# LogIn
def loginUser(request):
    page = 'login'

    context = {'page': page}

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        
        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        else:

            messages.error(request, 'Username OR Password incorrect!')
    return render(request, 'core/login_register.html', context)

# LogOut
def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')



# Register a New User
def registerUser(request):
    page = 'register'
    form = CustomUserCreationFrom()

    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User Account was created!')

            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, 'An error has occured during registration')
    
    context = {'page': page, 'form': form}
    return render(request, 'core/login_register.html', context)


# Profile List
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'core/profiles.html', context)


# User Profile
def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {'profile': profile}
    return render(request, 'core/user-profile.html', context)


# User Profile
@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    context = {'profile': profile}
    return render(request, 'core/account.html', context)

# Edit Account
@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('account')
    
    context = {'form': form}

    return render(request, 'core/profile_form.html', context)

    # return render(request, 'core/account.html', context)
