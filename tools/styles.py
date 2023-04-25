import streamlit as st

def get_bootstrap_styles():
	st.markdown(
	"""
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
	""",      
	unsafe_allow_html=True,)

	return True

def get_bootstrap_scripts():
	st.markdown(
	"""
		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous" defer></script>
	""",
	unsafe_allow_html=True)


def load_my_styles(style_name = "main"):
	# Read the css file with python
	with open(f"./assets/styles/{style_name}.css") as style_file:
		st.markdown(f'<style>{style_file.read()}</style>', unsafe_allow_html=True)


def load_header():
	# Header
	st.markdown(
		"""
			<img src="https://i.imgur.com/yiaC2Fk.png" class="header__img" alt="Streamlit Logo">
		""", 
		unsafe_allow_html=True
	)