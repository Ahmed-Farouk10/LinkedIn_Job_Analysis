# LinkedIn Job Market Analysis

## Project Overview
Analysis of LinkedIn job postings data to uncover job market trends, in-demand skills, and hiring patterns. This project includes data processing, analysis, and visualization using Power BI.

## Project Structure
```
LinkedIn_Job_Market_Analysis/
├── data/
│   ├── raw/clean_jobs.csv
│   ├── processed/cleaned_jobs_data.csv
├── scripts/
│   ├── data_cleaning.pq
│   ├── dax_measures.dax
│   ├── data_prep.ps1
├── reports/
│   ├── LinkedIn_Job_Market_2025.pbix
│   ├── documentation/dashboard_user_guide.md
├── assets/
│   ├── templates/power_bi_theme.json
└── README.md
```

## Setup Instructions

1. **Data Preparation**
   ```powershell
   cd scripts
   .\data_prep.ps1
   ```

2. **Power BI Setup**
   - Open Power BI Desktop
   - Import cleaned_jobs_data.csv
   - Apply LinkedInTheme from assets/templates/power_bi_theme.json
   - Copy DAX measures from scripts/dax_measures.dax

3. **Dashboard Creation**
   - Follow layout in dashboard_user_guide.md
   - Set canvas size to 1280x720
   - Apply theme and measures
   - Create drill-through and drill-down features

## Features
- Interactive dashboard with drill-through capabilities
- Location-based analysis with drill-down
- Remote vs. Onsite job distribution
- Company-wise job posting analysis
- Top job titles and skills analysis

## Requirements
- Power BI Desktop
- Python 3.x
- PowerShell

## Timeline
- Project Start: [Start Date]
- Submission Deadline: May 18, 2025, 11 PM EEST

## Contact
For questions or support, please contact: [Your Contact Information]