// HW3.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <iomanip>
#include<vector>
using namespace std;

void menu(void);
int func_add(void);
int func_sub(void);
int func_mult(void);
void func_tran(void);
int func_deter(void);
int func_inver(void);

int main()
{
	int choice = 0;
	for (;;) {
		menu();
		cin >> choice;
		switch (choice) {
		case 1: func_add(); break;
		case 2: func_sub(); break;
		case 3: func_mult(); break;
		case 4: func_tran(); break;
		case 5: func_deter(); break;
		case 6: func_inver(); break;
		case 7:
			return 0;
		default: break;
		}
	}

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
vector<vector<int>>&input_matrix (int row, int col) {


	vector<vector<int>> matrix(row);
	for (int i = 0; i < matrix.size(); i++)
		matrix[i].resize(col);


    cout << "Please enter the values of elements:";
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			cin >> matrix[i][j];
		}
	}
	return matrix;
}
void display_matrix(vector<vector<int>>&matr, int row, int col) {
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			cout << setw(6) << matr[i][j];
		}
		cout << endl;
	}
}
int func_add(void) {
	int row = 0, col = 0, row2 = 0, col2 = 0;
	cout << "Please enter the number of row:";
	cin >> row;
	cout << "Please enter the number of column:";
	cin >> col;
	vector<vector<int>> &mart1 = input_matrix(row, col);
	cout << "Your input is:" << endl;
	display_matrix(mart1, row, col);

	cout << "Please enter the number of row:";
	cin >> row2;
	cout << "Please enter the number of column:";
	cin >> col2;
	if (row != row2&&col != col2) {
		cout << "The operation is not supported" << endl;
		return 0;
	}
	vector<vector<int>> &mart2 = input_matrix(row, col);
	cout << "Your input is:" << endl;
	display_matrix(mart2, row, col);

	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			mart1[i][j] += mart2[i][j];
		}
	}
	display_matrix(mart1, row, col);

}
int func_sub(void)
{
	/*int row = 0, col = 0, row2 = 0, col2 = 0;
	cout << "Please enter the number of row:";
	cin >> row;
	cout << "Please enter the number of column:";
	cin >> col;
	int **mart1 = input_matrix(row, col);
	cout << "Your input is:" << endl;
	display_matrix(mart1, row, col);

	cout << "Please enter the number of row:";
	cin >> row2;
	cout << "Please enter the number of column:";
	cin >> col2;
	if (row != row2&&col != col2) {
		cout << "The operation is not supported" << endl;
		return 0;
	}
	int **mart2 = input_matrix(row, col);
	cout << "Your input is:" << endl;

	display_matrix(mart2, row, col);

	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			mart1[i][j] -= mart2[i][j];
		}
	}
	display_matrix(mart1, row, col);
	for (int i = 0; i < row; i++) {
		delete[]mart1[i];
		delete[]mart2[i];
	}
	delete[]mart1;
	delete[]mart2;*/
	return 0;
}
int func_mult(void) {
/*	int row = 0, col = 0, row2 = 0, col2 = 0;
	cout << "Please enter the number of row:";
	cin >> row;
	cout << "Please enter the number of column:";
	cin >> col;
	int **mart1 = input_matrix(row, col);
	cout << "Your input is:" << endl;
	display_matrix(mart1, row, col);

	cout << "Please enter the number of row:";
	cin >> row2;
	cout << "Please enter the number of column:";
	cin >> col2;
	if (row != row2&&col != col2) {
		cout << "The operation is not supported" << endl;
		return 0;
	}
	int **mart2 = input_matrix(row, col);
	cout << "Your input is:" << endl;
	display_matrix(mart2, row, col);

	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			mart1[i][j] *= mart2[i][j];
		}
	}
	display_matrix(mart1, row, col);
	for (int i = 0; i < row; i++) {
		delete[]mart1[i];
		delete[]mart2[i];
	}
	delete[]mart1;
	delete[]mart2;
*/
	return 0;

}
void func_tran(void) {
/*	int row = 0, col = 0, row2 = 0, col2 = 0;
	cout << "Please enter the number of row:";
	cin >> row;
	cout << "Please enter the number of column:";
	cin >> col;
	int **mart1 = input_matrix(row, col);
	cout << "Your input is:" << endl;
	display_matrix(mart1, row, col);

	cout << "The result is:" << endl;
	for (int i = 0; i < col; i++) {
		for (int j = 0; j < row; j++) {
			cout << setw(6) << mart1[j][i];
		}
		cout << endl;
	}
	for (int i = 0; i < row; i++) {
		delete[]mart1[i];
	}
	delete[]mart1;
	*/
}
int func_deter(void) {
/*	int row = 0, col = 0, row2 = 0, col2 = 0;
	cout << "Please enter the number of row:";
	cin >> row;
	cout << "Please enter the number of column:";
	cin >> col;
	if (col != 3 && row != 3) {
		cout << "Please enter a 3X3 matrix!" << endl;
		return 0;
	}
	int **mart1 = input_matrix(row, col);

	cout << "Your input is:" << endl;
	display_matrix(mart1, row, col);

	cout << "The result is:" << endl;
	int res = 0;
	res = mart1[0][0] * (mart1[1][1] * mart1[2][2] - mart1[1][2] * mart1[2][1]) - mart1[0][1] * (mart1[1][0] * mart1[2][2] - mart1[1][2] * mart1[2][0]) + mart1[0][2] * (mart1[1][0] * mart1[2][1] - mart1[1][1] * mart1[2][0]);
	cout << res << endl;
	for (int i = 0; i < 3; i++) {
		delete[]mart1[i];
	}
	delete[]mart1;*/
	return 0;
}
int func_inver(void) {
/*	int row = 0, col = 0, row2 = 0, col2 = 0;
	cout << "Please enter the number of row:";
	cin >> row;
	cout << "Please enter the number of column:";
	cin >> col;
	if (col != 3 && row != 3) {
		cout << "Please enter a 3X3 matrix!" << endl;
		return 0;
	}
	int **mart1 = input_matrix(row, col);

	cout << "Your input is:" << endl;
	display_matrix(mart1, row, col);

	cout << "The result is:" << endl;
	int res = 0;
	for (int i = 2; i >= 0; i--) {
		for (int j = 2; j >= 0; j--) {
			cout << setw(6) << mart1[i][j];
		}
		cout << endl;
	}
	for (int i = 0; i < 3; i++) {
		delete[]mart1[i];
	}
	delete[]mart1;*/
	return 0;
}

