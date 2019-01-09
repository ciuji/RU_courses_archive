#include "drawStrategy.h"
#include "StockAccount.h"
#include <yvals.h>
#if(_MSC_VER>=1600)
#define __STDC_utf_16__
#endif

#pragma comment(lib, "libmx.lib")
#pragma comment (lib, "libmex.lib")
#pragma comment (lib,"libeng.lib")

#include<yvals.h>
#include <iostream>
#include <engine.h>
using namespace std;


void StockAccount::drawGraph()
{
	Engine *ep;
	ep = engOpen(NULL);
	if (ep == NULL) {
		cout << "Error: init engine failed" << endl;
		return;
	}
	double timeData[40];
	double priceData[40];

	ifstream ifile;
	if (!checkIsHistory(PORTFOLIO_VALUE_HISTORY)) {
		cout << PORTFOLIO_VALUE_HISTORY << " not exist" << endl;
		return;
	}
	ifile.open(PORTFOLIO_VALUE_HISTORY);
	if (ifile.fail()) {
		cout << "cannot open " << PORTFOLIO_VALUE_HISTORY << endl;
		return;
	}
	string line;
	for (int i=0;getline(ifile,line)&&i<40;i++) {
		if (i == 0) {
			timeData[0] = atof(splitLine(line, 2).c_str());
			continue;
		}
		timeData[i] = (atof(splitLine(line, 2).c_str()) - timeData[0]) / 60.0;
		priceData[i] = atof(splitLine(line, 1).c_str());
	}
	ifile.close();

	mxArray *X;
	X = mxCreateDoubleMatrix(1, 40, mxREAL);
	memcpy((void *)mxGetPr(X), (void *)time, sizeof(double) * 40);
	mxArray *Y;
	Y = mxCreateDoubleMatrix(1, 40, mxREAL);
	memcpy((void *)mxGetPr(X), (void *)time, sizeof(double) * 40);

	engPutVariable(ep, "x", X);
	engPutVariable(ep, "y", Y);
	engEvalString(ep, "plot(x, y");
	system("pause");

	mxDestroyArray(X);
	mxDestroyArray(Y);
	engEvalString(ep, "close;");
	engClose(ep);
}

drawStrategy::drawStrategy()
{
}


drawStrategy::~drawStrategy()
{
}
