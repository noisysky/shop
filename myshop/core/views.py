from django.views.generic import TemplateView
from core.models import Products

class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
#        context['listed'] = ["Featured products", "New products", "Frequently purchased products", "Recently viewed products"]
        products = Products.objects.all().select_related().order_by('price')[:10]  # JOIN for ForeignKey
        context['products'] = products
        return context