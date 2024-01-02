import customtkinter as ctk


class LoanCalculator:
    def __init__(self):
        window = ctk.CTk()
        window.title("Loan Calculator")


        ctk.CTkLabel(window, text = "Annual Interest Rate").grid(row = 1,
        column = 1, sticky = 'W')
        ctk.CTkLabel(window, text = "Number of Years").grid(row = 2,
        column = 1, sticky = 'W')
        ctk.CTkLabel(window, text = "Loan Amount").grid(row = 3,
        column = 1, sticky = 'W')
        ctk.CTkLabel(window, text = "Monthly Payment").grid(row = 4,
        column = 1, sticky = 'W')
        ctk.CTkLabel(window, text = "Total Payment").grid(row = 5,
        column = 1, sticky = 'W')


        self.annualInterestRateVar = ctk.StringVar()
        ctk.CTkEntry(window, textvariable = self.annualInterestRateVar,
        justify ='left').grid(row = 1, column = 2)


        self.numberOfYearsVar = ctk.StringVar()
        ctk.CTkEntry(window, textvariable = self.numberOfYearsVar,
        justify ='left').grid(row = 2, column = 2)


        self.loanAmountVar = ctk.StringVar()
        ctk.CTkEntry(window, textvariable = self.loanAmountVar,
        justify ='left').grid(row = 3, column = 2)

        self.monthlyPaymentVar = ctk.StringVar()
        ctk.CTkLabel(window, textvariable =
        self.monthlyPaymentVar).grid(row = 4, column = 2,
        sticky = 'E')


        self.totalPaymentVar = ctk.StringVar()
        ctk.CTkLabel(window, textvariable =
        self.totalPaymentVar).grid(row = 5,
        column = 2, sticky = 'E')
        
        ctk.CTkButton(window, text = "Compute Payment",
        command = self.computePayment).grid(
        row = 6, column = 2, sticky = 'E')

        for widget in window.winfo_children():
            widget.grid(padx=5,pady=5)

        window.mainloop() # Create an event loop
        

    def computePayment(self):
        loanAmount  = float(self.loanAmountVar.get())
        interestRate = float(self.annualInterestRateVar.get()) / 1200
        years = int(self.numberOfYearsVar.get())    

        monthlyPayment = self.getMonthlyPayment(loanAmount,interestRate,years)
        self.monthlyPaymentVar.set(format(monthlyPayment, "10.2f"))

        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * years
        self.totalPaymentVar.set(format(totalPayment, "10.2f"))

    def getMonthlyPayment(self,loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1- 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment
    

LoanCalculator()
# Create GUI