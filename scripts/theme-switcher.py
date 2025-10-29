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
hyprland = "/home/ranger/.config/hypr/hyprland.conf"
    
def themeSwitcher():
    #this gets the colors from pywal
    with open(hex_colors, "r") as wal_colors:
        wal_colors_lines = wal_colors.readlines()
        blurredBackground1 = ImageColor.getcolor(wal_colors_lines[0], "RGB")
        blurredBackground = blurredBackground1 + (0.7,)
        iconBackground  = ImageColor.getcolor(wal_colors_lines[3], "RGB")
        iconBackground = iconBackground + (0.3,)
        hoverBackground = ImageColor.getcolor(wal_colors_lines[0], "RGB")
        hoverBackground = hoverBackground + (0.7,)
        widgetIconBackground = ImageColor.getcolor(wal_colors_lines[5], "RGB")
        widgetIconBackground = widgetIconBackground + (1.0,)
        rgba_str = f"rgba({widgetIconBackground[0]}, {widgetIconBackground[1]}, {widgetIconBackground[2]}, {widgetIconBackground[3]})"
        clean_col = rgba_str.replace(" ", "")
        widgetIconBackground = clean_col
        print(widgetIconBackground)
        widgetIconForeground = wal_colors_lines[0].strip()
        iconForeground = wal_colors_lines[5].strip()
        textForeground = wal_colors_lines[15].strip()
        vscodeBackground = wal_colors_lines[0].strip()
        ghosttyBackground = wal_colors_lines[0].strip()
        ghosttyForeground = wal_colors_lines[4].strip()
        hoverForeground = wal_colors_lines[9].strip()
        
        print(blurredBackground)
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
        lines[31] = f"color:{textForeground};" + "\n" #vscodeIconForeground
        lines[48] = f"color:{textForeground};" + "\n" #yt-musicIconForeground
        lines[66] = f"color:{textForeground};" + "\n" #youtubeIconForeground
        lines[84] = f"color:{textForeground};" + "\n" #ryujinxIconForeground
        lines[102] = f"color:{textForeground};" + "\n" #discordIconForeground
        lines[119] = f"color:{textForeground};" + "\n" #steamIconForeground
        lines[136] = f"color:{textForeground};" + "\n" #dolphinIconForeground
        lines[155] = f"color:{textForeground};" + "\n" #gimpIconForeground
        lines[172] = f"color:{textForeground};" + "\n" #kdenliveIconForeground
        lines[189] = f"color:{textForeground};" + "\n" #inkscapeIconForeground
        lines[206] = f"color:{textForeground};" + "\n" #ghosttyIconForeground
        lines[223] = f"color:{textForeground};" + "\n" #unityIconForeground
        lines[240] = f"color:{textForeground};" + "\n" #blenderIconForeground
        lines[257] = f"color:{textForeground};" + "\n" #libreofficeIconForeground
        lines[274] = f"color:{textForeground};" + "\n" #obsIconForeground
        lines[291] = f"color:{textForeground};" + "\n" #shortwaveIconForeground
        lines[308] = f"color:{textForeground};" + "\n" #obsidianIconForeground
        lines[324] = f"color:{textForeground};" + "\n" #godotIconForeground
        lines[341] = f"color:{textForeground};" + "\n" #ardourIconForeground
        lines[358] = f"color:{textForeground};" + "\n" #btdbattlesIconForeground
        lines[375] = f"color:{textForeground};" + "\n" #qt6settingsIconForeground
        lines[392] = f"color:{textForeground};" + "\n" #thefinalsIconForeground
        lines[410] = f"color:{textForeground};" + "\n" #personaIconForeground
        lines[427] = f"color:{textForeground};" + "\n" #minecraftIconForeground
        lines[444] = f"color:{textForeground};" + "\n" #firefoxIconForeground
        lines[473] = f"color:{hoverForeground};" + "\n" #hoverIconForeground
        lines[11] = f"border: 2px solid {iconForeground};" + "\n" #waybarBottomBorder

    with open(bottom_bar_css, "w") as bottom_bar_config:
        bottom_bar_config.writelines(lines)
   
    with open(top_bar_css, "r") as top_bar_config:
        top_bar_lines = top_bar_config.readlines()
        top_bar_lines[1] = f"background-color: rgba{blurredBackground};" + "\n"  #windowBackground
        top_bar_lines[20] = f"background-color: rgba{iconBackground};" + "\n" #workspaceBackground
        top_bar_lines[48] = f"background-color: rgba{iconBackground};" + "\n" #activeWorkspaceBackground
        top_bar_lines[92] = f"background-color: rgba{iconBackground};" + "\n" #clockBackground
        top_bar_lines[110] = f"background-color: rgba{iconBackground};" + "\n" #batteryBackground
        top_bar_lines[169] = f"background-color: rgba{iconBackground};" + "\n" #networkBackground
        top_bar_lines[192] = f"background-color: rgba{iconBackground};" + "\n" #customLogoBackground
        top_bar_lines[231] = f"background-color: rgba{iconBackground};" + "\n" #mprisBackground
        top_bar_lines[311] = f"background-color: rgba{iconBackground};" + "\n" #wifiIconBackground
        top_bar_lines[331] = f"background-color: rgba{iconBackground};" + "\n" #customAudioIconBackground
        top_bar_lines[350] = f"background-color: rgba{iconBackground};" + "\n" #customAudioBackground
        top_bar_lines[370] = f"background-color: rgba{iconBackground};" + "\n" #customBluetoothBackground
        top_bar_lines[390] = f"background-color: rgba{iconBackground};" + "\n" #customBluetoothLabelBackground
        top_bar_lines[410] = f"background-color: rgba{iconBackground};" + "\n" #customClockIconBackground
        top_bar_lines[431] = f"background-color: rgba{iconBackground};" + "\n" #windowTitleBackground
        top_bar_lines[452] = f"background-color: rgba{iconBackground};" + "\n" #hyprshotBackground
        top_bar_lines[473] = f"background-color: rgba{iconBackground};" + "\n" #hyprpickerBackground
        top_bar_lines[515] = f"background-color: rgba{iconBackground};" + "\n" #customShurikenBackground
        top_bar_lines[494] = f"background-color: rgba{iconBackground};" + "\n" #customPowerBackground
        top_bar_lines[21] = f"color:{iconForeground};" + "\n" #workspaceIconForeground
        top_bar_lines[49] = f"color:{iconForeground};" + "\n" #workspaceActiveIconForeground
        top_bar_lines[54] = f"color:{iconForeground};" + "\n" #workspaceUrgentIconForeground
        top_bar_lines[111] = f"color:{iconForeground};" + "\n" #batteryForeground
        top_bar_lines[312] = f"color:{iconForeground};" + "\n" #wifiIconForeground
        top_bar_lines[332] = f"color:{iconForeground};" + "\n" #audioIconForeground
        top_bar_lines[371] = f"color:{iconForeground};" + "\n" #customBluetoothIconForeground
        top_bar_lines[453] = f"color:{iconForeground};" + "\n" #hyprshotIconForeground
        top_bar_lines[474] = f"color:{iconForeground};" + "\n" #hyprpickerIconForeground
        top_bar_lines[516] = f"color:{iconForeground};" + "\n" #shurikenIconForeground
        top_bar_lines[495] = f"color:{iconForeground};" + "\n" #customPowerIconForeground
        top_bar_lines[93] = f"color:{textForeground};" + "\n" #clockTextForeground
        top_bar_lines[170] = f"color:{textForeground};" + "\n" #networkTextForeground
        top_bar_lines[193] = f"color:{textForeground};" + "\n" #customLogoTextForeground
        top_bar_lines[232] = f"color:{textForeground};" + "\n" #mprisTextForeground
        top_bar_lines[351] = f"color:{textForeground};" + "\n" #customAudioTextForeground
        top_bar_lines[391] = f"color:{textForeground};" + "\n" #customBluetoothLabel
        top_bar_lines[432] = f"color:{textForeground};" + "\n" #windowTitleForeground
        top_bar_lines[16] = f"border: 0px solid {widgetIconForeground};" + "\n" #workspaceButtonBorder
        top_bar_lines[88] = f"border: 0px solid {widgetIconForeground};" + "\n" #clockBorder
        top_bar_lines[106] = f"border: 0px solid {widgetIconForeground};" + "\n" #batteryBorder
        top_bar_lines[163] = f"border-top: 0px solid {widgetIconForeground};" + "\n" #networkBorderTop
        top_bar_lines[164] = f"border-right: 0px solid {widgetIconForeground};" + "\n" #networkBorderRight
        top_bar_lines[165] = f"border-bottom: 0px solid {widgetIconForeground};" + "\n" #networkBorderBottom
        top_bar_lines[188] = f"border: 0px solid {widgetIconForeground};" + "\n" #customLogoBorder
        top_bar_lines[227] = f"border: 0px solid {widgetIconForeground};" + "\n" #mprisBorder
        top_bar_lines[305] = f"border-top: 0px solid {widgetIconForeground};" + "\n" #wifiIconTopBorder
        top_bar_lines[306] = f"border-left: 0px solid {widgetIconForeground};" + "\n" #wifiIconLeftBorder
        top_bar_lines[307] = f"border-bottom: 0px solid {widgetIconForeground};" + "\n" #wifiIconBottomBorder
        top_bar_lines[325] = f"border-top: 0px solid {widgetIconForeground};" + "\n" #audioIconTopBorder
        top_bar_lines[326] = f"border-left: 0px solid {widgetIconForeground};" + "\n" #audioIconLeftBorder
        top_bar_lines[327] = f"border-bottom: 0px solid {widgetIconForeground};" + "\n" #audioIconBottomBorder
        top_bar_lines[344] = f"border-top: 0px solid {widgetIconForeground};" + "\n" #audiIconTopBorder
        top_bar_lines[345] = f"border-right: 0px solid {widgetIconForeground};" + "\n" #audioIconRightBorder
        top_bar_lines[346] = f"border-bottom: 0px solid {widgetIconForeground};" + "\n" #audioIconBottomBorder
        top_bar_lines[364] = f"border-top: 0px solid {widgetIconForeground};" + "\n" #customBluetoothTopIconBorder
        top_bar_lines[365] = f"border-left: 0px solid {widgetIconForeground};" + "\n" #customBluetoothLeftIconBorder
        top_bar_lines[366] = f"border-bottom: 0px solid {widgetIconForeground};" + "\n" #customBluetoothBottomIconBorder
        top_bar_lines[384] = f"border-top: 0px solid {widgetIconForeground};" + "\n" #customBluetoothLabelIconTopLabel
        top_bar_lines[385] = f"border-right: 0px solid {widgetIconForeground};" + "\n" #customBluetoothLabelIconRightLabel
        top_bar_lines[386] = f"border-bottom: 0px solid {widgetIconForeground};" + "\n" #customBluetoothLabelIconBottomLabel
        top_bar_lines[427] = f"border: 0px solid {widgetIconForeground};" + "\n" #windowTitleBorder
        top_bar_lines[448] = f"border: 0px solid {widgetIconForeground};" + "\n" #hyprshotBorder
        top_bar_lines[469] = f"border: 0px solid {widgetIconForeground};" + "\n" #hyprpickerBorder
        top_bar_lines[490] = f"border: 0px solid {widgetIconForeground};" + "\n" #customPowerBorder
        top_bar_lines[511] = f"border: 0px solid {widgetIconForeground};" + "\n" #shurikenBorder
        top_bar_lines[2] = f"border: 2px solid {iconForeground};" + "\n"

    with open(top_bar_css, "w") as top_bar_config:
        top_bar_config.writelines(top_bar_lines)

    with open(vscode_theme, "r") as vscode_config:
        vscode_lines = vscode_config.readlines()
        vscode_lines[155] = f'"editor.background": "{widgetIconForeground}",' + "\n" 
        vscode_lines[156] = f'"activityBar.background": "{widgetIconForeground}",' + "\n"
        vscode_lines[157] = f'"sideBar.background": "{widgetIconForeground}",' + "\n"
        vscode_lines[158] = f'"editorGroupHeader.tabsBackground": "{widgetIconForeground}",' + "\n"

    with open(vscode_theme, "w") as vscode_config:
        vscode_config.writelines(vscode_lines)

    with open(ghostty_theme, "r") as ghostty_config:
        ghostty_lines = ghostty_config.readlines()
        ghostty_lines[43] = f'background = "#000000"' + "\n"
        ghostty_lines[44] = f'foreground = "{ghosttyForeground}"' + "\n"

    with open(ghostty_theme, "w") as ghostty_config:
        ghostty_config.writelines(ghostty_lines)


    with open(hyprland, 'r') as hypr_config:
        hyprland_lines = hypr_config.readlines()
    hyprland_lines[100] = f"col.active_border = {clean_col}" + "\n"
    hyprland_lines[101] = f"col.inactive_border = {clean_col}" + "\n"

    with open(hyprland, 'w') as hypr_config:
        hypr_config.writelines(hyprland_lines)

