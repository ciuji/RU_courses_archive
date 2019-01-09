#pragma once
#ifndef STOCKACCOUNT_H
#define STOCKACCOUNT_H

#include "BaseAccount.h"
#include <iostream>
#include <fstream>
#include "DoubleLinkedList.h"
#include <time.h>

#define STOCK_HISTORY_FILE "stock_transaction_history.txt"
#define RESULT_FILE_1 ".\\stock\\Result_1.txt"
#define RESULT_FILE_2 ".\\stock\\Result_2.txt"
#define PORTFOLIO_FILE "portfolio_record.txt"
#define PORTFOLIO_VALUE_HISTORY "portfolio_value_history.txt"
#define BANK_FILE "bank_transaction_history.txt"

using namespace std;

/*
**BankTransactionHistory.txt would store the history of records.
**
*/
class StockAccount :
	public BaseAccount
{

 public:
	StockAccount();
	double getStockPriceFromFile(string stockName);
	void printStockPrice(string sName);
	void getPortfolio();
	void printPortfolio();
	void updateStockPrice();
	void sortPFList();
	void addPortfolioHistory();
	void renewPortfolioFilio();
	string splitLine(string line, int pos) const;

	//sell or buy stock
	bool doSellStock(string sName, int sNum, double sPrice);
	bool doBuyStock(string sName, int sNum, double sPrice);

	//get stocks's price by its name.
	void doDeposit(double moneyVal);//do deposit
	void doWithdraw(double moneyVal);
	bool addHistory(string sName, int sNum, double sPrice, int mode) const;
	//do withdraw
	virtual bool addHistory(double moneyVal,int mode) const;//add transaction history
	void printHistory() const;
	void templateMethod();
	//print transaction history
	void drawGraph();

	int countLines();

	~StockAccount();
private:
	double portfolioAmout;
	DoubleLinkedList PFList;
	//portfolio double linked list/
};

#endif // !STOCKACCOUNT_H
