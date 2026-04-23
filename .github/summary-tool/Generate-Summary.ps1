<#
.SYNOPSIS
    MyNotes Summary Generator

.DESCRIPTION
    Scans MyNotes project for Markdown files and generates a SUMMARY.md file.

.EXAMPLE
    .\Generate-Summary.ps1

.NOTES
    Author: AI Assistant
    Version: 1.0
    Date: 2026-04-23
#>

# Project root directory
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$SummaryFile = Join-Path -Path $ProjectRoot -ChildPath "SUMMARY.md"

# Collect all Markdown files
Write-Host "Collecting Markdown files..."
$markdownFiles = @()

Get-ChildItem -Path $ProjectRoot -Recurse -File | ForEach-Object {
    if ($_.Extension -eq ".md" -and $_.Name -ne "SUMMARY.md" -and $_.Name -ne ".gitignore") {
        $relativePath = $_.FullName.Substring($ProjectRoot.Length + 1)
        $relativePath = $relativePath -replace '\\', '/'
        if ($relativePath -notmatch "\.git/" -and $relativePath -notmatch "\.idea/" -and $relativePath -notmatch "\.vscode/") {
            $markdownFiles += $relativePath
        }
    }
}

# Organize files by directory
Write-Host "Organizing files by directory..."
$organized = @{}

foreach ($filePath in $markdownFiles) {
    $parts = $filePath -split '/'
    if ($parts.Length -eq 1) {
        if (!$organized.ContainsKey("root")) {
            $organized["root"] = @()
        }
        $organized["root"] += $filePath
    } else {
        $dirName = $parts[0]
        if (!$organized.ContainsKey($dirName)) {
            $organized[$dirName] = @()
        }
        $organized[$dirName] += $filePath
    }
}

# Generate summary content
Write-Host "Generating summary content..."
$content = @()
$content += '# MyNotes Summary'
$content += ''
$content += "Generated on: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$content += ''
$content += '## Directory Structure'
$content += ''

# Add root files
if ($organized.ContainsKey("root")) {
    $content += '### Root Directory'
    $content += ''
    foreach ($file in $organized["root"] | Sort-Object) {
        $fileName = Split-Path -Leaf $file
        $content += "- [$fileName]($file)"
    }
    $content += ''
}

# Add subdirectory files
foreach ($dirName in $organized.Keys | Sort-Object) {
    if ($dirName -eq "root") {
        continue
    }
    
    $content += "### $dirName"
    $content += ''
    foreach ($file in $organized[$dirName] | Sort-Object) {
        $fileName = Split-Path -Leaf $file
        $content += "- [$fileName]($file)"
    }
    $content += ''
}

# Write to file
Write-Host "Writing summary to file..."
try {
    $content -join "`n" | Out-File -FilePath $SummaryFile -Encoding UTF8
    Write-Host "Summary generated successfully at $SummaryFile" -ForegroundColor Green
} catch {
    Write-Host "Error writing summary file: $($_.ToString())" -ForegroundColor Red
}
