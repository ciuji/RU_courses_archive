#pragma once
#include "ThreeDimensionalShape.h"
class Sphere :
	public ThreeDimensionalShape
{
public:
	Sphere(double = 0,double=0,double=0,double=0);
	void setRadius(double);
	double getArea() const;//polymorphism
	double getVolumn()const;//polymorphism
	void print()const;//polymorphism
	~Sphere();
private:
	double radius;
};

