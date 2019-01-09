#include "BankAccount.h"


BankAccount::BankAccount()
{
	accountType = "BANKACCOUNT";
	initTransHistroy(accountType);

}

//design pattern: singleton pattern
//initialize the static pointer
BankAccount* BankAccount::m_pInstance = NULL;

void BankAccount::doDeposit(double moneyVal)
{
	balance += moneyVal;
	renewBalanceFile();
	addHistory(moneyVal, 1);
}

void BankAccount::doWithdraw(double moneyVal)
{
	if (balance < moneyVal) {
		cout << endl << "Error: money in your account less than " <<fixed<< moneyVal << " !" << endl;
	}
	else {
		balance -= moneyVal;
		renewBalanceFile();
		addHistory(moneyVal, 2);
	}
}

//add new record to the history file.
bool BankAccount::addHistory(double moneyVal, int mode) const
{
	string process = "";
	switch (mode) {
	case 1:
		process = "Deposit";
		break;
	case 2:
		process = "Withdraw";
		break;
	default:
		return false;
		break;
	}
	struct tm t;
	time_t nowTime;
	time(&nowTime);
	localtime_s(&t, &nowTime);


	stringstream ss1,ss2;
	ss1 << fixed << (setprecision(2)) << moneyVal;
	ss2 << fixed << (setprecision(2)) << balance;

	
	string timeStr = to_string(t.tm_year + 1900) + "/" + to_string(t.tm_mon) + "/" + to_string(t.tm_mday);
	string moneyStr = "$" + ss1.str();
	string balanceStr = "$" +ss2.str();
	ofstream ofile(BANK_FILE, ios::app);
	ofile <<left<< setw(16) << process  <<setw(16)<< moneyStr<<setw(16)  <<timeStr <<setw(16) <<balanceStr << endl;
	ofile.close();
	return true;
}

void BankAccount::printHistory() const
{
	cout <<left<< setw(16) << "Event" << setw(16) << "Amount" << setw(16) << "Date" << setw(16) << "Balance" << endl;
	printLines(BANK_FILE);
}

//design pattern: template pattern.
void BankAccount::templateMethod()
{
	if (!checkIsHistory(BANK_FILE)) {
		createNewHistory(BANK_FILE);
	}
}

BankAccount::~BankAccount()
{
	m_pInstance = NULL;
}
