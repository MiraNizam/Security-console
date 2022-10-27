from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    guest_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in guest_visits:
        this_passcard_visits.append(
            {
            'entered_at': localtime(visit.entered_at),
            'duration': visit.get_duration(),
            'is_strange': visit.is_visit_long()
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
