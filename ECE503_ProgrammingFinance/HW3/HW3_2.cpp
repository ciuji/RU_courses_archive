/*
Title: Homework 3: matrix (Vector version)

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time:

Course:332:503 Programming Finance
**/
//#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

//declare the functions' prototype
void menu(void);
int func_add(void);
int func_sub(void);
int func_mult(void);
void func_tran(void);
int func_deter(void);
int func_inver(void);

int main()
{
    //use choice to store users input
	int choice = 0;
	//write a loop to ensure user can call different function again and again.
	for (;;) {
        //a print function to show what user can do
		menu();
        //get user's input
		cin >> choice;
		//decide which function to work depend on the user's input.
		switch (choice) {
        //call different functions.
		case 1: func_add(); break;
		case 2: func_sub(); break;
		case 3: func_mult(); break;
		case 4: func_tran(); break;
		case 5: func_deter(); break;
		case 6: func_inver(); break;
		case 7: //system("pause");
			return 0;
		default: break;
		}
	}
	//system("pause");
	return 0;
}


void menu(void)
{
	cout << "Menu";
	cout << "\n Choice 1: Addition";
	cout << "\n Choice 2: Subtraction";
	cout << "\n Choice 3: Multiplication";
	cout << "\n Choice 4: Transpose";
	cout << "\n Choice 5: Determinant";
	cout << "\n Choice 6: Inverse";
	cout << "\n Choice 7: Quit";
	cout << "\n ";
}
 //a function to fulfill the vector by user's input
void input_matrix (vector<vector<int>>&matrix, int row, int col) {
    //resize the vector to achieve space allocate
    matrix.resize(row);
    for (int i = 0; i < matrix.size(); i++)
		matrix[i].resize(col);
    cout << "Please enter the values of elements:";
    //get user's input and set them in the matrix.
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			cin >> matrix[i][j];
		}
	}

}

//a function to show the matrix
void display_matrix(vector<vector<int>>&matr, int row, int col) {
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			cout << setw(6) << matr[i][j];
		}
		cout << endl;
	}
}

//a function to achieve add of two matrix.
int func_add(void) {
	int row = 0, col = 0, row2 = 0, col2 = 0;
	cout << "Please enter the number of row:";
	cin >> row;
	cout << "Please enter the number of column:";
	cin >> col;
	//initial the matrix
	vector<vector<int>> mart1(1);

	//call the input function to fulfill the matrix.
    input_matrix(mart1,row,col);

	cout << "Your input is:" << endl;
	display_matrix(mart1, row, col);

	cout << "Please enter the number of row:";
	cin >> row2;
	cout << "Please enter the number of column:";
	cin >> col2;

	//judge whether the two matrix have the same row and column.
	if (row != row2&&col != col2) {
		cout << "The operation is not supported" << endl;
		return 0;
	}

	//initial and call the input function to fulfill the matrix.
	vector<vector<int>> mart2(1);
	input_matrix(mart2,row,col);
	cout << "Your input is:" << endl;
	display_matrix(mart2, row, col);

	//add matrix2 to matrix1.
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			mart1[i][j] += mart2[i][j];
		}
	}

	//display the result.
	cout<<"The result is:"<<endl;
	display_matrix(mart1, row, col);

}

