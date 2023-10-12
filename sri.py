pin,cash=input('enter your pin and withdraw amount').split('@')
print('user pin',pin)
print('withdraw amount',cash)                                                          
cashvalue=int(cash)
#cashout=4000
#print('collect ur money',cash,cashout,sep='@@',end='$$$')
#print("tq using for this ATM",end='\t')
#print("your balance:")#
#print(type(cashvalue))
remaingamount=100000
currentbalnce=remaingamount-cashvalue
print("in the bank;",currentbalnce)
print('take your cash {0},balnce in your account {1}'.format(cashvalue,currentbalnce))
