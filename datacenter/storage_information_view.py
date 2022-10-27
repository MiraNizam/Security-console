from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []
    active_guests = Visit.objects.filter(leaved_at__isnull=True)

    for guest in active_guests:
        non_closed_visits.append(
            {
                'who_entered': guest.passcard.owner_name,
                'entered_at': localtime(guest.entered_at),
                'duration': format_duration(guest.get_duration())
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
