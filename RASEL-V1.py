#!/usr/bin/env python3
# Tool  : RASEL V1
# Owner : RASEL
# Telegram : https://t.me/GCSF_CYBER_RASEL
# GitHub : https://github.com/cyberrasel999

import os
from time import sleep
import signal
import time
import sys
import random

gren = "\033[0m\033[38;5;46m"
reed = "\033[0m\033[38;5;196m"
white = "\033[38;5;15m"
reset = "\033[0m"
blue = "\033[1;34m"
cyan = "\033[1;36m"
yellow = "\033[1;33m"
purple = "\033[1;35m"

os.system('clear')

def matrix_rain():
    chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
    for _ in range(5):
        line = ""
        for _ in range(60):
            c = random.choice(chars) if random.random() > 0.4 else " "
            colors = ['\033[38;5;46m', '\033[38;5;47m', '\033[38;5;48m', '\033[38;5;82m', '\033[38;5;40m']
            line += random.choice(colors) + c
        sys.stdout.write(f"\r{line}{reset}")
        sys.stdout.flush()
        sleep(0.07)

def blur_text(text, color):
    dim = "\033[2m"
    for i in range(len(text)+1):
        blurred = text[:i]
        rest = text[i:]
        sys.stdout.write(f"\r{color}{blurred}{dim}{rest}{reset}")
        sys.stdout.flush()
        sleep(0.02)
    sys.stdout.write(f"\r{color}{text}{reset}\n")

def hack_glitch(text, color):
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?~`"
    for _ in range(4):
        sys.stdout.write(f"\r{color}{text}{reset}")
        sys.stdout.flush()
        sleep(0.06)
        glitch = ''.join(random.choice(glitch_chars) for _ in text)
        sys.stdout.write(f"\r{reed}{glitch}{reset}")
        sys.stdout.flush()
        sleep(0.05)
    sys.stdout.write(f"\r{color}{text}{reset}\n")

def spinner_3d():
    frames = ["◴", "◷", "◶", "◵", "◸", "◹", "◺", "◿", "⬔", "⬕", "⬖", "⬗", "⬘", "⬙"]
    for _ in range(4):
        for f in frames:
            sys.stdout.write(f"\r{cyan}[{yellow}{f}{cyan}] {white}3D Rendering...{reset}")
            sys.stdout.flush()
            sleep(0.06)

def hacker_animation():
    spinner_3d()
    hack_glitch("RASEL V1", cyan)
    frames = [
        f"{cyan}[>] Initializing RASEL V1{reset}",
        f"{cyan}[>>] Loading security modules...{reset}",
        f"{cyan}[>>>] Establishing encrypted connection...{reset}",
        f"{cyan}[>>>>] Initializing 3D engine...{reset}",
        f"{cyan}[>>>>>] Fetching banner assets...{reset}",
        f"{cyan}[>>>>>>] Compiling interface...{reset}",
        f"{cyan}[>>>>>>>] Access granted!{reset}",
    ]
    for frame in frames:
        sys.stdout.write(f"\r{frame}")
        sys.stdout.flush()
        sleep(0.15)
    print()

def typewriter_effect(text, color):
    cursor = "\033[5m_\033[0m"
    for i in range(len(text)+1):
        sys.stdout.write(f"\r{color}{text[:i]}{cursor}{reset}")
        sys.stdout.flush()
        sleep(0.025)
    sys.stdout.write(f"\r{color}{text}{reset}\n")
    sys.stdout.flush()

def glitch_fade(text, color):
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?~`"
    for _ in range(3):
        sys.stdout.write(f"\r{color}{text}{reset}")
        sys.stdout.flush()
        sleep(0.04)
        glitch = ''.join(random.choice(glitch_chars) for _ in text)
        sys.stdout.write(f"\r{reed}{glitch}{reset}")
        sys.stdout.flush()
        sleep(0.04)
    blur_text(text, color)

