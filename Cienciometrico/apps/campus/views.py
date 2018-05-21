from django.shortcuts import render
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.campus.form import CampusForm
from apps.campus.models import campus
from apps.pais.models import pais
from apps.provincia.models import provincia
from apps.zona.models import zona
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
# Create your views here.












class CampusList(ListView):
    model = campus
    template_name = 'campus/campus_listar.html'
 #   paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(CampusList, self).get_context_data(**kwargs)
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

class CampusCreate(CreateView):
    model = campus
    form_class = CampusForm
    template_name = 'campus/campus_crear.html'
    success_url = reverse_lazy('campus:campus_listar')
    def get_context_data(self, **kwargs):
        context = super(CampusCreate, self).get_context_data(**kwargs)
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



class CampusUpdate(UpdateView):
    model = campus
    form_class =CampusForm
    template_name = 'campus/campus_update.html'
    success_url = reverse_lazy('campus:campus_listar')










class CampusDelete(DeleteView):
    model = campus
    template_name = 'campus/campus_delete.html'
    success_url = reverse_lazy('campus:campus_listar')
    def get_context_data(self, **kwargs):
        context = super(CampusDelete, self).get_context_data(**kwargs)
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
