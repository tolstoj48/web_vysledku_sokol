from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name="vysledky_s/robots.txt", content_type='text/plain')),
    path('vysledky/2018-2019/Mladší dorost/', views.nehrano_2018_2019), #upravit s views
    #path('vysledky/2019-2020/Starší dorost/', views.zatim_nehrano_2019_2020),
    #path('vysledky/2019-2020/Mladší dorost/', views.zatim_nehrano_2019_2020),
    #path('vysledky/2019-2020/Starší žáci/', views.zatim_nehrano_2019_2020),
    #path('vysledky/2019-2020/Mladší žáci A/', views.zatim_nehrano_2019_2020),
    #path('vysledky/2019-2020/Mladší žáci B/', views.zatim_nehrano_2019_2020),
    #path('vysledky/2019-2020/Mladší žáci C/', views.zatim_nehrano_2019_2020),
    path('', views.hlavni),
    path('vysledky/<sezona>/', views.uvodni_sezona),
    path('vysledky/<sezona>/strelci/', views.strelci),
    path('vysledky/<sezona>/<tyms>/', views.tym),
    path('vysledky/<sezona>/<tyms>/<id>/', views.detail),
    path('rozpisy/', views.rozpisy),
    path('appis/<hodnota>/', views.appis)
]