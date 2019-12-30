{% include 'includes/header.php' %}
		{% include 'includes/menu.php' %}
		
		<div class="container">
			<div class="titulo">Panel Administrativo</div>
			<div class="contenido">
				<div class="row">
					<div class="col-md-8 offset-md-2 expandirDiv">
						<form action="{{ url_for('panel') }}" method="post">
							<!-- Usuario -->
							<div class="input-group">
								<div class="input-group-prepend">
									<span class="input-group-text font-weight-bold" style="width: 120px;">Usuario</span>
								</div>
								<input type="text" name="usuario" class="form-control" placeholder="Ingrese su Usuario">
							</div>
							<br/>
							
							<!-- Contrasena -->
							<div class="input-group">
								<div class="input-group-prepend">
									<span class="input-group-text font-weight-bold" style="width: 120px;">Contrase&ntilde;a</span>
								</div>
								<input type="password" name="clave" class="form-control" placeholder="Ingrese su Contrase&ntilde;a">
							</div>
							<br/>
							
							<!-- Boton para acceder al sistema -->
							<input type="submit" class="btn btn-sm font-weight-bold float-right colorMorado" value="INGRESAR AL SISTEMA">
						</form>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>