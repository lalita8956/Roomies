
from .models import Work , Day ,User

from django.views.generic import ListView


class WorkListView(ListView):
    model = Work
    template_name = 'Worksheet/work_list.html'
    context_object_name = 'works'

    def get_queryset(self):
        return Work.objects.all()

class DayListView(ListView):
    model = Day
    template_name = 'Worksheet/work_list.html'
    context_object_name = 'days'

    def get_queryset(self):
        return Day.objects.all()

class UserListView(ListView):
    model = User
    template_name = 'Worksheet/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()
    
    

    

    
