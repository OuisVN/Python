from django.contrib import admin
from inicio.models import * # Todos los modelos creados hasta el momento.

# Todo lo que viene de aqui para adelante es solo para que cada modelo aparezca en el panel administrativo.

admin.site.register(usuarios)
admin.site.register(publicaciones)
admin.site.register(publicaciones_comentarios)
admin.site.register(publicaciones_likes)
admin.site.register(publicaciones_archivados)
admin.site.register(seguidores)