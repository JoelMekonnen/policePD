from django.urls import path, include
from .views import homePage, PoliceCreateView, CaseCreateView, ShowCases, CaseUpdateView, CaseDeleteView, CreateAssignedCases
urlpatterns = [
    path('', homePage, name='home'),
    path('signup/', PoliceCreateView.as_view(), name='signnup'),
    path('case/create', CaseCreateView.as_view(), name='caseCreate'),
    path('case/show', ShowCases.as_view(), name='showCase'),
    path('case/update/<int:pk>/', CaseUpdateView.as_view(), name='caseUpdate'),
    path('case/delete/<int:pk>/', CaseDeleteView.as_view(), name='caseDelete'),
    path('case/assign/create', CreateAssignedCases.as_view(), name='caseAssign')
]
