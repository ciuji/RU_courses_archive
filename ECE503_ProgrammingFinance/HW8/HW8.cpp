/*
Title: HW8 (inheritance)

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time: Nov-2

Course:332:503 Programming Finance
**/
#include <iostream>
#include "Circle.h"
#include "Sphere.h"
#include "Tetrahedron.h"
#include "Triangle.h"
using namespace std;
int main() {
	//store user's input
	int choice = 0;
	double x = 0, y = 0, z = 0;
	for (;;) {
		cout << "Please choose a shape or 0 to exit:" << endl;
		cout << "1. Circle" << endl << "2. Triangle" << endl << "3. Sphere" << endl << "4. Regular Tetrahedron" << endl;
		cout << "0. Exit" << endl;
		cin >> choice;
		if (!choice) {
			break;
		}
		cout << "Your choice:" << choice << endl;
		//call diffirent class
		switch (choice) {
		case 1: {
			double r = 0;
			cout << "Please enter the center of the triangle (x-coordinate and then y-coordinate):" << endl;
			cin >> x >> y;
			cout << "please enter the radius of the circle" << endl;
			cin>> r;
			Circle cir(x, y,r);
			cir.print();
			break;
		}
		case 2: {
			double edge = 0;
			cout << "Please enter the center of the triangle (x-coordinate and then y-coordinate): " << endl;
			cin >> x >> y;
			cout << "Please enter the edge length of the triangle: " << endl;
			cin>> edge;

			Triangle tri(x, y, edge);
			tri.print();

			break;
		}
		case 3: {
			double r = 0;
			cout << "Please enter the center of the sphere (x-coordinate, y-coordinate, then z-coordinate): " << endl;
			cin >> x >> y >> z;
			cout << "Please enter the radius of the sphere: " << endl;
			cin >> r;

			Sphere sph(x, y, z, r);
			sph.print();
			break;
		}
		case 4: {
			double edge = 0;
			cout << "Please enter the center of the tetrahedron (x-coordinate, y-coordinate, then z-coordinate): " << endl;
			cin >> x >> y >> z;
			cout << "Please enter the edge length of the tetrahedron: " << endl;
			cin >> edge;

			Tetrahedron tet(x, y, z, edge);
			tet.print();
			break;
		}
		default: {
			cout << "Sorry! Invalid choice!" << endl;
			break;
		}
		}

	}
	system("pause");
	return 0;

}