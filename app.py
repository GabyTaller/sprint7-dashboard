import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Dashboard de anuncios de venta de coches')

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Distribución del kilometraje')

    fig = px.histogram(
        car_data,
        x='odometer',
        title='Distribución del kilometraje'
    )

    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Relación entre precio y kilometraje')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Precio vs. Kilometraje'
    )

    st.plotly_chart(fig, use_container_width=True)