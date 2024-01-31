import webbrowser as wb
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


recruiter_websites = {"Agrijob": "https://www.agrijob.co.za/jobs/",
                      "M3 recruitment": "https://jobs.m3online.co.za/sys/jobList",
                      "Indeed": "https://za.indeed.com/jobs?q=agriculture&l=Western+Cape&from=searchOnHP&vjk=21775e26431b8827",
                      "Farm Managers": "https://farmmanagersa.co.za/job-vacancies/",
                      "Exceed recruitment": "https://www.exceed.co.za/job-category/agriculture/",
                      "CA support": "https://casupport.co.za/vacancies/"
                      }

class MainApp(App):
    pass


class MainWidgets(Widget):
    pass


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)




MainApp().run()
