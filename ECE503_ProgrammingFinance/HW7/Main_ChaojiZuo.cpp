// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include "Polynomial_ChaojiZuo.h"
using std::cout;
using std::cin;
using std::endl;

int main()
{
	//declare the variables;
	Polynomial poly1;
	Polynomial poly2;
	//use tempPoly to record the initial poly1, use resultPoly to record the result;
	Polynomial tempPoly, resultPoly;

	poly1.setArr();
	cout << endl;
	poly2.setArr();
	cout << endl;
	//call the overload opeartor "=";
	tempPoly = poly1;
	cout << "First Polynomial is:" << poly1;
	cout << "Second Polynomial is:" << poly2 << endl;
	//call the overload operator "+";
	resultPoly = poly1 + poly2;
	cout << "Adding polynomial yields:" << resultPoly;	
	//call the overload operator "+=";
	cout << "+= the polynomial yields:" << (poly1 += poly2) << endl;
	poly1 = tempPoly;
	//call the overload operator "-";
	resultPoly = poly1 - poly2;
	cout << "Subtracting the polynomial yield:" << resultPoly;
	//call the overload operator "-=";
	cout << "-= the polynomial yields:" << (poly1 -= poly2) << endl;
	poly1 = tempPoly;
	//call the overload operator "*";
	resultPoly = poly1 * poly2;
	cout << "Multiplying the polynomial yields:" << resultPoly;
	//call the overload operator "*=";
	cout << "*= the polynomial yields:" << (poly1 *= poly2) << endl;
	system("pause");
	return 0;
}

