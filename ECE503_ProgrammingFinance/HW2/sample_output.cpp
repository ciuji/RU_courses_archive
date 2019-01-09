#include <iostream>
#include <fstream>
using namespace std;

// function main begins program execution
int main(){
	ofstream file;
	//opens the file myfile.txt
	file.open("myfile.txt");
	//for loop to write the values to the file
	for(int i = 0;i<100;i++){
		file<<i<<","<<i+5<<"\n";
	}
	cout<<"Printed numbers to file myfile.txt\n";
}
