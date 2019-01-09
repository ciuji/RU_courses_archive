#ifndef THREEDIMENSIONALPOINT_H
#define THREEDIMENSIONALPOINT_H

#include "point.h"

class ThreeDimensionalPoint:public Point{
private:
	int z;
public:
	ThreeDimensionalPoint();
	ThreeDimensionalPoint(int, int, int);
	int getz();
	void setz(int);
	void addPoints(ThreeDimensionalPoint);
};

#endif 