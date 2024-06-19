#Imports
from variables import animationFolder, themeColors

import customtkinter as CGUI
from PIL import Image
from os import walk






#Animation Handling
class AnimatedLabel(CGUI.CTkLabel):
    def __init__(self, master):
        self.frames = self.importFolders(f'{animationFolder}/loading')
        self.framei = 0
        self.anilength = len(self.frames) - 1

        super().__init__(master = master, height = 0, width = 0, bg_color = themeColors['bg'], corner_radius = 0, text = '', image = self.frames[self.framei])
        self.pack(expand = True)
        self.animate()

        

    def importFolders(self, loadingPath: str):
        images = [(f'{loadingPath}/{item}') for item in sorted(list(walk(loadingPath))[-1][-1], key = lambda i: int(i.split('loading-')[-1].split('.')[0]))]
        for i in range(len(images)):
            image = Image.open(images[i])
            images[i] = CGUI.CTkImage(light_image = image, dark_image = image, size = (50, 50))
        return images
    


    def animate(self):
        self.framei += 1
        self.configure(image = self.frames[self.framei])

        if self.framei >= self.anilength: self.framei = 0
        self.after(30, self.animate)