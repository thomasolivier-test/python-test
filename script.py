# !/usr/bin/env python3
# Author: Thomas Olivier
# Date: 31 Januray 2020

from datetime import datetime
import vote

# Election object
# An election has candidates
# An election receive voters votes
# An election is an event that occur between a start date and an end date
# At the end of an election, a candidate win the election

class Election(object): 
    def __init__(self, name, description):
        super(Election, self).__init__()
        self.name = name
        self.description = description
        self.start_date = datetime.now()
        self.end_date = datetime.now() + datetime.timedelta(days = 7)
        self.status = "CREATED"
        self.running = False
        self.number_of_grades = 6
        self.grades = ["Excellent", "Very good", "Good", "Passable", "Inadequate", "Mediocre", "Bad"]
        self.candidates = []
        self.votes = []

    def set_start_date(self, start_date):
        if(not self.is_running()):    
            if(datetime.now() < start_date and start_date < self.end_date):
                self.start_date = start_date
            elif(start_date > self.end_date):
                self.end_date = start_date + datetime.timedelta(days = 7)
                print("The end date of the election has been updated accordingly.\n")
            else:
                print("You cannot change the election launch for a date prior to today.\n")

    def set_end_date(self, end_date):
        if(datetime.now() < end_date and self.start_date < end_date):
            self.end_date = end_date
        else:
            print("You cannot change the closing date of the election for a date prior to the start date or prior to today.\n")

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_status(self):
        return self.status
    
    def get_candidates(self):
        return self.candidates

    def is_running(self):
        if(self.start_date < datetime.now() and datetime.now() < self.end_date):
            self.running = True
        else:
            self.running = False
            if(datetime.now() > self.end_date):
                self.status = "FINISHED"
        return self.running

    def set_number_of_grades(self, number):
        if(number >= 5 and number <= 7):
            self.number_of_grades = number
            return True
        else:
            return False

    def get_grades(self):
        grades = []
        grades = self.grades
        



    def append_candidate(self, new_candidate):
        if(not self.is_running()):
            self.candidates.append(new_candidate)
            return True
        else:
            return False
    
    def list_candidates(self):
        for candidate in self.candidates:
            print(candidate + "\n")
        return True

    def start(self):
        if(not self.is_running()):  
            self.start_date = datetime.now()
            self.running = True
            self.status = "STARTED"
            return True
        else:
            print("Election already running.\n")
            return False

    def stop(self):
        if(self.is_running()):  
            self.end_date = datetime.now()
            self.running  = False
            self.status = "STOPPED"
            return True
        else:
            print("Election not running.\n")
            return False

    def append_vote(self, vote):
        if(self.is_running()):
            self.votes.append(vote)
            return True
        else:
            return False
    
    def validate_vote(self, vote):
        return True
