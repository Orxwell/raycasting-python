try:
    from customtkinter import CTk
    from customtkinter import set_appearance_mode # Modifiers...
    from win32api      import GetSystemMetrics
    
    import settings as const
    import sys
    
    print('  ~Library [win32api     ] was imported correctly.~')
    print('  ~Library [customtkinter] was imported correctly.~')
    print('  ~Library [settings     ] was imported correctly.~')
    print('  ~Library [sys          ] was imported correctly.~')
    
except ImportError as err:
    print(f'\n  ~Fatal error trying to import necessary libraries.~\n    - {err}\n')
    exit()


class Game:
    """ Initializing properties """
    # -root-&-variables-
    __root : CTk
    __title: str
    '-----------------------------'
    # -screen-metrics-
    __screen_x: int
    __screen_y: int
    '-----------------------------'
    # -root-metrics-
    __root_x: int
    __root_y: int
    '-----------------------------'
    
    def __init__(self, *, title: str='Default-Title') -> None:

        # Modifiers...____________
        set_appearance_mode('dark') # System=(Default), light=Light, dark=Dark
        '_________________________'
        
        # Instantiating Root
        self.__root = CTk()
        '_________________'
        
        # Instantiation of Attributes_______
        self.title = title
        
        self.__screen_x = GetSystemMetrics(0)
        self.__screen_y = GetSystemMetrics(1)
        
        self.__root_x = const.R_WIDTH
        self.__root_y = const.R_HEIGHT
        '___________________________________'
        
        self.__config()
    
    def __config(self) -> None:

        # Configuration's Root & Attributes________
        self.__root.title(self.title)
        self.__root.attributes('-alpha', 0.97)
        self.__root.attributes('-fullscreen', False)
        self.__root.resizable(False, False)
        '__________________________________________'
        
        # Center the Root on screen______________________
        rel_x = int((self.__screen_x - self.__root_x) / 2)
        rel_y = int((self.__screen_y - self.__root_y) / 2)
        
        self.__root.geometry(
            f'{self.__root_x}x{self.__root_y}'+
            f'+{rel_x}+{rel_y-40}'
        )
        '________________________________________________'
    
    def run(self) -> None:
        self.__root.mainloop()
        sys.exit()

