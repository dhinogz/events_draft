from pipes import Template
from django.template.response import TemplateResponse

from events.models import Event

def event_list_view(request):
    context = {}
    context['event_list'] = Event.objects.all()

    return TemplateResponse(request, 'events/event_list.html', context)

def event_detail_view(request, pk):
    context = {}
    context['event'] = Event.objects.get(pk=pk)

    return TemplateResponse(request, 'events/event_detail.html', context)

