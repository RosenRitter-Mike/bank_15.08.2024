from datetime import datetime, timedelta

bank_accounts: dict = {
    1001: {
        "first_name": "Alice",
        "last_name": "Smith",
        "id_number": "123456789",
        "balance": 2500.50,
        "transactions_to_execute": [
            ("2024-08-17 14:00:00", 1001, 1002, 300), ("2024-08-17 15:00:00", 1001, 1003, 200)],
        "transaction_history": [
            ("2024-08-15 09:00:00", 1001, 1002, 500), ("2024-08-15 09:30:00", 1001, 1003, 100)]
    },
    1002: {
        "first_name": "Bob",
        "last_name": "Johnson",
        "id_number": "987654321",
        "balance": 3900.75,
        "transactions_to_execute": [],
        "transaction_history": []
    }}

def new_tra() -> None:
    while True:
        send: int = int(input("sender account number: "));
        if send not in bank_accounts:
            print(f"sender account- {send} - could not be found");
            continue;
        rec: int = int(input("recipient account number: "));

        if rec not in bank_accounts:
            print(f"recipient account- {rec} - could not be found");
            continue;
        tr_sum: float = float(input("sum of transfer: "));

        if bank_accounts[send]["balance"] < tr_sum:
            print(f"sender account balance- {bank_accounts[send]['balance']}\nthe transfer sum - {tr_sum}\n"
                  f"not enough balance");
            continue;
        else:
            temp_t: tuple = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), send, rec, tr_sum);
            bank_accounts[send]["transactions_to_execute"].append(temp_t);
            return;

def com_tra() -> None:
    while True:
        acc: int = int(input("account number: "));
        if acc not in bank_accounts:
            print(f"account- {acc} - could not be found");
            continue;
        for tra in bank_accounts[acc]["transactions_to_execute"]:
            bank_accounts[acc]['balance'] -= tra[3];
            bank_accounts[acc]["transaction_history"].append(tra);
            bank_accounts[acc]["transactions_to_execute"].remove(tra);
        else:
            print(f"account data\n{bank_accounts[acc]}")
            return;

def find_by_id() -> None:
    id_num: int = int(input("id number: "));
    for key in bank_accounts.keys():
        if bank_accounts[key]["id_number"] == str(id_num):
            print(bank_accounts[key]);
    return;

def find_by_name() -> None:
    name: str = input("first name: ");
    for key in bank_accounts.keys():
        if name.lower() in bank_accounts[key]["first_name"].lower():
            print(bank_accounts[key]);
    return;

def acc_by_bal() -> None:
    acc_list: list = list(bank_accounts.keys());
    acc_list.sort();
    for acc_n in acc_list:
        print(bank_accounts[acc_n]);
    return;

def neg_bal() -> None:
    for key in bank_accounts.keys():
        if bank_accounts[key]["balance"] < 0:
            print(bank_accounts[key]);
    return;

def acc_sum() -> None:
    a_sum: int = 0;
    for key in bank_accounts.keys():
        a_sum += bank_accounts[key]["balance"];
    print(f"sun of all accounts; {a_sum}");
    return;

def tr_today() -> None:
    tod_tr: list = [];
    today: str = datetime.today().strftime('%Y-%m-%d');
    for key in bank_accounts.keys():
        for transaction in bank_accounts[key]["transaction_history"]:
            tr_date: list[str] = str(transaction[0]).split(' ')[0];
            print(tr_date);
            if tr_date == today:
                tod_tr.append(transaction);
    print(f"today's transactions:\n{tod_tr}");
    return;
def open_acc()->None:
    acc_num: int = max(bank_accounts.keys()) + 1;
    fname: str = input("first name: ");
    lname: str = input("last name: ");
    id_num: str = input("id number: ");
    bal: int = int(input("starting balance: "));

    new_acc: dict = {
        "first_name": fname,
        "last_name": lname,
        "id_number": id_num,
        "balance": bal,
        "transactions_to_execute": [],
        "transaction_history": []
    }

    bank_accounts[acc_num] = new_acc;
    return;

def view_rep() -> None:
    print("===========Report Menu==============")
    print("0 - back to previous menu\n1 - print all\n2 - print account\n3 - find by id\n4 - find by name\n"
          "5 - print all accounts sorted by balance\n6 -  print all account with negative balance\n"
          "7 - print sum of all accounts\n8 - print transactions today");
    action: int = int(input("What is the purpose of your visit? "));
    while True:
        match action:
            case 0:
                return;
            case 1:
                print(bank_accounts);
                return;
            case 2:
                acc: int = int(input("account number: "));
                if acc in bank_accounts.keys():
                    print(bank_accounts[acc]);
                else:
                    print(f"account- {acc} - could not be found");
                return;
            case 3:
                find_by_id();
                return;
            case 4:
                find_by_name();
                return;
            case 5:
                acc_by_bal();
                return;
            case 6:
                neg_bal();
                return;
            case 7:
                acc_sum();
                return;
            case 8:
                tr_today();
                return;
            case _:
                print("invalid input");
                continue;


def main_menu() -> None:
    # action: int = None;
    while True:
        print("===========Main Menu==============")
        print("0 - open new account\n1 - new transaction\n2 - commit all transactions\n3 - reports menu\n999 - exit");
        action: int = int(input("What is the purpose of your visit? "));
        match action:
            case 0:
                open_acc();
            case 1:
                new_tra();
            case 2:
                com_tra();
            case 3:
                view_rep();
            case 999:
                print("leaving the system, have a nice day!")
                break;
            case _:
                print("invalid input");
                continue;

        print()
    return;

main_menu();