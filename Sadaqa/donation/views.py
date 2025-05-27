from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Donation
from .forms import DonationForm
from projects.models import Project


@login_required
def create_donation(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = request.user
            donation.project = project
            donation.save()

            # Send email receipt here (if implemented)
            return redirect('donation:success', donation_id=donation.id)
    else:
        form = DonationForm()

    return render(request, 'donation/donate.html', {
        'form': form,
        'project': project
    })


@login_required
def donation_success(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id, donor=request.user)
    return render(request, 'donation/success.html', {'donation': donation})


@login_required
def donation_history(request):
    donations = Donation.objects.filter(donor=request.user) \
        .select_related('project') \
        .order_by('-donation_date')
    return render(request, 'donation/history.html', {'donations': donations})


@login_required
def donation_receipt(request, pk):
    donation = get_object_or_404(Donation, id=pk, donor=request.user)
    return render(request, 'donation/receipt.html', {'donation': donation})