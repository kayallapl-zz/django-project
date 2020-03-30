from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.descricao
