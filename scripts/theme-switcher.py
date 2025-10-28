#ranger097
#so far i only need subprocess and pillow idk but im sure there is a library that can do this easier
import subprocess
import PIL
from PIL import ImageColor

#make sure to specify the correct path to wallpapers here
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

#specify configs globally so lines can be changed in functions
state = "/home/ranger/Github/waybar-theme-switcher/state/themes.txt"
bottom_bar_css = "/home/ranger/.config/waybar/bottom_bar.css"
top_bar_css = "/home/ranger/.config/waybar/style.css"
vscode_theme = "/home/ranger/.config/Code/User/settings.json"
ghostty_theme = "/home/ranger/.config/ghostty/config"
hex_colors = "/home/ranger/.cache/wal/colors"

#this gets the colors from pywal
with open(hex_colors, "r") as wal_colors:
    wal_colors_lines = wal_colors.readlines()
    blurredBackground = ImageColor.getcolor(wal_colors_lines[0], "RGB")
    iconBackground  = ImageColor.getcolor(wal_colors_lines[1], "RGB")
    hoverBackground = ImageColor.getcolor(wal_colors_lines[0], "RGB")
    widgetIconBackground = ImageColor.getcolor(wal_colors_lines[0], "RGB")
    widgetIconForeground = wal_colors_lines[3].strip()
    iconForeground = wal_colors_lines[6].strip()
    textForeground = wal_colors_lines[7].strip()
    vscodeBackground = wal_colors_lines[0].strip()
    ghosttyBackground = wal_colors_lines[0].strip()
    ghosttyForeground = wal_colors_lines[4].strip()
    hoverForeground = wal_colors_lines[9].strip()
    
