#  create employee class 
class Employee:
    def __init__(self, employee_name, employee_id, department, base_salary, bonus):
        self.employee_name = employee_name
        self.employee_id = employee_id 
        self.departmenet = department
        self.base_salary = base_salary
        self.bonus = bonus


# convert Employee object to dict
    def to_dict(self):
        return {
            'employee_name': self.employee_name,
            'employee_id': self.employee_id,
            'department': self.departmenet,
            'base_salary': self.base_salary,
            'bonus': self.bonus
        }