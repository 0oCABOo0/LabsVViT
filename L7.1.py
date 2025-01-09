class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_project(self):
        return f"Менеджер {self.name} управляет в отделе {self.department}."

class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Техник {self.name} специалист {self.specialization}."

class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = [member.get_info() for member in self.team]
        return "Команда:\n" + "\n".join(team_info)

emp1 = Employee("Иван Иванов", 1)
mgr1 = Manager("Петр Петров", 2, "IT")
tech1 = Technician("Сидор Сидоров", 3, "Электрик")
tech_mgr = TechManager("Ольга Ольгина", 4, "Проектный", "Сетевой администратор")

tech_mgr.add_employee(emp1)
tech_mgr.add_employee(mgr1)
tech_mgr.add_employee(tech1)

print(mgr1.manage_project())
print(tech1.perform_maintenance())
print(tech_mgr.get_team_info())