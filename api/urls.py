from django.urls import path
from .views import AlunosListCreateApiView, AlunosPendentesApiView, AlunosDeleteApiView, AlunosRetrieveApiView
urlpatterns = [
    path('list/', AlunosListCreateApiView.as_view(), name='list_api_view'),
    path('alunos_pendentes/', AlunosPendentesApiView.as_view(), name='alunos_pendentes_api_view'),
    path('destroy/<int:pk>/', AlunosDeleteApiView.as_view(), name='alunos_delete_api_view'),
    path('retrieve/<int:pk>/', AlunosRetrieveApiView.as_view(), name='alunos_retrieve_api_view'),
]
