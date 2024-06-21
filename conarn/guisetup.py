#Imports
from variables import themeColors, Items, itemGridSize
from functions import RemoveSave, AddSave, ParseSave, filesFromFolder, saveCount
from savehandler import SaveFileHandler as SFH

import tkinter as GUI
from tkinter import ttk as Widget
from animationhandling import AnimatedLabel

from base64 import b64decode





#Functions
def WindowMain() -> GUI.Tk:
    Window = GUI.Tk()
    Window.title('Conarn')
    Window.geometry('300x100')
    Window.iconbitmap('assets/icon/icon.ico')

    return Window





def WindowLoading(Window: GUI.Tk) -> None:
    image_logo = Image.open('assets/icon/logo.png')
    image_logo = CTkImage(light_image = image_logo, dark_image = image_logo, size = (200, 138))
    
    label_title = Widget.Label(master = Window, text = '', image = image_logo)
    label_title.configure(image = image_logo)
    
    frame_loading = Widget.Frame(master = Window, width = 150)
    label_loading = AnimatedLabel(master = frame_loading)
    
    label_title.pack()
    label_loading.pack()
    frame_loading.pack()





def WindowDisplay(Window, SaveFile) -> None:
    oldIndex = SaveFile.saveslot
    Notebook_InsideItems = []
    Notebook_OutsideItems = []

    frame_filedisplay = Widget.Frame(master = Window, padding = 10)

    notebook_filedisplay = Widget.Notebook(master = frame_filedisplay, width = 600, height = 340)
    notebook_filedisplay.pack(expand = False)
    NotebookFrames = [Widget.Frame() for i in range(3)]
    NotebookFNames = ['General Information', 'Inside Items', 'Outside Items']
    for i in range(len(NotebookFrames)): notebook_filedisplay.add(NotebookFrames[i], text = NotebookFNames[i])

    frame_bottomButtons = Widget.Frame(master = Window, padding = 10)
    frame_generalInformation = Widget.Frame(master = NotebookFrames[0], relief = 'sunken')
    frame_insideItems = Widget.Frame(master = NotebookFrames[1], relief = 'sunken')
    frame_outsideItems = Widget.Frame(master = NotebookFrames[2], relief = 'sunken')
    frame_addInsideItem = Widget.Frame(master = NotebookFrames[1], relief = 'sunken')
    frame_addOutsideItem = Widget.Frame(master = NotebookFrames[2], relief = 'sunken')
    
    frame_filedisplay.pack()
    frame_bottomButtons.pack(after = frame_filedisplay)
    frame_generalInformation.pack()
    frame_insideItems.pack()
    frame_outsideItems.pack()
    frame_addInsideItem.pack(side = 'bottom')
    frame_addOutsideItem.pack(side = 'bottom')



    def saveContent() -> None:
        frame_loading = Widget.Frame(master = Window, width = 150)

        label_loading = AnimatedLabel(master = frame_loading)
        label_error = Widget.Label(master = Window, text = 'There was an error in saving.', background = themeColors['bg'], foreground = '#B46464', font = 'Courier 10')
        label_success = Widget.Label(master = Window, text = 'Successfully saved.', background = themeColors['bg'], foreground = '#6AB464', font = 'Courier 10')
        label_loading.pack()


        Information = NotebookFrames[0].children['!frame'].children
        InformationNames = [i for i in Information]


        def checkSeed(value: int) -> bool: return str(value).isdigit() and len(str(value)) < 4
        def checkMoney(value: int) -> bool: return str(value).isdigit() and len(str(value)) < 7
        def checkViews(value: int) -> bool: return str(value).isdigit() and len(str(value)) < 10
        

        Values = {}
        for i in range(int(len(Information) / 2)):
            name = Information[InformationNames[i * 2]]['text']           
            try: value = Information[InformationNames[i * 2 + 1]].get()
            except: value = Information[InformationNames[i * 2 + 1]]['text']
            Values.update({name : value})
        

        if any([not checkSeed(Values['Seed']), not checkMoney(Values['Money']), not checkViews(Values['Views'])]):
            frame_loading.destroy()
            Window.after(0, lambda: label_error.pack())
            Window.after(2000, lambda: label_error.destroy())
            return False


        for name in Values: SaveFile.UpdateValue(name, Values[name])
        if SaveFile.saveslot != oldIndex: RemoveSave(oldIndex)
        frame_loading.destroy()

        Window.after(0, lambda: label_success.pack())
        Window.after(2000, lambda: label_success.destroy())
        return AddSave(SaveFile.saveslot, SaveFile.formatDetails)
    


    def goBack() -> None:
        notebook_filedisplay.destroy()
        Window.geometry('300x100')
        Window.after(0, lambda: WindowLoading(Window))
        Window.after(500, lambda: WindowSelect(Window))
        for widget in Window.winfo_children(): widget.destroy()
    


    def removeItem(itemName: str, location: str) -> None:
        if location == 'house': index = SaveFile.display_houseItems.index(itemName)
        else: index = SaveFile.display_outsideItems.index(itemName)

        if SaveFile.RemoveItem(index, location):
            if location == 'house':
                Notebook_InsideItems[index].destroy()
                Notebook_InsideItems.pop(index)
                for i in range(len(Notebook_InsideItems)): Notebook_InsideItems[i].grid(row = int(i / itemGridSize), column = i % itemGridSize, sticky = GUI.E + GUI.W)
            else:
                Notebook_OutsideItems[index].destroy()
                Notebook_OutsideItems.pop(index)
                for i in range(len(Notebook_OutsideItems)): Notebook_OutsideItems[i].grid(row = int(i / itemGridSize), column = i % itemGridSize, sticky = GUI.E + GUI.W)
    


    def removeallItems(location: str) -> None:
        if SaveFile.RemoveAllItems(location):
            if location == 'house':
                for i in range(len(Notebook_InsideItems)): Notebook_InsideItems[i].destroy()
                for i in range(len(Notebook_InsideItems)): Notebook_InsideItems.pop(-1)
            else:
                for i in range(len(Notebook_OutsideItems)): Notebook_OutsideItems[i].destroy()
                for i in range(len(Notebook_OutsideItems)): Notebook_OutsideItems.pop(-1)
    


    def addItem(itemName: str, location: str) -> None:
        if SaveFile.AddItem(itemName, location):
            if location == 'house':
                Notebook_InsideItems.append(Widget.Button(master = frame_insideItems, text = itemName, command = lambda x=itemName: removeItem(x, 'house')))
                for i in range(len(Notebook_InsideItems)): Notebook_InsideItems[i].grid(row = int(i / itemGridSize), column = i % itemGridSize, sticky = GUI.E + GUI.W)
            else:
                Notebook_OutsideItems.append(Widget.Button(master = frame_outsideItems, text = itemName, command = lambda x=itemName: removeItem(x, 'outside')))
                for i in range(len(Notebook_OutsideItems)): Notebook_OutsideItems[i].grid(row = int(i / itemGridSize), column = i % itemGridSize, sticky = GUI.E + GUI.W)
    


    Notebook_GeneralInformation = [
        ('Index', SaveFile.saveslot, 'menu'),
        ('Seed', SaveFile.seed, 'value'),
        ('Week', SaveFile.week, 'menu'),
        ('Day', SaveFile.day, 'menu'),
        ('Time', SaveFile.display_time, 'menu'),
        ('Money', SaveFile.money, 'value'),
        ('Views', SaveFile.display_views, 'value'),
        ('Map', SaveFile.display_map, 'menu')
    ]


    for name, value, valueType in Notebook_GeneralInformation:
        label = Widget.Label(master = frame_generalInformation, text = name, font = 'Courier 10')

        match valueType:
            case 'value':
                inputValue = Widget.Entry(master = frame_generalInformation, textvariable = GUI.StringVar(), font = 'Courier 10')
                inputValue.insert(0, str(value))

            case 'menu':
                options = {
                    'Index' : ['0', '1', '2'],
                    'Week' : [str(i + 1) for i in range(10)],
                    'Day' : ['1', '2', '3'],
                    'Time' : ['Morning', 'Evening'],
                    'Map' : ['Factory', 'Mines', 'Ship']
                }[name]
                inputValue = Widget.OptionMenu(frame_generalInformation, GUI.StringVar(), str(value), *options)

        label.grid(row = Notebook_GeneralInformation.index((name, value, valueType)), column=0, sticky = 'news')
        inputValue.grid(row = Notebook_GeneralInformation.index((name, value, valueType)), column=1, padx = 5, pady=5, sticky = 'news')
    


    Notebook_InsideItems = [Widget.Button(master = frame_insideItems, text = item, command = lambda x=item: removeItem(x, 'house')) for item in SaveFile.display_houseItems]
    Notebook_OutsideItems = [Widget.Button(master = frame_outsideItems, text = item, command = lambda x=item: removeItem(x, 'outside')) for item in SaveFile.display_outsideItems]
    for i in range(len(Notebook_InsideItems)): Notebook_InsideItems[i].grid(row = int(i / itemGridSize), column = i % itemGridSize, sticky = GUI.E + GUI.W)
    for i in range(len(Notebook_OutsideItems)): Notebook_OutsideItems[i].grid(row = int(i / itemGridSize), column = i % itemGridSize, sticky = GUI.E + GUI.W)



    addInsideText = GUI.StringVar()
    opmenu_addInsideItem = Widget.OptionMenu(frame_addInsideItem, addInsideText, list(Items['NAME'].keys())[0], *Items['NAME'])
    opmenu_addInsideItem.grid(row = 0, column = 0)
    button_addInsideItem = Widget.Button(master = frame_addInsideItem, text = 'Add', command = lambda x=addInsideText: addItem(x.get(), 'house'))
    button_addInsideItem.grid(row = 0, column = 1)
    button_removeallInsideItems = Widget.Button(master = frame_addInsideItem, text = 'Remove All', command = lambda: removeallItems('house'))
    button_removeallInsideItems.grid(row = 0, column = 2, padx = 10)

    addOutsideText = GUI.StringVar()
    opmenu_addOutsideItem = Widget.OptionMenu(frame_addOutsideItem, addOutsideText, list(Items['NAME'].keys())[0], *Items['NAME'])
    opmenu_addOutsideItem.grid(row = 0, column = 0)
    button_addOutsideItem = Widget.Button(master = frame_addOutsideItem, text = 'Add', command = lambda x=addOutsideText: addItem(x.get(), 'outside'))
    button_addOutsideItem.grid(row = 0, column = 1)
    button_removeallOutsideItems = Widget.Button(master = frame_addOutsideItem, text = 'Remove All', command = lambda: removeallItems('outside'))
    button_removeallOutsideItems.grid(row = 0, column = 2, padx = 10)


    button_saveContent = Widget.Button(master = frame_bottomButtons, text = 'Save Changes', command = lambda: saveContent())
    button_goBack = Widget.Button(master = frame_bottomButtons, text = 'Back', command = lambda: goBack())
    button_saveContent.grid(row = 0, column = 0)
    button_goBack.grid(row = 0, column = 1, padx = 10)






def WindowSelect(Window):
    for widget in Window.winfo_children(): widget.destroy()

    image_logo = Image.open('assets/icon/logo.png')
    image_logo = CTkImage(light_image = image_logo, dark_image = image_logo, size = (200, 138))
    
    label_title = Widget.Label(master = Window, text = '', image = image_logo)
    label_title.configure(image = image_logo)
    label_title.pack()

    frame_savefiles = Widget.Frame(master = Window, width = 150)
    frame_loading = Widget.Frame(master = Window, width = 150, padding = 10)
    frame_savefiles.pack()

    label_loading = AnimatedLabel(master = frame_loading)
    label_loading.pack()



    def loadSave(save: int):
        frame_savefiles.pack_forget()
        frame_loading.pack()
        SaveFile = SFH(ParseSave(filesFromFolder()[save]))

        frame_loading.pack_forget()
        Window.geometry('600x615')
        WindowDisplay(Window, SaveFile)


    for i in range(saveCount()):
        button = Widget.Button(master = frame_savefiles, name = f'savebutton_{i}', text = f'Save {i + 1}', command = lambda x=i: loadSave(x))
        button.grid(column = i, row = 0, padx = 10)
