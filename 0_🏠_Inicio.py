import streamlit as st
from tools import styles
import random

styles.get_bootstrap_styles()
styles.get_bootstrap_scripts()
styles.load_my_styles()
styles.load_header()


# Frase inicial
st.markdown(
    """
		<h1 class="text-center">
			Talleres<span class='color-yellow'>,</span> conferencias<span class='color-yellow'>,</span> programación<span class='color-yellow'>,</span> Python y más<span class='color-yellow'>...</span>
        </h1>
    """,
	unsafe_allow_html=True
)

col1, col2 = st.columns(2)

st.markdown(
	"""
	<div class="container">
    """,
	unsafe_allow_html=True)
with col1:
	images = [
		'https://i.imgur.com/jAQILyd.jpg',
		'https://i.imgur.com/OVNsYDy.jpg',
		'https://i.imgur.com/EGjQzQY.jpg',
		'https://i.imgur.com/T7pglCl.jpg',
		'https://i.imgur.com/NaAIdil.jpg',
		'https://i.imgur.com/cWjWIBC.jpg',
		'https://i.imgur.com/HQJ6HAQ.jpg',
	]
	st.image(random.choice(images), use_column_width=True)

with col2:
	# Acerca del evento
	st.markdown(
		f"""
			<h2 class="title"> Acerca del evento 🐍</h2>
			<p class="text font-size-large text-start">
				<span class="font-weight-bold">BeePy, es un evento enfocado en talleres de programación</span>, especialmente en Python, diseñados para dar a conocer el potencial de la programación en <span class="font-weight-bold">diversas áreas de la ciencia</span> y ayudar a los estudiantes de la <span class="font-weight-bold">DCI</span> a aplicar lo aprendido en sus respectivos campos científicos. Además, busca difundir la importancia de las <span class="font-weight-bold">ciencias de datos</span> y <span class="font-weight-bold">ciencias computacionales</span> como herramientas para resolver problemas de manera eficiente y accesible. Si gustas, puedes ver estadísticas de los eventos pasados en la sección de <a href="{st.secrets.base_url}/Ediciones_Anteriores" target="_self">estadísticas</a>, tenemos mucho que mejorar, con tu feedback lo lograremos.
			</p>
		""",
		unsafe_allow_html=True)
	

	st.markdown(
		"""
			<h2 class="title"> ¿Cuándo y dónde? 📅</h2>
			<p class="text font-size-large text-start">
				El próximo BeePy se llevará a cabo el <span class="font-weight-bold">sábado 20 de Mayo</span> de 2023, de 9:00 a 18:00 horas, en la mágica y asombrosa <span class="font-weight-bold">DCI</span> (Auditorio y Aula 1 del Edificio G, Salones de cómputo F).
			</p>
		""",
	unsafe_allow_html=True)

st.markdown(
	"""
		</div>
    """,
	unsafe_allow_html=True)

# Register section
st.markdown(
	"""
		<h2 class="title"> Regístrate 📝</h2>
		<p class="text">
			Para participar en el evento, debes registrarte en el siguiente formulario:
		</p>
		<br>
		<div class="text-center">
			<a href="https://forms.gle/HHNswqvHMUgm2zVh6"> <button class="btn" id="register-btn"> Registrarme </button> </a>
		</div>
	""",
	unsafe_allow_html=True)

# Colaboradores
st.markdown("""
<br>
<br>
<br>
	<h2 class="title"> Colaboraciones 🎈</h2>
	<p class="text"> Gracias a las siguientes organizaciones el BeePy es posible </p>
	<br>
""", unsafe_allow_html=True)

st.markdown(
	"""
	<section class="container">
	<div class="row">
		<div class="col-md-4">
			<div class="image-container">
				<img src="https://i.imgur.com/AerZRis.jpg" class="img-fluid" alt="GOLF Logo">
			</div>
			</div>
			<div class="col-md-4">
			<div class="image-container">
				<img src="https://i.imgur.com/3PAleeO.png" class="img-fluid" alt="GitHub Logo">
			</div>
			</div>
			<div class="col-md-4">
			<div class="image-container">
				<img src="https://i.imgur.com/f3TY2Gq.png" class="img-fluid" alt="UG Logo">
			</div>
			</div>
		</div>
	</section>
	""", 
	unsafe_allow_html=True)

# Footer
st.markdown(
	"""
	<div class="footer">
		<p class="text-center">
			Por cierto, esta página está hecha en Python con ayuda de: <a href="http://streamlit.io" target="_blank"> <img src="https://i.imgur.com/iIOA6kU.png" class="footer__img" alt="Streamlit Logo"></a> con ❤️ por <a href="https://github.com/Bubudavid" target="_blank">Bubu</a> para la DCI 🐝
		</p>
	""",
unsafe_allow_html=True)

