from django.shortcuts import render , HttpResponseRedirect , HttpResponse
from django.urls import reverse , reverse_lazy
from django.db.models import Q  , Sum , Avg , Count , FilteredRelation

from django.views.generic import TemplateView, DetailView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin ,PermissionRequiredMixin
from django.contrib.auth import views as auth_views

from productos.models import *
# Create your views here.

from easy_pdf.views import PDFTemplateResponseMixin , PDFTemplateView

#from Django Forms
from productos.forms import *


class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'productos/index.html'

    def get_context_data(self , *args , **kwargs):
        prices = Product.objects.all()
        return {'prices': prices}

# class PrintPricer(PDFTemplateResponseMixin , DetailView):
#     template_name = 'productos/preciador.html'
#     model = Pricer
#     slug_field = 'id_pricer'
#     slug_url_kwarg = 'id_pricer'
#     queryset = Pricer.objects.all()
#     context_object_name = 'pricer'
#
#     def get_object(self, queryset=None):
#         pricer = super(PrintPricer, self).get_object(queryset=queryset)
#         return pricer

class PrintPricer(LoginRequiredMixin, DetailView):
    template_name = 'productos/preciador.html'
    model = Pricer
    slug_field = 'id_pricer'
    slug_url_kwarg = 'id_pricer'
    queryset = Pricer.objects.all()
    context_object_name = 'pricer'

    def get_context_data(self , *args , **kwargs):
        context = super(PrintPricer, self).get_context_data(**kwargs)
        id_pricer = self.get_object()
        context['counter'] = range(0,id_pricer.cant)
        return context

    # def get_object(self, queryset=None):
    #     pricer = super(PrintPricer, self).get_object(queryset=queryset)
    #     counter =
    #     return pricer

class SeasonView(LoginRequiredMixin, TemplateView):
    template_name = 'productos/season_list.html'

    def get_context_data(self , *args , **kwargs):
        seasons = Season.objects.all()
        return {'seasons': seasons}

class CreateSeason(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    template_name = 'productos/season_list.html'
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    form_class = SeasonForm
    success_message = 'Temporada Agregada'
    success_url = reverse_lazy('season_list')

class CreatePricer(SuccessMessageMixin, LoginRequiredMixin,CreateView):
    template_name = 'productos/pricer_list.html'
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    form_class = PricerForm
    success_message = 'Preciador Agregado'
    success_url = reverse_lazy('pricer_list')

class CreateProduct(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    template_name = 'productos/product_list.html'
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    form_class = ProductForm
    success_message = 'Producto Agregado'
    success_url = reverse_lazy('product_list')

class PricerList(LoginRequiredMixin,TemplateView):
    template_name = 'productos/pricer_list.html'

    def get_context_data(self, *args, **kwargs):
        pricers = Pricer.objects.all()
        products = Product.objects.all()
        sizes = Size.objects.all()
        seasons = Season.objects.all()
        return {'pricers': pricers , 'products':products , 'sizes': sizes , 'seasons':seasons,}

class UpdatePrice(LoginRequiredMixin,UpdateView):
    # permission_required = 'ordenes.assign_service'
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    model = Pricer
    fields = ['season' , 'size' , 'cant']
    success_url = reverse_lazy('pricer_list')
    template_name = 'productos/components/update_service.html'
    success_message = 'La orden se ha actualizado correctamente!'

class ComputerPricerList(LoginRequiredMixin, TemplateView):
    template_name = 'productos/computer_pricer_list.html'

    def get_context_data(self, *args, **kwargs):
        devices = ComputerPricer.objects.all()
        return {'devices': devices}

class ProductList(LoginRequiredMixin,TemplateView):
    template_name = 'productos/product_list.html'

    def get_context_data(self, *args, **kwargs):
        products = Product.objects.all()
        return {'products': products}

class ComputerList(LoginRequiredMixin,TemplateView):
    template_name = 'productos/computer_list.html'

    def get_context_data(self, *args, **kwargs):
        devices = Computer.objects.all()
        return {'devices': devices}


"""Función para desplegar una impresion de multpiples precios"""
def MultiPrint(request):
    query = request.GET.getlist('id')
    # sucursal_user= request.user.sucursal.pk
    if query:
        pricers = Pricer.objects.filter(pk__in=query).order_by('size__pk')
    else:
        pricers =[]
    return render(request , "productos/multi_preciador.html" , { 'pricers' :pricers })

"""Función para desplegar una impresion de computadora"""
def ComputerPrint(request):
    query = request.GET.getlist('id')
    # sucursal_user= request.user.sucursal.pk
    if query:
        pricers = ComputerPricer.objects.filter(pk__in=query)
    else:
        pricers =[]
    return render(request , "productos/computer_multi_preciador.html" , { 'pricers' :pricers })



# incompleto por el tamanio de precio
def makePricer(request):
    id_season = request.GET.get('season')
    id_size = request.GET.get('size')
    size = Size.objects.get(pk=id_size)
    season_design = Season.objects.get(pk=id_season)
    products = Product.objects.all()
    for p in products:
        product = Product.objects.get(pk=p.pk)
        pricer = Pricer.objects.create(
        season = season_design,
        product = product,
        size = size,
        cant = p.stock
        )
        pricer.save()
    return HttpResponseRedirect(reverse('index'))


def makePricerPC(request):
    # 1 para size laptop
    # 7 season normal
    id_season = request.GET.get('season')
    id_size = request.GET.get('size')
    size = Size.objects.get(pk=id_size)
    season_design = Season.objects.get(pk=id_season)
    computers = Computer.objects.all()
    for p in computers:
        product = Computer.objects.get(pk=p.pk)
        pricer = ComputerPricer.objects.create(
        season = season_design,
        computer = product,
        size = size,
        cant = 1
        )
        pricer.save()
    return HttpResponseRedirect(reverse('index'))


class LoginView(SuccessMessageMixin , auth_views.LoginView):
    template_name = 'productos/login.html'
    success_message = "Bienvenido!"
