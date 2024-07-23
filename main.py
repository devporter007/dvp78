import os
import sys
import shlex
import subprocess

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
    "reset": "\u001b[0m",
}

VERSION = "0.3g"

BANNER = f'''
                                                [[yellow]]Port007[[white]] proudly presents:
                                            [[red]]     *\\*_o__ **o/   o** __o    
                                                      v    |/  /v     v\\   
                                                          /   />       <\\  
                                                        o/    \\o       o/  
                                                       /v      |>_   _<|   
                                                      />      /         \\  
                                                    o/        \\         /  
                                                   /v          o       o   
                                                  />           <\\__ __/>   
                                                         [[cyan]]{VERSION}[[white]]
                              [[magenta]]     Making tools to create quality releases since 2023     
                        This tool is part of a tool pack made to archive movies for the uncertain future[[white]]
'''

def colorize(text):
    for color, code in COLORS.items():
        text = text.replace(f"[[{color}]]", code)
    return text + COLORS["reset"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colorize(BANNER))

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        sys.exit(1)

def process_file(file_path):
    file_path = os.path.abspath(file_path)
    if not os.path.isfile(file_path):
        print(f"File does not exist: {file_path}")
        sys.exit(1)

    work_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    name_without_ext = os.path.splitext(file_name)[0]

    hevc_output = os.path.join(work_dir, f"{name_without_ext}.hevc")
    mka_output = os.path.join(work_dir, f"{name_without_ext}.mka")
    final_output = os.path.join(work_dir, f"{name_without_ext}.P8.mkv")

    print("Step 1: Extracting RPU and removing EL...")
    run_command(f'ffmpeg -y -i {shlex.quote(file_path)} -dn -c:v copy -vbsf hevc_mp4toannexb -f hevc - | dovi_tool -m 2 convert --discard - -o {shlex.quote(hevc_output)}')
    clear_screen()

    print("Step 2: Generating mka without video, keeping everything else intact...")
    run_command(f'mkvmerge --output {shlex.quote(mka_output)} --no-video {shlex.quote(file_path)}')
    clear_screen()

    print("Step 3: Combining everything...")
    run_command(f'mkvmerge -o {shlex.quote(final_output)} {shlex.quote(hevc_output)} {shlex.quote(mka_output)}')
    clear_screen()

    print("Step 4: Cleaning up intermediates...")
    os.remove(hevc_output)
    os.remove(mka_output)
    clear_screen()

    print("Processing completed successfully.")

def main():
    clear_screen()
    try:
        if len(sys.argv) < 2:
            print("Usage: python script.py <file_path>")
            print("Please provide a file path as an argument.")
            sys.exit(1)

        process_file(sys.argv[1])

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        print("Press any key to exit...")
        input()

if __name__ == "__main__":
    main()
