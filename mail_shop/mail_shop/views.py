from django.shortcuts import render

from packages.models import Package
from customers.models import Customer
from mailboxes.models import Mailbox, MailboxOwner


def index(request):
    packages = Package.objects.filter(date_claimed__is=True)
    context = {
        'packages': packages,
    }
    return render(request, 'index.html', context)
