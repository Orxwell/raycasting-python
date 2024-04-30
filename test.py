try:
    from game import Game
    
    print('  ~Library [game         ] was imported correctly.~')
    
except ImportError as err:
    print(f'\n  ~Fatal error trying to import necessary libraries.~\n    - {err}\n')
    exit()


if __name__ == '__main__':
    app = Game(title='RaycastingV0')
    app.run()
