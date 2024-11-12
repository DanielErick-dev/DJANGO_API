from .models import ApiAluno
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializer import ModelSerializerApi
from datetime import datetime
from setup.permissions import GlobalDefaultPermission
from rest_framework import views
class AlunosListCreateApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = ApiAluno.objects.all()
    serializer_class = ModelSerializerApi
class AlunosPendentesApiView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    serializer_class = ModelSerializerApi
    def get_queryset(self):
        data_atual = datetime.now().date()
        alunos_pendentes = ApiAluno.objects.filter(expiration_date__lt=data_atual)
        return alunos_pendentes

class AlunosDeleteApiView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = ApiAluno.objects.all()
    serializer_class = ModelSerializerApi


class AlunosRetrieveApiView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = ApiAluno.objects.all()
    serializer_class = ModelSerializerApi