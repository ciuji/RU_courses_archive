#include "OvernightPackage.h"
#include <iostream>
#include <string>
using namespace std;



OvernightPackage::OvernightPackage(string s_name, string s_address, string s_city, string s_state, string s_zip, string r_name, string r_address, string r_city, string r_state, string r_zip,
	double weightVal, double cost, double flatFeeVal):Package(s_name, s_address,  s_city,  s_state,  s_zip,  r_name,  r_address,  r_city,  r_state,  r_zip,
		 weightVal,  cost)
{
	this->typeName = "Overnight Delivery";
	if(flatFeeVal>0)
		this->flatFee = flatFeeVal;
	else {
		cout << "Sorry! The flat fee must be positive!" << endl;
	}
}

double  OvernightPackage::calculateCost() {
	return (this->flatFee + this->costPerOunce)*this->weight;
}

string OvernightPackage::getType() {
	return this->typeName;
}

OvernightPackage::~OvernightPackage()
{
}
