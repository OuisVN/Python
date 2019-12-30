{% include 'includes/header.php' %}
		{% include 'includes/menu.php' %}
		
		<div class="container">
			<div class="titulo font-weight-bold"><i class="fas fa-file-csv"></i> CSV Consultas de Informaci&oacute;n</div>
			<div class="contenido">
				<div class="row text-center">
					<div class="col-md-10 offset-md-1">
						<h4>&iquest;Qu&eacute; consulta desea visualizar en CSV?</h4><hr/>
						<table class="table table-bordered text-center" style="width: 100%">
							<tbody>
								<tr>
									<td>
										<form action="{{ url_for('csv_consultas') }}" method="post">
											<input type="hidden" name="valor" value="1">
											<input type="submit" class="btn btn-sm btn-primary blanco" style="width: 300px;" value="Cantidad de Pokémones x Cada Tipo">
										</form>
									</td>
									<td>
										<a href="csv_menu" class="btn btn-sm btn-danger blanco sombra font-weight-bold"><i class="fas fa-backward"></i> Regresar</a>
									</td>
								</tr>
								<tr>
									<td>
										<form action="{{ url_for('csv_consultas') }}" method="post">
											<input type="hidden" name="valor" value="2">
											<input type="submit" class="btn btn-sm btn-primary blanco" style="width: 300px;" value="Ranking Pokémones x Velocidad">
										</form>
									</td>
									<td></td>
								</tr>
								<tr>
									<td>
										<form action="{{ url_for('csv_consultas') }}" method="post">
											<input type="hidden" name="valor" value="3">
											<input type="submit" class="btn btn-sm btn-primary blanco" style="width: 300px;" value="Ranking Pokémones x Ataque">
										</form>
									</td>
									<td></td>
								</tr>
								<tr>
									<td>
										<form action="{{ url_for('csv_consultas') }}" method="post">
											<input type="hidden" name="valor" value="4">
											<input type="submit" class="btn btn-sm btn-primary blanco" style="width: 300px;" value="Lista de Pokémones Ascendente">
										</form>
									</td>
									<td></td>
								</tr>
								<tr>
									<td>
										<form action="{{ url_for('csv_consultas') }}" method="post">
											<input type="hidden" name="valor" value="5">
											<input type="submit" class="btn btn-sm btn-primary blanco" style="width: 300px;" value="Lista de Pokémones Descendente">
										</form>
									</td>
									<td></td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
				<h4>Consultas de Informaci&oacute;n</h4><hr/>
				{% for table in tables %}
					{{ table|safe }}
				{% endfor %}
			</div>
		</div>
	</body>
</html>