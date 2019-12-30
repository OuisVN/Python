{% include 'includes/header.php' %}
		{% include 'includes/menu.php' %}
		
		<div class="container">
			<div class="titulo font-weight-bold"><i class="fas fa-file-csv"></i> CSV Gr&aacute;ficas</div>
			<div class="contenido">
				<div class="row text-center">
					<div class="col-md-10 offset-md-1">
						<table class="table table-bordered text-center" style="width: 100%">
							<tbody>
								<tr>
									<td class="text-right">
										<a href="csv_menu" class="btn btn-sm btn-danger blanco sombra font-weight-bold"><i class="fas fa-backward"></i> Regresar</a>
									</td>
								</tr>
							</tbody>
						</table>
						<h4>Gr&aacute;fica Lineal</h4><hr/>
						<img src="{{url_for('static', filename='images/csv_graficas/lineal.png')}}" /><br/><br/>
						<h4>Gr&aacute;fica de Columnas</h4><hr/>
						<img src="{{url_for('static', filename='images/csv_graficas/columnas.png')}}" /><br/><br/>
						<h4>Gr&aacute;fica de Barras</h4><hr/>
						<img src="{{url_for('static', filename='images/csv_graficas/barras.png')}}" /><br/><br/>
						<h4>Gr&aacute;fica Histograma</h4><hr/>
						<img src="{{url_for('static', filename='images/csv_graficas/histograma.png')}}" /><br/><br/>
						<h4>Gr&aacute;fica de Porcentajes</h4><hr/>
						<img src="{{url_for('static', filename='images/csv_graficas/porcentajes.png')}}" />
						<br/><br/><br/>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>