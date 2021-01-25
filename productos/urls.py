from django.urls import path
from productos.views import *

urlpatterns = [
    path('login/' , LoginView.as_view() , name='login'),
    path('' , IndexView.as_view() , name='index'),
    path('imprimir/preciador/<int:pk>' , PrintPricer.as_view() , name='print_pricer'),
    path('imprimir/' , MultiPrint, name='multiprint'),
    path('imprimir-precios/' , ComputerPrint, name='computerprint'),
    path('ver/temporada/' , SeasonView.as_view() , name='season_list'),
    path('agregar/temporada/' , CreateSeason.as_view() , name='season_add'),
    path('agregar/preciador/' , CreatePricer.as_view() , name='pricer_add'),
    path('agregar/producto/' , CreateProduct.as_view() , name='product_add'),
    path('ver/preciadores/' , PricerList.as_view() , name='pricer_list'),
    path('ver/preciadores-computadoras/' , ComputerPricerList.as_view() , name='pricer_computer_list'),
    path('ver/productos/' , ProductList.as_view() , name='product_list'),
    path('ver/computadora-laptops/' , ComputerList.as_view() , name='computer_list'),
    path('generar-precios/' , makePricer , name='pricer_generate'),
    path('generar-precios/laptops' , makePricerPC , name='pricer_generate_pc'),

]
