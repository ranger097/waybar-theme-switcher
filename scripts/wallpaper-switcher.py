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
        if num > len(wallpaperDict) or num > 90:
            num = 0
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])
   
            x = wallpaperDict[num]

            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
            
            

            wallpapers()

        
        else:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])
   
            print(cache)
   
            x = wallpaperDict[num]
            subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"])
            

wallpapers()





 
