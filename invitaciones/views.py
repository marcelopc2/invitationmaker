from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Invitacion
from .forms import InvitacionForm, CapaParallaxFormSet
from django.db import transaction

# --- VISTAS PÚBLICAS ---

class InvitacionListView(ListView):
    model = Invitacion
    template_name = 'invitaciones/index.html'
    context_object_name = 'invitaciones'

class InvitacionDetailView(DetailView):
    model = Invitacion
    template_name = 'invitaciones/invitacion_detail.html'
    context_object_name = 'invitacion'

# --- VISTAS CMS (DASHBOARD) ---

class CMSDashboardView(ListView):
    model = Invitacion
    template_name = 'invitaciones/cms/dashboard.html'
    context_object_name = 'invitaciones'

class InvitacionCreateView(CreateView):
    model = Invitacion
    form_class = InvitacionForm
    template_name = 'invitaciones/cms/form.html'
    success_url = reverse_lazy('cms_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nueva Invitación'
        if self.request.POST:
            context['capas_formset'] = CapaParallaxFormSet(self.request.POST, self.request.FILES)
        else:
            context['capas_formset'] = CapaParallaxFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        capas_formset = context['capas_formset']
        with transaction.atomic():
            self.object = form.save()
            if capas_formset.is_valid():
                capas_formset.instance = self.object
                capas_formset.save()
        return super().form_valid(form)

class InvitacionUpdateView(UpdateView):
    model = Invitacion
    form_class = InvitacionForm
    template_name = 'invitaciones/cms/form.html'
    success_url = reverse_lazy('cms_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar: {self.object.titulo_landing}'
        if self.request.POST:
            context['capas_formset'] = CapaParallaxFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['capas_formset'] = CapaParallaxFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        capas_formset = context['capas_formset']
        with transaction.atomic():
            self.object = form.save()
            if capas_formset.is_valid():
                capas_formset.instance = self.object
                capas_formset.save()
        return super().form_valid(form)

class InvitacionDeleteView(DeleteView):
    model = Invitacion
    template_name = 'invitaciones/cms/confirm_delete.html'
    success_url = reverse_lazy('cms_dashboard')
