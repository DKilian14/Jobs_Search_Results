from bs4 import BeautifulSoup
import requests
from datetime import date
import sqlite3
from jobclass import Opportunity


dbconnection = sqlite3.connect('jobs.db')
cursor = dbconnection.cursor()

class JobsResults(object):
    def __init__(self,mid):
        self.mid = mid

    def create_sql():
        try:
            cursor.execute("""CREATE TABLE opportunities (
            title text,
            company text,
            skills text,
            posted text
            )""")
            dbconnection.commit()
            dbconnection.close()
        except:
            pass

    def collect_jobs(self):

        full_url  = self.draft_url()
        html_text = requests.get(full_url).text
        soup      = BeautifulSoup(html_text,'lxml')
        jobs      = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

        for job in jobs:
            published_date = job.find('span', class_='sim-posted').span.text

            if 'Posted few days ago' in published_date:

                published_date  = date.today()
                company_name    = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
                skills          = job.find('span',class_='srp-skills').text.replace(' ','')
                title           = job.find('a').text


                opp = Opportunity(company_name,skills,published_date,title)
                temp_opp = Opportunity(company_name,skills,published_date,title)
                print("JOB TITLE:       ",temp_opp.scrub_title())
                print("COMPANY NAME:    ", temp_opp.scrub_comp_name())
                print("SKILLS REQUIRED: ", temp_opp.scrub_skills())
                print("JOB POSTED DATE: ", temp_opp.scrub_date())
                print("_________________________________________")
                # print("TASK COMPLETE: ", temp_opp)


                oppt = opp.scrub_title()
                oppc = opp.scrub_comp_name()
                opps = opp.scrub_skills()
                oppd = opp.scrub_date()
                """
                Before updating the database, I need to make sure each item (oppt, oppc, opps, oppd)
                is an entire string. Only one sting can be saved per cell in sqlite3.
                Online, someone mntioned coding the items into JSON. Not sure what to do yet...
                """
                # self.update_sql(oppt,oppc,opps,oppd)


    def draft_url(self):
        url_body = ""
        for hit in self.mid:
            url_body += hit+'+'
        complete_url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords='+url_body+'&txtLocation='
        return complete_url


    def update_sql(self, oppt, oppc, opps, oppd):
        print("you are in UPDATE_SQL")
        cursor.execute("INSERT INTO opportunities VALUES(?,?,?,?)", (oppt, oppc, opps, oppd))
        dbconnection.commit()
        dbconnection.close()
        pass


    create_sql()
