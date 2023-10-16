<#
.SYNOPSIS
    Show the SHA-256 Hashes of all items in a directory
#>

param (
    [Parameter(Position=0)]
    [string]$Location="."
)

foreach ($file in (Get-ChildItem -Path $Location -File)) 
{
    $hash = (Get-FileHash -Path $file.FullName -Algorithm SHA256).Hash
    Write-Host "$file : $hash"
}
