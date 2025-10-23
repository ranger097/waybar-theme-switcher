import subprocess

wallpaperDict = { 
    1 : "/home/ranger/waybar-theme-switcher/wallpapers/1a3w6zriyiqe1.png",
    2 : "/home/ranger/waybar-theme-switcher/wallpapers/829604.jpg",
    3 : "/home/ranger/waybar-theme-switcher/wallpapers/939177.jpg",
    4 : "/home/ranger/waybar-theme-switcher/wallpapers/1337718.jpeg",
    5 : "/home/ranger/waybar-theme-switcher/wallpapers/9391771.jpg",
    6 : "/home/ranger/waybar-theme-switcher/wallpapers/Dan_Da_Dan_1_dark.png",
    7 : "/home/ranger/waybar-theme-switcher/wallpapers/dandadan.png",
    8 : "/home/ranger/waybar-theme-switcher/wallpapers/dnd.png",
    9 : "/home/ranger/waybar-theme-switcher/wallpapers/JJK_3_dark.jpeg",
    10 : "/home/ranger/waybar-theme-switcher/wallpapers/wallpaper-theme-conv.png",
    11 : "/home/ranger/waybar-theme-switcher/wallpapers/wallpaper-theme-converter1.png",
    12 : "/home/ranger/waybar-theme-switcher/wallpapers/wallpaper-theme-converter3.png",
    13 : "/home/ranger/waybar-theme-switcher/wallpapers/wallpaper-theme-converter4.png",
    14 : "/home/ranger/waybar-theme-switcher/wallpapers/wallpaper-theme-converter5.png",
    15 : "/home/ranger/waybar-theme-switcher/wallpapers/wallpaper.png"
}

def wallpapers():
    state = "/home/ranger/waybar-theme-switcher/state/wallpapers.txt"
    with open(state, 'r') as state_management:
        wallpaper_state = state_management.readlines()
        cache = wallpaper_state[0]
        num = int(cache)
        if num > len(wallpaperDict):
            num = 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])
   
            x = wallpaperDict[num]

            try:
                subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"], check=True)
                subprocess.run(["wal", "-i", x], check=True)

            except:
                print("Please check your wallpaper paths!")
                print("- ranger097")


            wallpapers()
        else:
            num = num + 1
            wallpaper_state[0] = str(num)
            with open(state, 'w') as state_management:
                state_management.writelines(wallpaper_state[0])
   
            print(cache)
   
            x = wallpaperDict[num]

            try:
                subprocess.run(["swww", "img", x, "--transition-step", "10", "--transition-type", "center", "--transition-fps", "120"], check=True)
                subprocess.run(["wal", "-i", x], check=True)
                
            except:
                print("Please check your wallpaper paths!")
                print("- ranger097")


wallpapers()





 
