# Will take in the data provided by Timesjobs
# and prettify it to prepare for insertion
#to sqlite3 database, "jobs.db"

class Opportunity(object):

    def __init__(self,company,skills,date,job_title):
        self.company = company
        self.skills = skills
        self.date = date
        self.job_title = job_title
        self.special_char = '@_!#$%^&*()<>?/\|}{~:;.[],-'


    """
    Removes special characters from any of the data coming in.
    """
    def rm_spec_char(self):
        return list(self.special_char)


    def scrub_comp_name(self):
        self.company = self.company.split()
        return self.company[0]


    def scrub_skills(self):
        self.skills = self.skills.split()
        self.skills = self.skills[0].split(',')
        return self.skills


    def scrub_date(self):
        return self.date


    def scrub_title(self):
        clean_title = []
        chopped_title = self.job_title.split()

        for i in chopped_title:
            if i not in self.rm_spec_char():
                clean_title.append(i)
        return clean_title


    def __repr__(self):
        return "Opportunity('{}','{}','{}','{}')".format(self.company, self.skills, self.date, self.job_title)
