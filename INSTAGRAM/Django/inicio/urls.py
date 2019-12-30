from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio.as_view(), name='inicio'), # Pagina inicial del aplicativo.
    path('registrarse', registrarse.as_view(), name='registrarse'), # Pagina de registro del aplicativo.
    path('instagram', instagram.as_view(), name='instagram'), # Pagina donde salen las historias e imagenes de tus seguidores y tuyas.
    path('perfil', perfil.as_view(), name='perfil'), # Buscar un perfil.
    path('cerrar_sesion', cerrar_sesion.as_view(), name='cerrar_sesion'), # Cerrar sesion.
    
    path('perfil_subir', perfil_subir.as_view(), name='perfil_subir'), # Subir imagen al perfil.
    path('perfil_editar', perfil_editar.as_view(), name='perfil_editar'), # Editar perfil.
    path('seguir', seguir.as_view(), name='seguir'), # Seguir y dejar de seguir.
    path('comentarios', comentarios.as_view(), name='comentarios'), # Dejar un comentario.
    path('borrar_comentarios', borrar_comentarios.as_view(), name='borrar_comentarios'), # Borra un comentario.
    
    path('borrar_publicaciones', borrar_publicaciones.as_view(), name='borrar_publicaciones'), # Borra una publicacion.
    
    path('me_gusta/<int:id>', me_gusta.as_view(), name='me_gusta'), # Me gusta.
    path('guardar/<int:id>', guardar.as_view(), name='guardar'), # Guardar.
    
    path('publicaciones_guardadas', publicaciones_guardadas.as_view(), name='publicaciones_guardadas'), # Ver publicaciones guardadas.
]