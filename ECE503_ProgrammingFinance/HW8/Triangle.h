#pragma once
#include "TwoDimensionalShape.h"
class Triangle :
	public TwoDimensionalShape
{
public:
	Triangle(double = 0, double = 0, double = 0);
	void setEdge(double);
	double getArea() const;//polymorphism
	void print() const;//polymorphism
	~Triangle();
private:
	double edge;
};

