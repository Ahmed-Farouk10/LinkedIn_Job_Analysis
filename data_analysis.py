import pandas as pd
import numpy as np
from datetime import datetime

# Load the data
df = pd.read_csv('../data/cleaned_jobs_data.csv')

# Basic Analysis
print("\n=== Basic Statistics ===")
print(f"Total Job Postings: {len(df)}")
print(f"Unique Companies: {df['company'].nunique()}")
print(f"Unique Locations: {df['location'].nunique()}")
print(f"Date Range: {df['date_posted'].min()} to {df['date_posted'].max()}")

# Work Type Analysis
print("\n=== Work Type Distribution ===")
work_type_dist = df['work_type'].value_counts()
print(work_type_dist)
print(f"Remote Jobs Percentage: {(work_type_dist.get('1', 0) / len(df) * 100):.2f}%")

# Top Job Titles
print("\n=== Top 10 Job Titles ===")
top_titles = df['title'].value_counts().head(10)
print(top_titles)

# Company Analysis
print("\n=== Top 10 Companies by Job Postings ===")
top_companies = df['company'].value_counts().head(10)
print(top_companies)

# Location Analysis
print("\n=== Top 10 Locations ===")
top_locations = df['location'].value_counts().head(10)
print(top_locations)

# Time Analysis
df['date_posted'] = pd.to_datetime(df['date_posted'])
df['month'] = df['date_posted'].dt.to_period('M')
monthly_trends = df.groupby('month').size()
print("\n=== Monthly Posting Trends ===")
print(monthly_trends)

# Save insights to a markdown file
with open('../reports/data_insights.md', 'w') as f:
    f.write("# LinkedIn Job Market Analysis Insights\n\n")
    
    f.write("## Key Metrics\n")
    f.write(f"- Total Job Postings: {len(df)}\n")
    f.write(f"- Unique Companies: {df['company'].nunique()}\n")
    f.write(f"- Unique Locations: {df['location'].nunique()}\n")
    f.write(f"- Date Range: {df['date_posted'].min()} to {df['date_posted'].max()}\n\n")
    
    f.write("## Work Type Distribution\n")
    f.write("```\n")
    f.write(str(work_type_dist))
    f.write("\n```\n\n")
    
    f.write("## Top 10 Job Titles\n")
    f.write("```\n")
    f.write(str(top_titles))
    f.write("\n```\n\n")
    
    f.write("## Top 10 Companies\n")
    f.write("```\n")
    f.write(str(top_companies))
    f.write("\n```\n\n")
    
    f.write("## Top 10 Locations\n")
    f.write("```\n")
    f.write(str(top_locations))
    f.write("\n```\n\n")
    
    f.write("## Monthly Posting Trends\n")
    f.write("```\n")
    f.write(str(monthly_trends))
    f.write("\n```\n")

print("\nAnalysis complete! Insights saved to reports/data_insights.md") 