/*
Title: Homework 9 Package Inheritance Hierarchy

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time: Nov-9-2018

Course:332:503 Programming Finance
**/
#include <iostream>
#include "TwoDayPackage.h"
#include "OvernightPackage.h"
#include "Package.h"
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;
double calculateTotal(vector<Package *>p);//prototype of function

int main()
{
	//initial the price of different type of package
	double regular = 0.5;
	double cost_twoDay = 2.0;
	double cost_overNight = 5.0;
	cout << "Package delivery services program" << endl;

	cout<<endl << "Cost per ounce for a package : $" << fixed << setprecision(2) << regular << "/ounce" << endl;
	cout << "Additional cost for two day delivery : $" << fixed << setprecision(2) << cost_twoDay << "/ounce" << endl;
	cout << "Additional cost for overnight delivery : $" << fixed << setprecision(2) << cost_overNight << "/ounce" << endl;
	//declare packages.
	Package *package1=new Package("John Smith", "1 Davidson Road", "Piscataway", "NJ", "08854", "Tom Smith", "2 Davidson Road", "Piscataway", "NJ", "08854", 10.0, regular);
	TwoDayPackage *package2=new TwoDayPackage("Mary Smith", "3 Davidson Road", "Piscataway", "NJ", "08854", "Jennifer Smith", "4 Davidson Road", "Piscataway", "NJ", "08854", 5.0, regular, cost_twoDay);
	OvernightPackage *package3=new OvernightPackage("John Smith", "1 Davidson Road", "Piscataway", "NJ", "08854", "Mary Smith", "3 Davidson Road", "Piscataway", "NJ", "08854", 2.0, regular, cost_overNight);

	//use vector to store these packages.
	vector<Package *> packages;
	packages.push_back(package1);
	packages.push_back(package2);
	packages.push_back(package3);

	//call the print function.
	cout << endl << "Package 1:" << endl << endl;
	package1->print();
	cout << endl << "Package 2:" << endl << endl;
	package2->print();
	cout << endl << "Package 3:" << endl << endl;
	package3->print();

	//call calculateTotal function to calculate the amount of cost.
	cout << "Total cost of all the package:" <<calculateTotal(packages)<< endl;
	//free the space.
	delete package1;
	delete package2;
	delete package3;

	system("pause");
	return 0;
}

double calculateTotal(vector<Package *>p) {
	double res = 0;
	//get every package's cost.
	for (int i = 0; i < p.size(); i++) {
		if (p[i]->calculateCost())
			res += p[i]->calculateCost();
	}
	return res;
}
