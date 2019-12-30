from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from datetime import datetime, timedelta, time
from .models import *

# template_name = EJ: Si en el navegador escribe "/registrarse" django buscara en urls.py a que clase dentro de este archivo(views.py) tiene asignada esa ruta y, mostrara el respectivo template.

class inicio(TemplateView):
    template_name = 'index.html'
    
    # Verificamos que la variable de sesion bienvenido sea igual a 1. Si es asi, es porque el usuario ya ha iniciado sesion en la plataforma.
    def get(self, request, *args, **kwargs):
        if(request.session.get('bienvenido') == 1):
            return redirect('instagram')
        else:
            return render(request, 'index.html')
    
    def post(self, request, *args, **kwargs):
        verificar = usuarios.objects.filter(usuario=request.POST['usuario'], contrasena=request.POST['contrasena']).exists() # Esto lo que hace es verificar que el usuario exista en la base de datos con los parametros que le llego del formulario.
        
        if verificar is True:
            usuario_encontrado = usuarios.objects.get(usuario=request.POST['usuario'], contrasena=request.POST['contrasena']) # Se utiliza para obtener el id del usuario.
            
            # Variables de sesion personalizadas.
            request.session['bienvenido'] = 1
            request.session['usuario_id'] = usuario_encontrado.id
            request.session['usuario'] = request.POST['usuario']
            
            return redirect('instagram')
        else:
            return render(request, 'index.html', {'error' : 'El usuario o la contraseña son incorrectos.'})

class registrarse(TemplateView):
    template_name = 'registrarse.html'
    
    # Verificamos que la variable de sesion bienvenido sea igual a 1. Si es asi, es porque el usuario ya ha iniciado sesion en la plataforma.
    def get(self, request, *args, **kwargs):
        if(request.session.get('bienvenido') == 1):
            return redirect('instagram')
        else:
            return render(request, 'registrarse.html')
    
    def post(self, request, *args, **kwargs):
        if(request.POST['usuario'] == '' or request.POST['correo'] == '' or request.POST['nombre'] == '' or request.POST['contrasena'] == ''):
            return render(request, 'registrarse.html', {'error' : 'Rellene todos los datos requeridos.'})
        else:
            verUsuario = usuarios.objects.filter(usuario=request.POST['usuario']).exists() # Verificamos el usuario para que no vayan a crear duplicados.
            
            if verUsuario is True:
                return render(request, 'registrarse.html', {'error' : 'Lo siento, el usuario ya existe.'})
            else:
                verCorreo = usuarios.objects.filter(correo=request.POST['correo']).exists() # Verificamos el correo para que no vayan a crear duplicados.
                
                if verCorreo is True:
                    return render(request, 'registrarse.html', {'error' : 'Lo siento, el correo ya existe.'})
                else:
                    usuario = usuarios.objects.create(usuario=request.POST['usuario'], correo=request.POST['correo'], nombre_completo=request.POST['nombre'], contrasena=request.POST['contrasena']) # Creamos el usuario con los datos proporcionados en el formulario de registro.
                    
                    # Variables de sesion personalizadas.
                    request.session['bienvenido'] = 1
                    request.session['usuario_id'] = usuario.id
                    request.session['usuario'] = request.POST['usuario']
                    return redirect('instagram')

