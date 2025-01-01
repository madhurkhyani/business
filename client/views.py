from django.views import View
from django.views.generic.edit import CreateView
from .forms import ClientForm
from .models import ClientData
from django.shortcuts import render,get_object_or_404,redirect
# Create your views here.

class addClient(CreateView):
    template_name = "client/add-client.html"
    model = ClientData
    form_class = ClientForm
    success_url="/clients/"


class ClientPage(CreateView):
    model=ClientData
    fields = "__all__"
    template_name="client/client_page.html"
    context_object_name="client_info"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_info'] = ClientData.objects.all()  # Fetch all records
        return context

def client_detail(request,client_id):
    info=get_object_or_404(ClientData,id=client_id)
    return render(request, "client/client_detail.html",{"client_info":info
    })