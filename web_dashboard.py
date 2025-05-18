import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import numpy as np

# Set page config
st.set_page_config(
    page_title="LinkedIn Job Market Analysis",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF;
    }
    .stMetric {
        background-color: #F8F9FA;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stMetric label {
        color: #0077B5;
        font-weight: bold;
    }
    h1 {
        color: #0077B5;
    }
    </style>
    """, unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/cleaned_jobs_data.csv')
    df['date_posted'] = pd.to_datetime(df['date_posted'])
    return df

df = load_data()

# Header
st.title("LinkedIn Job Market Analysis 2025")
st.markdown("---")

# KPI Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Job Postings", len(df))
with col2:
    st.metric("Unique Companies", df['company'].nunique())
with col3:
    st.metric("Unique Locations", df['location'].nunique())

# Main Content
st.markdown("## Market Overview")

# Top Job Titles
st.subheader("Top 10 Job Titles")
top_titles = df['title'].value_counts().head(10)
fig_titles = px.bar(
    top_titles,
    title="Most In-Demand Job Titles",
    labels={'value': 'Number of Postings', 'title': 'Job Title'},
    color=top_titles.values,
    color_continuous_scale='Blues'
)
fig_titles.update_layout(
    showlegend=False,
    plot_bgcolor='white',
    height=400
)
st.plotly_chart(fig_titles, use_container_width=True)

# Company Distribution
st.subheader("Top Companies by Job Postings")
top_companies = df['company'].value_counts().head(10)
fig_companies = px.bar(
    top_companies,
    title="Companies with Most Job Postings",
    labels={'value': 'Number of Postings', 'company': 'Company'},
    color=top_companies.values,
    color_continuous_scale='Blues'
)
fig_companies.update_layout(
    showlegend=False,
    plot_bgcolor='white',
    height=400
)
st.plotly_chart(fig_companies, use_container_width=True)

# Location Analysis
st.subheader("Job Distribution by Location")
top_locations = df['location'].value_counts().head(10)
fig_locations = px.bar(
    top_locations,
    title="Top Locations for Job Postings",
    labels={'value': 'Number of Postings', 'location': 'Location'},
    color=top_locations.values,
    color_continuous_scale='Blues'
)
fig_locations.update_layout(
    showlegend=False,
    plot_bgcolor='white',
    height=400
)
st.plotly_chart(fig_locations, use_container_width=True)

# Work Type Distribution
st.subheader("Work Type Distribution")
work_type_dist = df['work_type'].value_counts()
fig_work_type = px.pie(
    values=work_type_dist.values,
    names=work_type_dist.index,
    title="Distribution of Work Types",
    color_discrete_sequence=px.colors.sequential.Blues_r
)
fig_work_type.update_layout(
    plot_bgcolor='white',
    height=400
)
st.plotly_chart(fig_work_type, use_container_width=True)

# Time Analysis
st.subheader("Job Posting Trends")
daily_postings = df.groupby('date_posted').size().reset_index(name='count')
fig_trend = px.line(
    daily_postings,
    x='date_posted',
    y='count',
    title="Daily Job Posting Trends",
    labels={'count': 'Number of Postings', 'date_posted': 'Date'},
    color_discrete_sequence=['#0077B5']
)
fig_trend.update_layout(
    plot_bgcolor='white',
    height=400
)
st.plotly_chart(fig_trend, use_container_width=True)

# Interactive Filters
st.sidebar.title("Filters")
st.sidebar.markdown("---")

# Location Filter
selected_locations = st.sidebar.multiselect(
    "Select Locations",
    options=df['location'].unique(),
    default=[]
)

# Company Filter
selected_companies = st.sidebar.multiselect(
    "Select Companies",
    options=df['company'].unique(),
    default=[]
)

# Work Type Filter
selected_work_types = st.sidebar.multiselect(
    "Select Work Types",
    options=df['work_type'].unique(),
    default=[]
)

# Apply Filters
if selected_locations:
    df = df[df['location'].isin(selected_locations)]
if selected_companies:
    df = df[df['company'].isin(selected_companies)]
if selected_work_types:
    df = df[df['work_type'].isin(selected_work_types)]

# Data Table
st.markdown("## Detailed Job Data")
st.dataframe(
    df[['title', 'company', 'location', 'work_type', 'date_posted']].sort_values('date_posted', ascending=False),
    use_container_width=True
)

# Footer
st.markdown("---")
st.markdown("Data last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 