from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import PoliceCreateForm, PoliceChangeForm
from .models import PoliceInfo, CaseInfo, CaseAssign

class PoliceAdmin(UserAdmin):
    add_form = PoliceCreateForm
    form = PoliceChangeForm
    model = PoliceInfo
    list_display = ['first_name', 'last_name', 'email', 'username', 'gender', 'rank']

admin.site.register(PoliceInfo, PoliceAdmin)
admin.site.register(CaseInfo)
admin.site.register(CaseAssign)
