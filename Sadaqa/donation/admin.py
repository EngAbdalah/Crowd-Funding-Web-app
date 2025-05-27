from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('id', 'donor', 'project', 'amount', 'currency', 'donation_date')
    list_filter = ('currency', 'donation_date')
    search_fields = ('donor__email', 'project__title')
    date_hierarchy = 'donation_date'