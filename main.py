from pay_system import PaySystem

def main():
        pay_system = PaySystem()
    
        while True:
            print("""
            \nEmployee Payroll System
            1. Add Employee
            2. Apply Bonus
            3. Generate Single Payslip (by ID)
            4. Generate All Payslips
            5. Exit
            """)
            choice = input('👉 Choose an option:')

            if choice == '1':
                pay_system.add_employee()

            elif choice == '2':
                pay_system.apply_bonus()

            elif choice == '3':
                pay_system.generate_single_payslip()

            elif choice == '4':
                pay_system.generate_payslips()

            elif choice == '5':
                print('Thank you for using Assassin Pay. See you soon!')
                break
            else:
                print('Invaild Option Try again!')
                


if __name__ == '__main__':
     main()