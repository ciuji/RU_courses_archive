#pragma once
#include "Package.h"
#include <string>
class TwoDayPackage :
	public Package
{
public:

	virtual string getType();
	TwoDayPackage(string s_name, string s_address, string s_city, string s_state, string s_zip, string r_name, string r_address, string r_city, string r_state, string r_zip, double weightVal, double cost, double flatFeeVal);
	virtual double calculateCost();
	~TwoDayPackage();
private:
	double flatFee;
};

