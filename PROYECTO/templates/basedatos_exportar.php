{% include 'includes/header.php' %}
		{% include 'includes/menu.php' %}
		
		<div class="container">
			<div class="titulo font-weight-bold"><i class="fas fa-folder-open"></i> Base de Datos Exportar</div>
			<div class="contenido">
				<div class="row text-center">
					<div class="col-md-10 offset-md-1">
						<h4>&iquest;En qu&eacute; formato desea descargar la Base de Datos?</h4><hr/>
						<table class="table table-bordered text-center" style="width: 100%">
							<tbody>
								<tr>
									<td>
										<form action="{{ url_for('basedatos_exportar') }}" method="post">
											<input type="hidden" name="valor" value="1">
											<input type="submit" class="btn btn-sm btn-primary blanco" value="Exportar como CSV">
										</form>
									</td>
									<td>
										<form action="{{ url_for('basedatos_exportar') }}" method="post">
											<input type="hidden" name="valor" value="2">
											<input type="submit" class="btn btn-sm btn-primary blanco" value="Exportar como EXCEL">
										</form>
									</td>
									<td>
										<a href="basedatos_menu" class="btn btn-sm btn-danger blanco sombra font-weight-bold"><i class="fas fa-backward"></i> Regresar</a>
									</td>
								</tr>
							</tbody>
						</table>
						<br/><br/><br/>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>