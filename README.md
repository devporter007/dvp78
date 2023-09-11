# DV78
A script that automates the conversion of Dolby Vision Profile 7(MEL,FEL) to P8

## Requirements:
<LI> ffmpeg</LI>
<LI> dovi_tool</LI>
<LI> mkvmerge</LI>

All of the above mentioned tools should be present at env vars, a check that ensures this will be implemented soon.


## Notes:
DoVi P7 MEL to P8 conversion is completely LOSSLESS with no changes in bitrate.<br><br>
DoVi P8 FEL to P8 conversion is NOT LOSSLESS as it results in EL being removed and overall bitrate being reduced.
<br><br>
I have only used this script on a windows machine so i dont know if it is compatible with unix based systems.

I personally prefer to create a binary of this script using pyinstaller and put it in my env and call it whenever i like.