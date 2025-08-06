
from .models import Work
from django.views.generic import ListView

class WorkListView(ListView):
    model = Work
    template_name = "app/index.html"
    context_object_name= 'work'