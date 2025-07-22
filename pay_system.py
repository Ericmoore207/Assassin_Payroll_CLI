import os
import json
import random
from employee import Employee

class PaySystem:
    def __init__(self, employee_file='employees.json'):
        self.employee_file = employee_file
        self.employees = self.load_employees()

    def load_employees(self):
        if not os.path.exists(self.employee_file):
            with open(self.employee_file, 'w') as f :
                json.dump({}, f)
        with open(self.employee_file, 'r') as f:
            return json.load(f)

    def save_employees(self):
        with open(self.employee_file, 'w' ) as f:
            json.dump(self.employees, f, indent=4)


    def add_employee(self):

        while True:
            try:
                employee_name = input('\nEnter employee\'s  Full name: ').strip().capitalize()
                if not employee_name.replace(" ", "").isalpha():
                    print("Name can only contain letters.")
                else:
                    break
            except TypeError:
                print("This field can only contain letters.")
                
        while True:
            try:
                
                employee_id = input('\nEnter employee\'s ID: ')
                if not employee_id.isdigit():
                    print("ID can only be numbers.")
                elif len(employee_id) > 3 :  
                    print("ID can't be greater than 3 Digit")
                elif employee_id in self.employees:
                    print("Employee ID already exists.")
                else:
                    break
            except ValueError:
                print("This field can only contain numbers.")


        while True:
            try:
                department = input('\nEnter employee\'s department: ').strip().upper()
                if not department.replace(" ", "").isalpha():
                    print("This field can only contain letters.")
                else:
                    break
            except TypeError:
                print("This field can only contain letters.")


        while True:
            try:
                base_salary = input("\nEnter employee's base salary: ")
                if not base_salary.isdigit() or float(base_salary) <= 0:
                    print('Invalid amount.')
                else:
                    base_salary = float(base_salary)
                    break

            except ValueError:
                print("This field can only contain numbers.")


        while True:
            try:
                bonus = input('\nEnter employee\'s bonus: ')
                if not bonus.isdigit() or float(bonus) <= 0:
                    print('Invalid amount.')
                else:
                    bonus = float(bonus)
                    break
            except ValueError:
                print("This field can only contain numbers.")


        employee = Employee(
            employee_name=employee_name,
            employee_id=employee_id,
            department=department,
            base_salary=base_salary,
            bonus=bonus
        )
            
        self.employees[employee_id] = employee.to_dict()
        self.save_employees()

        print(f"\nEmployee {self.employees[employee_id]['employee_name']} added successfully!")
        input('\nPress Enter to continue...')




    def apply_bonus(self):
        print('apply bonus')

    def calculate_net_salary(self):
        print('calculate_net_salary')

    def generate_single_payslip(self):
        print('generate_single_payslip')

    def generate_payslips(self):
        print('generate_payslips')