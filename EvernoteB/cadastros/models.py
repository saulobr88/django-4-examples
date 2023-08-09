from django.db import models

# Create your models here.


class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255, verbose_name="Descrição")

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)


class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    pontos = models.DecimalField(max_digits=4, decimal_places=1)
    detalhes = models.TextField()

    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.descricao, self.campo.nome)
