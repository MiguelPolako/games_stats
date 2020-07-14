from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import ContentType, Permission, User, Group

from accounts.forms import UserForm, GroupForm


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # '/accounts/login/'
    template_name = 'singup.html'

    def add_permissions_to_users(self):
        ct = ContentType.objects.all()
        permissions = Permission.objects.filter(content_type__in=ct)
        self.object.user_permissions.set(permissions)

    def form_valid(self, form):
        http_presponse = super().form_valid(form)
        self.add_permissions_to_users()
        return http_presponse

    def get_success_url(self):
        print('get_succes_url')
        print(f"{self.object}")
        return super().get_success_url()

class UpdateUserView(UpdateView):
    form_class = UserForm
    model = User
    template_name = 'form.html'
    success_url = "/"

class GroupsView(View):

    def get(self, request):
        groups = Group.objects.all()
        return render(request, "groups.html", {'groups': groups})


class UpdateGroupsView(PermissionRequiredMixin, UpdateView):
    permission_required = ['auth.add_group', 'auth.change_group']

    form_class = GroupForm
    model = Group
    template_name = 'form.html'
    success_url = reverse_lazy("groups")