def print_loading_bar(percentage):
    bar_length = 38
    filled_length = int(bar_length * percentage / 100)
    bar = '█' * filled_length + ' ' * (bar_length - filled_length)
    colors = ['\033[38;5;196m', '\033[38;5;202m', '\033[38;5;214m', '\033[38;5;226m', '\033[38;5;46m']
    c = colors[min(percentage // 25, 4)]
    arrow = ["▸", "▹", "▹", "·"][percentage % 4]
    sys.stdout.write(f"\r{cyan}Loading {arrow} {c}[{bar}{cyan}] {c}{percentage}%{reset}")
    sys.stdout.flush()

matrix_rain()
sleep(0.2)
hacker_animation()
total_time = 2.0
interval = total_time / 100
for i in range(101):
    print_loading_bar(i)
    time.sleep(interval)

os.system(f"cat core/main.logo 2>/dev/null")
sleep(0.5)

hack_glitch("* RASEL V1 LOADED *", gren)

print(f"\n{cyan}╔{'═'*50}╗")
print(f"{cyan}║{white}     Welcome to RASEL V1 - Termux Customizer      {cyan}║")
print(f"{cyan}║{purple}       Telegram: {white}t.me/GCSF_CYBER_RASEL{cyan}            ║")
print(f"{cyan}║{purple}       GitHub: {white}github.com/cyberrasel999{cyan}           ║")
print(f"{cyan}╚{'═'*50}╝{reset}")
sleep(1)

print(f"\n{cyan}[{white}+{cyan}] Setting up Zsh Shell + Auto-Suggestions...")
os.system("pkg install zsh zsh-autosuggestions zsh-syntax-highlighting -y > /dev/null 2>&1")
os.system("sh -c \"$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\" --unattended > /dev/null 2>&1")
os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k > /dev/null 2>&1")
os.system("git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting > /dev/null 2>&1")
os.system("sed -i 's/ZSH_THEME=\"robbyrussell\"/ZSH_THEME=\"powerlevel10k\\/powerlevel10k\"/' $HOME/.zshrc > /dev/null 2>&1")
with open(os.path.expanduser("~/.zshrc"), 'a') as f:
    f.write("\n# Enable tab completion\n")
    f.write("autoload -Uz compinit && compinit\n")
    f.write("zstyle ':completion:*' menu select\n")
    f.write("zstyle ':completion:*' verbose yes\n")
    f.write("zstyle ':completion:*' group-name ''\n")
    f.write("zstyle ':completion:*' format '%B%F{blue}%d%f%b'\n")
    f.write("zstyle ':completion:*' list-colors \"${(s.:.)LS_COLORS}\"\n")
    f.write("zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'\n")
    f.write("setopt auto_menu\n")
    f.write("setopt complete_in_word\n")
    f.write("setopt always_to_end\n")
    f.write("setopt correct\n")
    f.write("\n# Enable auto-suggestions\n")
    f.write("source /data/data/com.termux/files/usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh 2>/dev/null\n")
    f.write("ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=8'\n")
    f.write("ZSH_AUTOSUGGEST_STRATEGY=(match_prev_cmd completion history)\n")
    f.write("bindkey '^ ' autosuggest-accept\n")
    f.write("bindkey '^]' autosuggest-execute\n")
    f.write("\n# Enable syntax highlighting\n")
    f.write("source /data/data/com.termux/files/usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null\n")
os.system("chsh -s zsh > /dev/null 2>&1")
print(f"{cyan}[{white}+{cyan}] Zsh Shell + Auto-Suggestions + Syntax Highlighting ready! Restart Termux to apply.")
sleep(1)

about_tool = f"""\033[0m
{cyan}╔{'═'*50}╗
{cyan}║{white}           RASEL V1 - Termux Customizer           {cyan}║
{cyan}╚{'═'*50}╝

{white}About:
    {gren}RASEL V1 is a powerful banner customization tool for Termux.
    Create personalized banners, custom prompts, and unique terminal
    experiences with hacker-style aesthetics.

{white}Features:
{gren}
    [*] 47+ Banner Styles
    [*] 270+ Font Designs
    [*] 50+ PS1 Prompt Styles  
    [*] 21 Text Colors
    [*] 3D Animations
    [*] Hacker Theme

{white}Owner:
    {cyan}Name    :{white} RASEL
    {cyan}Telegram:{white} https://t.me/GCSF_CYBER_RASEL
    {cyan}GitHub  :{white} https://github.com/cyberrasel999

{cyan}╔{'═'*50}╗
{cyan}║{gren}  Unleash your terminal with RASEL V1!{cyan}            ║
{cyan}╚{'═'*50}╝
"""

menux = f"""\033[0m{cyan}╔{'═'*50}╗
{cyan}║{white}                  ✦  RASEL V1  ✦                  {cyan}║
{cyan}║{purple}                Termux Customizer                 {cyan}║
{cyan}╚{'═'*50}╝
{purple}──────────────────────────────────────────────────{reset}
{cyan}[{white}1{cyan}]{white} Set Banner Only
{cyan}[{white}2{cyan}]{white} Set Name Only
{cyan}[{white}3{cyan}]{white} Set Banner With Name
{cyan}[{white}4{cyan}]{white} Restore Default
{cyan}[{white}5{cyan}]{white} More Tools
{cyan}[{white}6{cyan}]{white} About
{cyan}[{white}E{cyan}]{white} Exit
{purple}──────────────────────────────────────────────────{reset}
{gren}Tip: press 3 for banner + name together.{reset}

{reed}inputx>{white} """

fon_type = f"""\033[0m{cyan}╔{'═'*50}╗
{cyan}║{white}                 Select Font Set                  {cyan}║
{cyan}╚{'═'*50}╝
{cyan}[{white}1{cyan}]{white} Font Set 1
{cyan}[{white}2{cyan}]{white} Font Set 2
{cyan}[{white}3{cyan}]{white} Font Set 3
{cyan}[{white}4{cyan}]{white} Font Set 4
{cyan}[{white}5{cyan}]{white} Font Set 5
{cyan}[{white}6{cyan}]{white} Font Set 6
{cyan}[{white}7{cyan}]{white} Font Set 7
{reed}inputx>{white} """

def exited():
    print(f"\n{reset}{cyan}╔{'═'*50}╗")
    print(f"{cyan}║{gren}  Thank you for using RASEL V1! Stay Hacky!{cyan}       ║")
    print(f"{cyan}╚{'═'*50}╝")
    print(f"{cyan}    Telegram: {white}t.me/GCSF_CYBER_RASEL")
    print(f"{cyan}    GitHub  : {white}github.com/cyberrasel999{reset}\n")
    exit()

def safe_exit(signum, frame):
    print(f"\n\n{reed}[!] Ctrl+C detected. Exiting gracefully...")
    exited()

signal.signal(signal.SIGINT, safe_exit)

def set_new_bnr():
    print(f"\n{reset}{cyan}[{white}+{cyan}] Applying new banner in your termux.")
    os.system("chsh -s bash")
    os.system("mkdir $HOME/.backupx > /dev/null 2>&1 &")
    os.system("mv /data/data/com.termux/files/usr/etc/motd $HOME/.backupx > /dev/null 2>&1 &")
    os.system("rm $HOME/.bashrc > /dev/null 2>&1 &")
    os.system("mv bashrc_file $HOME/.bashrc > /dev/null 2>&1 &")
    sleep(1)
    print(f"\n{cyan}[{white}+{cyan}] New Banner has been successfully set! Exit and reopen termux.")
    exited()

def restore_dflt():
    os.system("clear")
    print(f"\n{cyan}[{white}+{cyan}] Restoring Default look of termux.")
    os.system("rm $HOME/.bashrc > /dev/null 2>&1 &")
    os.system("mv $HOME/.backupx/motd /data/data/com.termux/files/usr/etc > /dev/null 2>&1 &")
    sleep(1)
    print(f"\n{cyan}[{white}+{cyan}] Default Banner restored successfully.")
    exited()

def show_prompt_templates():
    print(f"{cyan}╔{'═'*54}╗")
    print(f"{cyan}║{white}       Prompt Style Templates (30+ Designs)       {cyan}║")
    print(f"{cyan}╚{'═'*54}╝")
    templates = [
        ["01", f"┌──($USER@termux)-[~]", f"└──{reed}❯{yellow}❯{gren}❯{white} $USER"],
        ["02", f"┌──[$USER@termux]-[~]", f"└──{reed}❯❯❯{white} $USER"],
        ["03", f"{white}$USER{cyan}@{white}termux{cyan} [~]", f"{reed}──❯{white} $USER"],
        ["04", f"┌─[$USER]-[termux]-[~]", f"└──{reed}❯{white} $USER"],
        ["05", f"{cyan}[$USER@termux ~]", f"{white}$ $USER"],
        ["06", f"┌──($USER)-(termux)-(~)", f"└──{reed}►{white} $USER"],
        ["07", f"{purple}$USER{cyan}@{yellow}termux{cyan} ~", f"{reed}❯{white} $USER"],
        ["08", f"{cyan}╭─$USER@termux─~", f"╰─{reed}❯{white} $USER"],
        ["09", f"{cyan}[$USER@termux ~]", f"{reed}➤{white} $USER"],
        ["10", f"{cyan}┌[$USER@termux ~]", f"└[{reed}❯{cyan}]{white} $USER"],
        ["11", f"{gren}$USER{cyan}@{blue}termux{cyan}:~", f"{reed}$ {white}$USER"],
        ["12", f"{reed}$USER{cyan}@{yellow}termux{cyan} → ~", f"{reed}❯❯❯{white} $USER"],
        ["13", f"{cyan}[$USER|termux|~]", f"{reed}═> {white}$USER"],
        ["14", f"{cyan}┌─[$USER@termux ~]─[%T]", f"└──{reed}❯{white} $USER"],
        ["15", f"{purple}$USER{cyan}@{blue}termux{cyan} ~", f"{reed}└─❯{white} $USER"],
        ["16", f"{cyan}┌──($USER@termux)-[~]", f"│ {yellow}%T{cyan}\\n└──{reed}❯{white} $USER"],
        ["17", f"{blue}$USER{cyan}@{gren}termux{cyan}:~", f"{reed}# {white}$USER"],
        ["18", f"{cyan}[$USER@{gren}termux{cyan} ~]", f"{reed}$ {white}$USER"],
        ["19", f"{cyan}┌[$USER]─[termux]─[~]", f"└[{reed}❯{cyan}]{white} $USER"],
        ["20", f"{reed}$USER{cyan}@{white}termux{cyan} ~", f"{reed}$ {white}$USER"],
        ["21", f"{cyan}╭─$USER─termux─~", f"╰─{reed}➤{white} $USER"],
        ["22", f"{gren}$USER{cyan}@{blue}termux{cyan}:~", f"{reed}$ {white}$USER"],
        ["23", f"{cyan}[$USER@termux ~]", f"{reed}└─❯ {white}$USER"],
        ["24", f"{cyan}┌[$USER]-[termux]-[~]", f"└[{reed}❯❯❯{cyan}]{white} $USER"],
        ["25", f"{purple}$USER{cyan}@{reed}termux{cyan} ~", f"{reed}❯❯❯{white} $USER"],
        ["26", f"{yellow}$USER{cyan}@{white}termux{cyan} ~ [%D{{%T}}]", f"{reed}$ {white}$USER"],
        ["27", f"{cyan}[$USER]─[termux]─[~]", f"└─[{reed}❯{cyan}]{white} $USER"],
        ["28", f"{cyan}┌─$USER@termux─~", f"└─{reed}❯{white} $USER"],
        ["29", f"{cyan}╭─$USER@termux:~", f"╰─{reed}❯{white} $USER"],
        ["30", f"{cyan}┌──($USER@termux)-[~]", f"│ {yellow}%D{{%d/%m/%y %T}}{cyan}\\n└──{reed}❯{white} $USER"],
    ]
    for t in templates:
        print(f"{cyan}╔{'═'*4}╦{'═'*48}╗")
        print(f"{cyan}║{white} {t[0]}{cyan} ║ {t[1]}")
        print(f"{cyan}║    ║ {t[2]}")
        print(f"{cyan}╚{'═'*4}╩{'═'*48}╝")
    print(f"{cyan}╔{'═'*4}╦{'═'*48}╗")
    print(f"{cyan}║{white} B{cyan} ║ {white}Back")
    print(f"{cyan}╚{'═'*4}╩{'═'*48}╝")

prompt_templates = {
    "1": r'PS1="\[\e[1;32m\]┌──(\[\e[1;33m\]\u\[\e[1;32m\]@\[\e[1;34m\]\h\[\e[1;32m\])-\[\e[1;32m\][\[\e[1;36m\]\w\[\e[1;32m\]]\n\[\e[1;32m\]└──\[\e[1;31m\]❯\[\e[1;33m\]❯\[\e[1;32m\]❯\[\e[1;37m\] \[\033[38;5;',
    "2": r'PS1="\[\e[1;34m\]┌──[\[\e[1;33m\]\u\[\e[1;34m\]@\[\e[1;32m\]\h\[\e[1;34m\]]-[\[\e[1;36m\]\w\[\e[1;34m\]]\n\[\e[1;34m\]└──\[\e[1;31m\]❯❯❯\[\e[1;37m\] \[\033[38;5;',
    "3": r'PS1="\[\e[1;37m\]\u\[\e[1;36m\]@\[\e[1;32m\]\h\[\e[1;36m\] [\[\e[1;33m\]\w\[\e[1;36m\]]\n\[\e[1;31m\]──❯\[\e[1;37m\] \[\033[38;5;',
    "4": r'PS1="\[\e[1;32m\]┌─[\[\e[1;33m\]\u\[\e[1;32m\]]-[\[\e[1;34m\]\h\[\e[1;32m\]]-[\[\e[1;36m\]\w\[\e[1;32m\]]\n\[\e[1;32m\]└──\[\e[1;31m\]❯\[\e[1;37m\] \[\033[38;5;',
    "5": r'PS1="\[\e[1;36m\][\[\e[1;33m\]\u\[\e[1;36m\]@\[\e[1;32m\]\h\[\e[1;36m\] \[\e[1;37m\]\w\[\e[1;36m\]]\n\[\e[1;37m\]$ \[\033[38;5;',
    "6": r'PS1="\[\e[1;32m\]┌──(\[\e[1;33m\]\u\[\e[1;32m\])-(\[\e[1;34m\]\h\[\e[1;32m\])-(\[\e[1;36m\]\w\[\e[1;32m\])\n\[\e[1;32m\]└──\[\e[1;31m\]►\[\e[1;37m\] \[\033[38;5;',
    "7": r'PS1="\[\e[1;35m\]\u\[\e[1;36m\]@\[\e[1;33m\]\h\[\e[1;35m\] \[\e[1;36m\]\w\[\e[1;35m\]\n\[\e[1;31m\]❯\[\e[1;37m\] \[\033[38;5;',
    "8": r'PS1="\[\e[1;36m\]╭─\[\e[1;33m\]\u\[\e[1;36m\]@\[\e[1;34m\]\h\[\e[1;36m\]─\[\e[1;37m\]\w\[\e[1;36m\]\n\[\e[1;36m\]╰─\[\e[1;31m\]❯\[\e[1;37m\] \[\033[38;5;',
    "9": r'PS1="\[\e[1;36m\][\[\e[1;33m\]\u\[\e[1;36m\]@\[\e[1;32m\]\h\[\e[1;36m\] \[\e[1;37m\]\w\[\e[1;36m\]]\n\[\e[1;31m\]➤\[\e[1;37m\] \[\033[38;5;',
    "10": r'PS1="\[\e[1;36m\]┌[\[\e[1;33m\]\u\[\e[1;36m\]@\[\e[1;32m\]\h\[\e[1;36m\] \[\e[1;37m\]\w\[\e[1;36m\]]\n\[\e[1;36m\]└[\[\e[1;31m\]❯\[\e[1;36m\]]\[\e[1;37m\] \[\033[38;5;',
    "11": r'PS1="\[\e[1;32m\]\u\[\e[1;36m\]@\[\e[1;34m\]\h\[\e[1;36m\]:\[\e[1;37m\]\w\[\e[1;36m\]\n\[\e[1;31m\]$ \[\033[38;5;',
    "12": r'PS1="\[\e[1;31m\]\u\[\e[1;36m\]@\[\e[1;33m\]\h\[\e[1;36m\] → \[\e[1;37m\]\w\[\e[1;36m\]\n\[\e[1;31m\]❯❯❯\[\e[1;37m\] \[\033[38;5;',
    "13": r'PS1="\[\e[1;36m\][\[\e[1;33m\]\u\[\e[1;36m\]|\[\e[1;32m\]\h\[\e[1;36m\]|\[\e[1;37m\]\w\[\e[1;36m\]]\n\[\e[1;31m\]═> \[\033[38;5;',
    "14": r'PS1="\[\e[1;36m\]┌─[\[\e[1;33m\]\u\[\e[1;36m\]@\[\e[1;32m\]\h\[\e[1;36m\] \[\e[1;37m\]\w\[\e[1;36m\]]─[\[\e[1;33m\]\D{%T}\[\e[1;36m\]]\n\[\e[1;36m\]└──\[\e[1;31m\]❯\[\e[1;37m\] \[\033[38;5;',
    "15": r'PS1="\[\e[1;35m\]\u\[\e[1;36m\]@\[\e[1;34m\]\h\[\e[1;35m\] \[\e[1;36m\]\w\[\e[1;35m\]\n\[\e[1;31m\]└─❯\[\e[1;37m\] \[\033[38;5;',
    "16": r'PS1="\[\e[1;36m\]┌──(\[\e[1;33m\]\u\[\e[1;36m\]@\h)-[\[\e[1;37m\]\w\[\e[1;36m\]]\n\[\e[1;36m\]│ \[\e[1;33m\]\D{%T}\[\e[1;36m\]\n\[\e[1;36m\]└──\[\e[1;31m\]❯\[\e[1;37m\] \[\033[38;5;',
    "17": r'PS1="\[\e[1;34m\]\u\[\e[1;36m\]@\[\e[1;32m\]\h\[\e[1;36m\]:\[\e[1;37m\]\w\[\e[1;36m\]\n\[\e[1;31m\]# \[\033[38;5;',
    "18": r'PS1="\[\e[1;36m\][\[\e[1;33m\]\u\[\e[1;36m\]@\[\e[1;32m\]\h\[\e[1;36m\] \[\e[1;37m\]\w\[\e[1;36m\]]\[\e[1;31m\]$\[\e[1;37m\] \[\033[38;5;',
    "19": r'PS1="\[\e[1;36m\]┌[\[\e[1;33m\]\u\[\e[1;36m\]]─[\[\e[1;34m\]\h\[\e[1;36m\]]─[\[\e[1;37m\]\w\[\e[1;36m\]]\n\[\e[1;36m\]└[\[\e[1;31m\]❯\[\e[1;36m\]]\[\e[1;37m\] \[\033[38;5;',
    "20": r'PS1="\[\e[1;31m\]\u\[\e[1;36m\]@\[\e[1;37m\]\h\[\e[1;36m\] \[\e[1;37m\]\w\[\e[1;36m\]\n\[\e[1;31m\]$ \[\033[38;5;',
    "21": r'PS1="\[\e[1;36m\]╭─\[\e[1;33m\]\u\[\e[1;36m\]─\[\e[1;34m\]\h\[\e[1;36m\]─\[\e[1;37m\]\w\[\e[1;36m\]\n\[\e[1;36m\]╰─\[\e[1;31m\]➤\[\e[1;37m\] \[\033[38;5;',
    "22": r'PS1="\[\e[1;32m\]\u\[\e[1;36m\]@\[\e[1;34m\]\h\[\e[1;36m\]:\[\e[1;37m\]\w\[\e[1;36m\]\[\e[1;31m\]$ \[\033[38;5;',
    "23": r'PS1="\[\e[1;36m\][\[\e[1;33m\]\u\[\e[1;36m\]@\[\e[1;32m\]\h\[\e[1;36m\] \[\e[1;37m\]\w\[\e[1;36m\]]\n\[\e[1;31m\]└─❯ \[\033[38;5;',
    "24": r'PS1="\[\e[1;36m\]┌[\[\e[1;33m\]\u\[\e[1;36m\]]-[\[\e[1;34m\]\h\[\e[1;36m\]]-[\[\e[1;37m\]\w\[\e[1;36m\]]\n\[\e[1;36m\]└[\[\e[1;31m\]❯❯❯\[\e[1;36m\]]\[\e[1;37m\] \[\033[38;5;',
    "25": r'PS1="\[\e[1;35m\]\u\[\e[1;36m\]@\[\e[1;31m\]\h\[\e[1;35m\] \[\e[1;36m\]\w\[\e[1;35m\]\n\[\e[1;31m\]❯❯❯\[\e[1;37m\] \[\033[38;5;',
    "26": r'PS1="\[\e[1;33m\]\u\[\e[1;36m\]@\[\e[1;37m\]\h\[\e[1;33m\] \[\e[1;36m\]\w\[\e[1;33m\] [\[\e[1;34m\]\D{%T}\[\e[1;33m\]]\n\[\e[1;31m\]$ \[\033[38;5;',
    "27": r'PS1="\[\e[1;36m\][\[\e[1;33m\]\u\[\e[1;36m\]]─[\[\e[1;34m\]\h\[\e[1;36m\]]─[\[\e[1;37m\]\w\[\e[1;36m\]]\n\[\e[1;36m\]└─[\[\e[1;31m\]❯\[\e[1;36m\]]\[\e[1;37m\] \[\033[38;5;',
    "28": r'PS1="\[\e[1;36m\]┌─\[\e[1;33m\]\u\[\e[1;36m\]@\[\e[1;34m\]\h\[\e[1;36m\]─\[\e[1;37m\]\w\[\e[1;36m\]\n\[\e[1;36m\]└─\[\e[1;31m\]❯\[\e[1;37m\] \[\033[38;5;',
    "29": r'PS1="\[\e[1;36m\]╭─\[\e[1;33m\]\u\[\e[1;36m\]@\[\e[1;34m\]\h\[\e[1;36m\]:\[\e[1;37m\]\w\[\e[1;36m\]\n\[\e[1;36m\]╰─\[\e[1;31m\]❯\[\e[1;37m\] \[\033[38;5;',
    "30": r'PS1="\[\e[1;36m\]┌──(\[\e[1;33m\]\u\[\e[1;36m\]@\h)-[\[\e[1;37m\]\w\[\e[1;36m\]]\n\[\e[1;36m\]│ \[\e[1;33m\]\D{%d/%m/%y %T}\[\e[1;36m\]\n\[\e[1;36m\]└──\[\e[1;31m\]❯\[\e[1;37m\] \[\033[38;5;',
}

def select_pt():
    print(f"\n{cyan}[{white}+{cyan}] Enter your display name for prompt (or press Enter for system username): ")
    disp_name = input(f"{reset}{reed}name>{white} ").strip()
    if disp_name == '':
        disp_name = r'\u'
    while True:
        os.system('clear')
        show_prompt_templates()
        mprot = input(f"{reset}{reed}inputx>{white} ")
        if mprot == '':
            pass
        elif mprot in prompt_templates:
            tmpl = prompt_templates[mprot]
            tmpl = tmpl.replace(r'\u', disp_name)
            return tmpl
        elif mprot.lower() == 'b':
            break

def colorsx():
    print(f"\n{cyan}╔{'═'*50}╗")
    print(f"{cyan}║{white}             Select Input Text Color              {cyan}║")
    print(f"{cyan}╚{'═'*50}╝")
    print(f"\n{reset}{cyan}[{white}01{cyan}] {reed}Red Color")
    print(f"{cyan}[{white}02{cyan}] {gren}Green Color")
    print(f"{cyan}[{white}03{cyan}] {blue}Blue Color")
    print(f"{cyan}[{white}04{cyan}] {yellow}Yellow Color")
    print(f"{cyan}[{white}05{cyan}] {purple}Purple Color")
    print(f"{cyan}[{white}06{cyan}] {cyan}Cyan Color")
    print(f"{cyan}[{white}07{cyan}] {white}White Color")
    print(f"{cyan}[{white}08{cyan}] Orange Color")
    print(f"{cyan}[{white}09{cyan}] Pink Color")
    print(f"{cyan}[{white}10{cyan}] Brown Color")
    print(f"{cyan}[{white}11{cyan}] Light Green Color")
    print(f"{cyan}[{white}12{cyan}] Light Blue Color")
    print(f"{cyan}[{white}13{cyan}] Light Yellow Color")
    print(f"{cyan}[{white}14{cyan}] Light Purple Color")
    print(f"{cyan}[{white}15{cyan}] Light Cyan Color")
    print(f"{cyan}[{white}16{cyan}] Light Gray Color")
    print(f"{cyan}[{white}17{cyan}] Dark Gray Color")
    print(f"{cyan}[{white}18{cyan}] Gold Color")
    print(f"{cyan}[{white}19{cyan}] Lavender Color")
    print(f"{cyan}[{white}20{cyan}] Magenta Color")
    print(f"{cyan}[{white}21{cyan}] Teal Color\n")

def select_clr():
    while True:
        os.system("clear")
        colorsx()
        colx = input(f"{reset}{reed}inputx> {white}")
        if colx == "":
            pass
        elif colx in ("1","01"): return '196m\\]"'
        elif colx in ("2","02"): return '46m\\]"'
        elif colx in ("3","03"): return '21m\\]"'
        elif colx in ("4","04"): return '226m\\]"'
        elif colx in ("5","05"): return '129m\\]"'
        elif colx in ("6","06"): return '51m\\]"'
        elif colx in ("7","07"): return '15m\\]"'
        elif colx in ("8","08"): return '202m\\]"'
        elif colx in ("9","09"): return '219m\\]"'
        elif colx == "10": return '130m\\]"'
        elif colx == "11": return '48m\\]"'
        elif colx == "12": return '33m\\]"'
        elif colx == "13": return '229m\\]"'
        elif colx == "14": return '141m\\]"'
        elif colx == "15": return '87m\\]"'
        elif colx == "16": return '7m\\]"'
        elif colx == "17": return '8m\\]"'
        elif colx == "18": return '220m\\]"'
        elif colx == "19": return '183m\\]"'
        elif colx == "20": return '200m\\]"'
        elif colx == "21": return '23m\\]"'

def bnr_m():
    print(f"{cyan}╔{'═'*50}╗")
    print(f"{cyan}║{white}             Unique Banner Selection              {cyan}║")
    print(f"{cyan}╚{'═'*50}╝")
    items_m = [("26","Android"),("27","Apple"),("28","Biohazard"),("29","Boy"),("30","Danger_skull"),
               ("31","Deamon"),("32","Deamonl"),("33","Funny_skull"),("34","Github"),("35","Hanuman"),
               ("36","Headphone_skull"),("37","Hydra"),("38","Linux"),("39","Lionston"),("40","Panda"),
               ("41","Radioactive"),("42","Single_eye"),("43","Skull"),("44","Stop"),("45","Termux"),
               ("46","Ubuntu"),("47","Warn")]
    for num, name in items_m:
        print(f"{cyan}─"*50)
        print(f"{cyan}[{white}{num}{cyan}]{white} {name} Banner")
        os.system(f"cat core/bnr/{name.lower()}.bnr")
    print(f"{cyan}─"*50)
    print(f"{cyan}[{white}B{cyan}]{white} Back")
    print(f"{cyan}─"*50)

def bnr_main():
    print(f"{cyan}╔{'═'*50}╗")
    print(f"{cyan}║{white}             Simple Banner Selection              {cyan}║")
    print(f"{cyan}╚{'═'*50}╝")
    items = [("01","Fish","blowfish"),("02","Frog","bud-frogs"),("03","Cheese","cheese"),("04","Deamon","daemon"),
             ("05","Dragon And Cow","dragon-and-cow"),("06","Dragon","dragon"),("07","Elephant","elephant"),
             ("08","Eyes","eyes"),("09","Flaming Sheep","flaming-sheep"),("10","Ghostbuster","ghostbusters"),
             ("11","Kiss","kiss"),("12","Kitty","kitty"),("13","Meow","meow"),("14","Milk","milk"),
             ("15","Moofasa","moofasa"),("16","Moose","moose"),("17","Ren","ren"),("18","Sheep","sheep"),
             ("19","Skeleton","skeleton"),("20","Stegosaurus","stegosaurus"),("21","Stimpy","stimpy"),
             ("22","Surgery","surgery"),("23","Turkey","turkey"),("24","Turtle","turtle"),("25","Tux","tux")]
    for num, name, fname in items:
        print(f"{cyan}─"*50)
        print(f"{cyan}[{white}{num}{cyan}]{white} {name} Banner")
        os.system(f"cat core/bnr/{fname}.bnr")
    print(f"{cyan}─"*50)
    print(f"{cyan}[{white}B{cyan}]{white} Back")
    print(f"{cyan}─"*50)

def fontsta():
    print(f"{cyan}╔{'═'*50}╗")
    print(f"{cyan}║{white}                    Font Set 1                    {cyan}║")
    print(f"{cyan}╚{'═'*50}╝")
    items = [("01","3D-ASCII"),("02","3D_Diagonal"),("03","3-D"),("04","3d"),("05","3x5"),("06","4Max"),
             ("07","5lineoblique"),("08","Acrobatic"),("09","alligator3"),("10","Alligator"),
             ("11","Alphabet"),("12","Alpha"),("13","AMC_3_Line"),("14","amc3line"),("15","AMC_3_Liv1"),
             ("16","amc3liv1"),("17","amcaaa01"),("18","amcneko"),("19","AMC_Neko"),("20","amcrazo2"),
             ("21","amcrazor"),("22","amcslash"),("23","amcslder"),("24","amcthin"),("25","amctubes"),
             ("26","amcun1"),("27","ANSI_Regular"),("28","ANSI_Shadow"),("29","Arrows"),
             ("30","ASCII_New_Roman"),("31","Avatar"),("32","Banner3-D"),("33","Banner3"),
             ("34","Banner4"),("35","Banner"),("36","Barbwire"),("37","Basic"),("38","Bear"),
             ("39","Bell"),("40","bigchief")]
    for num, name in items:
        print(f"{cyan}─"*50)
        print(f"{cyan}[{white}{num}{cyan}]{white} {name} Font Style\n")
        os.system(f"cat core/fontxx/{name}.fnt")
    print(f"{cyan}─"*50)
    print(f"{cyan}[{white}B{cyan}]{white} Get Back")
    print(f"{cyan}─"*50)

def fontstb():
    print(f"{cyan}╔{'═'*50}╗")
    print(f"{cyan}║{white}                    Font Set 2                    {cyan}║")
    print(f"{cyan}╚{'═'*50}╝")
    items = [("41","Big_Chief"),("42","Bigfig"),("43","Big"),("44","Big_Money-ne"),("45","Big_Money-nw"),
             ("46","Big_Money-se"),("47","Big_Money-sw"),("48","Binary"),("49","Block"),("50","Blocks"),
             ("51","Bloody"),("52","Bolger"),("53","Braced"),("54","Bright"),("55","Broadway"),
             ("56","Broadway_KB"),("57","Bubble"),("58","Bulbhead"),("59","Caligraphy2"),("60","Caligraphy"),
             ("61","Calvin_S"),("62","Cards"),("63","Catwalk"),("64","Chiseled"),("65","Chunky"),
             ("66","Coinstak"),("67","Cola"),("68","Colossal"),("69","Computer"),("70","Contessa"),
             ("71","Contrast"),("72","Cosmike"),("73","Crawford2"),("74","Crawford"),("75","Crazy"),
             ("76","Cricket"),("77","Cursive"),("78","Cyberlarge"),("79","Cybermedium"),("80","Cybersmall")]
    for num, name in items:
        print(f"{cyan}─"*50)
        print(f"{cyan}[{white}{num}{cyan}]{white} {name} Font Style\n")
        os.system(f"cat core/fontxx/{name}.fnt")
    print(f"{cyan}─"*50)
    print(f"{cyan}[{white}B{cyan}]{white} Get Back")
    print(f"{cyan}─"*50)

def fontstc():
    print(f"{cyan}╔{'═'*50}╗")
    print(f"{cyan}║{white}                    Font Set 3                    {cyan}║")
    print(f"{cyan}╚{'═'*50}╝")
    items = [("81","Cygnet"),("82","DANC4"),("83","Dancing_Font"),("84","defleppard"),
             ("85","Delta_Corps_Priest_1"),("86","Diamond"),("87","dietcola"),("88","Digital"),
             ("89","Doh"),("90","Doom"),("91","DOS_Rebel"),("92","dotmatrix"),("93","Double"),
             ("94","doubleshorts"),("95","drpepper"),("96","eftichess"),("97","eftifont"),
             ("98","eftirobot"),("99","eftitalic"),("100","eftiwall"),("101","eftiwater"),
             ("102","Electronic"),("103","Elite"),("104","Epic"),("105","Fender"),("106","Filter"),
             ("107","Fire_Font-k"),("108","Fire_Font-s"),("109","Flipped"),("110","flowerpower"),
             ("111","fourtops"),("112","Fraktur"),("113","funface"),("114","funfaces"),("115","Fuzzy"),
             ("116","Georgi16"),("117","Georgia11"),("118","Ghost"),("119","Ghoulish"),("120","Glenyn")]
    for num, name in items:
        print(f"{cyan}─"*50)
        print(f"{cyan}[{white}{num}{cyan}]{white} {name} Font Style\n")
        os.system(f"cat core/fontxx/{name}.fnt")
    print(f"{cyan}─"*50)
    print(f"{cyan}[{white}B{cyan}]{white} Get Back")
    print(f"{cyan}─"*50)

def fontstd():
    print(f"{cyan}╔{'═'*50}╗")
    print(f"{cyan}║{white}                    Font Set 4                    {cyan}║")
    print(f"{cyan}╚{'═'*50}╝")
    items = [("121","Goofy"),("122","Gothic"),("123","Graceful"),("124","Gradient"),("125","Graffiti"),
             ("126","Greek"),("127","halfiwi"),("128","Heart_Left"),("129","Heart_Right"),("130","henry3d"),
             ("131","Hieroglyphs"),("132","Hollywood"),("133","horizontalleft"),("134","horizontalright"),
             ("135","Impossible"),("136","Invita"),("137","Isometric1"),("138","Isometric2"),
             ("139","Isometric3"),("140","Isometric4"),("141","Jacky"),("142","Jazmine"),("143","Jerusalem"),
             ("144","JS_Block_Letters"),("145","JS_Bracket_Letters"),("146","JS_Capital_Curves"),
             ("147","JS_Cursive"),("148","JS_Stick_Letters"),("149","Katakana"),("150","Kban"),
             ("151","Keyboard"),("152","Knob"),("153","larry3d"),("154","LCD"),("155","Lean"),
             ("156","Letters"),("157","lildevil"),("158","lineblocks"),("159","Linux"),("160","Lockergnome")]
    for num, name in items:
        print(f"{cyan}─"*50)
        print(f"{cyan}[{white}{num}{cyan}]{white} {name} Font Style\n")
        os.system(f"cat core/fontxx/{name}.fnt")
    print(f"{cyan}─"*50)
    print(f"{cyan}[{white}B{cyan}]{white} Get Back")
    print(f"{cyan}─"*50)

def fontste():
    print(f"{cyan}╔{'═'*50}╗")
    print(f"{cyan}║{white}                    Font Set 5                    {cyan}║")
    print(f"{cyan}╚{'═'*50}╝")
    items = [("161","Madrid"),("162","Marquee"),("163","Maxfour"),("164","maxiwi"),("165","Merlin1"),
             ("166","Merlin2"),("167","Mini"),("168","miniwi"),("169","Modular"),("170","Moscow"),
             ("171","Muzzle"),("172","Nancyj-Fancy"),("173","Nancyj"),("174","Nancyj-Underlined"),
             ("175","Nipples"),("176","NScript"),("177","ntgreek"),("178","O8"),("179","Ogre"),
             ("180","oldbanner"),("181","OS2"),("182","Patorjk-HeX"),("183","Patorjk_s_Cheese"),
             ("184","Pawp"),("185","Peaks"),("186","peaksslant"),("187","Pebbles"),("188","Pepper"),
             ("189","Poison"),("190","Puffy"),("191","Puzzle"),("192","Pyramid"),("193","Rammstein"),
             ("194","Rectangles"),("195","Red_Phoenix"),("196","Relief2"),("197","Relief"),
             ("198","Reverse"),("199","Roman"),("200","Rotated")]
    for num, name in items:
        print(f"{cyan}─"*50)
        print(f"{cyan}[{white}{num}{cyan}]{white} {name} Font Style\n")
        os.system(f"cat core/fontxx/{name}.fnt")
    print(f"{cyan}─"*50)
    print(f"{cyan}[{white}B{cyan}]{white} Get Back")
    print(f"{cyan}─"*50)

def fontstf():
    print(f"{cyan}╔{'═'*50}╗")
    print(f"{cyan}║{white}                    Font Set 6                    {cyan}║")
    print(f"{cyan}╚{'═'*50}╝")
    items = [("201","Rounded"),("202","rowancap"),("203","Rozzo"),("204","Runyc"),("205","santaclara"),
             ("206","sblood"),("207","Script"),("208","Serifcap"),("209","Shadow"),("210","Shimrod"),
             ("211","Short"),("212","Slant"),("213","Slide"),("214","slscript"),("215","SL_Script"),
             ("216","smallcaps"),("217","Small"),("218","smisome1"),("219","smkeyboard"),("220","smscript"),
             ("221","smshadow"),("222","smslant"),("223","smtengwar"),("224","Soft"),("225","Speed"),
             ("226","Spliff"),("227","s-relief"),("228","Stacey"),("229","Stampate"),("230","Stampatello"),
             ("231","Standard"),("232","starstrips"),("233","Star_Strips"),("234","starwars"),
             ("235","Star_Wars"),("236","Stellar"),("237","Stforek"),("238","Stick_Letters"),
             ("239","Stop"),("240","Straight")]
    for num, name in items:
        print(f"{cyan}─"*50)
        print(f"{cyan}[{white}{num}{cyan}]{white} {name} Font Style\n")
        os.system(f"cat core/fontxx/{name}.fnt")
    print(f"{cyan}─"*50)
    print(f"{cyan}[{white}B{cyan}]{white} Get Back")
    print(f"{cyan}─"*50)

def fontstg():
    print(f"{cyan}╔{'═'*50}╗")
    print(f"{cyan}║{white}                    Font Set 7                    {cyan}║")
    print(f"{cyan}╚{'═'*50}╝")
    items = [("241","Stronger_Than_All"),("242","Sub-Zero"),("243","swampland"),("244","Swan"),
             ("245","Sweet"),("246","Tanja"),("247","Tengwar"),("248","Test1"),("249","The_Edge"),
             ("250","Thick"),("251","Thin"),("252","THIS"),("253","Thorned"),("254","Ticks"),
             ("255","ticksslant"),("256","Tiles"),("257","Tinker-Toy"),("258","Tombstone"),
             ("259","Train"),("260","Trek"),("261","Tsalagi"),("262","Tubular"),("263","Twisted"),
             ("264","Univers"),("265","usaflag"),("266","Varsity"),("267","Wavy"),("268","Weird"),
             ("269","wetletter"),("270","Whimsy")]
    for num, name in items:
        print(f"{cyan}─"*50)
        print(f"{cyan}[{white}{num}{cyan}]{white} {name} Font Style\n")
        os.system(f"cat core/fontxx/{name}.fnt")
    print(f"{cyan}─"*50)
    print(f"{cyan}[{white}B{cyan}]{white} Get Back")
    print(f"{cyan}─"*50)

def banners():
    while True:
        os.system('clear')
        banerx = input(f"{cyan}[{white}+{cyan}] Select an option\n\n{cyan}[{white}1{cyan}]{white} Simple banner\n{cyan}[{white}2{cyan}]{white} Unique Banner\n\n{reed}inputx> {white}")
        if banerx == "":
            pass
        elif banerx in ("01","1"):
            while True:
                os.system('clear')
                bnr_main()
                s_brx = input(f"\n{reed}inputx> {white}")
                if s_brx == '': pass
                elif s_brx in ("1","01"): return 'blowfish'
                elif s_brx in ("2","02"): return 'bud-frogs'
                elif s_brx in ("3","03"): return 'cheese'
                elif s_brx in ("4","04"): return 'daemon'
                elif s_brx in ("5","05"): return 'dragon-and-cow'
                elif s_brx in ("6","06"): return 'dragon'
                elif s_brx in ("7","07"): return 'elephant'
                elif s_brx in ("8","08"): return 'eyes'
                elif s_brx in ("9","09"): return 'flaming-sheep'
                elif s_brx == "10": return 'ghostbusters'
                elif s_brx == "11": return 'kiss'
                elif s_brx == "12": return 'kitty'
                elif s_brx == "13": return 'meow'
                elif s_brx == "14": return 'milk'
                elif s_brx == "15": return 'moofasa'
                elif s_brx == "16": return 'moose'
                elif s_brx == "17": return 'ren'
                elif s_brx == "18": return 'sheep'
                elif s_brx == "19": return 'skeleton'
                elif s_brx == "20": return 'stegosaurus'
                elif s_brx == "21": return 'stimpy'
                elif s_brx == "22": return 'surgery'
                elif s_brx == "23": return 'turkey'
                elif s_brx == "24": return 'turtle'
                elif s_brx == "25": return 'tux'
                elif s_brx.lower() == "b": break
        elif banerx in ("02","2"):
            while True:
                os.system('clear')
                bnr_m()
                tr_brx = input(f"\n{reed}inputx> {white}")
                if tr_brx == "": pass
                elif tr_brx == "26": return "android"
                elif tr_brx == "27": return "apple"
                elif tr_brx == "28": return "biohazard"
                elif tr_brx == "29": return "boy"
                elif tr_brx == "30": return "danger_skull"
                elif tr_brx == "31": return "deamon"
                elif tr_brx == "32": return "deamonl"
                elif tr_brx == "33": return "funny_skull"
                elif tr_brx == "34": return "github"
                elif tr_brx == "35": return "hanuman"
                elif tr_brx == "36": return "headphone_skull"
                elif tr_brx == "37": return "hydra"
                elif tr_brx == "38": return "linux"
                elif tr_brx == "39": return "lionston"
                elif tr_brx == "40": return "panda"
                elif tr_brx == "41": return "radioactive"
                elif tr_brx == "42": return "single_eye"
                elif tr_brx == "43": return "skull"
                elif tr_brx == "44": return "stop"
                elif tr_brx == "45": return "termux"
                elif tr_brx == "46": return "ubuntu"
                elif tr_brx == "47": return "warn"
                elif tr_brx.lower() == "b": break

font_maps = {
    "1": {"01":"3D-ASCII","02":"3D_Diagonal","03":"3-D","04":"3d","05":"3x5","06":"4Max","07":"5lineoblique",
          "08":"Acrobatic","09":"alligator3","10":"Alligator","11":"Alphabet","12":"Alpha","13":"AMC_3_Line",
          "14":"amc3line","15":"AMC_3_Liv1","16":"amc3liv1","17":"amcaaa01","18":"amcneko","19":"AMC_Neko",
          "20":"amcrazo2","21":"amcrazor","22":"amcslash","23":"amcslder","24":"amcthin","25":"amctubes",
          "26":"amcun1","27":"ANSI_Regular","28":"ANSI_Shadow","29":"Arrows","30":"ASCII_New_Roman",
          "31":"Avatar","32":"Banner3-D","33":"Banner3","34":"Banner4","35":"Banner","36":"Barbwire",
          "37":"Basic","38":"Bear","39":"Bell","40":"bigchief"},
    "2": {"41":"Big_Chief","42":"Bigfig","43":"Big","44":"Big_Money-ne","45":"Big_Money-nw","46":"Big_Money-se",
          "47":"Big_Money-sw","48":"Binary","49":"Block","50":"Blocks","51":"Bloody","52":"Bolger",
          "53":"Braced","54":"Bright","55":"Broadway","56":"Broadway_KB","57":"Bubble","58":"Bulbhead",
          "59":"Caligraphy2","60":"Caligraphy","61":"Calvin_S","62":"Cards","63":"Catwalk","64":"Chiseled",
          "65":"Chunky","66":"Coinstak","67":"Cola","68":"Colossal","69":"Computer","70":"Contessa",
          "71":"Contrast","72":"Cosmike","73":"Crawford2","74":"Crawford","75":"Crazy","76":"Cricket",
          "77":"Cursive","78":"Cyberlarge","79":"Cybermedium","80":"Cybersmall"},
    "3": {"81":"Cygnet","82":"DANC4","83":"Dancing_Font","84":"defleppard","85":"Delta_Corps_Priest_1",
          "86":"Diamond","87":"dietcola","88":"Digital","89":"Doh","90":"Doom","91":"DOS_Rebel",
          "92":"dotmatrix","93":"Double","94":"doubleshorts","95":"drpepper","96":"eftichess",
          "97":"eftifont","98":"eftirobot","99":"eftitalic","100":"eftiwall","101":"eftiwater",
          "102":"Electronic","103":"Elite","104":"Epic","105":"Fender","106":"Filter","107":"Fire_Font-k",
          "108":"Fire_Font-s","109":"Flipped","110":"flowerpower","111":"fourtops","112":"Fraktur",
          "113":"funface","114":"funfaces","115":"Fuzzy","116":"Georgi16","117":"Georgia11","118":"Ghost",
          "119":"Ghoulish","120":"Glenyn"},
    "4": {"121":"Goofy","122":"Gothic","123":"Graceful","124":"Gradient","125":"Graffiti","126":"Greek",
          "127":"halfiwi","128":"Heart_Left","129":"Heart_Right","130":"henry3d","131":"Hieroglyphs",
          "132":"Hollywood","133":"horizontalleft","134":"horizontalright","135":"Impossible","136":"Invita",
          "137":"Isometric1","138":"Isometric2","139":"Isometric3","140":"Isometric4","141":"Jacky",
          "142":"Jazmine","143":"Jerusalem","144":"JS_Block_Letters","145":"JS_Bracket_Letters",
          "146":"JS_Capital_Curves","147":"JS_Cursive","148":"JS_Stick_Letters","149":"Katakana",
          "150":"Kban","151":"Keyboard","152":"Knob","153":"larry3d","154":"LCD","155":"Lean",
          "156":"Letters","157":"lildevil","158":"lineblocks","159":"Linux","160":"Lockergnome"},
    "5": {"161":"Madrid","162":"Marquee","163":"Maxfour","164":"maxiwi","165":"Merlin1","166":"Merlin2",
          "167":"Mini","168":"miniwi","169":"Modular","170":"Moscow","171":"Muzzle","172":"Nancyj-Fancy",
          "173":"Nancyj","174":"Nancyj-Underlined","175":"Nipples","176":"NScript","177":"ntgreek",
          "178":"O8","179":"Ogre","180":"oldbanner","181":"OS2","182":"Patorjk-HeX",
          "183":"Patorjk_s_Cheese","184":"Pawp","185":"Peaks","186":"peaksslant","187":"Pebbles",
          "188":"Pepper","189":"Poison","190":"Puffy","191":"Puzzle","192":"Pyramid","193":"Rammstein",
          "194":"Rectangles","195":"Red_Phoenix","196":"Relief2","197":"Relief","198":"Reverse",
          "199":"Roman","200":"Rotated"},
    "6": {"201":"Rounded","202":"rowancap","203":"Rozzo","204":"Runyc","205":"santaclara","206":"sblood",
          "207":"Script","208":"Serifcap","209":"Shadow","210":"Shimrod","211":"Short","212":"Slant",
          "213":"Slide","214":"slscript","215":"SL_Script","216":"smallcaps","217":"Small","218":"smisome1",
          "219":"smkeyboard","220":"smscript","221":"smshadow","222":"smslant","223":"smtengwar",
          "224":"Soft","225":"Speed","226":"Spliff","227":"s-relief","228":"Stacey","229":"Stampate",
          "230":"Stampatello","231":"Standard","232":"starstrips","233":"Star_Strips","234":"starwars",
          "235":"Star_Wars","236":"Stellar","237":"Stforek","238":"Stick_Letters","239":"Stop",
          "240":"Straight"},
    "7": {"241":"Stronger_Than_All","242":"Sub-Zero","243":"swampland","244":"Swan","245":"Sweet",
          "246":"Tanja","247":"Tengwar","248":"Test1","249":"The_Edge","250":"Thick","251":"Thin",
          "252":"THIS","253":"Thorned","254":"Ticks","255":"ticksslant","256":"Tiles","257":"Tinker-Toy",
          "258":"Tombstone","259":"Train","260":"Trek","261":"Tsalagi","262":"Tubular","263":"Twisted",
          "264":"Univers","265":"usaflag","266":"Varsity","267":"Wavy","268":"Weird","269":"wetletter",
          "270":"Whimsy"}
}

font_funcs = {"1":fontsta,"2":fontstb,"3":fontstc,"4":fontstd,"5":fontste,"6":fontstf,"7":fontstg}

def fontsx():
    while True:
        os.system('clear')
        sel_set = input(fon_type)
        if sel_set == "":
            pass
        elif sel_set in font_maps:
            fn = font_funcs.get(sel_set)
            if fn:
                while True:
                    os.system('clear')
                    fn()
                    choice = input(f"{reset}{reed}inputx> {white}")
                    if choice == "":
                        pass
                    elif choice in font_maps[sel_set]:
                        return font_maps[sel_set][choice]
                    elif choice.lower() == "b":
                        break



os.system("rm bashrc_file > /dev/null 2>&1 &")
os.system("cp core/bashrc bashrc_file > /dev/null 2>&1 &")

while True:
    os.system('clear')
    maix = input(menux)
    if maix == "":
        pass
    elif maix in ("01","1"):
        typewriter_effect(">> Set Banner Only", cyan)
        sleep(0.3)
        s_ban = banners()
        prt_x = select_pt()
        prt_y = select_clr()
        pro_x = prt_x + prt_y
        filex = "bashrc_file"
        with open(filex, 'a') as file:
            file.write(f"\ncowsay -f {s_ban} 'Welcome To Termux!' | lolcat\n")
            file.write(f"\n{pro_x}\n")
        file.close()
        set_new_bnr()
    elif maix in ("02","2"):
        glitch_fade(">> Set Name Only", cyan)
        sleep(0.3)
        os.system('clear')
        print()
        while True:
            namex = input(f"{reset}{cyan}[{white}+{cyan}] Enter Your Name: {white}")
            if namex == '':
                pass
            else:
                break
        s_fnt = fontsx()
        prt_x = select_pt()
        prt_y = select_clr()
        pro_x = prt_x + prt_y
        filex = "bashrc_file"
        with open(filex, 'a') as file:
            file.write(f"\nfiglet -f {s_fnt} '{namex}' | lolcat\n")
            file.write(f"\n{pro_x}\n")
        file.close()
        set_new_bnr()
    elif maix in ("03","3"):
        typewriter_effect(">> Set Banner With Name", cyan)
        sleep(0.3)
        sn_bnr = banners()
        os.system('clear')
        print()
        while True:
            namexx = input(f"{cyan}[{white}+{cyan}] Enter Your Name: {white}")
            if namexx == '':
                pass
            else:
                break
        sn_fnt = fontsx()
        ps_x = select_pt()
        ps_y = select_clr()
        pr_x = ps_x + ps_y
        filex = "bashrc_file"
        with open(filex, 'a') as file:
            file.write(f"\ncowsay -f {sn_bnr} 'Welcome To Termux!' | lolcat\n")
            file.write("echo")
            file.write(f"\nfiglet -f {sn_fnt} '{namexx}' | lolcat\n")
            file.write(f"\n{pr_x}\n")
        file.close()
        set_new_bnr()
    elif maix in ("04","4"):
        glitch_fade(">> Restore Default", yellow)
        sleep(0.3)
        restore_dflt()
    elif maix in ("05","5"):
        hack_glitch(">> More Tools", cyan)
        sleep(0.3)
        print(f"\n{cyan}[{white}+{cyan}] Opening tool list..\n")
        sleep(1)
        os.system("xdg-open https://github.com/cyberrasel999?tab=repositories > /dev/null 2>&1 &")
        input(f"{blue}Press ENTER To Back")
    elif maix in ("06","6"):
        glitch_fade(">> About RASEL V1", purple)
        sleep(0.3)
        os.system('clear')
        print()
        for line in about_tool.split('\n'):
            typewriter_effect(line, cyan)
        input(f"\n{blue}Press ENTER To Back")
    elif maix.lower() == "e":
        glitch_fade(">> Exiting RASEL V1...", reed)
        sleep(0.3)
        exited()
