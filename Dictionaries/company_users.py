# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
# •	Until you receive the "End" command, you will be receiving input in the format:
# "{company_name} -> {employee_id}".
# •	The input always will be valid.

company_users = {}
command = input()

while command != "End":
    company, employee_id = command.split(" -> ")
    if company not in company_users:
        company_users[company] = []
    if employee_id not in company_users[company]:
        company_users[company].append(employee_id)

    command = input()

for company, employee_id in company_users.items():
    print(company)
    for employee in employee_id:
        print(f"-- {employee}")
