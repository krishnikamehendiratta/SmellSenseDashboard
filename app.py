import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Smell Sense Dashboard", page_icon="🫁")

st.title("🫁 Smell Sense Dashboard")
st.subheader("Simulating VOC Breath Signatures")

st.write("Adjust the VOC levels and see the breath fingerprint.")

# VOC sliders
voc_list = {
    "Acetone": 1.0,
    "Benzene": 1.0,
    "Ethanol": 1.0,
    "Toluene": 1.0,
    "Ammonia": 1.0
}

st.sidebar.header("VOC Controls")

for voc in voc_list:
    voc_list[voc] = st.sidebar.slider(voc, 0.0, 5.0, 1.0)

# Radar chart
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=list(voc_list.values()),
    theta=list(voc_list.keys()),
    fill='toself',
    name='Breath VOC Profile'
))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
    showlegend=False
)

st.plotly_chart(fig)

# Interpretation
avg_voc = sum(voc_list.values()) / len(voc_list)

if avg_voc < 2:
    st.success("Breath Signature: Looks generally normal 💛")
elif avg_voc < 3.5:
    st.warning("Breath Signature: Some anomalies detected 🔎")
else:
    st.error("Breath Signature: High VOC pattern — further investigation needed 🫁")
