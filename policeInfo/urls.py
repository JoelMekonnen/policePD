from django.urls import path, include
from .views import homePage, PoliceCreateView, CaseCreateView, ShowCases
urlpatterns = [
    path('', homePage, name='home'),
    path('signup/', PoliceCreateView.as_view(), name='signnup'),
    path('case/create', CaseCreateView.as_view(), name='caseCreate'),
    path('case/show', ShowCases.as_view(), name='showCase'),
]
