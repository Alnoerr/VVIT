class Employee:
    def __init__(self, employee_id, employee_name, *args):
        self.id = employee_id
        self.name = employee_name

    def get_info(self):
        return self.__dict__


class Manager(Employee):
    def __init__(self, employee_id, employee_name, department, *args):
        super().__init__(employee_id, employee_name, *args)
        self.department = department

    def manage_project(self):
        print(f"{self.name} performing management")


class Technician(Employee):
    def __init__(self, employee_id, employee_name, specialization, *args):
        super().__init__(employee_id, employee_name, *args)
        self.specialization = specialization

    def perform_maintenance(self):
        print(f"{self.name} performing maintenance")


class TechManager(Manager, Technician):
    def __init__(self, employee_id, employee_name, department, specialization, employee_list, *args):
        super().__init__(employee_id, employee_name, department, specialization, *args)
        self.employee_list = employee_list

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def get_team_info(self):
        return [employee.get_info() for employee in self.employee_list]


if __name__ == '__main__':
    tech_manager = TechManager(
        0,
        "sample tech manager name",
        "sample department",
        "sample specialization",
        []
    )
    print(TechManager.mro())

    tech_manager.perform_maintenance()
    print(tech_manager.get_info())
    tech_manager.manage_project()

    tech_manager.add_employee(
        Employee(
            employee_id=1,
            employee_name="sample employee name 2"
        )
    )
    tech_manager.add_employee(
        Manager(
            employee_id=2,
            employee_name="sample manager name 3",
            department="sample department"
        )
    )
    print(tech_manager.get_team_info())
