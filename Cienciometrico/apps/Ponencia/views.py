from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from apps.Ponencia.form import PonenciaForm
from apps.Ponencia.models import ponencia
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
# Create your views here.
class PonenciaList(ListView):
    model = ponencia
    template_name = 'ponencia/ponencia_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(PonenciaList, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio= []
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
class PonenciaCreate(CreateView):
    model = ponencia
    form_class = PonenciaForm
    template_name = 'ponencia/ponencia_crear.html'
    success_url = reverse_lazy('ponencia:ponencia_listar')
    def get_context_data(self, **kwargs):
        context = super(PonenciaCreate, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio= []
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
class PonenciaUpdate(UpdateView):
    model = ponencia
    form_class = PonenciaForm
    template_name = 'ponencia/ponencia_update.html'
    success_url = reverse_lazy('ponencia:provincia_listar')
    def get_context_data(self, **kwargs):
        context = super(PonenciaUpdate, self).get_context_data(**kwargs)

        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio= []
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
class PonenciaDelete(DeleteView):
    model = ponencia
    template_name = 'ponencia/ponencia_delete.html'
    success_url = reverse_lazy('ponencia:ponencia_listar')
    def get_context_data(self, **kwargs):
        context = super(PonenciaDelete, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio= []
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

