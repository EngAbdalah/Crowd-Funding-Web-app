from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('donation:history')  # Redirect to donation history
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})