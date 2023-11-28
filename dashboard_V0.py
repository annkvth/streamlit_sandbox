# Import libraries
import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Create Data
x = np.arange(-10,10,.01)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

function_dict = {
    'Sin': y1,
    'Cos': y2,
    'Tan': y3
}

# Streamlit App
st.title('My first Dashboard')

# Dropdown: Select Function
select_function = st.selectbox('Select Function', list(function_dict.keys()))

# Create Plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=function_dict[select_function], mode='lines', name=select_function))
st.plotly_chart(fig)