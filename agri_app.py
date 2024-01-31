import webbrowser as wb
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


# Main function
def open_webs():
    recruiter_websites = ["https://www.agrijob.co.za/jobs/",
                          "https://jobs.m3online.co.za/sys/jobList",
                          "https://za.indeed.com/jobs?q=agriculture&l=Western+Cape&from=searchOnHP&vjk=21775e26431b8827",
                          "https://farmmanagersa.co.za/job-vacancies/",
                          "https://www.exceed.co.za/job-category/agriculture/",
                          "https://casupport.co.za/vacancies/",
                          ]
    for site in recruiter_websites:
        wb.open_new_tab(site)


# open_webs()


class main_app(App):
    pass


class main_layout(BoxLayout):
    pass



main_app().run()
