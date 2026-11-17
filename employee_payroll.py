PF_RATE = 0.12
TAX_RATE = 0.10
TAX_LIMIT = 50000
OVERTIME_RATE = 200
BONUS_RATE = 0.10
PAYSLIP_FILE = "payroll.txt"


def show_number(value):
    # Print 2000 instead of 2000.0, but keep decimals when needed
    value = round(value, 2)
    if value == int(value):
        return str(int(value))
    return f"{value:.2f}"


class Employee:
    def __init__(self, emp_id, name, basic, overtime_hours):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic
        self.overtime_hours = overtime_hours

    def calculate_overtime(self):
        return self.overtime_hours * OVERTIME_RATE

    def calculate_bonus(self):
        return 0

    def calculate_gross(self):
        return self.basic + self.calculate_overtime() + self.calculate_bonus()

    def calculate_pf(self):
        return self.basic * PF_RATE

    def calculate_tax(self):
        gross = self.calculate_gross()
        if gross > TAX_LIMIT:
            return gross * TAX_RATE
        return 0

    def calculate_net(self):
        return self.calculate_gross() - self.calculate_pf() - self.calculate_tax()

    def earnings_line(self):
        return ("Overtime: " + show_number(self.calculate_overtime())
                + " | Gross: " + show_number(self.calculate_gross()))

    def payslip_text(self):
        lines = [
            "----- Payslip -----",
            "Employee: " + self.emp_id + ", " + self.name,
            self.earnings_line(),
            "PF: " + show_number(self.calculate_pf())
            + " | Tax: " + show_number(self.calculate_tax()),
            "Net Salary: " + show_number(self.calculate_net()),
            "-------------------",
        ]
        return "\n".join(lines)


class Manager(Employee):
    def calculate_bonus(self):
        return self.basic * BONUS_RATE

    def earnings_line(self):
        return ("Overtime: " + show_number(self.calculate_overtime())
                + " | Bonus: " + show_number(self.calculate_bonus())
                + " | Gross: " + show_number(self.calculate_gross()))


# ---------- Input with validation ----------

def read_basic():
    while True:
        text = input("Basic salary: ").strip()
        try:
            value = float(text)
            if value > 0:
                return value
        except ValueError:
            pass
        print("Invalid basic salary. Enter a positive number.")


def read_overtime_hours():
    while True:
        text = input("Overtime hours: ").strip()
        try:
            value = float(text)
            if value >= 0:
                return value
        except ValueError:
            pass
        print("Invalid overtime hours. Enter a non-negative number.")


def read_name():
    while True:
        name = input("Name: ").strip()
        if name != "":
            return name
        print("Name cannot be empty.")


# ---------- Saving ----------

def save_payslip(text):
    with open(PAYSLIP_FILE, "a") as file:
        file.write(text + "\n\n")


# ---------- Main menu ----------

def main():
    while True:
        print("\n1. Add Employee")
        print("2. Add Manager")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1" or choice == "2":
            emp_id = input("Employee ID: ").strip().upper()
            name = read_name()
            basic = read_basic()
            overtime_hours = read_overtime_hours()

            if choice == "1":
                person = Employee(emp_id, name, basic, overtime_hours)
            else:
                person = Manager(emp_id, name, basic, overtime_hours)

            payslip = person.payslip_text()
            print(payslip)
            save_payslip(payslip)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1, 2 or 3.")


main()