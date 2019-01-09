// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <deque>
#include <algorithm>
#include <numeric>
#include <iterator>
using namespace std;
bool greaterSix(int i) { return i > 6 ? 1 : 0; }
int main()
{
	//declare the deque
	deque<int> myque;
	//1. insert the numbers
	myque.push_back(3);
	myque.push_back(4);
	myque.push_back(6);
	myque.push_back(2);
	myque.push_back(9);
	myque.push_back(1);
	myque.push_back(5);
	myque.push_back(0);
	myque.push_back(7);
	myque.push_back(9);

	//2. do the remove and erase
	myque.erase(remove(myque.begin(),myque.end(), 7), myque.end());

	//3. replace values greater than 6 in the quene with 10
	replace_if(myque.begin(), myque.end(), greaterSix, 10);
	
	//4. calculate the sum of the deque
	int total;
	total = accumulate(myque.begin(), myque.end(), 0);
	cout <<"The sum of the numbers 0 to 9 after removing 7 and replacing values greater than 6 with 10:"<< total<<endl;
	myque.push_front(total);


	//5. number of elements greater than 6
	int countGreaterSix = count_if(myque.begin(), myque.end(), greaterSix);
	cout << "Now the number of elements greater than 6 is:" << countGreaterSix << endl;

	//6. output half of every element
	cout << "The half of every element in the deque is:";
	for (deque<int>::iterator it = myque.begin(); it != myque.end(); it++) {
		cout << *it / 2 << " " ;
	}

	//7. sort the queue
	sort(myque.begin(), myque.end());

	//8. find the location of 6
	cout<<endl<<"After sorting, the location of 6 is at index:" << myque.at(6) << endl;

	//9. use ostream_iterator and copy to print

	ostream_iterator<int> os(cout, ", ");
	cout << "The items in the deque are:";
	copy(myque.begin(), myque.end(), os);
	cout << endl;
	system("pause");
	return 0;
}