def themeSwitcher():
    
    with open(bottom_bar_css, 'r') as bottom_bar_config:
        lines = bottom_bar_config.readlines()
        lines[8] = f"background-color: rgba{blurredBackground};" + "\n" #waybarBackground
        lines[29] = f"background-color: rgba{iconBackground};" + "\n" #vscodeIconBackground
        lines[46] = f"background-color: rgba{iconBackground};" + "\n" #yt-musicIconBackground
        lines[64] = f"background-color: rgba{iconBackground};" + "\n" #youtubeIconBackground
        lines[82] = f"background-color: rgba{iconBackground};" + "\n" #ryujinxIconBackground
        lines[100] = f"background-color: rgba{iconBackground};" + "\n" #discordIconBackground
        lines[117] = f"background-color: rgba{iconBackground};" + "\n" #steamIconBackground
        lines[134] = f"background-color: rgba{iconBackground};" + "\n" #dolphinIconBackground
        lines[153] = f"background-color: rgba{iconBackground};" + "\n" #gimpIconBackground
        lines[170] = f"background-color: rgba{iconBackground};" + "\n" #kdenliveIconBackground
        lines[187] = f"background-color: rgba{iconBackground};" + "\n" #inkscrapeIconBackground
        lines[204] = f"background-color: rgba{iconBackground};" + "\n" #ghosttyIconBackground
        lines[221] = f"background-color: rgba{iconBackground};" + "\n" #unityIconBackground
        lines[238] = f"background-color: rgba{iconBackground};" + "\n" #blenderIconBackground
        lines[255] = f"background-color: rgba{iconBackground};" + "\n" #libreofficeIconBackground
        lines[272] = f"background-color: rgba{iconBackground};" + "\n" #obsIconBackground
        lines[289] = f"background-color: rgba{iconBackground};" + "\n" #shortwaveIconBackground
        lines[306] = f"background-color: rgba{iconBackground};" + "\n" #obsidianIconBackground
        lines[322] = f"background-color: rgba{iconBackground};" + "\n" #godotIconBackground
        lines[339] = f"background-color: rgba{iconBackground};" + "\n" #ardourIconBackground
        lines[356] = f"background-color: rgba{iconBackground};" + "\n" #btdbattlesIconBackground
        lines[373] = f"background-color: rgba{iconBackground};" + "\n" #qt6settingsIconBackground 
        lines[390] = f"background-color: rgba{iconBackground};" + "\n" #theFinalsIconBackground
        lines[408] = f"background-color: rgba{iconBackground};" + "\n" #personaIconBackground
        lines[425] = f"background-color: rgba{iconBackground};" + "\n" #minecraftIconBackground
        lines[442] = f"background-color: rgba{iconBackground};" + "\n" #firefoxIconBackground
        lines[472] = f"background-color: rgba{hoverBackground};" +"\n" #hoverIconBackground
        lines[31] = f"color:{iconForeground};" + "\n" #vscodeIconForeground
        lines[48] = f"color:{iconForeground};" + "\n" #yt-musicIconForeground
        lines[66] = f"color:{iconForeground};" + "\n" #youtubeIconForeground
        lines[84] = f"color:{iconForeground};" + "\n" #ryujinxIconForeground
        lines[102] = f"color:{iconForeground};" + "\n" #discordIconForeground
        lines[119] = f"color:{iconForeground};" + "\n" #steamIconForeground
        lines[136] = f"color:{iconForeground};" + "\n" #dolphinIconForeground
        lines[155] = f"color:{iconForeground};" + "\n" #gimpIconForeground
        lines[172] = f"color:{iconForeground};" + "\n" #kdenliveIconForeground
        lines[189] = f"color:{iconForeground};" + "\n" #inkscapeIconForeground
        lines[206] = f"color:{iconForeground};" + "\n" #ghosttyIconForeground
        lines[223] = f"color:{iconForeground};" + "\n" #unityIconForeground
        lines[240] = f"color:{iconForeground};" + "\n" #blenderIconForeground
        lines[257] = f"color:{iconForeground};" + "\n" #libreofficeIconForeground
        lines[274] = f"color:{iconForeground};" + "\n" #obsIconForeground
        lines[291] = f"color:{iconForeground};" + "\n" #shortwaveIconForeground
        lines[308] = f"color:{iconForeground};" + "\n" #obsidianIconForeground
        lines[324] = f"color:{iconForeground};" + "\n" #godotIconForeground
        lines[341] = f"color:{iconForeground};" + "\n" #ardourIconForeground
        lines[358] = f"color:{iconForeground};" + "\n" #btdbattlesIconForeground
        lines[375] = f"color:{iconForeground};" + "\n" #qt6settingsIconForeground
        lines[392] = f"color:{iconForeground};" + "\n" #thefinalsIconForeground
        lines[410] = f"color:{iconForeground};" + "\n" #personaIconForeground
        lines[427] = f"color:{iconForeground};" + "\n" #minecraftIconForeground
        lines[444] = f"color:{iconForeground};" + "\n" #firefoxIconForeground
        lines[473] = f"color:{hoverForeground};" + "\n" #hoverIconForeground

    with open(bottom_bar_css, "w") as bottom_bar_config:
        bottom_bar_config.writelines(lines)
   
    with open(top_bar_css, "r") as top_bar_config:
        top_bar_lines = top_bar_config.readlines()
        top_bar_lines[1] = f"background-color: rgba{blurredBackground};" + "\n"  #windowBackground
        top_bar_lines[8] = f"background-color: rgba{widgetIconBackground};" + "\n" #workspaceBackground
        top_bar_lines[52] = f"background-color: rgba{widgetIconBackground};" + "\n" #activeWorkspaceBackground
        top_bar_lines[81] = f"background-color: rgba{widgetIconBackground};" + "\n" #clockBackground
        top_bar_lines[101] = f"background-color: rgba{widgetIconBackground};" + "\n" #batteryBackground
        top_bar_lines[158] = f"background-color: rgba{widgetIconBackground};" + "\n" #networkBackground
        top_bar_lines[186] = f"background-color: rgba{widgetIconBackground};" + "\n" #customLogoBackground
        top_bar_lines[222] = f"background-color: rgba{widgetIconBackground};" + "\n" #mprisBackground
        top_bar_lines[303] = f"background-color: rgba{widgetIconBackground};" + "\n" #wifiIconBackground
        top_bar_lines[323] = f"background-color: rgba{widgetIconBackground};" + "\n" #customAudioIconBackground
        top_bar_lines[343] = f"background-color: rgba{widgetIconBackground};" + "\n" #customAudioBackground
        top_bar_lines[362] = f"background-color: rgba{widgetIconBackground};" + "\n" #customBluetoothBackground
        top_bar_lines[382] = f"background-color: rgba{widgetIconBackground};" + "\n" #customBluetoothLabelBackground
        top_bar_lines[402] = f"background-color: rgba{widgetIconBackground};" + "\n" #customClockIconBackground
        top_bar_lines[422] = f"background-color: rgba{widgetIconBackground};" + "\n" #windowTitleBackground
        top_bar_lines[443] = f"background-color: rgba{widgetIconBackground};" + "\n" #hyprshotBackground
        top_bar_lines[464] = f"background-color: rgba{widgetIconBackground};" + "\n" #hyprpickerBackground
        top_bar_lines[485] = f"background-color: rgba{widgetIconBackground};" + "\n" #customShurikenBackground
        top_bar_lines[506] = f"background-color: rgba{widgetIconBackground};" + "\n" #customPowerBackground
        top_bar_lines[9] = f"color:{widgetIconForeground};" + "\n" #workspaceIconForeground
        top_bar_lines[53] = f"color:{widgetIconForeground};" + "\n" #workspaceActiveIconForeground
        top_bar_lines[58] = f"color:{widgetIconForeground};" + "\n" #workspaceUrgentIconForeground
        top_bar_lines[102] = f"color:{widgetIconForeground};" + "\n" #batteryForeground
        top_bar_lines[304] = f"color:{widgetIconForeground};" + "\n" #wifiIconForeground
        top_bar_lines[324] = f"color:{widgetIconForeground};" + "\n" #audioIconForeground
        top_bar_lines[363] = f"color:{widgetIconForeground};" + "\n" #customBluetoothIconForeground
        top_bar_lines[444] = f"color:{widgetIconForeground};" + "\n" #hyprshotIconForeground
        top_bar_lines[465] = f"color:{widgetIconForeground};" + "\n" #hyprpickerIconForeground
        top_bar_lines[486] = f"color:{widgetIconForeground};" + "\n" #shurikenIconForeground
        top_bar_lines[507] = f"color:{widgetIconForeground};" + "\n" #customPowerIconForeground
        top_bar_lines[82] = f"color:{textForeground};" + "\n" #clockTextForeground
        top_bar_lines[159] = f"color:{textForeground};" + "\n" #networkTextForeground
        top_bar_lines[187] = f"color:{textForeground};" + "\n" #customLogoTextForeground
        top_bar_lines[223] = f"color:{textForeground};" + "\n" #mprisTextForeground
        top_bar_lines[344] = f"color:{textForeground};" + "\n" #customAudioTextForeground
        top_bar_lines[383] = f"color:{textForeground};" + "\n" #customBluetoothLabel
        
    with open(top_bar_css, "w") as top_bar_config:
        top_bar_config.writelines(top_bar_lines)

    with open(vscode_theme, "r") as vscode_config:
        vscode_lines = vscode_config.readlines()
        vscode_lines[155] = f'"editor.background": "{vscodeBackground}",' + "\n" 
        vscode_lines[156] = f'"activityBar.background": "{vscodeBackground}",' + "\n"
        vscode_lines[157] = f'"sideBar.background": "{vscodeBackground}",' + "\n"
        vscode_lines[158] = f'"editorGroupHeader.tabsBackground": "{vscodeBackground}",' + "\n"

    with open(vscode_theme, "w") as vscode_config:
        vscode_config.writelines(vscode_lines)

    with open(ghostty_theme, "r") as ghostty_config:
        ghostty_lines = ghostty_config.readlines()
        ghostty_lines[43] = f'background = "{ghosttyBackground}"' + "\n"
        ghostty_lines[44] = f'foreground = "{ghosttyForeground}"' + "\n"

    with open(ghostty_theme, "w") as ghostty_config:
        ghostty_config.writelines(ghostty_lines)


def wallpapers():
    
    with open(state, 'r') as state_management:
        wallpaper_state = state_management.readlines()
        cache = wallpaper_state[0]
        num = int(cache)
        if num > len(wallpaperDict) or num > 90:
            num = 0
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])
   
            x = wallpaperDict[num]
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
            wallpapers()
            
        elif num == 47:
             wallpaper_state[0] = str(num)
             with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])
             num = num + 1
             x = wallpaperDict[num]
             subprocess.run(["wal", "-i", x])
             themeSwitcher()
             subprocess.run(["pkill", "waybar"])
             subprocess.run(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
             subprocess.run(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
             subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
             
            
        
        else:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])
   
            print(cache)
   
            x = wallpaperDict[num]
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
            

wallpapers()
