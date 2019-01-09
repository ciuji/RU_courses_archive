#pragma once
#include "TwoDimensionalShape.h"
class Circle :
	public TwoDimensionalShape
{
public:
	Circle(double =0,double=0,double=0);
	void setRadius(double);
	double getArea() const;
	void print()const;
	~Circle();
private:
	double radius;
};

