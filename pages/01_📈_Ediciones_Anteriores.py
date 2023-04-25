import streamlit as st
from tools import styles
from tools.tools import get_data
import plotly.graph_objects as go
import plotly.express as px


# Load styles
styles.get_bootstrap_styles()
styles.load_my_styles('past')
# Getting airtable data
data = get_data()

st.markdown("# Información de BeePy 2.0 🐝")
st.markdown("### 19 Noviembre 2022")

st.image('https://i.imgur.com/03TYRbN.jpg', use_column_width=True)


col1, col2, col3 = st.columns(3)

with col1:
	st.markdown(f"""
		<div class="card">
			<p class="card__number">+{len(data.index)}</p>
			<p class="card__title">Asistentes</p>
		</div>
	""", unsafe_allow_html=True)


with col2:
	st.markdown(f"""
		<div class="card">
			<p class="card__number">6</p>
			<p class="card__title">Talleres</p>
		</div>
	""", unsafe_allow_html=True)

with col3:
	st.markdown(f"""
		<div class="card">
			<p class="card__number">+10</p>
			<p class="card__title">Premios</p>
		</div>
	""", unsafe_allow_html=True)

colors = {
	'Femenino': '#FFC107',
	'Masculino': '#3979AA',
	'No binario': 'darkorange',
	'Prefiero no decirlo': 'pink'
}

# Gender section
st.markdown("## Distribución de género")
gender_count = data['gender'].value_counts()
# Create a donut chart using Plotly
fig = go.Figure(data=[go.Pie(
	labels = gender_count.index,
	values = gender_count.values,
	hole=0.3,
	textinfo='label+value',
	hoverinfo='label',
	marker=dict(colors=list(colors.values()), line=dict(color='gray', width=1)),
)])

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)


# Semester section
# Group the data by semester and gender and count the number of students
semester_gender = data.groupby(["semester", "gender"]).size().reset_index(name="count")

# Create a list of bar traces for each gender
bar_traces = []
for gender in colors:
    filtered_df = semester_gender[semester_gender["gender"] == gender]
    trace = go.Bar(
        x=filtered_df["semester"],
        y=filtered_df["count"],
        name=gender,
        marker_color=colors[gender]
    )
    bar_traces.append(trace)

# Create the layout for the plot
layout = go.Layout(
    title="Número de estudiantes por semestre y género",
    xaxis=dict(title="Semestre"),
    yaxis=dict(title="Número de estudiantes"),
    barmode="stack",
)

# Combine the bar traces and layout into a figure
fig = go.Figure(data=bar_traces, layout=layout)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Career section
st.markdown("## Distribución de carreras")
career_count = data['career'].value_counts()
# Create a donut chart using Plotly
fig = go.Figure(data=[go.Pie(
	labels = career_count.index,
	values = career_count.values,
	hole=0.3,
	textinfo='label+value',
	hoverinfo='label',
	marker=dict(colors=list(colors.values()), line=dict(color='gray', width=1)),
)])

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)


# Programming knowledge section
st.markdown("## Distribución de conocimiento en programación")

fig = go.Figure(data=[go.Bar(
	x = data['programming_level'].value_counts().index,
	y = data['programming_level'].value_counts().values,
	text = data['programming_level'].value_counts().values,
	textposition='auto',
	marker_color = '#FFC107'
)], layout = go.Layout(
	title="Nivel de conocimiento en programación",
	xaxis=dict(title="Nivel"),
	yaxis=dict(title="Número de estudiantes"),
))
st.plotly_chart(fig, use_container_width=True)
