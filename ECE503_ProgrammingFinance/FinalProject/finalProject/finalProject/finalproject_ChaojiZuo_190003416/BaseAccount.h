#ifndef BASEACCOUNT_H
#define BASEACCOUNT_H
#include <string>
#include <fstream>
#include <iomanip>
#include <time.h>
#include <iostream>
#include <sstream>
#pragma once
using namespace std;
//Abstract base class

class BaseAccount
{
public:
	void setBalance(double balance);//set balance
	double getBalance() const;//get balance
	
	void printLines(const char * fileName) const;//print lines.
	virtual void printHistory() const =0;//print history
	virtual bool addHistory(double moneyVal, int mode) const =0;//add transaction history
	bool checkIsHistory(const char* fileName) const;//check wheather a historyfile exist.
	void createNewHistory(const char* fileName);//create new history txt.
	void addLineHistory(char *fileName, string reocrd);//add new line at the end of the file.

	//design pattern: template method
	void initTransHistroy(const string accountType);//initialize transaction history file

	void renewBalanceFile();//renew the balancefile
	BaseAccount();
	~BaseAccount();

protected:
	double balance;
	string accountType;
	virtual void templateMethod() = 0;


};

#endif BASEACCOUNT_H