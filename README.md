# DV78
A script that automates the conversion of Dolby Vision Profile 7 (MEL, FEL) to P8.

## Requirements:
<LI> ffmpeg</LI>
<LI> dovi_tool</LI>
<LI> mkvmerge</LI>
<br>
All of the above-mentioned tools should be present in the environment variables. A check that ensures this will be implemented soon.


## Notes:
DoVi P7 MEL to P8 conversion is completely lossless with no changes in bitrate.<br><br>
DoVi P7 FEL to P8 conversion is not lossless as it results in EL being removed and overall bitrate being reduced. However, this does not mean that the raw visual quality of the media is reduced. It is just that the EL that made the media look better is not present.
<br><br>
I have only used this script on a Windows machine, so I do not know if it is compatible with Unix-based systems.

 personally prefer to create a binary of this script using PyInstaller and put it in my system environment so I can call it whenever I like.