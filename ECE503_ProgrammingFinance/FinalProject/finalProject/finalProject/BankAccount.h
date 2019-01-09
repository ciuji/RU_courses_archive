#pragma once
#ifndef BANKACCOUNT_H
#define BANKACCOUNT_H

#include "BaseAccount.h"
#include <iostream>
#include <fstream>
#include "DoubleLinkedList.h"
#include <time.h>
#include <sstream>

#define BANK_FILE "bank_transaction_history.txt"
using namespace std;

class BankAccount :
	public BaseAccount
{
public:
	/*
	design pattern: singleton pattern
	ensure there would only be one bank account at anytime.
	*/
	static BankAccount * GetInstance() {
		if (m_pInstance==NULL)
			m_pInstance = new BankAccount();
		return m_pInstance;
	}
	void doDeposit(double moneyVal);//do deposit
	void doWithdraw(double moneyVal);//do withdraw
	bool addHistory(double moneyVal, int mode) const;//add transaction history
	void printHistory() const;//print transaction history

	//design pattern: template pattern
	void templateMethod();
	~BankAccount();
	//BankAccount();

private:
	/*
	design pattern: singleton pattern
	*/
	BankAccount();
	static BankAccount* m_pInstance ;
	static int a;
};



#endif // !BANKACCOUNT_H
