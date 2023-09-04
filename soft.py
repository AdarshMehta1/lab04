class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"


def sort_employees(employees, key):
    if key == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif key == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif key == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        raise ValueError("Invalid sorting parameter")

def print_employee_table(employee_list):
    print("Employee ID\tName\tAge\tSalary (PM)")
    for employee in employee_list:
        print(employee)


if __name__ == "__main__":
    employee_data = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    sorting_key = int(input("Enter your choice: "))

    sorted_employees = sort_employees(employee_data, sorting_key)
    print_employee_table(sorted_employees)
