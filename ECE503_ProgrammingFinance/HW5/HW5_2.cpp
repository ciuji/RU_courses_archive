//author: chaoji zuo
//RUID: 190003416
//title: Homework 5, quesition 2
//time: 12-Oct-18
//course: ECE503-ProgrammingFinance

#include <iostream>
#include <vector>
using namespace std;

bool recursion(vector<int> ,int );
int main(){
	//using a vector to store the array.
	vector <int> arr;
	cout<<"Please enter a row of positive integers, and the end of the row must be 0:"<<endl;
	int item=0;
	cin>>item;
	while(item!=0){
		//get user's input.
		arr.push_back(item);
		cin>>item;
	}
	//add the 0 to the end of the row
	arr.push_back(0);
	bool result=false;
	//call recursion function
	if(arr[0]<arr.size())
		result =recursion(arr,arr[0]);
	//show the result.
	if(result)
		cout<<"Right array";
	else 
		cout<<"Wrong array. Cannot move to the rightmost one";
	system("pause");
	return 0;
}

bool recursion(vector<int> arr,int index){
	//use temp to store the index.
	int temp = arr[index];
	//Judge the arr[index].If get 0, return true.
	if(arr[index]==0)
		return true;
	//if the position has visited, return false.
	if(arr[index]==-1)
		return false;
	else 
		//set the position visited to -1.
		arr[index]=-1;

	//If it can move to the right direction, move to right side.
	if(index+temp<arr.size()){
		//if right side is the right choice, then return true. if not, then go to the left side.
		if(recursion(arr,index+temp))
			return true;
	}
	//if it can move to the left side, move to left side.
	if(index-temp>=0)
	{
		//if left side is the right choice, then return true.
		if(recursion(arr,index-temp))
			return true;
	}
	//if no way to go or both the right side and left side cannot move to the mostright number, return false.
	return false;
}
