<#
.SYNOPSIS
    Show the SHA-256 Hashes of all items in a directory
#>

param (
    [switch]$FullHash,
    [switch]$Dashed,
    [string]$Location = "."
)

foreach ($file in (Get-ChildItem -Path $Location -File)) {
    $hash = (Get-FileHash -Path $file.FullName -Algorithm SHA256).Hash.ToLower()
    if (!$FullHash) {
        $hash = $hash.Substring(0,8)
    }
    if ($Dashed) {
        $hash = ($hash -replace '(.{4})', '$1-').TrimEnd('-')
    }
    Write-Host "$file`n`t$hash"
}
