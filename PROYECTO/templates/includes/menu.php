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
						<li class="nav-item">
							<div class="nav-link text-center">
								<a href="csv_menu" class="font-weight-bold blanco"><i class="fas fa-file-csv"></i> CSV, Excel</a>
							</div>
						</li>
						<li class="nav-item">
							<div class="nav-link text-center">
								<a href="basedatos_menu" class="font-weight-bold blanco"><i class="fas fa-folder-open"></i> Base de Datos</a>
							</div>
						</li>
						<li class="nav-item">
							<div class="nav-link text-center">
								<a href="webscraper_menu" class="font-weight-bold blanco"><i class="fas fa-search"></i> Web Scraper</a>
							</div>
						</li>
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