#include "point.h"

Point::Point(){
	setx(0);
	sety(0);
}

Point::Point(int xin, int yin){
	setx(xin);
	sety(yin);
}
int Point::getx(){
	return x;
};
int Point::gety(){
	return y;
};

void Point::setx(int xin){
	x = xin;
};
void Point::sety(int yin){
	y = yin;
}