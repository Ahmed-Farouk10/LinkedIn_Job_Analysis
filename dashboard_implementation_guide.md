# LinkedIn Job Market Analysis Dashboard Implementation Guide

## 1. Data Import
1. Open Power BI Desktop
2. Click "Get Data" > "Text/CSV"
3. Navigate to and select `data/cleaned_jobs_data.csv`
4. Click "Load"

## 2. Apply Theme
1. Go to "View" > "Themes"
2. Click "Browse for themes"
3. Select `assets/templates/power_bi_theme.json`
4. Click "Open"

## 3. Create Measures
1. Open the DAX file at `scripts/dax_measures.dax`
2. Copy each measure
3. In Power BI, right-click on the table and select "New measure"
4. Paste and create each measure

## 4. Dashboard Layout

### Header Section
1. Add a text box with title "LinkedIn Job Market Analysis 2025"
2. Create three KPI cards:
   - Total Postings
   - Unique Companies
   - Unique Locations

### Main Visualizations
1. **Top Job Titles (Bar Chart)**
   - Add a bar chart
   - Axis: title
   - Values: Total Postings
   - Sort by Total Postings (descending)
   - Limit to top 10

2. **Company Distribution (Bar Chart)**
   - Add a bar chart
   - Axis: company
   - Values: Total Postings
   - Sort by Total Postings (descending)
   - Limit to top 10

3. **Location Map**
   - Add a map visual
   - Location: location
   - Size: Total Postings
   - Color: Total Postings

4. **Work Type Distribution (Donut Chart)**
   - Add a donut chart
   - Legend: work_type
   - Values: Total Postings

### Filters
1. Add slicers for:
   - Location
   - Company
   - Work Type
   - Date Posted

## 5. Formatting Guidelines

### Colors
- Primary: #0077B5 (LinkedIn Blue)
- Secondary: #00A0DC (Light Blue)
- Background: #FFFFFF (White)
- Text: #000000 (Black)

### Typography
- Font Family: Segoe UI
- Headers: 14pt, SemiBold
- Body: 12pt, Regular
- KPI Values: 24pt, Bold

### Layout
- Canvas Size: 1280x720 pixels
- Margins: 20px
- Padding between visuals: 10px

## 6. Interactivity
1. Enable cross-filtering between all visuals
2. Add drill-through from location map to detailed location view
3. Enable tooltips with additional metrics
4. Add bookmarks for different views

## 7. Performance Optimization
1. Remove unused columns
2. Use calculated columns sparingly
3. Optimize DAX measures
4. Enable data reduction where appropriate

## 8. Final Steps
1. Save the .pbix file
2. Test all interactions
3. Verify data refresh
4. Create documentation

## 9. Publishing
1. Click "Publish" to Power BI Service
2. Set up scheduled refresh
3. Share with stakeholders
4. Set up appropriate permissions

## 10. Maintenance
1. Monitor performance
2. Update data source as needed
3. Review and update measures
4. Gather user feedback 