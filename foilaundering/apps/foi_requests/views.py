from django.views.generic import CreateView, ListView

from .forms import ArticleForm
from .models import FOIRequest

class SubmitView(CreateView):
    form_class = ArticleForm
    template_name = "submit_form.html"
    success_url = "/request/thanks/"

class RequestsListView(ListView):
    queryset = FOIRequest.objects.all()