class instagram(TemplateView):
    template_name = 'instagram.html'
    
    def get(self, request, *args, **kwargs):
        if(request.session.get('bienvenido') != 1):
            return redirect('inicio')
        else:
        
            # Verificamos si tiene publicaciones creadas los usuarios que ha seguido, si no, retornara 0.
            usuarios = seguidores.objects.filter(usuario=request.session['usuario_id']).count()
            
            # Verificamos si tiene publicaciones propias creadas, si no, retornara 0.
            usuario_propio = publicaciones.objects.filter(usuario=request.session['usuario_id']).count()
            
            arreglo_publicaciones = []
            arreglo_likes = []
            arreglo_comentarios = []
            mensaje = []
            arreglo_guardados = []
            
            # Filtrar por fecha hoy - mañana.
            hoy = datetime.now().date()
            manana = hoy + timedelta(1)
            hoy_inicio = datetime.combine(hoy, time())
            hoy_final = datetime.combine(manana, time())
            
            seguir = seguidores.objects.all().filter(usuario=request.session['usuario_id'])
            for seguidor in seguir:
                arreglo_publicaciones.append(seguidor.usuario_seguido.id)
            
            arreglo_publicaciones.append(request.session['usuario_id'])
            noticias = publicaciones.objects.all().filter(usuario__in=arreglo_publicaciones, tipo=1).order_by('-fecha_creacion')
            historias = publicaciones.objects.all().filter(usuario__in=arreglo_publicaciones, tipo=2, fecha_creacion__gte=hoy_inicio, fecha_creacion__lt=hoy_final).order_by('-fecha_creacion')
            for noticia in noticias:
                cantidad_likes = publicaciones_likes.objects.filter(publicacion=noticia.id).count() # Comprobamos si la publicacion por lo menos tiene 1 me gusta.
                if cantidad_likes != 0:
                    mensaje.append([noticia.id, 'Le gusta a:'])
                    obtener_nombres = publicaciones_likes.objects.all().filter(publicacion=noticia.id)
                    for obtener in obtener_nombres:
                        arreglo_likes.append([noticia.id, obtener.usuario.usuario, obtener.usuario.nombre_completo+',', 'color: red'])
                
                    if len(arreglo_likes) != 0:
                        arreglo_likes[-1][2] = arreglo_likes[-1][2][:-1]
                        
                cantidad_comentarios = publicaciones_comentarios.objects.filter(publicacion=noticia.id).count() # Comprobamos si la publicacion por lo menos tiene 1 comentario.
                if cantidad_comentarios != 0:
                    comentarios = publicaciones_comentarios.objects.all().filter(publicacion=noticia.id)
                    for cmt in comentarios:
                        arreglo_comentarios.append([noticia.id, cmt.usuario.usuario, cmt.usuario.nombre_completo, cmt.mensaje, cmt.id])
                        
                cantidad_guardado = publicaciones_archivados.objects.filter(publicacion=noticia.id).count() # Comprobamos si la publicacion esta guardada.
                if cantidad_guardado != 0:
                    obtener_guardados = publicaciones_archivados.objects.all().filter(publicacion=noticia.id)
                    for guardados in obtener_guardados:
                        arreglo_guardados.append([noticia.id, guardados.usuario.usuario, 'color: red'])
            
            return render(request, 'instagram.html', {'usuarios':usuarios, 'usuario_propio':usuario_propio, 'noticias':noticias, 'historias':historias, 'mensaje':mensaje, 'arreglo':arreglo_likes, 'comentarios':arreglo_comentarios, 'guardado':arreglo_guardados})

class perfil(TemplateView):
    template_name = 'perfil.html'
    
    def get(self, request, *args, **kwargs):
        noticias = publicaciones.objects.filter(usuario=request.session['usuario_id'], tipo=1)
        datos = usuarios.objects.filter(id=request.session['usuario_id'])
        cant_publicaciones = publicaciones.objects.filter(usuario=request.session['usuario_id'], tipo=1).count()
        cant_seguidos = seguidores.objects.filter(usuario=request.session['usuario_id']).count()
        cant_seguidores = seguidores.objects.filter(usuario_seguido=request.session['usuario_id']).count()
        
        return render(request, 'perfil.html', {'noticias':noticias, 'datos':datos, 'publicaciones':cant_publicaciones, 'seguidos':cant_seguidos, 'seguidores':cant_seguidores})
    
    def post(self, request, *args, **kwargs):
        verUsuario = usuarios.objects.filter(usuario=request.POST['buscar']).exists() # Verificamos si el usuario existe.
        
        if verUsuario is True:
            usuario_encontrado = usuarios.objects.get(usuario=request.POST['buscar']) # Se utiliza para obtener el id del usuario.
            noticias = publicaciones.objects.filter(usuario=usuario_encontrado.id, tipo=1)
            datos = usuarios.objects.filter(id=usuario_encontrado.id)
            cant_publicaciones = publicaciones.objects.filter(usuario=usuario_encontrado.id, tipo=1).count()
            cant_seguidos = seguidores.objects.filter(usuario=usuario_encontrado.id).count()
            cant_seguidores = seguidores.objects.filter(usuario_seguido=usuario_encontrado.id).count()
            
            # Verificamos si el usuario activo lo esta siguiendo, si no, retornara 0.
            siguiendo = seguidores.objects.filter(usuario=request.session['usuario_id'], usuario_seguido=usuario_encontrado.id).count()
            
            return render(request, 'perfil.html', {'noticias':noticias, 'datos':datos, 'publicaciones':cant_publicaciones, 'seguidos':cant_seguidos, 'seguidores':cant_seguidores, 'siguiendo':siguiendo})
        else:
            return redirect('instagram')

