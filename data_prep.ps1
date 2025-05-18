# scripts/data_prep.ps1
$inputPath = "..\data\clean_jobs.csv"
$outputPath = "..\data\cleaned_jobs_data.csv"
$data = Import-Csv -Path $inputPath

function Expand-Rows { param ([PSCustomObject]$row)
    $totalRows = 100
    # Extract percentage from title if present
    if ($row.title -match '(\d+)%') {
        $percent = [int]$matches[1]
        $count = [math]::Round($percent / 100 * $totalRows)
        $result = @()
        for ($i = 0; $i -lt $count; $i++) {
            $newRow = [PSCustomObject]@{
                id = $row.id; title = ($row.title -replace '\d+%', '').Trim()
                company = $row.company; location = $row.location
                link = $row.link; source = $row.source
                date_posted = $row.date_posted; work_type = $row.work_type
                employment_type = $row.employment_type; description = $row.description
            }
            $result += $newRow
        }
        return $result
    } else {
        return $row
    }
}

$expandedData = @()
foreach ($row in $data) {
    if ($row.title -match '%') { $expandedData += Expand-Rows -row $row }
    else { $expandedData += $row }
}
$expandedData | Export-Csv -Path $outputPath -NoTypeInformation
Write-Host "Processed data saved to $outputPath"

