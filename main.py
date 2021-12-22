import application.db.people
from application.salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    application.db.people.get_employees()
    calculate_salary()
    print(datetime.now())