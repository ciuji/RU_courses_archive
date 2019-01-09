#include "Tetrahedron.h"
#include<iostream>
#include<math.h>
using namespace std;


Tetrahedron::Tetrahedron(double x,double y,double z,double edge):ThreeDimensionalShape(x,y,z)
{
	setEdge(edge);
}

void Tetrahedron::setEdge(double edgeVal) {
	this->edge = edgeVal;
}

double Tetrahedron::getArea() const{
	return edge * edge*sqrt(3);
}

double Tetrahedron::getVolumn()const {
	return 1.0 / 12.0*sqrt(2)*edge*edge*edge;
}

void Tetrahedron::print()const {
	cout << "The regular tetrahedron with edge length " << this->edge << " at location (" << this->x << "," << this->y << "," << this->z << ") has:" << endl;
	cout << "Surface area of " << getArea() << endl;
	cout << "Volume of " << getVolumn() << endl;
}
Tetrahedron::~Tetrahedron()
{
}
