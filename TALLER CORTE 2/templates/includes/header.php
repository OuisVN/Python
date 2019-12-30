<!DOCTYPE html>
<html lang="es">
	<head>
		<!-- METADATOS -->
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<meta name="author" content="Juan David, Jhonattan Bedoya, Natalia Isaza">
		<meta name="description" content="Taller - 2do Corte">
		
		<!-- TITULO -->
		<title>Taller - 2do Corte</title>
		
		<!-- HOJAS DE ESTILO -->
		<link rel="icon" type="image/png" href="{{url_for('static', filename='images/index/favicon.png')}}" />
		<link rel="stylesheet" type="text/css" href="{{url_for('static', filename='css/bootstrap.css')}}" />
		<link rel="stylesheet" type="text/css" href="{{url_for('static', filename='css/bootstrap.datatables.css')}}" />
		<link rel="stylesheet" type="text/css" href="{{url_for('static', filename='css/sweetalert.css')}}" />
		<link rel="stylesheet" type="text/css" href="{{url_for('static', filename='css/importante.css')}}" />
		<link rel="stylesheet" type="text/css" href="{{url_for('static', filename='css/estilos.css')}}" />
		<link rel="stylesheet" type="text/css" href="{{url_for('static', filename='css/chosen.css')}}" />
		
		<!-- SCRIPTS NECESARIOS -->
		<script type="text/javascript" src="{{url_for('static', filename='js/jquery.js')}}"></script>
		<script type="text/javascript" src="{{url_for('static', filename='js/popper.js')}}"></script>
		<script type="text/javascript" src="{{url_for('static', filename='js/bootstrap.js')}}"></script>
		<script type="text/javascript" src="{{url_for('static', filename='js/jquery.datatables.js')}}"></script>
		<script type="text/javascript" src="{{url_for('static', filename='js/bootstrap.datatables.js')}}"></script>
		<script type="text/javascript" src="{{url_for('static', filename='js/fontawesome.js')}}"></script>
		<script type="text/javascript" src="{{url_for('static', filename='js/sweetalert.js')}}"></script>
		<!-- OTROS SCRIPTS -->
		<script type="text/javascript">$(document).ready(function(){ $('#tabla').DataTable({ "order": []});});</script>
		<script type="text/javascript">$(function(){ $('[data-toggle="tooltip"]').tooltip() });</script>
	</head>
	<body class="fuentePrincipal">