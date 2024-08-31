from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


#This function will render the Home Page when requested
def home(request):
    form = TransactionForm(data=request.POST or None) #Retrieve Transaction Form
    #Checks if request method is POST
    if request.method == "POST":
        pk = request.POST['account'] #if the form is submitted, retrieve which account the user wants to view
        return balance(request, pk) #call balance function to render that account's Balance Sheet
    content = {'form': form} #pass content to the template in the dictionary
    #Adds content of form to page
    return render(request, 'checkbook/index.html', content)

#This function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None) #Retrieve the Account form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): #check to see if the submitted form is valid and if so, saves the form
            form.save() #saves new account
            return redirect('index') #saves content to the template as a dictionary
    content = {'form': form}
    #adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)

#This function will render the Balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) #Retrieve the requested account using its primary key
    transactions = Transaction.Transaction.filter(account=pk) #Retrieve all of that account's transactions
    current_total = account.initial_deposit #Create account total variable, starting with initial deposit value
    table_contents = {} #Creates a dictionary into which transaction information will be placed
    for t in transactions: #Loop through transactions and determine which is a deposit or withdrawal
        if t.type =='Deposit':
            current_total += t.amount #If deposit, add amount to balance
            table_contents.update({t: current_total}) #Add transaction and total to the dictionary
        else:
            current_total -= t.amount #If withdrawal, subtract amount from balance
            table_contents.update({t: current_total}) #ADd Transaction and total to the dictionary
    #pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

#this function will render the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None) #Retrieve the Transaction Form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid(): #Check to see if the submitted form is valid and if so, saves the form
            pk = request.POST['account']
            form.save() #saves the transaction form
            return balance(request, pk) #redirects the user to the home page after form submission
    #pass the content to the template in the dictionary
    content = {'form': form}
    #Add content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)

