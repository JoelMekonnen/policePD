from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views import View
from django.urls import reverse_lazy
from .forms import PoliceCreateForm, PoliceChangeForm
from .models import PoliceInfo, CaseInfo, CaseAssign
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
class AgentDB(ListView):
    def GetAgent(self):
        name = self.request.user.username
        return {'name':name}
def homePage(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html') 
    else:
        if request.user.is_staff:
            #list of users that have signed up
            usersList = PoliceInfo.objects.all()
            caseList = CaseInfo.objects.all()
            assignList = CaseAssign.objects.all()
            userCount = 0
            caseCount = 0
            assignCount = 0
            completedCases = 0
            for user in usersList:
                userCount = userCount + 1
            for case in caseList:
                caseCount = caseCount + 1
            for assigns in assignList:
                assignCount = assignCount + 1
                if assigns.CaseCompleted:
                    completedCases = completedCases + 1
            return render(request, 'staff/st_index.html', {'usercount': userCount, 'casecount': caseCount, 'assigncount':assignCount, 'complete': completedCases})
        else:
            Agent = AgentDB()
            return render(request, 'policeClient/pc_index.html', Agent.GetAgent())

class PoliceCreateView(PermissionRequiredMixin, CreateView):
    form_class = PoliceCreateForm
    model = PoliceInfo
    success_url = reverse_lazy('home')
    template_name = 'sign.html'
    permission_required = 'is_staff'
   

class CaseCreateView(CreateView):
    model = CaseInfo
    template_name = 'staff/CaseCreate.html'
    success_url = reverse_lazy('home')
    fields = ['CaseName', 'CaseDescription']
class ShowCases(ListView):
    model = CaseInfo
    paginate_by = 2
    context_object_name = 'Cases'
    template_name = "staff/ShowCases.html"
    queryset = CaseInfo.objects.all()
    #lets get the co
   


class CaseUpdateView(UpdateView):
    model = CaseInfo
    template_name = 'staff/CaseUpdate.html'
    fields = ['CaseName', 'CaseDescription']
    context_object_name = "Cases"
    success_url = reverse_lazy('home')

class CaseDeleteView(DeleteView):
    model = CaseInfo
    template_name = 'staff/CaseDelete.html'
    context_object_name = 'Cases'
    success_url = reverse_lazy('home')

class CreateAssignedCases(CreateView):
    model = CaseAssign
    template_name = 'staff/CaseAssignCreate.html'
    context_object_name = 'Assign'
    success_url = reverse_lazy('home')
    fields = ['AssignedTo', 'AssignedCase']

    

