from pipes import Template
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

from events.models import Event

@login_required
def event_list_view(request):
    context = {}
    context['event_list'] = Event.objects.all()

    return TemplateResponse(request, 'events/event_list.html', context)

@login_required
def event_detail_view(request, pk):
    context = {}
    context['event'] = Event.objects.get(pk=pk)

    return TemplateResponse(request, 'events/event_detail.html', context)

def event_new_view(request):
    #if request.method == 'POST':
    pass


