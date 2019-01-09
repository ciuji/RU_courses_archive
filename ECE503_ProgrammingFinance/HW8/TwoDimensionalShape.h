#pragma once
#include "Shape.h"
class TwoDimensionalShape :
	public Shape
{
public:
	TwoDimensionalShape(double=0,double=0);
	~TwoDimensionalShape();
protected:
	double area;
};

