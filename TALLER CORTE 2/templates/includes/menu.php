		<nav class="navbar navbar-expand-lg fixed-top menu sombra">
			<div class="container-fluid">
				<button type="button" class="navbar-toggler navbar-toggler-right" data-toggle="collapse" data-target="#navbar">
					<span class="fas fa-align-center blanco"></span>
				</button>
				<div class="collapse navbar-collapse" id="navbar">
					<ul class="navbar-nav">
						<li class="nav-item">
							<div class="nav-link text-center">
								<a href="/" class="font-weight-bold blanco"><i class="fas fa-home"></i> Inicio</a>
							</div>
						</li>
					</ul>
					<ul class="navbar-nav ml-auto">
						<li class="nav-item">
							<div class="nav-link text-center">
								<a href="informacion" class="font-weight-bold blanco"><i class="fas fa-box"></i> Qui&eacute;nes S&oacute;mos</a>
							</div>
						</li>
						<li class="nav-item">
							<div class="nav-link text-center">
								<a href="productos" class="font-weight-bold blanco"><i class="fas fa-box"></i> Productos y Servicios</a>
							</div>
						</li>
						<li class="nav-item">
							<div class="nav-link text-center">
								<a href="contacto" class="font-weight-bold blanco"><i class="fas fa-box"></i> Contacto</a>
							</div>
						</li>
					</ul>
					<ul class="navbar-nav ml-auto">
						{% if session['usuario'] is defined %}
							<li class="nav-item">
								<div class="nav-link text-center">
									<a href="logout" class="font-weight-bold blanco">{{session['usuario']}}</a>
								</div>
							</li>
						{% else %}
							<li class="nav-item">
								<div class="nav-link text-center">
									<a href="panel" class="font-weight-bold blanco"><i class="fas fa-box"></i> Admin</a>
								</div>
							</li>
						{% endif %}
					</ul>
				</div>
			</div>
		</nav>
		<br/><br/><br/><br/>
		{% with mensajes = get_flashed_messages(with_categories=True) %}
			{% if mensajes %}
				{% for categoria, mensaje in mensajes %}
					<script type="text/javascript">
						swal({
							title: "",
							text: "{{mensaje}}",
							timer: 2000,
							type: "{{categoria}}",
							showConfirmButton: false
						});
					</script>
				{% endfor%}
			{% endif %}
		{% endwith %}