#include "StockAccount.h"
#include<yvals.h>
#include <iostream>
#include <engine.h>

#if(_MSC_VER>=1600)
#define __STDC_UTF_16__
#endif

#include "mex.h"

#pragma comment(lib, "libmx.lib")
#pragma comment (lib, "libmex.lib")
#pragma comment (lib,"libeng.lib")


using namespace std;


void StockAccount::drawGraph()
{


	double timeData[50];
	double valueData[50];

	ifstream ifile;
	if (!checkIsHistory(PORTFOLIO_VALUE_HISTORY)) {
		cout << PORTFOLIO_VALUE_HISTORY << " not exist" << endl;
		return;
	}
	int linesCount = countLines();
	ifile.open(PORTFOLIO_VALUE_HISTORY);
	if (ifile.fail()) {
		cout << "cannot open " << PORTFOLIO_VALUE_HISTORY << endl;
		return;
	}
	int i = 0;
	string line;
	if (linesCount > 50) {
		for (int i=0;getline(ifile,line)&&i<linesCount-51;i++){}
	}
	for ( i=0;getline(ifile,line)&&i<50;i++) {
		if (i == 0) {
			timeData[0] = atof(splitLine(line, 3).c_str());
			valueData[i] = atof(splitLine(line, 2).c_str());

			continue;
		}
		//change seconde to minute.
		timeData[i] = (atof(splitLine(line, 3).c_str())-timeData[0])/60;
		valueData[i] = atof(splitLine(line, 2).c_str());
	}
	ifile.close();
	
	//if not 50 records. set the rest of value the same to the last one.
	for (int j = i; j < 50; j++) {
		timeData[j] = timeData[i - 1];
		valueData[j] = valueData[j - 1];
	}

	Engine *ep;
	ep = engOpen(NULL);
	if (ep == NULL) {
		cout << "Error: Not Found" << endl;
		exit(1);
	}

	timeData[0] = 0;
	mxArray *X;
	X = mxCreateDoubleMatrix(1, 50, mxREAL);
	memcpy((void *)mxGetPr(X), (void *)timeData, sizeof(double) * 50);
	mxArray *Y;
	Y = mxCreateDoubleMatrix(1, 50, mxREAL);
	memcpy((void *)mxGetPr(Y), (void *)valueData, sizeof(double) * 50);

	engPutVariable(ep, "x", X);
	engPutVariable(ep, "y", Y);
	engEvalString(ep, "plot(x, y)");
	engEvalString(ep, "title('portfolio total value trend line')");
	engEvalString(ep, "xlabel('time (min)')");
	engEvalString(ep, "ylabel('total value ($)')");

	system("pause");

	mxDestroyArray(X);
	mxDestroyArray(Y);
	engEvalString(ep, "close;");
	engClose(ep);
}

int StockAccount::countLines() {
	ifstream file;
	int count = 0;
	string tmp;
	file.open(PORTFOLIO_VALUE_HISTORY, ios::in);
	while (getline(file, tmp, '\n')) {
		count++;
	}
	file.close();
	return count;
}
