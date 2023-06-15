from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('sobre', views.sobre_view, name='sobre'),
    path('projetos', views.projetos_view, name='projetos'),
    path('web', views.web_view, name='web'),
    path('blog', views.blog_view, name='blog'),
    path('blog_novo/', views.nova_tarefa_view, name='blog_novo'),
    path('blog_editar/<int:portfolio_id>', views.edita_tarefa_view, name='blog_editar'),
    path('apaga/<int:portfolio_id>', views.apaga_tarefa_view, name='apaga'),
    path('contactos', views.contactos_view, name='contactos'),
    path('quizz', views.quizz, name='quizz'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')
]