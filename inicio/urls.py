from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('bici/', views.Bici, name='bici'),
    path('bicis/crear/', views.crear_bici_v2, name='crear_bici_v2'),
    path('bicis/eliminar/<int:id>/', views.eliminar_bici, name='eliminar_bici'),
    path('bicis/editar/<int:id>/', views.editar_bici, name='editar_bici'),
    path('bicis/<int:id>/', views.ver_bici, name='ver_bici'),
]
