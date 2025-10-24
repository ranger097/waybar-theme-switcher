import subprocess

wallpaperDict = { 
    0 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper1.png",
    1 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper1.png",
    2 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper2.png",
    3 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper3.png",
    4 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper4.png",
    5 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper5.png",
    6 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper6.png",
    7 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper7.jpg",
    8 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper8.jpg",
    9 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper9.png",
    10 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper10.png",
    11 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper11.jpg",
    12 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper12.jpg",
    13 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper13.png",
    14 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper14.png",
    15 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper15.jpg",
    16 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper16.png",
    17 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper17.jpg",
    18 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper18.jpeg",
    19 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper19.jpeg",
    20 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper20.jpeg",
    21 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper21.png",
    22 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper22.jpg",
    23 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper23.jpg",
    24 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper24.jpg",
    25 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper25.jpg",
    26 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper26.jpg",
    27 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper27.jpg",
    28 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper28.jpg",
    29 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper29.png",
    30 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper30.png",
    31 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper31.jpeg",
    32 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper32.png",
    33 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper33.jpeg",
    34 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper34.jpg",
    35 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper35.jpg",
    36 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper36.jpg",
    37 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper37.jpg",
    38 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper38.jpg",
    39 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper39.png",
    40 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper40.jpg",
    41 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper41.png",
    42 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper42.jpg",
    43 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper43.jpg",
    44 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper44.png",
    45 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper45.png",
    46 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper46.png",
    47 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper47.png",
    48 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper48.png",
    49 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper49.jpg",
    50 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper50.jpg",
    51 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper51.png",
    52 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper52.png",
    53 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper53.jpg",
    54 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper54.jpg",
    55 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper55.png",
    56 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper56.png",
    57 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper57.png",
    58 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper58.jpg",
    59 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper59.jpg",
    60 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper60.png",
    61 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper61.jpg",
    62 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper62.png",
    63 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper63.jpg",
    64 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper64.png",
    65 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper65.jpg",
    66 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper66.png",
    67 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper67.jpg",
    68 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper68.png",
    69 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper69.png",
    70 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper70.jpg",
    71 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper71.png",
    72 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper72.png",
    73 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper73.jpg",
    74 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper74.png",
    75 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper75.png",
    76 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper76.png",
    77 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper77.jpg",
    78 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper78.jpg",
    79 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper79.png",
    80 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper80.jpg",
    81 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper81.png",
    82 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper82.jpg",
    83 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper83.jpg",
    84 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper84.png",
    85 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper85.png",
    86 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper86.jpg",
    87 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper87.png",
    88 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper88.png",
    89 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper89.png",
    90 : "/home/ranger/Github/waybar-theme-switcher/wallpapers/wallpaper90.png"
}

