from django.views.generic.list import ListView

from .models import Paziente


class PazienteListView(ListView):

    model = Paziente

    def get_context_data(self, **kwargs):
        context = super(PazienteListView, self).get_context_data(**kwargs)
        return context
