from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.utils import timezone
from django.views import generic



from django.shortcuts import render


from .models import Image


class IndexView(generic.ListView):
    template_name = 'images/index.html'
    context_object_name = 'latest_image_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Image.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Image
    template_name = 'images/detail.html'


class ResultsView(generic.DetailView):
    model = Image
    template_name = 'images/results.html'

def tag(request, image_id):
    return HttpResponse("You're tagging on image %s." % image_id)