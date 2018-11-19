from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, FormView
from core.forms import RegisterForm
from core.models import Products, TelescopeType

class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
#        context['listed'] = ["Featured products", "New products", "Frequently purchased products", "Recently viewed products"]
#        products = Products.objects.all().select_related().order_by('price')[:10]  # JOIN for ForeignKey
        products = Products.objects.filter(
            status=Products.STATUS_IN_STOCK
        ).select_related().order_by('price')[:12]  # JOIN for ForeignKey
        context['products'] = products
        return context

class TelescopeView(ListView):
    template_name = 'telescope_type.html'
    model = Products

    def get_queryset(self):
        # trade_mark = TradeMark.objects.get(id=self.kwargs['trade_mark_id'])
        telescope_type = get_object_or_404(TelescopeType, id=self.kwargs['telescope_type_id'])
        queryset = self.model.objects.filter(telescope_type=telescope_type)
        # queryset = self.model.objects.filter(
        #     trade_mark__id=self.kwargs['trade_mark_id'],
        #     count__gt=0
        # )
        return queryset

class Register(FormView):
    template_name = 'auth/registration.html'
    form_class = RegisterForm
    success_url = '/'
    def form_valid(self, form):
        form.save()
        return super(Register, self).form_valid(form)