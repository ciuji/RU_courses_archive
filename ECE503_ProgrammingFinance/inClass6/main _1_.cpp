#include <iostream>

#include "point.h"
#include "threedimensionalpoint.h"

using namespace std;

int main(){
	ThreeDimensionalPoint point1(1,2,3);
	ThreeDimensionalPoint point2(4,5,6);
	point1.addPoints(point2);
	cout<<"\nThe value of the x value is: "<< point1.getx();
	cout<<"\nThe value of the y value is: "<< point1.gety();
	cout<<"\nThe value of the z value is: "<< point1.getz();
	cout<<"\n";
}