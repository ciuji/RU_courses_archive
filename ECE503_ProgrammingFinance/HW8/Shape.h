#pragma once
class Shape
{
public:
	Shape();
	void setx(double);
	void sety(double);
	void setz(double);

	virtual double getArea() const= 0;//virtual function
	virtual void print() const = 0;
	~Shape();
protected:
	double x;
	double y;
	double z;

};

