<?php
	session_start();
	require_once('config.php');
	
	$usuario 	= $_REQUEST['usuario'];
	$clave 		= strtoupper($_REQUEST['clave']);
	$codificar 	= md5($clave);
	
	$consulta 	= mysqli_query($conexion, "SELECT * FROM usuarios WHERE documento = '".$usuario."' AND contrasena = '".$codificar."'");
	$row 		= mysqli_fetch_array($consulta);
	
	if($usuario == $row['documento'] && $codificar == $row['contrasena']){
		$_SESSION['login'] 		= 1;
		$data['validacion'] 	= 'exito';
		$data['mensaje'] 		= "Acceso concedido, ya puede empezar a trabajar con esta plataforma.";
	}else{
		$_SESSION['login'] 		= 0;
		$data['validacion'] 	= 'error';
		$data['mensaje'] 		= "El usuario o la clave ingresada son incorrectos.";
	}
	
	echo json_encode($data);	
?>