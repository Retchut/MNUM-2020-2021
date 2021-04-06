#pragma once
#include <vector>
#include <utility>

using namespace std;

struct Data {
    double res;
    int numIt;
};

struct DataSis {
    double xi;
    double yi;
    double xp;
    double yp;
    int numIt;
};

double funcKa(double Ka);
double diffFuncKa(double Ka);
double picardPeanoKa(double Ka);
vector<Data> eqConstAbsorb();

double D(double t);
double diff1(double t, double mi);
double diff2(double mi, double mp);
vector<vector<double>> eulerDiff(double x0, double y0, double z0, double xf, int steps);
vector<vector<double>> rungeKutta2Diff(double x0, double y0, double z0, double xf, int steps);
vector<vector<double>> rungeKutta4Diff(double x0, double y0, double z0, double xf, int steps);
//vector<DataSis> sistemaDt();