class perfil_subir(TemplateView):
    template_name = 'perfil.html'
    
    def post(self, request, *args, **kwargs):
        id = usuarios.objects.get(pk = request.session['usuario_id']) # Obtengo el objeto de Usuario
        
        publicacion = publicaciones.objects.create(usuario=id, imagen=request.FILES['imagen'], mensaje=request.POST['mensaje'], tipo=request.POST['tipo']) # Creamos la publicacion con los datos proporcionados en el formulario de perfil.
        
        return redirect('perfil')

class perfil_editar(TemplateView):
    template_name = 'perfil.html'
    
    def post(self, request, *args, **kwargs):
        id = usuarios.objects.get(id = request.session['usuario_id']) # Obtenemos el usuario al que vamos a modificar.
        id.nombre_completo = request.POST['nombre_completo']
        id.imagen_perfil = request.FILES['imagen_perfil']
        id.save() # Guardamos los datos que modificaremos.
        
        return redirect('perfil')

class seguir(TemplateView):
    template_name = 'perfil.html'
    
    def post(self, request, *args, **kwargs):
        id = usuarios.objects.get(pk = request.session['usuario_id']) # Obtengo el objeto de Usuario
        id_seguido = usuarios.objects.get(pk = request.POST['id']) # Obtengo el objeto de Usuario
        
        existe = seguidores.objects.filter(usuario=id, usuario_seguido=id_seguido).count()
        if existe == 0:
            crear = seguidores.objects.create(usuario=id, usuario_seguido=id_seguido) # Sigue al usuario.
        else:
            borrar = seguidores.objects.get(usuario=id, usuario_seguido=id_seguido) # Deja de seguir al usuario.
            borrar.delete()
        
        # Me hubiese gustado no repetir esta linea de codigo.
        usuario_encontrado = usuarios.objects.get(id=request.POST['id']) # Se utiliza para obtener el id del usuario.
        noticias = publicaciones.objects.filter(usuario=usuario_encontrado.id, tipo=1)
        datos = usuarios.objects.filter(id=usuario_encontrado.id)
        cant_publicaciones = publicaciones.objects.filter(usuario=usuario_encontrado.id, tipo=1).count()
        cant_seguidos = seguidores.objects.filter(usuario=usuario_encontrado.id).count()
        cant_seguidores = seguidores.objects.filter(usuario_seguido=usuario_encontrado.id).count()
        
        # Verificamos si el usuario activo lo esta siguiendo, si no, retornara 0.
        siguiendo = seguidores.objects.filter(usuario=request.session['usuario_id'], usuario_seguido=usuario_encontrado.id).count()
        
        return render(request, 'perfil.html', {'noticias':noticias, 'datos':datos, 'publicaciones':cant_publicaciones, 'seguidos':cant_seguidos, 'seguidores':cant_seguidores, 'siguiendo':siguiendo})

