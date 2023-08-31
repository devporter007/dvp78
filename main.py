import os
import sys

ver = "0.1"
gen = f'''
                                                Port007 proudly presents:
                                                     
                                                 _\\__o__ __o/   o__ __o    
                                                      v    |/  /v     v\\   
                                                          /   />       <\\  
                                                        o/    \\o       o/  
                                                       /v      |>_   _<|   
                                                      />      /         \\  
                                                    o/        \\         /  
                                                   /v          o       o   
                                                  />           <\\__ __/>   
                                                                           
                                                         {ver} 
                                                         
                                    Making tools to create archive grade releases since 2023       
                        This tool is part of a tool pack made to archive art of movies for the uncertain future
'''
print(gen)
try:
    buddy = sys.argv[1]
    try:
        end = buddy.rindex("\\")
    except:
        print("Invalid af file system")
        sys.stdin.read(1)
        sys.exit()
    workdir = buddy[:end]
    medname = buddy[end:]
    extensionlessname = medname[:-4]
    print("Step-1 : Extracting RPU and removing EL....")
    os.system(f"ffmpeg -y -i {buddy} -dn -c:v copy -vbsf hevc_mp4toannexb -f hevc - | dovi_tool -m 2 convert --discard - -o {workdir}\\discarded.hevc")
    print("Step-2: Genering mka without video keeping everything else intact....")
    print("Do this yourself in MKVToolNiX GUI and press enter, this step is WIP")
    input("")
    print("Step-3: Combining shit...")
    os.system(f"mkvmerge -o {workdir}{medname}.P8.mkv {workdir}\\discarded.hevc {workdir}{extensionlessname}.mka")
    print("Step-4: Cleaning up shit")
    os.system(f"del {workdir}\\discarded.hevc")
    os.system(f"del {workdir}{extensionlessname}.mka")
    print("Hola, signing off....")
except IndexError:
    print("No inputs found, please drag the file to this binary.")

sys.stdin.read(1)

