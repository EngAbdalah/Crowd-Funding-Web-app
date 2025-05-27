from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from projects.models import Project
from .forms import DonationForm
from .models import Donation


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

            # Update project current donations
            project.current_donations += donation.amount
            project.save()

            messages.success(request, 'Thank you for your donation!')
            return redirect('projects:project_detail', project_id=project.id)
    else:
        form = DonationForm()

    return render(request, 'donation/donate.html', {
        'form': form,
        'project': project
    })