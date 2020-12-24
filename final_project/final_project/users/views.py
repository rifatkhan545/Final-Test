from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.models import User



def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email= email, password = password)
            return redirect('index')
    else:
        form = SignupForm()

    context = {
        'form': form
    }

    return render(request, 'signup.html', context= context)


