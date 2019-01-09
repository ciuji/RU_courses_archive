/*
Title: InClass 6
Author: Chaoji Zuo
Email: chaoji.zuo@rutgers.edu
Time: Nov-3-2018
Course:332:503 Programming Finance
**/
#include "threedimensionalpoint.h"

ThreeDimensionalPoint::ThreeDimensionalPoint(){
	setx(0);
	sety(0);
	setz(0);
}

ThreeDimensionalPoint::ThreeDimensionalPoint(int xin, int yin, int zin){
	//use setfunction to set values.
	setx(xin);
	sety(yin);
	setz(zin);
}
int ThreeDimensionalPoint::getz(){
	//please implement this function to get the z value
	return this->z;
}
void ThreeDimensionalPoint::setz(int zin){
	//please implement this function to set z value
	this->z=zin;
}

void ThreeDimensionalPoint::addPoints(ThreeDimensionalPoint pointin){
	//please implement this function to add the x,y and z values of point1 to values of the calling instance of the object
	setx(getx() + pointin.getx());
	sety(gety() + pointin.gety());
	setz(getz() + pointin.getz());
}