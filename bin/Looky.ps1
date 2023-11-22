<#
.SYNOPSIS
    Look for a file

.DESCRIPTION
    This script searches for files in a specified path.

.PARAMETER filter
    The filter to apply when searching for files. 
    Default is "*", which searches for all files.

.PARAMETER searchPath
    The path where the search should be performed. 
    Default is the current directory, represented by ".".
#>

param(
    [string]$filter="*",
    [string]$searchPath="."
)
Get-ChildItem -Path $searchPath -Recurse -File -Filter $filter -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName
