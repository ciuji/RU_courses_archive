#pragma once
#include "Shape.h"
class ThreeDimensionalShape :
	public Shape
{
public:
	ThreeDimensionalShape(double =0, double =0, double=0);
	virtual double getVolumn() const = 0;//polymorphism
	~ThreeDimensionalShape();
protected:
	double area;
	double volumn;
};

