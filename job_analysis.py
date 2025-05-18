import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the data file
data_path = os.path.join(os.path.dirname(script_dir), 'data', 'clean_jobs.csv')

# Load the data
df = pd.read_csv(data_path)

# Data preprocessing
df['date_posted'] = pd.to_datetime(df['date_posted'])
df['month_posted'] = df['date_posted'].dt.to_period('M')

# 1. Most in-demand job titles
def get_top_job_titles(df, n=10):
    return df['title'].value_counts().head(n)

# 2. Remote vs Onsite jobs
def get_work_type_distribution(df):
    return df['work_type'].value_counts()

# 3. Company-wise job posting frequency
def get_company_postings(df, n=10):
    return df['company'].value_counts().head(n)

# 4. Location-wise distribution
def get_location_distribution(df, n=10):
    return df['location'].value_counts().head(n)

# Create interactive dashboard
def create_dashboard():
    # Create subplot layout
    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=(
            'Top 10 Job Titles',
            'Remote vs Onsite Jobs',
            'Top Companies by Job Postings',
            'Job Distribution by Location',
            'Monthly Job Posting Trends',
            'Employment Type Distribution'
        ),
        specs=[
            [{"type": "bar"}, {"type": "pie"}],
            [{"type": "bar"}, {"type": "bar"}],
            [{"type": "scatter", "colspan": 2}, None]
        ]
    )

    # 1. Top Job Titles
    top_titles = get_top_job_titles(df)
    fig.add_trace(
        go.Bar(x=top_titles.index, y=top_titles.values, name="Job Titles"),
        row=1, col=1
    )

    # 2. Remote vs Onsite
    work_type_dist = get_work_type_distribution(df)
    fig.add_trace(
        go.Pie(labels=work_type_dist.index, values=work_type_dist.values, name="Work Type"),
        row=1, col=2
    )

    # 3. Company Postings
    company_postings = get_company_postings(df)
    fig.add_trace(
        go.Bar(x=company_postings.index, y=company_postings.values, name="Companies"),
        row=2, col=1
    )

    # 4. Location Distribution
    location_dist = get_location_distribution(df)
    fig.add_trace(
        go.Bar(x=location_dist.index, y=location_dist.values, name="Locations"),
        row=2, col=2
    )

    # 5. Monthly Trends
    monthly_trends = df.groupby('month_posted').size()
    fig.add_trace(
        go.Scatter(x=monthly_trends.index.astype(str), y=monthly_trends.values, name="Monthly Trends"),
        row=3, col=1
    )

    # Update layout
    fig.update_layout(
        height=1200,
        width=1200,
        title_text="LinkedIn Job Market Analysis Dashboard",
        showlegend=True,
        template="plotly_white"
    )

    # Save the dashboard
    reports_dir = os.path.join(os.path.dirname(script_dir), 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    fig.write_html(os.path.join(reports_dir, "job_analysis_dashboard.html"))

if __name__ == "__main__":
    create_dashboard()
    print("Dashboard has been created and saved to reports/job_analysis_dashboard.html") 