def wallpapers():
    
    with open(state, 'r') as state_management:
        wallpaper_state = state_management.readlines()
        cache = wallpaper_state[0].strip()
        num = int(cache)
        
        if num > len(wallpaperDict) or num > 90:
            num = 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
            
        elif num == 1:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 2:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 3:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 4:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 5:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 6:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 7:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 8:  
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 9:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 10:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 11:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 12:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 13:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 14:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 15:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 16: 
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 17:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 18:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 19:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 20: 
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 21:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 22:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 23:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 24:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 25:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 26:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 27:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 28:  
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 29:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 30:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 31:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 32:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 33:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 34:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 35:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 36: 
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 37:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 38:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 39:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 40: 
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 41:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 42:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 43:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 44:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 45:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 46:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 47:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 48:  
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 49:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 50:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 51:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 52:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 53:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 54:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 55:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 56: 
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 57:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 58:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 59:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 60: 
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 61:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 62:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 63:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 64:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 65:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 66:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 67:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 68:  
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 69:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 70:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 71:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 72:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 73:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 74:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 75:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 76: 
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 77:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 78:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 79:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 80: 
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 81:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 82:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 83:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 84:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 85:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 86:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 87:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 88:  
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 89:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
        elif num == 90:    
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])

            x = wallpaperDict[num]

            subprocess.run(["wal", "-i", x],check=True)

            themeSwitcher()

            subprocess.Popen(["pkill", "waybar"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/bottom_bar.jsonc", "-s", "/home/ranger/.config/waybar/bottom_bar.css"])
            subprocess.Popen(["waybar", "-c", "/home/ranger/.config/waybar/config.jsonc", "-s", "/home/ranger/.config/waybar/style.css"])
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
         
        
wallpapers()
