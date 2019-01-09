#pragma once
#ifndef POLYNOMIAL_H
#define POLYNOMIAL_H
#include <iostream>
#define MAX_NUM 10
class Polynomial
{
public:
	Polynomial();
	void setArr();
	//propotypes of all the overload functions.
	const Polynomial &operator=(const Polynomial&);
	const Polynomial &operator+=(const Polynomial&);
	const Polynomial &operator-=(const Polynomial&);
	const Polynomial &operator*=(const Polynomial&);
	friend Polynomial operator +(const Polynomial&,const Polynomial&);
	friend Polynomial operator -(const Polynomial&,const Polynomial&);
	friend Polynomial operator *(const Polynomial&,const Polynomial&);
	friend std::ostream& operator<<(std::ostream &output, const Polynomial &);


	~Polynomial();
private:
	//create an array to store coefiicients and exponents;
	int polArr[2*MAX_NUM+1];
};

#endif
