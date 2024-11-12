from django.contrib import admin
from .models import ApiAluno

@admin.register(ApiAluno)
class ApiAlunosAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'cpf', 'created_at', 'expiration_date',)
    search_fields = ('name',)