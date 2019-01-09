#include "TwoDayPackage.h"
#include <iostream>
#include <string>
using namespace std;


TwoDayPackage::TwoDayPackage(string s_name, string s_address, string s_city, string s_state, string s_zip, string r_name, string r_address, string r_city, string r_state, string r_zip,
	double weightVal, double cost, double flatFeeVal) :Package(s_name, s_address, s_city, s_state, s_zip, r_name, r_address, r_city, r_state, r_zip,
		weightVal, cost)
{
	this->typeName = "Two Day Delivery";
	if (flatFeeVal > 0)
		this->flatFee = flatFeeVal;
	else {
		cout << "Sorry! The flat fee must be positive!" << endl;
	}
}


double TwoDayPackage::calculateCost() {
	return (this->flatFee + this->costPerOunce)*this->weight;
}

string TwoDayPackage::getType() {
	return this->typeName;
}


TwoDayPackage::~TwoDayPackage()
{
}
