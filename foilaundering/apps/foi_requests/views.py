from django.views.generic import CreateView

from .forms import ArticleForm

class SubmitView(CreateView):
    form_class = ArticleForm
    template_name = "submit_form.html"
    success_url = "/request/thanks/"
