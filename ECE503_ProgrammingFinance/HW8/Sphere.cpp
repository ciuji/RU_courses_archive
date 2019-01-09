#include "Sphere.h"
#include<iostream>
#include<math.h>
using namespace std;


Sphere::Sphere(double x,double y,double z,double radius):ThreeDimensionalShape(x,y,z)
{
	setRadius(radius);
}

void Sphere::setRadius(double radiusVal) {
	this->radius = radiusVal;
}

double Sphere::getArea()const {
	return 4 * 3.14*radius;
}

double Sphere::getVolumn()const {
	return 4 * 3.14*radius*radius*radius / 3.0;

}

void Sphere::print()const {
	cout << "The sphere with radius " <<radius << " that is located at (" << this->x << "," << this->y << "," << this->z << ") has:" << endl;
	cout << "Surface area of " << getArea() << endl;
	cout << "Volume of " << getVolumn() << endl;
}
Sphere::~Sphere()
{
}
