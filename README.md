# Employee Payroll System

**Name:** Darshil Raj

**ERP:** RU-26-01791

**Section:** 1L

**Project:** PS 45, Employee Payroll System


## About This Project

This is a console program that works out the monthly pay for each person in a small company. You enter a basic salary and overtime hours, and the program prints a payslip with the overtime pay, gross salary, PF deduction, tax and final net salary.

There are two kinds of staff. A regular **Employee** gets basic pay plus overtime. A **Manager** gets the same, plus a bonus of 10% of their basic pay. Every payslip is also saved to `payroll.txt`, so there is a record after the program closes.

## Language and Concepts

**Language:** Python 3, run from the terminal. No GUI and no external libraries are needed.

**Concepts used:**

- **Classes and inheritance:** `Employee` holds the data and calculations. `Manager` inherits from it and changes only the bonus, so the shared logic is written once.
- **Functions:** Each calculation, such as overtime, gross, PF, tax and net, is its own method, and small helper functions handle input and saving.
- **Calculations:** Percentages for PF, tax and bonus, multiplication for overtime, and a condition that applies tax only when gross is above Rs.50,000.
- **Input validation:** `while True` loops with `try` and `except` keep asking until a valid number is entered.
- **File handling:** Payslips are appended to `payroll.txt` using `open()` in append mode, so earlier payslips are kept.

## Files

- `employee_payroll.py`: the whole program in one file, including the `Employee` and `Manager` classes
- `payroll.txt`: created automatically when the first payslip is saved
- `README.md`: this file
- `SUMMARY.md`: project statement, implementation, test cases and conclusion
- `screenshots/`: terminal screenshots of each test case

## How to Run

1. Make sure Python 3 is installed.
2. Put `employee_payroll.py` in a folder.
3. Open a terminal in that folder and run:

   ```
   python employee_payroll.py
   ```

4. Choose `1` to add an Employee, `2` to add a Manager, or `3` to exit.

## The Menu

```
1. Add Employee
2. Add Manager
3. Exit
```

## How the Pay is Worked Out

| Item | Rule |
|------|------|
| Overtime | Overtime hours × Rs.200 |
| Bonus | 10% of basic pay (Manager only) |
| Gross | Basic + Overtime + Bonus |
| PF | 12% of basic pay |
| Tax | 10% of gross, only when gross is above Rs.50,000. Otherwise 0. |
| Net Salary | Gross − PF − Tax |

## How the Program Checks Input

- **Name:** cannot be empty.
- **Basic salary:** must be a number greater than 0. Anything else asks again.
- **Overtime hours:** must be a number 0 or more. Anything else asks again.
- **Menu choice:** must be 1, 2 or 3.

The program keeps asking for a value until it gets a valid one, so one wrong entry doesn't stop the whole run.

## How the Code is Organised

- `Employee` holds the basic data and all the calculations: overtime, gross, PF, tax and net.
- `Manager` inherits from `Employee`. It only changes two things: it adds a bonus, and its payslip line shows the bonus.
- The `show_number()` helper prints whole numbers without decimals (for example `2000` instead of `2000.0`).

## Payslip Output

```
----- Payslip -----
Employee: E1, Aman
Overtime: 2000 | Gross: 32000
PF: 3600 | Tax: 0
Net Salary: 28400
-------------------
```

## Testing

I ran the four PS test cases in order. Delete `payroll.txt` first so that the file only contains the payslips from the test run.

1. **Test 1:** Add an Employee, ID `E1`, name `Aman`, basic `30000`, overtime `10`.
2. **Test 2:** Add an Employee, ID `E2`, name `Neha`, basic `10000`, overtime `0`.
3. **Test 3:** Add an Employee, ID `E3`, name `Test`. Enter basic `-5000` (rejected), then `30000`. Enter overtime `abc` (rejected), then `5`.
4. **Test 4:** Add a Manager, ID `M1`, name `Riya`, basic `60000`, overtime `5`.

## Known Limits

- Employee IDs are not checked for duplicates, so the same ID can be used twice.
- Tax is a flat 10% of gross above the limit, not a tax slab.
- `payroll.txt` only grows. The program has no way to view or delete old payslips.
- Overtime hours can be decimals, such as `2.5`.