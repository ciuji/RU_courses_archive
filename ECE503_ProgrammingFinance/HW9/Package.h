#pragma once
#ifndef PACKAGE_H
#define PACKAGE_H
#define MAX_NUM 30
#include <string>
using namespace std;
class Package
{
public:
	//consturctor of Package
	void setWeight(double);
	Package(string s_name, string s_address, string s_city, string s_state, string s_zip, string r_name, string r_address, string r_city, string r_state, string r_zip, double weightVal, double cost);
	void setCost(double);
	//virtual function, should be overrided by it's subclasses.
	virtual double calculateCost();
	virtual void print();
	virtual string getType() ;
	~Package();
protected:
	string send_name;
	string send_address;
	string send_city;
	string send_state;
	string send_zip;
	string reci_name;
	string reci_address;
	string reci_state;
	string reci_city;
	string reci_zip;
	double weight;
	double costPerOunce;
	string typeName= "Regular Delivery";
};

#endif // !
