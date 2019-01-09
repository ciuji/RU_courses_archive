#include "BaseAccount.h"

//init baseAccount. get balance
BaseAccount::BaseAccount()
{
	if (checkIsHistory("balance_record.txt")) {
		ifstream ifile;
		ifile.open("balance_record.txt");
		string record;
		if (getline(ifile, record)) {
			istringstream iss(record);
			iss >> balance;
		}
	}
	else {
		balance = 10000;
		renewBalanceFile();
	}
}



void BaseAccount::renewBalanceFile()
{
	stringstream ss;
	ss << balance;
	string newBalance = ss.str();
	if (checkIsHistory("balance_record.txt")) {
		ofstream ofile;
		ofile.open("balance_record.txt");
		ofile << newBalance;
		ofile.close();
		return;
	}
	else {
		createNewHistory("balance_record.txt");
		ofstream ofile;
		ofile.open("balance_record.txt");
		ofile << newBalance;
		ofile.close();
		return;
	}
}



//set balance
void BaseAccount::setBalance(double balance)
{
	this->balance = balance;
}

//get balance
double BaseAccount::getBalance() const
{
	return this->balance;
}

/*
Design Pattern: template pattern.
method in abstract class.
would be fullfilled in derived class;
*/
void BaseAccount::initTransHistroy(const string accountType)
{
	this->templateMethod();
}

bool BaseAccount::checkIsHistory(const char* fileName) const
{
	/*if (accountType == "Stock") {
		ifstream ifile("record/StockTransactionHistory.txt");
		if (!ifile)
		{
			ifile.close();
			return false;
		}
		return true;
	}
	else if (accountType == "Bank") {
		ifstream ifile("record/BankTransactionHistory.txt");
		if (!ifile) {
			ifile.close();
			return false;
		}
		return true;
	}*/
	ifstream ifile(fileName);
	if (!ifile)
	{
		ifile.close();
		return false;
	}
	else
		return true;
	return false;
}

//create new history file.
void BaseAccount::createNewHistory(const char* fileName)
{
	//const char*fileName = file.c_str();
	FILE * fp = NULL;
	errno_t err = 0;
	err = fopen_s(&fp, fileName, "w+");
	if (!err) {
		fclose(fp);
	}
}
void BaseAccount::addLineHistory(char * fileName, string record)
{
	ofstream ofile;
	ofile.open(fileName, ios::app);//mode of open
	if (ofile.fail()) {
		cout << "Fail when open " << fileName << endl;
		return;
	}
	else {
		ofile << record;
		ofile.close();
		return;
	}
}
BaseAccount::~BaseAccount()
{
}

void BaseAccount::printLines(const char * fileName ) const
{
	ifstream ifile;
	ifile.open(fileName);
	string line;
	while (getline(ifile, line)) {
		cout << line << endl;
	}
	ifile.close();
}
