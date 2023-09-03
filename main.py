import os
import sys
COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}

ver = "0.1"

gen = f'''
                                                [[yellow]]Port007[[white]] proudly presents:

                                            [[red]]     _\\__o__ __o/   o__ __o    
                                                      v    |/  /v     v\\   
                                                          /   />       <\\  
                                                        o/    \\o       o/  
                                                       /v      |>_   _<|   
                                                      />      /         \\  
                                                    o/        \\         /  
                                                   /v          o       o   
                                                  />           <\\__ __/>   

                                                         [[cyan]]{ver}[[white]]

                              [[magenta]]      Making tools to create archive grade releases since 2023     

                    This tool is part of a tool pack made to archive art of movies for the uncertain future[[white]]
'''



def colortext(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
def Clear():
    os.system('cls')
    print(colortext(gen))

Clear()

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
    Clear()
    print("Step-2: Genering mka without video keeping everything else intact....")
    print("Do this yourself in MKVToolNiX GUI and press enter, this step is WIP")
    input("")
    Clear()
    print("Step-3: Combining shit...")
    os.system(f"mkvmerge -o {workdir}{extensionlessname}.P8.mkv {workdir}\\discarded.hevc {workdir}{extensionlessname}.mka")
    Clear()
    print("Step-4: Cleaning up shit")
    os.system(f"del {workdir}\\discarded.hevc")
    os.system(f"del {workdir}{extensionlessname}.mka")
    Clear()
    print("Hola, signing off....")
except IndexError:
    print("No inputs found, please drag the file to this binary.")

sys.stdin.read(1)
