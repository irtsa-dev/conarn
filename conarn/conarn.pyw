#Imports
from guisetup import WindowMain, WindowSelect, WindowLoading

#Thanks to rdbende for Tkinter Theme
#https://github.com/rdbende/Sun-Valley-ttk-theme
import sv_ttk






#Initialization
Window = WindowMain()
WindowLoading(Window)

sv_ttk.set_theme("dark")
Window.after(500, lambda: WindowSelect(Window))
Window.mainloop()