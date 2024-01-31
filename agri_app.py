# Main function
import webbrowser as wb
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

open_webs()