//a function to achieve subtraction of two matrix.
int func_sub(void){
	int row = 0, col = 0, row2 = 0, col2 = 0;
	cout << "Please enter the number of row:";
	cin >> row;
	cout << "Please enter the number of column:";
	cin >> col;
	//initial the matrix
	vector<vector<int>> mart1(1);
 	//call the input function to fulfill the matrix.
   input_matrix(mart1,row,col);

	cout << "Your input is:" << endl;
	display_matrix(mart1, row, col);

	cout << "Please enter the number of row:";
	cin >> row2;
	cout << "Please enter the number of column:";
	cin >> col2;
	//judge whether the two matrix have the same row and column.
	if (row != row2&&col != col2) {
		cout << "The operation is not supported" << endl;
		return 0;
	}
	//initial and call the input function to fulfill the matrix.
	vector<vector<int>> mart2(1);
	input_matrix(mart2,row,col);
	//display the result.
	cout << "Your input is:" << endl;
	display_matrix(mart2, row, col);
    //do the subtraction
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			mart1[i][j] -= mart2[i][j];
		}
	}
	cout<<"The result is:"<<endl;
	display_matrix(mart1, row, col);
}
//a function to multiply two matrix
int func_mult(void) {
    int row = 0, col = 0, row2 = 0, col2 = 0;
	cout << "Please enter the number of row:";
	cin >> row;
	cout << "Please enter the number of column:";
	cin >> col;
    //initial the matrix of vector
	vector<vector<int>> mart1(1);
 	//call the input function to fulfill the matrix.
    input_matrix(mart1,row,col);

	cout << "Your input is:" << endl;
	display_matrix(mart1, row, col);

	cout << "Please enter the number of row:";
	cin >> row2;
	cout << "Please enter the number of column:";
	cin >> col2;
	//judge whether the two matrix have the same row and column.
	if (row != row2&&col != col2) {
		cout << "The operation is not supported" << endl;
		return 0;
	}
	//initial and call the input function to fulfill the matrix.
	vector<vector<int>> mart2(1);
	input_matrix(mart2,row,col);
	cout << "Your input is:" << endl;
	display_matrix(mart2, row, col);
    //do the multiplication
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			mart1[i][j] *= mart2[i][j];
		}
	}
    //show the result
	cout<<"The result is:"<<endl;
	display_matrix(mart1, row, col);

}
//a function to do the transfer of the matrix
void func_tran(void) {
    int row = 0, col = 0;
	cout << "Please enter the number of row:";
	cin >> row;
	cout << "Please enter the number of column:";
	cin >> col;
    //initial the matrix of vector
	vector<vector<int>> mart1(1);
 	//call the input function to fulfill the matrix.
    input_matrix(mart1,row,col);

    //call the display function to show the input
	cout << "Your input is:" << endl;
	display_matrix(mart1, row, col);
	cout << "The result is:" << endl;
	//show the transfer matrix
	for (int i = 0; i < col; i++) {
		for (int j = 0; j < row; j++) {
			cout << setw(6) << mart1[j][i];
		}
		cout << endl;
	}

}
//a function to calculate the determinant of the matrix.
int func_deter(void) {
    int row = 0, col = 0;
	cout << "Please enter the number of row:";
	cin >> row;
	cout << "Please enter the number of column:";
	cin >> col;
    //ensure user would input a 3X3 matrix.
	if (col != 3 && row != 3) {
		cout << "Please enter a 3X3 matrix!" << endl;
		return 0;
	}
	//initial and call the input function to fulfill the matrix.
	vector<vector<int>> mart1(1);
    input_matrix(mart1,row,col);

    //print the matrix user input
    cout<<"Your input is:"<<endl;
    display_matrix(mart1, row,col);
    //show the result
	cout << "The result is:" << endl;
	int res = 0;
	//calculate the determinant
	res = mart1[0][0] * (mart1[1][1] * mart1[2][2] - mart1[1][2] * mart1[2][1]) - mart1[0][1] * (mart1[1][0] * mart1[2][2] - mart1[1][2] * mart1[2][0]) + mart1[0][2] * (mart1[1][0] * mart1[2][1] - mart1[1][1] * mart1[2][0]);
	cout << res << endl;

	return 0;
}

//a function to do the inverse of a 3X3 matrix
int func_inver(void) {
	int row = 0, col = 0;
	cout << "Please enter the number of row:";
	cin >> row;
	cout << "Please enter the number of column:";
	cin >> col;
	//ensure user would input a 3X3 matrix.
	if (col != 3 && row != 3) {
		cout << "Please enter a 3X3 matrix!" << endl;
		return 0;
	}

	//initial and call the input function to fulfill the matrix.
	vector<vector<int>> mart1(1);
    input_matrix(mart1,row,col);

    //show user's input
	cout << "Your input is:" << endl;
	display_matrix(mart1, row, col);

	//show the result.
	cout << "The result is:" << endl;
	int res = 0;
	//do the inverse.
	for (int i = 2; i >= 0; i--) {
		for (int j = 2; j >= 0; j--) {
			cout << setw(6) << mart1[i][j];
		}
		cout << endl;
	}

	return 0;
}

