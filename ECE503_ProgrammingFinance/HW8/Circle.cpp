#include "Circle.h"
#include<iostream>
using namespace std;

Circle::Circle(double x,double y,double radius):TwoDimensionalShape(x,y)
{
	setRadius(radius);
}

void Circle::setRadius(double radiusVal) {
	this->radius = radiusVal;
}

//polymorphism
double Circle::getArea()const {
	return 3.14*radius*radius;
}
//polymorphism
void Circle::print()const {
	cout << "The circle with radius " << this->radius << " that is located at (" << this->x<< "," << this->y << ") has:" << endl;
	cout << "An area of " << getArea() << endl;
}
Circle::~Circle()
{
}
