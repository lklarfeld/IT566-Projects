"""Implements Team Roster Operations"""
import json
from datetime import date

class Roster(object):
    """Implements Team Roster Operations"""
    def __init__(self):
        self._Initialize_Roster_Directory()

    def load_roster(self):
        if __debug__:
            print('load_roster() called')
        try:
            file_path = self._get_file_path()
            with open(file_path, 'r', encoding='UTF-8') as f:
                self.dictionary = json.loads(f.read())
        except OSError:
            print('Problem loading file. Please try again :)')

    def print_roster(self):
        """Prints current Roster/Dictionary out"""
        if __debug__:
            print('print_roster() called')
        for key, value in self.dictionary.items():
            if key == 'members':
                print('members:')
                for item in value:
                    print(f'\t {item["name"]:25} \t {item["age"]}')
            else:
                print(f'{key}: \t {value}')

    def _get_file_path(self):
        """Gets file path from user"""
        f_path = input("Please enter path and filename: ")
        return f_path

    def _Initialize_Roster_Directory(self):
        if __debug__:
            print("Initializing new Roster Directory...")
        self.dictionary = {}
        self.dictionary['type'] = 'Team Roster'
        self.dictionary['date'] = date.today().isoformat()
        self.dictionary['sport'] = 'Curling'
        self.dictionary['country'] = 'USA'
        self.dictionary['members'] = []
        if __debug__:
            print("New Roster Directory Initialized")