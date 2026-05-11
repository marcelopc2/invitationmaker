from django.urls import path
from .views import (
    InvitacionDetailView,
    CMSDashboardView, InvitacionCreateView, InvitacionUpdateView, InvitacionDeleteView
)

urlpatterns = [
    # Página principal → CMS Dashboard
    path('', CMSDashboardView.as_view(), name='index'),

    # Rutas CMS
    path('cms/', CMSDashboardView.as_view(), name='cms_dashboard'),
    path('cms/nueva/', InvitacionCreateView.as_view(), name='cms_crear'),
    path('cms/editar/<slug:slug>/', InvitacionUpdateView.as_view(), name='cms_editar'),
    path('cms/borrar/<slug:slug>/', InvitacionDeleteView.as_view(), name='cms_borrar'),

    # Ruta Detalle Pública (debe ir al final para que <slug> no bloquee /cms/)
    path('<slug:slug>/', InvitacionDetailView.as_view(), name='invitacion_detail'),
]
