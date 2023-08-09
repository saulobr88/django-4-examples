from django.urls import path

from .views import (
    CampoCreateView,
    CampoUpdateView,
    AtividadeCreateView,
    AtividadeUpdateView,
    CampoDeleteView,
    AtividadeDeleteView,
    CampoListView,
    AtividadeListView,
)

urlpatterns = [
    path('cadastrar/campo/', CampoCreateView.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreateView.as_view(),
         name='cadastrar-atividade'),

    path('editar/campo/<int:pk>', CampoUpdateView.as_view(), name='atualizar-campo'),
    path('editar/atividade/<int:pk>',
         AtividadeUpdateView.as_view(), name='atualizar-atividade'),

    path('excluir/campo/<int:pk>', CampoDeleteView.as_view(), name='excluir-campo'),
    path('excluir/atividade/<int:pk>',
         AtividadeDeleteView.as_view(), name='excluir-atividade'),

    path('listar/campos/', CampoListView.as_view(), name='listar-campos'),
    path('listar/atividades/', AtividadeListView.as_view(),
         name='listar-atividades'),
]
