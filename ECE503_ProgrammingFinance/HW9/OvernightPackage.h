#pragma once
#ifndef OVERNIGHTPACKAGE_H
#define OVERNIGHTPACKAGE_H
#include "Package.h"
#include <string>

class OvernightPackage :
	public Package
{
public:

	OvernightPackage(string s_name, string s_address, string s_city, string s_state, string s_zip, string r_name, string r_address, string r_city, string r_state, string r_zip, double weightVal, double cost, double flatFeeVal);
	virtual double calculateCost();
	virtual string getType();
	~OvernightPackage();
private:
	double flatFee;

};

#endif // !OVERNIGHTPACKAGE_H

