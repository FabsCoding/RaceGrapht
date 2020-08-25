# pylint: disable=E1101
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import matplotlib.pyplot as plt
import csv

with open('steering.csv', newline='') as f:
    reader = csv.reader(f)
    raw_data = list(reader)

data = []
for x in raw_data:
    data.append(float(x[0]))

#plt.style.use('dark_background')
datafig = plt.figure()
plt.plot(data)
plt.title('Steering Input')
rdatafig = plt.figure()
plt.plot(data[::-1])
plt.title('Reversed Steering Input')

class GraphPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FigureCanvasKivyAgg(datafig))

class LoginPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text="Welcome to RaceGrapht",size_hint=(1,0.7)))
        self.login = Button(text="Login",size_hint=(1,0.3))
        self.login.bind(on_press=self.login_button)
        self.add_widget(self.login)
    
    def login_button(self, instance):
        Analyser.screen_manager.current = "graph"
        Analyser.resize_window(920,500)


class AnalysisApp(App):

    def resize_window(self,x,y):
        init_center = Window.center
        Window.size = (x,y)
        Window.left -= (Window.center[0] - init_center[0])
        Window.top -= (Window.center[1] - init_center[1])

    def build(self):
        self.screen_manager = ScreenManager()

        #Add login-page to screenmanager
        self.login_page = LoginPage()
        screen = Screen(name="login")
        screen.add_widget(self.login_page)
        self.screen_manager.add_widget(screen)

        #Add graph-page to screenmanager
        self.graph_page = GraphPage()
        screen = Screen(name="graph")
        screen.add_widget(self.graph_page)
        self.screen_manager.add_widget(screen)

        self.resize_window(300,150)

        return self.screen_manager

Analyser = AnalysisApp()
Analyser.run()
