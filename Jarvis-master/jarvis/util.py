#-*-coding:utf-8
class Family_Services:
    @classmethod
    def turnOnTheLight(cls):
        pass

    @classmethod
    def turnOffTheLight(cls):
        pass

    @classmethod
    def heatCoffee(cls):
        pass

    @classmethod
    def openTheTV(cls):
        pass

    @classmethod
    def openBrowser(cls):
        import webbrowser
        webbrowser.open('https://www.google.co.uk')

    @classmethod
    def openWindowCurtain(cls):
        pass

    @classmethod
    def singASong(cls):
        import pygame
        try:
            file = r'Only Love - Trademark.mp3'
            pygame.mixer.init()
            track = pygame.mixer.music.load(file)
            pygame.mixer.music.play()
        except Exception,e:
            pass

    @classmethod
    def stopSingSong(cls):
        import pygame
        try:
            pygame.mixer.music.play()
        except Exception,e:
            pass