def wallpapers():
    state = "/home/ranger/Github/waybar-theme-switcher/state/wallpapers.txt"
    with open(state, 'r') as state_management:
        wallpaper_state = state_management.readlines()
        cache = wallpaper_state[0]
        num = int(cache)
        if num > len(wallpaperDict):
            num = 0
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])
   
            x = wallpaperDict[num]

            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"], check=True)
            subprocess.run(["wal", "-i", x], check=True)
            
            print("Please check your wallpaper paths!")
            print("- ranger097")

            wallpapers()

        elif num == 59:
            
            num = num + 1
            
            bottom_bar_css = "/home/ranger/.config/waybar/bottom_bar.css"
            top_bar_css = "/home/ranger/.config/waybar/style.css"
            vscode_theme = "/home/ranger/.config/Code/User/settings.json"
            ghostty_theme = "/home/ranger/.config/ghostty/config"
            with open(bottom_bar_css, 'r') as bottom_bar_config:
                lines = bottom_bar_config.readlines()
                lines[32] = "background-color: rgba(255,240,207,0.8);" + "\n"
                lines[50] = "background-color: rgba(255,240,207,0.8);" + "\n"
                lines[89] = "background-color: rgba(255,240,207,0.8);" + "\n"
                lines[31] = "color: #ED1651;" + "\n"
                lines[51] = "color: #ED1651;" + "\n"
                lines[91] = "color: #ED1651;" + "\n"
            with open(bottom_bar_css, "w") as bottom_bar_config:
                bottom_bar_config.writelines(lines)
            
           
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            with open(ghostty_theme, "r") as ghostty_config:
                ghostty_lines = ghostty_config.readlines()
                ghostty_lines[43] = 'background = "#fff0cf"' + "\n"
                ghostty_lines[44] = 'foreground = "#ED1651"' + "\n"

            with open(ghostty_theme, "w") as ghostty_config:
                ghostty_config.writelines(ghostty_lines)
   
            with open(vscode_theme, "r") as vscode_config:
                vscode_lines = vscode_config.readlines()
                vscode_lines[155] = '"editor.background": "#FFF0CFCC",' + "\n"
                vscode_lines[156] = '"activityBar.background": "#FFF0CFCC",' + "\n"
                vscode_lines[157] = '"sideBar.background": "#FFF0CFCC",' + "\n"
                vscode_lines[158] = '"editorGroupHeader.tabsBackground": "#FFF0CFCC",' + "\n"

            with open(vscode_theme, "w") as vscode_config:
                vscode_config.writelines(vscode_lines)

            with open(top_bar_css, "r") as top_bar_config:
                top_bar_lines = top_bar_config.readlines()

                top_bar_lines[187] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[188] = "color: #ed1651;" + "\n"
                top_bar_lines[14] =  "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[15] =  "color: #ed1651;" + "\n"
                top_bar_lines[116] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[117] = "color: #ed1651;" + "\n"
                top_bar_lines[132] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[133] = "color: #ed1651;" + "\n"
                top_bar_lines[203] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[205] = "color: #ed1651;" + "\n"
                top_bar_lines[149] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[150] = "color: #ed1651;" + "\n"
                top_bar_lines[307] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[308] = "color: #ed1651;" + "\n"
                top_bar_lines[323] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[324] = "color: #ed1651;" + "\n" #icon
                top_bar_lines[39] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[41] = "color: #ed1651;" + "\n"
                top_bar_lines[356] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[357] = "color: #ed1651;" + "\n" #icon
                top_bar_lines[340] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[341] = "color: #ed1651;" + "\n"
                top_bar_lines[290] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[291] = "color: #ed1651;" + "\n" #icon
                top_bar_lines[273] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[274] = "color: #ed1651;" + "\n" #icon
                top_bar_lines[256] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[257] = "color: #ed1651;" + "\n" #icon
                top_bar_lines[239] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[240] = "color: #000000;" + "\n" #icon
                top_bar_lines[171] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[173] = "color: #ed1651;" + "\n" 
                top_bar_lines[101] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[102] = "color: #ed1651;" + "\n" 
                top_bar_lines[84] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[85] = "color: #ed1651;" + "\n"

            with open(top_bar_css, "w") as top_bar_config:
                top_bar_config.writelines(top_bar_lines)

            print(cache)
   
            x = wallpaperDict[num]
            subprocess.run(["wal", "-i", x])
            subprocess.run(["pkill", "waybar"])
            subprocess.run(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.run(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"], check=True)
            

            print("Please check your wallpaper paths!")
            print("- ranger097")
            
        elif num == 69:
            
            
            
            bottom_bar_css = "/home/ranger/.config/waybar/bottom_bar.css"
            top_bar_css = "/home/ranger/.config/waybar/style.css"
            vscode_theme = "/home/ranger/.config/Code/User/settings.json"
            ghostty_theme = "/home/ranger/.config/ghostty/config"
            with open(bottom_bar_css, 'r') as bottom_bar_config:
                lines = bottom_bar_config.readlines()
                lines[32] = "background-color: rgba(255,0,60,0.8);" + "\n"
                lines[50] = "background-color: rgba(255,0,60,0.8);" + "\n"
                lines[89] = "background-color: rgba(255,0,60,0.8);" + "\n"
                lines[31] = "color: #000000;" + "\n"
                lines[51] = "color: #000000;" + "\n"
                lines[91] = "color: #000000;" + "\n"
            with open(bottom_bar_css, "w") as bottom_bar_config:
                bottom_bar_config.writelines(lines)
            
           
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            with open(ghostty_theme, "r") as ghostty_config:
                ghostty_lines = ghostty_config.readlines()
                ghostty_lines[43] = 'background = "#fff0cf"' + "\n"
                ghostty_lines[44] = 'foreground = "#ED1651"' + "\n"

            with open(ghostty_theme, "w") as ghostty_config:
                ghostty_config.writelines(ghostty_lines)
   
            with open(vscode_theme, "r") as vscode_config:
                vscode_lines = vscode_config.readlines()
                vscode_lines[155] = '"editor.background": "#FFF0CFCC",' + "\n"
                vscode_lines[156] = '"activityBar.background": "#FFF0CFCC",' + "\n"
                vscode_lines[157] = '"sideBar.background": "#FFF0CFCC",' + "\n"
                vscode_lines[158] = '"editorGroupHeader.tabsBackground": "#FFF0CFCC",' + "\n"

            with open(vscode_theme, "w") as vscode_config:
                vscode_config.writelines(vscode_lines)

            with open(top_bar_css, "r") as top_bar_config:
                top_bar_lines = top_bar_config.readlines()

                top_bar_lines[187] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[188] = "color: #ed1651;" + "\n"
                top_bar_lines[14] =  "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[15] =  "color: #ed1651;" + "\n"
                top_bar_lines[116] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[117] = "color: #ed1651;" + "\n"
                top_bar_lines[132] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[133] = "color: #ed1651;" + "\n"
                top_bar_lines[203] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[205] = "color: #ed1651;" + "\n"
                top_bar_lines[149] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[150] = "color: #ed1651;" + "\n"
                top_bar_lines[307] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[308] = "color: #ed1651;" + "\n"
                top_bar_lines[323] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[324] = "color: #FEB990;" + "\n" #icon
                top_bar_lines[39] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[41] = "color: #ed1651;" + "\n"
                top_bar_lines[356] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[357] = "color: #FEB990;" + "\n" #icon
                top_bar_lines[340] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[341] = "color: #ed1651;" + "\n"
                top_bar_lines[290] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[291] = "color: #FEB990;" + "\n" #icon
                top_bar_lines[273] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[274] = "color: #FEB990;" + "\n" #icon
                top_bar_lines[256] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[257] = "color: #FEB990;" + "\n" #icon
                top_bar_lines[239] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[240] = "color: #FEB990;" + "\n" #icon
                top_bar_lines[171] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[173] = "color: #ed1651;" + "\n" 
                top_bar_lines[101] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[102] = "color: #ed1651;" + "\n" 
                top_bar_lines[84] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[85] = "color: #ed1651;" + "\n"

            with open(top_bar_css, "w") as top_bar_config:
                top_bar_config.writelines(top_bar_lines)

            print(cache)
   
            x = wallpaperDict[num]
            subprocess.run(["wal", "-i", x])
            subprocess.run(["pkill", "waybar"])
            subprocess.run(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.run(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"], check=True)
            

            print("Please check your wallpaper paths!")
            print("- ranger097")
            num = num + 1
        elif num == 87:
            num = num + 1
            
            
            bottom_bar_css = "/home/ranger/.config/waybar/bottom_bar.css"
            top_bar_css = "/home/ranger/.config/waybar/style.css"
            vscode_theme = "/home/ranger/.config/Code/User/settings.json"
            ghostty_theme = "/home/ranger/.config/ghostty/config"
            with open(bottom_bar_css, 'r') as bottom_bar_config:
                lines = bottom_bar_config.readlines()
                lines[32] = "background-color: rgba(254,185,144,0.7);" + "\n"
                lines[50] = "background-color: rgba(254,185,144,0.7);" + "\n"
                lines[89] = "background-color: rgba(254,185,144,0.7);" + "\n"
                lines[31] = "color: #1B1811;" + "\n"
                lines[51] = "color: #1B1811;" + "\n"
                lines[91] = "color: #1B1811;" + "\n"
            with open(bottom_bar_css, "w") as bottom_bar_config:
                bottom_bar_config.writelines(lines)
            
           
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            with open(ghostty_theme, "r") as ghostty_config:
                ghostty_lines = ghostty_config.readlines()
                ghostty_lines[43] = 'background = "#89624A"' + "\n"
                ghostty_lines[44] = 'foreground = "#1B1811"' + "\n"

            with open(ghostty_theme, "w") as ghostty_config:
                ghostty_config.writelines(ghostty_lines)
   
            with open(vscode_theme, "r") as vscode_config:
                vscode_lines = vscode_config.readlines()
                vscode_lines[155] = '"editor.background": "#FEB990",' + "\n"
                vscode_lines[156] = '"activityBar.background": "#FEB990",' + "\n"
                vscode_lines[157] = '"sideBar.background": "#FEB990",' + "\n"
                vscode_lines[158] = '"editorGroupHeader.tabsBackground": "#FEB990",' + "\n"

            with open(vscode_theme, "w") as vscode_config:
                vscode_config.writelines(vscode_lines)

            with open(top_bar_css, "r") as top_bar_config:
                top_bar_lines = top_bar_config.readlines()

                top_bar_lines[187] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[188] = "color: #FEB990;" + "\n"
                top_bar_lines[14] =  "background-color: rgba(137,98,74,0.0);" + "\n" #keep-transparent
                top_bar_lines[15] =  "color: #1B1811;" + "\n"
                top_bar_lines[116] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[117] = "color: #1B1811;" + "\n"
                top_bar_lines[132] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[133] = "color: #1B1811;" + "\n"
                top_bar_lines[203] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[205] = "color: #FEB990;" + "\n"
                top_bar_lines[149] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[150] = "color: #1B1811;" + "\n"
                top_bar_lines[307] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[308] = "color: #1B1811;" + "\n"
                top_bar_lines[323] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[324] = "color: #FEB990;" + "\n" #icon
                top_bar_lines[39] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[41] = "color: #1B1811;" + "\n"
                top_bar_lines[356] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[357] = "color: #FEB990;" + "\n" #icon
                top_bar_lines[340] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[341] = "color: #1B1811;" + "\n"
                top_bar_lines[290] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[291] = "color: #FEB990;" + "\n" #icon
                top_bar_lines[273] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[274] = "color: #FEB990;" + "\n" #icon
                top_bar_lines[256] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[257] = "color: #FEB990;" + "\n" #icon
                top_bar_lines[239] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[240] = "color: #FEB990;" + "\n" #icon
                top_bar_lines[171] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[173] = "color: #FEB990;" + "\n" 
                top_bar_lines[101] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[102] = "color: #FEB990;" + "\n" 
                top_bar_lines[84] = "background-color: rgba(137,98,74,0.7);" + "\n"
                top_bar_lines[85] = "color: #1B1811;" + "\n"
                top_bar_lines[56] = "color: #FEB990;" + "\n"

            with open(top_bar_css, "w") as top_bar_config:
                top_bar_config.writelines(top_bar_lines)

            print(cache)
   
            x = wallpaperDict[num]
            subprocess.run(["wal", "-i", x])
            subprocess.run(["pkill", "waybar"])
            subprocess.run(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.run(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"], check=True)
            

            print("Please check your wallpaper paths!")
            print("- ranger097")
            
            
        elif num == 63:
            
            num = num + 1
            
            bottom_bar_css = "/home/ranger/.config/waybar/bottom_bar.css"
            top_bar_css = "/home/ranger/.config/waybar/style.css"
            vscode_theme = "/home/ranger/.config/Code/User/settings.json"
            ghostty_theme = "/home/ranger/.config/ghostty/config"
            with open(bottom_bar_css, 'r') as bottom_bar_config:
                lines = bottom_bar_config.readlines()
                lines[32] = "background-color: rgba(255,240,207,0.8);" + "\n"
                lines[50] = "background-color: rgba(255,240,207,0.8);" + "\n"
                lines[89] = "background-color: rgba(255,240,207,0.8);" + "\n"
                lines[31] = "color: #ED1651;" + "\n"
                lines[51] = "color: #ED1651;" + "\n"
                lines[91] = "color: #ED1651;" + "\n"
            with open(bottom_bar_css, "w") as bottom_bar_config:
                bottom_bar_config.writelines(lines)
            
           
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            with open(ghostty_theme, "r") as ghostty_config:
                ghostty_lines = ghostty_config.readlines()
                ghostty_lines[43] = 'background = "#fff0cf"' + "\n"
                ghostty_lines[44] = 'foreground = "#ED1651"' + "\n"

            with open(ghostty_theme, "w") as ghostty_config:
                ghostty_config.writelines(ghostty_lines)
   
            with open(vscode_theme, "r") as vscode_config:
                vscode_lines = vscode_config.readlines()
                vscode_lines[155] = '"editor.background": "#FFF0CFCC",' + "\n"
                vscode_lines[156] = '"activityBar.background": "#FFF0CFCC",' + "\n"
                vscode_lines[157] = '"sideBar.background": "#FFF0CFCC",' + "\n"
                vscode_lines[158] = '"editorGroupHeader.tabsBackground": "#FFF0CFCC",' + "\n"

            with open(vscode_theme, "w") as vscode_config:
                vscode_config.writelines(vscode_lines)

            with open(top_bar_css, "r") as top_bar_config:
                top_bar_lines = top_bar_config.readlines()

                top_bar_lines[187] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[188] = "color: #ed1651;" + "\n"
                top_bar_lines[14] =  "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[15] =  "color: #ed1651;" + "\n"
                top_bar_lines[116] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[117] = "color: #ed1651;" + "\n"
                top_bar_lines[132] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[133] = "color: #ed1651;" + "\n"
                top_bar_lines[203] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[205] = "color: #ed1651;" + "\n"
                top_bar_lines[149] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[150] = "color: #ed1651;" + "\n"
                top_bar_lines[307] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[308] = "color: #ed1651;" + "\n"
                top_bar_lines[323] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[324] = "color: #ed1651;" + "\n" #icon
                top_bar_lines[39] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[41] = "color: #ed1651;" + "\n"
                top_bar_lines[356] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[357] = "color: #ed1651;" + "\n" #icon
                top_bar_lines[340] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[341] = "color: #ed1651;" + "\n"
                top_bar_lines[290] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[291] = "color: #ed1651;" + "\n" #icon
                top_bar_lines[273] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[274] = "color: #ed1651;" + "\n" #icon
                top_bar_lines[256] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[257] = "color: #ed1651;" + "\n" #icon
                top_bar_lines[239] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[240] = "color: #000000;" + "\n" #icon
                top_bar_lines[171] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[173] = "color: #ed1651;" + "\n" 
                top_bar_lines[101] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[102] = "color: #ed1651;" + "\n" 
                top_bar_lines[84] = "background-color: rgba(255,240,207,0.8);" + "\n"
                top_bar_lines[85] = "color: #ed1651;" + "\n"

            with open(top_bar_css, "w") as top_bar_config:
                top_bar_config.writelines(top_bar_lines)

            print(cache)
   
            x = wallpaperDict[num]
            subprocess.run(["wal", "-i", x])
            subprocess.run(["pkill", "waybar"])
            subprocess.run(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.run(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"], check=True)
            

            print("Please check your wallpaper paths!")
            print("- ranger097")

        else:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])
   
            print(cache)
   
            x = wallpaperDict[num]
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"], check=True)
            #subprocess.run(["wal", "-i", x], check=True)
            print("Please check your wallpaper paths!")
            print("- ranger097")

wallpapers()





 
