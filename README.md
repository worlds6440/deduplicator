# DeDuplicator
Duplicate Finder
WARNING: to be used at your own risk.

Geared up for duplicate image finding using a basic CRC check in python. 
CRC creation method was found on another website I can no longer remember (sorry).

Resultant duplication python list (result_dict) is actually a dictionary where the key is "CRC:FILESIZE". The value part is a FULL list of filenames (including the first filename found so don't delete all files in this list).
Example:
```result_dict = {
    [CRC:FILESIZE] : (file1.xyz, file2.xyz...)
    [CRC:FILESIZE] : (file1.xyz, file2.xyz...)
}
```

Current script only finds and lists duplicate files and reports total duplicate filespace that "could" be reclaimed. Starting down coding path to move duplicate files to a different location for later safe inspection before deletion.
