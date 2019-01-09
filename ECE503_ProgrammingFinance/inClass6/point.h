#ifndef POINT_H
#define POINT_H

class Point{
private:
	int x,y;
public:
	Point();
	Point(int, int);
	int getx();
	int gety();
	void setx(int);
	void sety(int);
};

#endif