#include "Polynomial_ChaojiZuo.h"
#include <iostream>
Polynomial::Polynomial()
{
	//initial the array of coefficients and exponents;
	for (int i = 0; i <= 2*MAX_NUM; i++) {
		this->polArr[i] = 0;
	}
}


void Polynomial::setArr() {
	//ask user to input the data of polynomial;
	std::cout << "Enter the number of polynomial terms: ";
	int num = 0;
	std::cin >> num;
	for (int i = 0; i < num; i++) {
		std::cout << "Enter coefficient and exponent:";
		int coe = 0, exp = 0;
		std::cin >> coe >> exp;

		//judge wheather the user enter the right exponent of polynomial;
		if (exp < MAX_NUM&&exp>=0) {
			this->polArr[exp] = coe;
		}
		else if (exp < 0) {
			std::cout << "Sorry, the exponent can not smaller than 0" << std::endl;
			i--;
		}
		else {
			std::cout << "Sorry, the exponent can not larger than "<<MAX_NUM<<std::endl;
			i--;
		}
	}

}
//overload function of operator<<
std::ostream& operator<<(std::ostream &output, const Polynomial &poly) {
	int isFirst = 1;
	for (int i = 0; i < 2*MAX_NUM; i++) {
		if (poly.polArr[i] != 0) {
			//ensure the first element of polynomial would not have a + behand of it
			if (!isFirst) {
				output << " + ";
			}

			//when conponent is 1 or 0, use different output;
			if (i == 0) {
				output << poly.polArr[i];
			}
			else if (i == 1) {
				output << poly.polArr[i] << "x";
			}
			else {
				output << poly.polArr[i] << "x^" << i;
			}
			isFirst = 0;
		}
	}
	output << std::endl;
	return output;
}

//overload function of operator =
const Polynomial &Polynomial::operator=(const Polynomial &right) {
	for (int i = 0; i < MAX_NUM; i++) {
		this->polArr[i] = right.polArr[i];
	}
	return *this;
}
//overload function of operator +=
const Polynomial &Polynomial::operator+=(const Polynomial &right) {
	for (int i = 0; i < MAX_NUM; i++) {
		this->polArr[i] += right.polArr[i];
	}
	return *this;
}


//overload function of operator -=
const Polynomial &Polynomial::operator-=(const Polynomial &right) {
	for (int i = 0; i < MAX_NUM; i++) {
		this->polArr[i] -= right.polArr[i];
	}
	return *this;
}

//overload function of operator *=
const Polynomial &Polynomial::operator*=(const Polynomial &right) {

	Polynomial temp;
	for (int i = 0; i < MAX_NUM; i++) {
		for (int j = 0; j < MAX_NUM; j++) {
				temp.polArr[i + j] += this->polArr[i] * right.polArr[j];
		}
	}
	for(int i=0;i<2*MAX_NUM;i++)
		this->polArr[i] = temp.polArr[i];
	return *this;
}

//overload function of operator +
Polynomial operator+(const Polynomial& left,const Polynomial &right) {
	Polynomial newPoly;
	for (int i = 0; i < MAX_NUM; i++) {
		newPoly.polArr[i] = left.polArr[i] + right.polArr[i];
	}
	return newPoly;
}
//overload function of operator -
Polynomial operator-(const Polynomial& left,const Polynomial &right) {
	Polynomial newPoly;
	for (int i = 0; i < MAX_NUM; i++) {
		newPoly.polArr[i] = left.polArr[i] - right.polArr[i];
	}
	return newPoly;
}

//overload function of operator *
Polynomial operator*(const Polynomial&left,const Polynomial &right) {
	Polynomial newPoly;
	for (int i = 0; i < MAX_NUM; i++) {
		for (int j = 0; j< MAX_NUM; j++) {
				newPoly.polArr[i + j] += left.polArr[i] * right.polArr[j];
		}
	}
	return newPoly;
}


Polynomial::~Polynomial()
{
}
