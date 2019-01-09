#include "Package.h"
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;


Package::Package(string s_name, string s_address, string s_city, string s_state, string s_zip, string r_name, string r_address, string r_city, string r_state,string r_zip,double weightVal,double cost)
	:send_name(s_name), send_address(s_address), send_city(s_city), send_state(s_state), send_zip(s_zip), reci_name(r_name), reci_address(r_address), reci_city(r_city), reci_state(r_state), reci_zip(r_zip)
 {
	setWeight(weightVal);
	setCost(cost);
}
//set cost
void Package::setCost(double costVal) {
	if(costVal>0)
		this->costPerOunce = costVal;
	else {
		cout << "Sorry! The cost of per ounce must be positive!" << endl;
	}
}
//set weight
void Package::setWeight(double weightVal) {
	if(weightVal>0)
		this->weight = weightVal;
	else {
		cout << "Sorry! The weight of the package must be positive!" << endl;
	}
}

//get type
string Package::getType() {
	return this->typeName;
}

//get cost
double Package::calculateCost() {
	return this->weight*this->costPerOunce;
}

//package print function
void Package::print() {
	cout << "Sender:" << endl;
	cout << this->send_name << endl << this->send_address << endl;
	cout << this->send_city << ", " << send_state << " " << send_zip << endl;
	cout << endl << "Receipent:" << endl;
	cout << this->reci_name << endl << this->reci_address << endl;
	cout << this->reci_city << ", " << reci_state << " " << reci_zip << endl;
	cout << endl << "Weight of package: " << fixed << setprecision(2)<<this->weight << " ounces" << endl;
	cout << "Type of delivery: " << this->typeName << endl;
	cout << "Cost of Package: $"<<fixed << setprecision(2) << calculateCost() << endl << endl;
}

Package::~Package()
{
}
