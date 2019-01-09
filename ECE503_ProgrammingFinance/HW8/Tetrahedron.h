#pragma once
#include "ThreeDimensionalShape.h"
class Tetrahedron :
	public ThreeDimensionalShape
{
public:
	Tetrahedron(double x,double y,double z,double edge);
	void setEdge(double);
	double getArea() const;//polymorphism
	double getVolumn() const;//polymorphism
	void print() const;//polymorphism
	~Tetrahedron();
private:
	double edge;
};

