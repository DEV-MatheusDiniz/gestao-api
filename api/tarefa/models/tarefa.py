from django.db import models

from api.usuario.models.usuario import UsuarioModel


class TarefaModel(models.Model):
    ds_descricao = models.TextField()
    fk_responsavel = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE)
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.ds_descricao

    class Meta:
        app_label = "tarefa"
        db_table = "tarefas"
