from django.db import models
from datetime import datetime # No esta haciendo nada pero en su momento se utilizo para algo, de pronto y puede servir para despues.

# Me pasaria horas explicando cada cosas asi que se hara de manera global.
# Cada clase es un modelo que contiene ciertos atributos con posibles restricciones.
    # EJ: Clase usuarios, posee atributos como usuario, contrasena, correo, entre otros...
    # Cada atributo posee una restriccion, en caso del usuario, que la longitud maxima no sobrepase los 255.

# Por otro lado, cada clase posee un Meta y una definicion...
    # El Meta nos permite pluralizar y singulizar el nombre de la clase dentro de los diferentes apartados de django.
        # EJ: El panel administrativo.
    # por parte de la definicion, nos permite decorar en los diferentes apartados de django la informacion que se muestra en pantalla
        # EJ: El panel administrativo.
        
# Estos dos ejemplos anteriores tienen la particularidad de que, en el panel administrativo si se deja sin estos dos elementos quedaria
    # EJ: Usuarioss. Y, (Object (1)), respectivamente para Meta y definicion.

class usuarios(models.Model):
    usuario = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    nombre_completo = models.CharField(max_length=255)
    imagen_perfil = models.ImageField(upload_to='static/images/perfil', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def __str__(self):
        return '{}'.format(self.nombre_completo)
    
class publicaciones(models.Model):
    tipos =((1, "Publicacion"), (2, "Historia"),) # Como la publicacion tiene dos formas de vista, se especifica aca para que en el panel sepan que opcion hace alusion al ID.

    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='static/images/publicaciones')
    mensaje = models.TextField(blank=True)
    tipo = models.IntegerField(choices=tipos, default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"
        
    def __str__(self):
        if(self.tipo == 1):
            publicacion = 'Publicacion'
        else:
            publicacion = 'Historia'
        return '{} creada por {} a las {}'.format(publicacion, self.usuario.nombre_completo, self.fecha_creacion)
    
class publicaciones_comentarios(models.Model):
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(publicaciones, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        
    def __str__(self):
        return 'Comentario creado por {} a las {}'.format(self.usuario.nombre_completo, self.fecha_creacion)
    
class publicaciones_likes(models.Model):
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(publicaciones, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        
    def __str__(self):
        return '{} dejo un me gusta a la publicacion de {}'.format(self.usuario.nombre_completo, self.publicacion.usuario.nombre_completo)
    
class publicaciones_archivados(models.Model):
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(publicaciones, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Archivado"
        verbose_name_plural = "Archivados"
    
    def __str__(self):
        return '{} guardo la publicacion de {}'.format(self.usuario.nombre_completo, self.publicacion.usuario.nombre_completo)
    
class seguidores(models.Model):
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name='seguidor') # Se utiliza related_name porque esta tabla en particular posee dos IDs de usuarios.
    usuario_seguido = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name='seguido')
    
    class Meta:
        verbose_name = "Seguidor"
        verbose_name_plural = "Seguidores"
    
    def __str__(self):
        return '{} ({}) empezo a seguir a {} ({})'.format(self.usuario.nombre_completo, self.usuario.id, self.usuario_seguido.nombre_completo, self.usuario_seguido.id)