from email.policy import default
from django.db import models

class New(models.Model):
    titulo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="static/portfolio/images", blank=True)
    autor = models.CharField(max_length=40)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=500)
    link = models.CharField(max_length=1000)

    def __str__(self):
          return self.titulo[:50]

class Person(models.Model):
    nome = models.CharField(max_length=60)
    linklusofona = models.CharField(max_length=1000, default='1')
    linklinkedin = models.CharField(max_length=1000, default='1')

    def __str__(self):
          return self.nome[:50]

class Tecnologia(models.Model):
    nome = models.CharField(max_length=30)
    acronimo = models.CharField(max_length=10, blank=True)
    ano = models.IntegerField()
    criador = models.CharField(max_length=40)
    logotipo = models.ImageField(upload_to="static/portfolio/images")
    link = models.CharField(max_length=500)
    descricao = models.TextField(max_length=1000)
    existente = models.BooleanField(default=False)

    def __str__(self):
          return self.nome[:50]

class Education(models.Model):
    formacao = models.CharField(max_length=70)
    curso = models.CharField(max_length=60)
    topicos = models.CharField(max_length=500, default='1')
    local = models.CharField(max_length=50)
    periodo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="static/portfolio/images", default='1')
    logotipo = models.ImageField(upload_to="static/portfolio/images")

    def __str__(self):
          return self.formacao[:50]

class Project(models.Model):
    titulo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="static/portfolio/images")
    tecnologia = models.ManyToManyField(Tecnologia)
    participantes = models.CharField(max_length=100)
    cadeira = models.CharField(max_length=40)
    ano = models.IntegerField()
    descricao = models.CharField(max_length=500)
    linkgithub = models.CharField(max_length=1000, blank=True)

    def __str__(self):
          return self.titulo[:50]

class Chair(models.Model):
    nome = models.CharField(max_length=60)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.TextField(max_length=1000)
    ects = models.IntegerField()
    ano_letivo = models.CharField(max_length=20, default='1')
    topicos_abordados = models.CharField(max_length=1000, default='1')
    ranking = models.IntegerField()
    docente_teorica = models.ForeignKey(Person, on_delete=models.CASCADE, default='1')
    docentes_praticas = models.ManyToManyField(Person, related_name='professor_pratica')
    link_cadeira = models.CharField(max_length=1000, default='1')
    linguagens = models.ManyToManyField(Tecnologia, blank=True)
    projetos = models.ManyToManyField(Project, blank=True)

    def __str__(self):
          return self.nome[:50]

class Achivement(models.Model):
    titulo = models.CharField(max_length=70, default='1')
    descricao = models.CharField(max_length=100, default='1')
    projetos = models.ManyToManyField(Project, blank=True)
    cadeira = models.CharField(max_length=40, default='1')

    def __str__(self):
          return self.titulo[:50]

class Noticia(models.Model):
    titulo = models.CharField(max_length=80)
    texto = models.TextField(max_length=1000)
    imagem = models.ImageField(upload_to="static/portfolio/images")
    link = models.CharField(max_length=1000)
    
    def __str__(self):
          return self.titulo[:50]

class Lab(models.Model):
    titulo = models.CharField(max_length=70)
    descricao = models.TextField(max_length=1000)
    link = models.CharField(max_length=1000)

    def __str__(self):
          return self.titulo[:50]

class TFC(models.Model):
    titulo = models.CharField(max_length=50)
    sumario = models.TextField(max_length=1000)
    linkGitHub = models.CharField(max_length=1000)
    linkYoutube = models.CharField(max_length=1000)
    linkRelatorio = models.CharField(max_length=1000)
    ano = models.IntegerField()
    orientador = models.ManyToManyField(Person)
    autor = models.CharField(max_length=70)
    imagem = models.ImageField(upload_to="static/portfolio/images", null=True, blank=True)

    def __str__(self):
          return self.titulo[:50]

class PontuacaoQuizz(models.Model):     
    nome = models.CharField(max_length=20)    
    apelido = models.CharField(max_length=20)     
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.nome[:50]

# Create your models here.
