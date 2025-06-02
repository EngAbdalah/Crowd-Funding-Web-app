from django.shortcuts import render, redirect
from .forms import DonationForm
from .models import Donation

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            if request.user.is_authenticated:
                donation.user = request.user
            else:
                donation.user = None
            donation.save()
            return redirect('success', donation_id=donation.id)
    else:
        form = DonationForm()
    return render(request, 'donation/donate.html', {'form': form})

def success(request, donation_id):
    donation = Donation.objects.get(id=donation_id)
    return render(request, 'donation/success.html', {'donation': donation})

def history(request):
    if request.user.is_authenticated:
        donations = Donation.objects.filter(user=request.user)
    else:
        donations = []  # or redirect to login page if needed
    return render(request, 'donation/history.html', {'donations': donations})
