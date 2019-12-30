{% include 'includes/header.php' %}
		{% include 'includes/menu.php' %}
		
		<div class="container">
			<div class="titulo font-weight-bold"><i class="fas fa-folder-open"></i> Base de Datos Procesos de Limpieza</div>
			<div class="contenido">
				<div class="row text-center">
					<div class="col-md-10 offset-md-1">
						<h4>&iquest;Qu&eacute; procesos de limpieza desea realizar en Base de Datos?</h4><hr/>
						<table class="table table-bordered text-center" style="width: 100%">
							<tbody>
								<tr>
									<td>
										<form action="{{ url_for('basedatos_procesos') }}" method="post">
											<input type="hidden" name="valor" value="1">
											<input type="submit" class="btn btn-sm btn-primary blanco" style="width: 300px;" value="Inicializar desde 1">
										</form>
									</td>
									<td>
										<a href="basedatos_menu" class="btn btn-sm btn-danger blanco sombra font-weight-bold"><i class="fas fa-backward"></i> Regresar</a>
									</td>
								</tr>
								<tr>
									<td>
										<form action="{{ url_for('basedatos_procesos') }}" method="post">
											<input type="hidden" name="valor" value="2">
											<input type="submit" class="btn btn-sm btn-primary blanco" style="width: 300px;" value="Retirar Pokémones Repetidos">
										</form>
									</td>
									<td></td>
								</tr>
								<tr>
									<td>
										<form action="{{ url_for('basedatos_procesos') }}" method="post">
											<input type="hidden" name="valor" value="3">
											<input type="submit" class="btn btn-sm btn-primary blanco" style="width: 300px;" value="Convertir Columna # en Numerica">
										</form>
									</td>
									<td></td>
								</tr>
								<tr>
									<td>
										<form action="{{ url_for('basedatos_procesos') }}" method="post">
											<input type="hidden" name="valor" value="4">
											<input type="submit" class="btn btn-sm btn-primary blanco" style="width: 300px;" value="Convertir Todo Entero en Decimal">
										</form>
									</td>
									<td></td>
								</tr>
								<tr>
									<td>
										<form action="{{ url_for('basedatos_procesos') }}" method="post">
											<input type="hidden" name="valor" value="5">
											<input type="submit" class="btn btn-sm btn-primary blanco" style="width: 300px;" value="Agrupar por Tipo de Pokémon">
										</form>
									</td>
									<td></td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
				<h4>Resultado de Proceso de Limpieza</h4><hr/>
				{% for table in tables %}
					{{ table|safe }}
				{% endfor %}
			</div>
		</div>
	</body>
</html>