class me_gusta(TemplateView):
    template_name = 'instagram.html'
    
    def get(self, request, *args, **kwargs):
        id_publicacion = publicaciones.objects.get(pk = self.kwargs['id']) # Obtengo el objeto de Publicacion
        id_usuario = usuarios.objects.get(pk = request.session['usuario_id']) # Obtengo el objeto de Usuario
        
        existe = publicaciones_likes.objects.filter(publicacion=id_publicacion, usuario=id_usuario).count()
        if existe == 0:
            crear = publicaciones_likes.objects.create(publicacion=id_publicacion, usuario=id_usuario) # Le da me gusta a la publicacion.
        else:
            borrar = publicaciones_likes.objects.filter(publicacion=id_publicacion, usuario=id_usuario) # Le quita el me gusta a la publicacion.
            borrar.delete()
        
        return redirect('instagram')

class comentarios(TemplateView):
    template_name = 'instagram.html'
    
    def post(self, request, *args, **kwargs):
        id_publicacion = publicaciones.objects.get(pk = request.POST['publicacion']) # Obtengo el objeto de Publicacion
        id_usuario = usuarios.objects.get(pk = request.session['usuario_id']) # Obtengo el objeto de Usuario
        
        if request.POST['comentario'] != '':
            crear = publicaciones_comentarios.objects.create(publicacion=id_publicacion, usuario=id_usuario, mensaje=request.POST['comentario']) # Crear un comentario.
        
        return redirect('instagram')

class borrar_comentarios(TemplateView):
    template_name = 'instagram.html'
    
    def post(self, request, *args, **kwargs):
        borrar = publicaciones_comentarios.objects.filter(id=request.POST['comentario_id']) # Borrar un comentario.
        borrar.delete()
        
        return redirect('instagram')
        
class borrar_publicaciones(TemplateView):
    template_name = 'perfil.html'
    
    def post(self, request, *args, **kwargs):
        borrar = publicaciones.objects.filter(id=request.POST['publicacion_id']) # Borrar una publicacion.
        borrar.delete()
        
        return redirect('perfil')
        
class guardar(TemplateView):
    template_name = 'perfil.html'
    
    def get(self, request, *args, **kwargs):
        id_publicacion = publicaciones.objects.get(pk = self.kwargs['id']) # Obtengo el objeto de Publicacion
        id_usuario = usuarios.objects.get(pk = request.session['usuario_id']) # Obtengo el objeto de Usuario
        
        existe = publicaciones_archivados.objects.filter(publicacion=id_publicacion, usuario=id_usuario).count()
        if existe == 0:
            crear = publicaciones_archivados.objects.create(publicacion=id_publicacion, usuario=id_usuario) # Guarda la publicacion.
        else:
            borrar = publicaciones_archivados.objects.filter(publicacion=id_publicacion, usuario=id_usuario) # Deja de guardar la publicacion.
            borrar.delete()
        
        return redirect('instagram')

class publicaciones_guardadas(TemplateView):
    template_name = 'publicaciones_guardadas.html'
    
    def post(self, request, *args, **kwargs):
        id_usuario = usuarios.objects.get(pk = request.POST['id']) # Obtengo el objeto de Usuario
        
        noticias = publicaciones_archivados.objects.filter(usuario=id_usuario.id)
        datos = usuarios.objects.filter(id=id_usuario.id)
        cant_publicaciones = publicaciones.objects.filter(usuario=id_usuario.id, tipo=1).count()
        cant_seguidos = seguidores.objects.filter(usuario=id_usuario.id).count()
        cant_seguidores = seguidores.objects.filter(usuario_seguido=id_usuario.id).count()
        
        return render(request, 'publicaciones_guardadas.html', {'noticias':noticias, 'datos':datos, 'publicaciones':cant_publicaciones, 'seguidos':cant_seguidos, 'seguidores':cant_seguidores})

class cerrar_sesion(TemplateView):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        # Borramos las variables de sesion que creamos.
        del request.session['bienvenido']
        del request.session['usuario_id']
        del request.session['usuario']
        return render(request, 'index.html')