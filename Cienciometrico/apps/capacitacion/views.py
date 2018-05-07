from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.capacitacion.form import CapacitacionForm
from apps.capacitacion.models import capacitacion
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.perfiles.models import Perfil
from apps.roles.models import Rol

# Create your views here.
class CapacitacionList(ListView):
    model = capacitacion
    template_name = 'capacitacion/capacitacion_listar.html'
    def get_context_data(self, **kwargs):
        context = super(CapacitacionList, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context

class CapacitacionCreate(CreateView):
    model = capacitacion
    form_class = CapacitacionForm
    template_name = 'capacitacion/capacitacion_crear.html'
    success_url = reverse_lazy('capacitacion:capacitacion_listar')
    def get_context_data(self, **kwargs):
        context = super(CapacitacionCreate, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context

class CapacitacionUpdate(UpdateView):
    model = capacitacion
    form_class = CapacitacionForm
    template_name = 'capacitacion/capacitacion_update.html'
    success_url = reverse_lazy('capacitacion:capacitacion_listar')
    def get_context_data(self, **kwargs):
        context = super(CapacitacionUpdate, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context
class CapacitacionDelete(DeleteView):
    model = capacitacion
    template_name = 'capacitacion/capacitacion_eliminar.html'
    success_url = reverse_lazy('capacitacion:capacitacion_listar')
    def get_context_data(self, **kwargs):
        context = super(CapacitacionDelete, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context