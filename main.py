from kivy.config import Config
Config.set('graphics','resizable',1)
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import App
from ctypes import cdll, c_int
import gc
from webbrowser import open_new_tab

# initializing c++ variables:
lib = cdll.LoadLibrary("./library.so")
Builder.load_file("window.kv")
sm = ScreenManager(transition=NoTransition())

class RoundButtonvar(Button):
    pass
class RoundButtonBack(Button):
    pass
class RoundButtonSolve(Button):
    pass

class GitButton(Button):
    def change_image(self):
        self.ids.gitimage.source = 'icons/Gitmark.png'
    def change_image_off(self):
        self.ids.gitimage.source = 'icons/Github_mark.png'
        open_new_tab("https://github.com/Alforreal")
class MainApp(App):
    def build(self):
        Window.size = (600, 337.5)
        self.title = "Gauss-Cramer"
        loginscreen = Screen(name='login')
        twovars = Screen(name='twovars')
        sltwo = Screen(name='sltwo')
        threevars = Screen(name='threevars')
        krammersol = Screen(name='krammersol')
        gausssol = Screen(name='gausssol')

        layoutbtn = GridLayout(cols=2, spacing=(60, 0), padding=(38, Window.size[1]/2 - 65))
        twovarsbtn = RoundButtonvar(text='2 variables', font_name='Caviar_Dreams_Bold', font_size=30, size_hint_y = None, size_hint_x = None, size = (230, 100))
        threevarsbtn = RoundButtonvar(text='3 variables',font_name='Caviar_Dreams_Bold', font_size=30, size_hint_y = None, size_hint_x = None, size = (230, 100))
        layoutbtn.add_widget(twovarsbtn)
        layoutbtn.add_widget(threevarsbtn)
        github = GitButton(font_size=20, size_hint_y = None, size_hint_x = None, size=(50, 50), pos=(Window.size[0]-60, Window.size[1]-60))
        loginscreen.add_widget(layoutbtn)
        loginscreen.add_widget(github)
        sm.add_widget(loginscreen)
        twovarsbtn.bind(on_release = lambda x:self.changetwovars())
        threevarsbtn.bind(on_release = lambda x:self.changethreevars())


        #layout for twovars screen:
        layout2 = GridLayout(cols=5, rows=3, padding = (30, 10))
        self.in1 = TextInput(text='', font_size=50, size_hint_x = None, font_name='Caviar_Dreams_Bold', size_hint_y = None, height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.in2 = TextInput(text='', font_size=50, size_hint_x = None, font_name='Caviar_Dreams_Bold', size_hint_y = None, height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.in3 = TextInput(text='', font_size=50, size_hint_x = None, font_name='Caviar_Dreams_Bold', size_hint_y = None, height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.in4 = TextInput(text='', font_size=50, size_hint_x = None, font_name='Caviar_Dreams_Bold', size_hint_y = None, height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.in5 = TextInput(text='', font_size=50, size_hint_x = None, font_name='Caviar_Dreams_Bold', size_hint_y = None, height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.in6 = TextInput(text='', font_size=50, size_hint_x = None, font_name='Caviar_Dreams_Bold', size_hint_y = None, height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        btnlayout0 = GridLayout(cols = 2, padding=(30, 250), spacing=(50, 0))
        backbtn = RoundButtonBack(text='Go back', font_size=32, size_hint_x = None, font_name='Caviar_Dreams_Bold', size_hint_y = None, size = (150, 75))
        processbtn = RoundButtonSolve(text="Solve via Cramer", font_size = 32, size_hint_x = None, font_name='Caviar_Dreams_Bold', size_hint_y = None, size = (300, 75))
        
        #adding widgets to the layout
        layout2.add_widget(self.in1)
        layout2.add_widget(Label(text='x + ', font_size = 50, font_name='Caviar_Dreams_Bold', size_hint_x = None, size_hint_y = None))
        layout2.add_widget(self.in2)
        layout2.add_widget(Label(text='y = ', font_size = 50, font_name='Caviar_Dreams_Bold', size_hint_x = None, size_hint_y = None))
        layout2.add_widget(self.in3)
        layout2.add_widget(self.in4)
        layout2.add_widget(Label(text='x + ', font_size = 50, font_name='Caviar_Dreams_Bold', size_hint_x = None, size_hint_y = None))
        layout2.add_widget(self.in5)
        layout2.add_widget(Label(text='y = ', font_size = 50, font_name='Caviar_Dreams_Bold', size_hint_x = None, size_hint_y = None))
        layout2.add_widget(self.in6)
        btnlayout0.add_widget(backbtn)
        btnlayout0.add_widget(processbtn)

        #adding the layout and the screen to their parents:
        twovars.add_widget(btnlayout0)
        sm.add_widget(twovars)

        # putting logic to buttons:
        backbtn.bind(on_press = lambda x:self.back())
        processbtn.bind(on_press = lambda x:self.processkrammer())
        
        #SLTWO SCREEN 
        #creating a layout for the screen:
        layout3 = GridLayout(cols=1, padding = (30, 30))
        layout3.add_widget(Label(text="Solution:", font_name='Caviar_Dreams_Bold', font_size=40))
        self.labeldelta = Label(text="", font_name='Caviar_Dreams_Bold', font_size=40)
        self.labeldeltax = Label(text="", font_name='Caviar_Dreams_Bold', font_size=40)
        self.labeldeltay = Label(text="", font_name='Caviar_Dreams_Bold', font_size=40)
        self.labelx = Label(text="", font_name='Caviar_Dreams_Bold', font_size=40)
        self.labely = Label(text="", font_name='Caviar_Dreams_Bold', font_size=40)
        self.answ = Label(text="", font_name='Caviar_Dreams_Bold', font_size=40)
        tmplayout = GridLayout(cols=2, spacing=(60, 0))
        backbtn = RoundButtonBack(text='Go back', font_size=32, size_hint_x = None, font_name='Caviar_Dreams_Bold',  size_hint_y = None, size = (150, 75))
        Krammerbtn = Button(text='Cramer wiki', font_size=32, font_name='Caviar_Dreams_Bold', size_hint_y = None, size_hint_x = None, background_color=(0, 0, 0, 0), underline = True, size = (200, 75), color = (0, 102/255, 204/255, 1))
        
        backbtn.bind(on_press = lambda x:self.back())
        Krammerbtn.bind(on_press = lambda x:self.cramer())
        tmplayout.add_widget(backbtn)
        tmplayout.add_widget(Krammerbtn)

        layout3.add_widget(self.labeldelta)
        layout3.add_widget(self.labeldeltax)
        layout3.add_widget(self.labeldeltay)
        layout3.add_widget(self.labelx)
        layout3.add_widget(self.labely)
        layout3.add_widget(self.answ)
        layout3.add_widget(tmplayout)

        #adding the layout and the screen to their parents:
        sltwo.add_widget(layout3)
        sm.add_widget(sltwo)

        twovars.add_widget(layout2)
        #THREEVARS SCREEN
        #setting up the layout
        layout4 = GridLayout(cols=7, padding = (30, 10))
        self.inp1 = TextInput(text='', font_size=50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold', height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.inp2 = TextInput(text='', font_size=50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold', height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.inp3 = TextInput(text='', font_size=50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold', height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.inp4 = TextInput(text='', font_size=50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold', height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.inp5 = TextInput(text='', font_size=50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold', height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.inp6 = TextInput(text='', font_size=50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold', height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.inp7 = TextInput(text='', font_size=50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold', height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.inp8 = TextInput(text='', font_size=50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold', height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.inp9 = TextInput(text='', font_size=50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold', height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.inp10 = TextInput(text='', font_size=50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold', height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.inp11 = TextInput(text='', font_size=50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold', height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))
        self.inp12 = TextInput(text='', font_size=50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold', height = 75, multiline = False, input_filter='float', foreground_color=(2/255, 18/255, 17/255, 1), background_color=(199/255, 225/255, 252/255, 1))

        # adding the widgets to the layout:
        layout4.add_widget(self.inp1)
        layout4.add_widget(Label(text="x + ", font_size = 50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold'))
        layout4.add_widget(self.inp2)
        layout4.add_widget(Label(text="y + ", font_size = 50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold'))
        layout4.add_widget(self.inp3)
        layout4.add_widget(Label(text="z = ", font_size = 50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold'))
        layout4.add_widget(self.inp4)

        layout4.add_widget(self.inp5)
        layout4.add_widget(Label(text="x + ", font_size = 50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold'))
        layout4.add_widget(self.inp6)
        layout4.add_widget(Label(text="y + ", font_size = 50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold'))
        layout4.add_widget(self.inp7)
        layout4.add_widget(Label(text="z = ", font_size = 50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold'))
        layout4.add_widget(self.inp8)

        layout4.add_widget(self.inp9)
        layout4.add_widget(Label(text="x + ", font_size = 50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold'))
        layout4.add_widget(self.inp10)
        layout4.add_widget(Label(text="y + ", font_size = 50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold'))
        layout4.add_widget(self.inp11)
        layout4.add_widget(Label(text="z = ", font_size = 50, size_hint_x = None, size_hint_y = None, font_name='Caviar_Dreams_Bold'))
        layout4.add_widget(self.inp12)

        #create a button layout:
        btnlayout = GridLayout(cols=3, rows=1, spacing=(10, 0), padding=(20, 330))
        krammerbtn = RoundButtonSolve(text="Solve via Cramer", font_size = 32, font_name='Caviar_Dreams_Bold',  size_hint_x = None, size_hint_y = None, size = (290, 80))
        returnbtn = RoundButtonBack(text="Go back", font_size = 32, font_name='Caviar_Dreams_Bold',  size_hint_x = None, size_hint_y = None, size = (150, 80))
        gaussbtn = RoundButtonSolve(text="Solve via Gauss", font_size = 32, font_name='Caviar_Dreams_Bold',  size_hint_x = None, size_hint_y = None, size = (290, 80))
        krammerbtn.bind(on_press= lambda x:self.processkrammer3())
        returnbtn.bind(on_press=lambda x:self.back())
        gaussbtn.bind(on_press=lambda x:self.processgauss())
        btnlayout.add_widget(returnbtn)
        btnlayout.add_widget(krammerbtn)
        btnlayout.add_widget(gaussbtn)

        threevars.add_widget(layout4)
        threevars.add_widget(btnlayout)
        sm.add_widget(threevars)

        #KRAMMERSOL SCREEN
        layout5 = GridLayout(cols=1, padding = (30, 10))
        self.krammerdelta = Label(text='', font_name='Caviar_Dreams_Bold', font_size = 32)
        self.krammerdeltahelp = Label(text='', font_name='Caviar_Dreams_Bold', font_size = 32)
        self.krammerdelx = Label(text='', font_name='Caviar_Dreams_Bold', font_size = 32)
        self.krammerdelxhelp = Label(text='', font_name='Caviar_Dreams_Bold', font_size = 32)
        self.krammerdely = Label(text='', font_name='Caviar_Dreams_Bold', font_size = 32)
        self.krammerdelyhelp = Label(text='', font_name='Caviar_Dreams_Bold', font_size = 32)
        self.krammerdelz = Label(text='', font_name='Caviar_Dreams_Bold', font_size = 32)
        self.krammerdelzhelp = Label(text='', font_name='Caviar_Dreams_Bold', font_size = 32)
        self.krammerx = Label(text='', font_name='Caviar_Dreams_Bold', font_size = 32)
        self.krammery = Label(text='', font_name='Caviar_Dreams_Bold', font_size = 32)
        self.krammerz = Label(text='', font_name='Caviar_Dreams_Bold', font_size = 32)
        homebtn = RoundButtonBack(text="Go back", font_size = 32, font_name='Caviar_Dreams_Bold', size_hint_x = None, size_hint_y = None, size = (150, 75))
        cramerbtn = Button(text='Cramer wiki', font_size=32, font_name='Caviar_Dreams_Bold', size_hint_y = None, size_hint_x = None, background_color=(0, 0, 0, 0), underline = True, size = (200, 100), color = (0, 102/255, 204/255, 1))
        layouttmp = GridLayout(cols=3, padding=(10, 590), spacing=(50, 0))
        layouttmp.add_widget(homebtn)
        layouttmp.add_widget(cramerbtn)
        layout5.add_widget(self.krammerdelta)
        layout5.add_widget(self.krammerdeltahelp)
        layout5.add_widget(Label(text='', font_size = 32))
        layout5.add_widget(self.krammerdelx)
        layout5.add_widget(self.krammerdelxhelp)
        layout5.add_widget(Label(text='', font_size = 32))
        layout5.add_widget(self.krammerdely)
        layout5.add_widget(self.krammerdelyhelp)
        layout5.add_widget(Label(text='', font_size = 32))
        layout5.add_widget(self.krammerdelz)
        layout5.add_widget(self.krammerdelzhelp)
        layout5.add_widget(self.krammerx)
        layout5.add_widget(self.krammery)
        layout5.add_widget(self.krammerz)
        layout5.add_widget(Label(text='', font_size = 32))
        layout5.add_widget(Label(text='', font_size = 32))
        homebtn.bind(on_press= lambda x:self.back())
        cramerbtn.bind(on_press= lambda x:self.cramer())
        krammersol.add_widget(layout5)
        krammersol.add_widget(layouttmp)
        sm.add_widget(krammersol)

        #GAUSSOL SCREEN:
        layout6 = GridLayout(cols=1, padding = (30, 30), spacing = (10, 10))
        self.entry0 = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        self.first0 = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        self.second0 = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        self.result0 = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        
        self.entry1 = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        self.first1 = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        self.second1 = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        self.result1 = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)

        self.entry2 = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        self.first2 = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        self.second2 = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        self.result2 = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)

        self.answx = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        self.answy = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        self.answz = Label(text='', font_name='Caviar_Dreams_Bold', font_size=32)
        buttonback = RoundButtonBack(text="Go back", font_size = 32, size_hint_x = None, font_name='Caviar_Dreams_Bold', size_hint_y = None, size = (150, 75))
        
        layout6.add_widget(self.entry0)
        layout6.add_widget(self.first0)
        layout6.add_widget(self.second0)
        layout6.add_widget(self.result0)
        layout6.add_widget(Label(text='', font_name='Caviar_Dreams_Bold', font_size=32))

        layout6.add_widget(self.entry1)
        layout6.add_widget(self.first1)
        layout6.add_widget(self.second1)
        layout6.add_widget(self.result1)
        layout6.add_widget(Label(text='', font_name='Caviar_Dreams_Bold', font_size=32))

        layout6.add_widget(self.entry2)
        layout6.add_widget(self.first2)
        layout6.add_widget(self.second2)
        layout6.add_widget(self.result2)
        layout6.add_widget(Label(text='', font_name='Caviar_Dreams_Bold', font_size=32))

        layout6.add_widget(self.answx)
        layout6.add_widget(self.answy)
        layout6.add_widget(self.answz)
        layout6.add_widget(Label(text='', font_name='Caviar_Dreams_Bold', font_size=32))
        layout6.add_widget(buttonback)
        gaussbtn = Button(text='Gauss wiki', font_size=32, font_name='Caviar_Dreams_Bold', size_hint_y = None, size_hint_x = None, background_color=(0, 0, 0, 0), underline = True, size = (200, 100), color = (0, 102/255, 204/255, 1), pos=(250, 20))
        gaussbtn.bind(on_press=lambda x:self.gauss())
        buttonback.bind(on_press=lambda x:self.back())
        gausssol.add_widget(layout6)
        gausssol.add_widget(gaussbtn)
        sm.add_widget(gausssol)
        return sm
    def changetwovars(self):
        sm.current = 'twovars'
        Window.size = (560, 350)
    def changethreevars(self):
        sm.current = 'threevars'
        Window.size = (790, 430)
    def back(self):
        sm.current = 'login'
        Window.size = (600, 337.5)
    def cramer(self):
        open_new_tab("https://en.wikipedia.org/wiki/Cramer%27s_rule")
    def gauss(self):
        open_new_tab("https://en.wikipedia.org/wiki/Gaussian_elimination#")

    
        

    def processkrammer(self):
        try:
            inp_raw = [int(self.in1.text), int(self.in2.text), int(self.in3.text), int(self.in4.text), int(self.in5.text), int(self.in6.text)]
            inp = (c_int * 6)(*inp_raw)
            lib.Krammer2(inp)
            sm.current = 'sltwo'
            Window.size = (600, 600)
            self.labeldelta.text = "Δ = " + str(self.in1.text) + " * " + str(self.in5.text) + " + " + str(abs(int(self.in2.text))) + " * " + str(abs(int(self.in4.text))) + " = " + str(lib.twoDelta0ret())
            self.labeldeltax.text = "Δx = " + str(self.in3.text) + " * " + str(self.in5.text) + " + " + str(abs(int(self.in2.text))) + " * " + str(abs(int(self.in6.text))) + " = " + str(lib.twoDelta1ret())
            self.labeldeltay.text = "Δy = " + str(self.in1.text) + " * " + str(self.in6.text) + " + " + str(abs(int(self.in3.text))) + " * " + str(abs(int(self.in4.text))) + " = " + str(lib.twoDelta2ret())
            self.labelx.text = "x = Δx/Δ = " + str(lib.twoDelta1ret()) + "/" + str(lib.twoDelta0ret()) + " = " + str(lib.Xret())
            self.labely.text = "y = Δy/Δ = " + str(lib.twoDelta2ret()) + "/" + str(lib.twoDelta0ret()) + " = " + str(lib.Yret())
            self.answ.text = "Answer: (" + str(lib.Xret()) + ", " + str(lib.Yret()) + ")"
            
        except ValueError:  # if you don't enter an number inside one of the texinput boxes you will get ValueError 
            print("oopsie! You didn't enter anything!")

    def processkrammer3(self):
        try:
            inp_raw = [int(self.inp1.text), int(self.inp2.text), int(self.inp3.text), int(self.inp4.text), int(self.inp5.text), int(self.inp6.text), int(self.inp7.text), int(self.inp8.text), int(self.inp9.text), int(self.inp10.text), int(self.inp11.text), int(self.inp12.text)]
            inp = (c_int * 12)(*inp_raw)
            lib.Krammer3(inp)
            del inp
            del inp_raw
            gc.collect()
            sm.current = 'krammersol'
            Window.size = (800, 700)
            self.krammerdelta.text = "Δ = (" + str(self.inp1.text) + " * " + str(self.inp6.text) + " * " + str(self.inp11.text) + ") + (" + str(self.inp2.text) + " * " + str(self.inp7.text) + " * " + str(self.inp9.text) + ") + (" + str(self.inp3.text) + " * " + str(self.inp5.text) + " * " + str(self.inp10.text) + ") -"
            self.krammerdeltahelp.text = "- (" + str(self.inp2.text) + " * " + str(self.inp5.text) + " * " + str(self.inp11.text) + ") - (" + str(self.inp1.text) + " * " + str(self.inp7.text) + " * " + str(self.inp10.text) + ") - (" + str(self.inp3.text) + " * " + str(self.inp6.text) + " * " + str(self.inp9.text) + ") = " + str(lib.threeDelta0ret())
            self.krammerdelx.text = "Δx = (" + str(self.inp4.text) + " * " + str(self.inp6.text) + " * " + str(self.inp11.text) + ") + (" + str(self.inp2.text) + " * " + str(self.inp7.text) + " * " + str(self.inp12.text) + ") + (" + str(self.inp3.text) + " * " + str(self.inp8.text) + " * " + str(self.inp10.text) + ") - "
            self.krammerdelxhelp.text = " - (" + str(self.inp2.text) + " * " + str(self.inp8.text) + " * " + str(self.inp11.text) + ") - (" + str(self.inp4.text) + " * " + str(self.inp7.text) + " * " + str(self.inp10.text) + ") - (" + str(self.inp3.text) + " * " + str(self.inp6.text) + " * " + str(self.inp12.text) + ") = " + str(lib.threeDelta1ret())
            self.krammerdely.text = "Δy = (" + str(self.inp1.text) + " * " + str(self.inp8.text) + " * " + str(self.inp11.text) + ") + (" + str(self.inp4.text) + " * " + str(self.inp7.text) + " * " + str(self.inp9.text) + ") + (" + str(self.inp3.text) + " * " + str(self.inp5.text) + " * " + str(self.inp12.text) + ") -"
            self.krammerdelyhelp.text = "- (" + str(self.inp4.text) + " * " + str(self.inp5.text) + " * " + str(self.inp11.text) + ") - (" + str(self.inp1.text) + " * " + str(self.inp7.text) + " * " + str(self.inp12.text) + ") - (" + str(self.inp3.text) + " * " + str(self.inp8.text) + " * " + str(self.inp9.text) + ") = " + str(lib.threeDelta2ret())
            self.krammerdelz.text = "Δz = (" + str(self.inp1.text) + " * " + str(self.inp6.text) + " * " + str(self.inp12.text) + ") + (" + str(self.inp2.text) + " * " + str(self.inp8.text) + " * " + str(self.inp9.text) + ") + (" + str(self.inp4.text) + " * " + str(self.inp5.text) + " * " + str(self.inp10.text) + ") -"
            self.krammerdelzhelp.text = "- (" + str(self.inp2.text) + " * " + str(self.inp5.text) + " * " + str(self.inp12.text) + ") - (" + str(self.inp1.text) + " * " + str(self.inp8.text) + " * " + str(self.inp10.text) + ") - (" + str(self.inp4.text) + " * " + str(self.inp6.text) + " * " + str(self.inp9.text) + ") = " + str(lib.threeDelta3ret()) 
            self.krammerx.text = "x = Δx/Δ = " + str(lib.Xret())
            self.krammery.text = "y = Δy/Δ = " + str(lib.Yret())
            self.krammerz.text = "z = Δz/Δ = " + str(lib.Zret())
        except ValueError:
            print("oopsie! You didn't enter anything!")
    def processgauss(self):
        try:
            inp_raw = [int(self.inp1.text), int(self.inp2.text), int(self.inp3.text), int(self.inp4.text), int(self.inp5.text), int(self.inp6.text), int(self.inp7.text), int(self.inp8.text), int(self.inp9.text), int(self.inp10.text), int(self.inp11.text), int(self.inp12.text)]
            inp = (c_int * 12)(*inp_raw)
            sm.current = 'gausssol'
            Window.size = (600, 800)
            lib.Gauss3(inp)
            del inp
            file = open("data.txt", "r")
            input = file.readlines()
            file.close()
            for i in range(len(input)):
                input[i].replace("\n", "")
            first = [0 for i in range(4)]
            second = [0 for i in range(3)]
            third = [0 for i in range(3)]
            lcm1 = int(input[0])
            lcm2 = int(input[1])
            for i in range(3):
                second[i] = int(input[i+2])
            lcm3 = int(input[5])
            lcm4 = int(input[6])
            for i in range(4):
                first[i] = int(input[i+7])
            lcm5 = int(input[14])
            for i in range(3):
                third[i] = int(input[i+11])
            lcm6 = int(input[15])
            result = [int(input[16]), int(input[17])]
            del input
            gc.collect()

            inp_raw[0] *= lcm1
            inp_raw[1] *= lcm1
            inp_raw[2] *= lcm1
            inp_raw[3] *= lcm1
            inp_raw[4] *= lcm2
            inp_raw[5] *= lcm2
            inp_raw[6] *= lcm2
            inp_raw[7] *= lcm2
            inp_raw[8] *= lcm4
            inp_raw[9] *= lcm4
            inp_raw[10] *= lcm4
            inp_raw[11] *= lcm4

            #<------------------------I AND II------------------------>
            self.entry0.text = "I * " + str(lcm1) + " - II * " + str(lcm2) + ":"
            self.first0.text += "I: "
            
            if(inp_raw[0] != 1 and inp_raw[0] != 0):
                self.first0.text += str(inp_raw[0]) + "X "
            elif(inp_raw[0] == 1):
                self.first0.text += "X "
            
            if(inp_raw[1] > 1 and inp_raw[1] != -1):
                self.first0.text += "+ " + str(inp_raw[1]) + "Y "
            elif(inp_raw[1] < 0 and inp_raw[1] != -1):
                self.first0.text += "- " + str(-1*inp_raw[1]) + "Y "
            elif(inp_raw[1] == 1):
                self.first0.text += "+ Y "
            elif(inp_raw[1] == -1):
                self.first0.text += "- Y "
            

            if(inp_raw[2] > 1):
                self.first0.text += "+ " + str(inp_raw[2]) + "Z "
            elif(inp_raw[2] < 0 and inp_raw[2] != -1):
                self.first0.text += "- " + str(-1*inp_raw[2]) + "Z "
            elif(inp_raw[2] == 1):
                self.first0.text += "+ Z"
            elif(inp_raw[2] == -1):
                self.first0.text += "- Z"
            self.first0.text += " = " + str(inp_raw[3])

            self.second0.text += "II: "
            if(inp_raw[4] != 1 and inp_raw[4] != 0):
                self.second0.text += str(inp_raw[4]) + "X "
            elif(inp_raw[4] == 1):
                self.second0.text += "X "
            
            if(inp_raw[5] > 1):
                self.second0.text += "+ " + str(inp_raw[5]) + "Y "
            elif(inp_raw[5] < 0 and inp_raw[5] != -1):
                self.second0.text += "- " + str(-1*inp_raw[5]) + "Y "
            elif(inp_raw[5] == 1):
                self.second0.text += "+ Y "
            elif(inp_raw[5] == -1):
                self.second0.text += "- Y "
            
            if(inp_raw[6] > 1):
                self.second0.text += "+ " + str(inp_raw[6]) + "Z "
            elif(inp_raw[6] < 0 and inp_raw[6] != -1):
                self.second0.text += "- " + str(-1*inp_raw[6]) + "Z "
            elif(inp_raw[6] == 1):
                self.second0.text += "+ Z"
            elif(inp_raw[6] == -1):
                self.second0.text += "- Z"
            
            self.second0.text += " = " + str(inp_raw[7])

            self.result0.text += "Result(IV): "
            if(second[0] != 1 and second[0] != 0 and second[0] != -1):
                self.result0.text += str(second[0]) + "Y "
            elif(second[0] == 1):
                self.result0.text += "Y "
            elif(second[0] == -1):
                self.result0.text += "-Y "

            if(second[1] > 1):
                self.result0.text +=  "+ " + str(second[1]) + "Z "
            elif(second[1] < 1 and second[1]!= -1):
                self.result0.text += "- " + str(-1*second[1]) + "Z "
            elif(second[1]== 1):
                self.result0.text += "+ Z "
            elif(second[1]== -1):
                self.result0.text += "- Z "
            self.result0.text += "= " + str(second[2])


            #<------------------------I AND III------------------------>
            self.entry1.text = "I * " + str(lcm3) + " - III * " + str(lcm4) + ":"

            self.first1.text = "I: "
            if(first[0] != 1 and first[0] != 0):
                self.first1.text += str(first[0]) + "X "
            elif(first[0] == 1):
                self.first1.text += "X ";

            if(first[1] > 1):
                self.first1.text +=  "+ " + str(first[1]) + "Y "
            elif(first[1] < 1):
                self.first1.text +=  "- " +  str(-(first[1])) + "Y "
            elif(first[1] == 1):
                self.first1.text +=  "+ Y "
            elif(first[1] == -1):
                self.first1.text += "- Y "

            if(first[2] > 1):
                self.first1.text += "+ " + str(first[2]) + "Z "
            elif(first[2] < 1 and first[2] != -1):
                self.first1.text += "- " + str(-(first[2])) + "Z "
            elif(first[2] == 1):
                self.first1.text +=  "+ Z "
            elif(first[2] == -1):
                self.first1.text += "- Z "
            self.first1.text += "= " + str(first[3])
            
            #outputting the second row:
            self.second1.text = "III: "
            if(inp_raw[8] != 1 and inp_raw[8] != 0):
                self.second1.text += str(inp_raw[8]) + "X "
            elif(inp_raw[8] == 1):
                self.second1.text += "X "
            
            if(inp_raw[9] > 1):
                self.second1.text += "+ " + str(inp_raw[9]) + "Y "
            elif(inp_raw[9] < 1 and inp_raw[9] != -1):
                self.second1.text += "- " + str(-1*inp_raw[9]) + "Y "
            elif(inp_raw[9] == 1):
                self.second1.text += "+ Y "
            elif(inp_raw[9] == -1):
                self.second1.text += "- Y "
            

            if(inp_raw[10] > 1):
                self.second1.text += "+ " + str(inp_raw[10]) + "Z "
            elif(inp_raw[10] < 1 and inp_raw[10] != -1):
                self.second1.text += "- " + str(-1*inp_raw[10]) + "Z "
            elif(inp_raw[10] == 1):
                self.second1.text += "+ Z "
            elif(inp_raw[10] == -1):
                self.second1.text += "- Z "
            self.second1.text += "= " + str(inp_raw[11])

            self.result1.text = "Result(V): "
            if(third[0] != 1 and third[0] != 0 and third[0] != -1):
                self.result1.text += str(third[0]) + "Y "
            elif(third[0] == 1):
                self.result1.text += "Y "
            elif(third[0] == -1):
                self.result1.text += "-Y "
            
            if(third[1] > 1):
                self.result1.text += "+ " + str(third[1]) + "Z "
            elif(third[1] < 1 and third[1] != -1):
                self.result1.text += "- " + str(-1*third[1]) + "Z "
            elif(third[1] == 1):
                self.result1.text += "+ Z "
            elif(third[1] == -1):
                self.result1.text += "- Z "
            self.result1.text += "= " + str(third[2])
            
            self.entry2.text = "IV * " + str(lcm5) + " - V * " + str(lcm6) + ":"
            for i in range(len(second)):
                second[i] *= lcm5
            for i in range(len(third)):
                third[i] *= lcm6
            self.first2.text = "IV: "
            if(second[0] != 1 and second[0] != 0 and second[0] != -1):
                self.first2.text += str(second[0]) + "Y "
            elif(second[0] == 1):
                self.first2.text += "Y "
            elif(second[0] == -1):
                self.first2.text += "-Y "
            
            if(second[1] > 1):
                self.first2.text += "+ " + str(second[1]) + "Z "
            elif(second[1] < 1 and second[1] != -1):
                self.first2.text += "- " + str(-1*second[1]) + "Z "
            elif(second[1] == 1):
                self.first2.text += "+ Z "
            elif(second[1] == -1):
                self.first2.text += "- Z "
            self.first2.text += "= " + str(second[2])
            self.second2.text = "V: "
            if(third[0] != 1 and third[0] != 0 and third[0] != -1):
                self.second2.text += str(third[0]) + "Y "
            elif(third[0] == 1):
                self.second2.text += "Y "
            elif(third[0] == -1):
                self.second2.text += "-Y "
            
            if(third[1] > 1):
                self.second2.text += "+ " + str(third[1]) + "Z "
            elif(third[1] < 1 and third[1] != -1):
                self.second2.text += "- " + str(-1*third[1]) + "Z "
            elif(third[1] == 1):
                self.second2.text += "+ Z "
            elif(third[1] == -1):
                self.second2.text += "- Z "
            self.second2.text += "= " + str(third[2])
            self.result2.text = "Result: "

            if(result[0] != 1 and result[0] != -1 and result[0] != 0):
                self.result2.text += str(result[0]) + "Z "
            elif(result[0] == 1):
                self.result2.text += "Z "
            elif(result[0] == -1):
                self.result2.text += "-Z "
            else:
                self.result2.text += "0 "
            
            self.result2.text += "= " + str(result[1])
            self.answx.text = "Z = " + str(result[1]) + "/" + str(result[0]) + " = " + str(lib.Zret())
            self.answy.text = "Y = (" + str(second[2]) + " - (" + str(second[1]) + "*" + str(lib.Zret()) + ")) / " + str(second[0]) + " = " + str(lib.Yret())
            self.answz.text = "X = (" + str(first[3]) + " - (" + str(first[2]) + "*" + str(lib.Zret()) + ") - (" + str(first[1]) + "*" + str(lib.Yret()) + ")) / " + str(first[0]) + " = " + str(lib.Xret())
 
        except ValueError:
            print("oopsie! You didn't enter anything!")
        except IndexError:
            if(lib.divbyzeroret()):
                self.entry0.text = "It seems like you got unlucky :("
                self.second0.text = "If you're seeing this, then probably"
                self.result0.text = "your system has division by zero"

if __name__ == "__main__":
    MainApp().run()
    