$(document).on("click", ".imagen", function(e){
	var perfil 	= $(this).data("perfil");
	var imagen 	= $(this).data("imagen");
	var mensaje = $(this).data("mensaje");
	var nombre 	= $(this).data("nombre");
	
	$("#perfil").attr("src", perfil);
	$("#historia").attr("src", imagen);
	$("#mensaje").html(mensaje);
	$("#nombre").html(nombre);
});