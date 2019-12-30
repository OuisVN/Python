{% include 'includes/header.php' %}
		{% include 'includes/menu.php' %}
		
		<div class="container">
			<div class="titulo">&Aacute;rea de Contacto</div>
			<div class="contenido">
				{% if session['usuario'] is defined %}
					<form action="{{ url_for('contacto') }}" method="post">
						<div class="row">
							<div class="col-md-1"></div>
							<div class="col-md-6 expandirDiv">
								<span class="font-weight-bold">&Aacute;rea de Contacto</span><hr/>
								<i class="fas fa-at colorNaranja"></i> <b>Correo Electr&oacute;nico:</b>
								<input name="correo" class="form-control form-control-sm" value="{{ informacion[0] }}">
								<i class="fas fa-phone colorNaranja"></i> <b>Tel&eacute;fono:</b>
								<input name="telefono" class="form-control form-control-sm" value="{{ informacion[1] }}">
								<i class="fas fa-mobile colorNaranja"></i> <b>Celular:</b>
								<input name="celular" class="form-control form-control-sm" value="{{ informacion[2] }}">
								<i class="fas fa-map-marked-alt colorNaranja"></i> <b>Direcci&oacute;n:</b>
								<input name="direccion" class="form-control form-control-sm" value="{{ informacion[3] }}">
							</div>
							<div class="col-md-4">
								<img class="zoom" src="{{url_for('static', filename='images/index/pentagram.png')}}" width="256" height="auto" />
							</div>
							<div class="col-md-1"></div>
							
							<div class="col-md-1"></div>
							<div class="col-md-4">
								<input type="submit" class="btn btn-sm font-weight-bold float-right colorMorado" value="MODIFICAR INFORMACION">
							</div>
							<div class="col-md-7"></div>
						</div>
					</form>
				{% else %}
					<div class="row">
						<div class="col-md-1"></div>
						<div class="col-md-6 expandirDiv">
							<span class="font-weight-bold">&Aacute;rea de Contacto</span><hr/>
							<i class="fas fa-at colorNaranja"></i> <b>Correo Electr&oacute;nico:</b> {{ informacion[0] }}<br/>
							<i class="fas fa-phone colorNaranja"></i> <b>Tel&eacute;fono:</b> {{ informacion[1] }}<br/>
							<i class="fas fa-mobile colorNaranja"></i> <b>Celular:</b> {{ informacion[2] }}<br/>
							<i class="fas fa-map-marked-alt colorNaranja"></i> <b>Direcci&oacute;n:</b> {{ informacion[3] }}<br/><br/>
						</div>
						<div class="col-md-4">
							<img class="zoom" src="{{url_for('static', filename='images/index/pentagram.png')}}" width="256" height="auto" />
						</div>
						<div class="col-md-1"></div>
					</div>
				{% endif %}
			</div>
		</div>
	</body>
</html>