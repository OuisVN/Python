{% include 'includes/header.php' %}
		{% include 'includes/menu.php' %}
		
		<div class="container">
			<div class="titulo">Qui&eacute;nes S&oacute;mos</div>
			<div class="contenido">
				{% if session['usuario'] is defined %}
					<form action="{{ url_for('informacion') }}" method="post">
						<div class="row">
							<div class="col-md-1"></div>
							<div class="col-md-6 expandirDiv">
								<span class="font-weight-bold">Qui&eacute;nes S&oacute;mos</span><hr/>
								<textarea name="info" class="form-control form-control-sm" style="height:200px;">{{ informacion[0] }}</textarea>
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
							<span class="font-weight-bold">Qui&eacute;nes S&oacute;mos</span><hr/>
							{{ informacion[0] }}<br/><br/>
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