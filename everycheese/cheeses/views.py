""" Our cheese views so we can talk about cheese!"""


from django.views.generic import ListView, DetailView, CreateView

from .models import Cheese


class CheeseListView(ListView):
    model = Cheese


class CheeseDetailView(DetailView):
    model = Cheese 


class CheeseCreateView(CreateView):
    model = Cheese
    fields = [ 
        'name', 
        'description', 
        'firmness', 
        'country_of_origin',
    ]
    action = "Add"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)