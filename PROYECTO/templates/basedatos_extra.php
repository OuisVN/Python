{% include 'includes/header.php' %}
		{% include 'includes/menu.php' %}
		
		<div class="container">
			<div class="titulo font-weight-bold"><i class="fas fa-folder-open"></i> Base de Datos Consultas Propia</div>
			<div class="contenido">
				<div class="row text-center">
					<div class="col-md-10 offset-md-1">
						<h4>&iquest;Qu&eacute; consulta desea crear en Base de Datos?</h4><hr/>
						<i>Campos que acepta por el momento: <b>Total, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed</b></i>
						<table class="table table-bordered text-center" style="width: 100%">
							<tbody>
								<tr>
									<td>
										<form action="{{ url_for('basedatos_extra') }}" method="post">
											<textarea name="valor" class="form-control form-control-sm contenido" style="resize: none;" placeholder="Escribe aqui tu consulta"></textarea>
											<input type="submit" class="btn btn-sm btn-primary blanco" value="Enviar Consulta">
										</form>
									</td>
									<td>
										<a href="basedatos_menu" class="btn btn-sm btn-danger blanco sombra font-weight-bold"><i class="fas fa-backward"></i> Regresar</a>
									</td>
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