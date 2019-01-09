#include "Triangle.h"
#include <iostream>
#include <math.h>

Triangle::Triangle(double x,double y,double edge):TwoDimensionalShape(x,y)
{
	setEdge(edge);
}

void Triangle::setEdge(double edge) {
	this->edge = edge;
}
double Triangle::getArea() const {
	return edge * edge*sqrt(3) / 4.0;
}
void Triangle::print() const {
	std::cout << "The triangle with edge length " << this->edge << " that is located at (" << this->x << "," << this->y<< ") has:" << std::endl;
	std::cout << "An area of " << getArea() << std::endl;
}

Triangle::~Triangle()
{
}
