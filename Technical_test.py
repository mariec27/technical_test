 
import pandas as pd  
import numpy as np

def ifnull(df, val):
    """This function is necessary to print default values when a Dataframe is empty
    Attributes
    ----------
    df : :obj:`pandas.DataFrame` 
    val : string used as value to print if df is empty
    """
    if df.empty:
        print(val)
    else:
        print(df)

def get_account_stats(df, number):
    """This function ask you to write  an account  number and  gives you  information  about the  transactions  of  this  one :
    transaction number, subscription name , total amount , total amount per transaction type, transaction history and average of all the dataframe's transactions group by transaction type
    If you press "Enter" instead of write an account number, the function print a dataset with every account_number and the transaction_type associated and the amount sum.

    Attributes
    ----------
    df : :obj:`pandas.DataFrame` 
    number :'int' : account number 
    """
    if number:
        DataAccount =df[  df.account_number == int(number)].reset_index(drop=True)
        print("\n")
        print ("Account Number : " + number)
        print("\n")
        transactions_nb =DataAccount.shape[0]
        print('Transactions number: ', transactions_nb)
        print("\n")
        subs = DataAccount["subs_name"].unique()
        print('Subscription Name : ', subs[0])
        print("\n")
        Sum_amount  = DataAccount["amount"].sum()
        print('Total Transactions: ', Sum_amount)
        print("\n")
        print("Transactions per type: ")

        DataAccount_cheque_debit = DataAccount[  DataAccount.transaction_type == "cheque_debit"]
        DataAccount_cb_debit = DataAccount[  DataAccount.transaction_type == "cb_debit"]
        DataAccount_withdrawal_debit = DataAccount[  DataAccount.transaction_type == "withdrawal_debit"]
        ifnull(DataAccount_withdrawal_debit[["transaction_type","amount"]].groupby('transaction_type').sum(),"withdrawal_debit      0")
        ifnull(DataAccount_cheque_debit[["transaction_type","amount"]].groupby('transaction_type').sum(),"cheque_debit      0")
        ifnull(DataAccount_cb_debit[["transaction_type","amount"]].groupby('transaction_type').sum(),"cb_debit      0")
    #  print(DataAccount[["transaction_type","amount"]].groupby('transaction_type').sum().sort_values(by="transaction_type", ascending = True))     ##Can't be used beacause doesn't show every values but it's another solution
        print("\n")
        print("Transaction History: ")
        print(DataAccount[["transaction_start","amount"]].groupby('transaction_start').sum().sort_values(by = 'transaction_start', ascending = True))
    else:
        print("Every account with the amount associated : " )
        print(df[["account_number","transaction_type","amount"]].groupby(['account_number',"transaction_type"]).sum())

    print("\n")
    print("Mean Transaction : " )
    print(df[["transaction_type","amount"]].groupby('transaction_type').mean())


if __name__=='__main__':
    df_accounts_data = pd.read_csv("accounts_data.csv")  
    df_bank_offers= pd.read_csv("bank_offers.csv")
    stats_df= pd.merge(df_accounts_data, df_bank_offers, how="left", on="subs_id")
    number = input('Write an account number or click enter to have a data summary : ')
    get_account_stats(stats_df, number)