param(
    [switch]$Fetch,
    [switch]$Diff
)

if ($Diff)
{
        # --diff-filter=M \
        # --name-only \
        

    git submodule foreach --recursive --quiet 'git diff \
        --ignore-submodules=all \
        --numstat \
        --line-prefix="\"$name/\""'
    Exit 0
}

if ($Fetch) {
    # Fetch everything and clean up extra branches, tags, etc. 
    # This is really slow when you have lots of submodules. 
    git fetch --tags --prune --recurse-submodules=yes --jobs=4 origin
}

# Clean up the base repository.
git reset --hard HEAD              # Drop all local changes
git clean -fdx                     # Drop all untracked files/dirs
git checkout master                # Goto master/main
if ($LASTEXITCODE -ne 0) { 
    git checkout main 
}
git reset --hard "@{upstream}"     # Sync local master/main to the remote one

# Clean all the submodules. Does the same thing as above. 
git submodule foreach --recursive @"
    git reset --hard HEAD
    git clean -fdx
    git checkout master || git checkout main
    git reset --hard @{upstream}
"@


