#include <iostream>
#include "utilFuncs.h"
#include <math.h>

//Obtenção do Valor de Ka
extern double ke; //Constante cinética de eliminação total (unidades min^-1)
extern double t_max; //Instante de C plasmática máxima do farmaco (unidades h)
extern double ka;

extern vector<Data> kaResults;

double funcKa(double Ka)
{
	return ((Ka*60) * exp(-(Ka*60) * t_max) - (ke *60) * exp(-(ke * 60) * t_max));
}

double diffFuncKa(double Ka) {
	return (-(3600 * Ka * t_max - 60)*exp(-(Ka*60) * t_max));
}

double picardPeanoKa(double Ka) {
	return (Ka * exp((60 * ke * t_max) - 60 * Ka * t_max)) - ke;
}

vector<Data> eqConstAbsorb()
{
	vector<Data> results(4); //um elemento para cada tipo de resolução
	double Error = pow(10, -8); //0.00000001
	int N = 0;

	//1 - Método da Bisseção

	double a = 0, b = 0.00001; //Intervalo no qual procurar o zero

	double xN = (a + b) / 2;

	double comp = b - a;

	while (comp > Error)
	{
		if (funcKa(a) * funcKa(xN) < 0) {
			a = a;
			b = xN;
		}
		else {
			a = xN;
			b = b;
		}

		N++;
		comp = abs(b - a);
		xN = (a + b) / 2;
	}

	results.at(0).res = xN;
	results.at(0).numIt = N;

	//2 - Método da Corda

	N = 0;
	a = a = 0, b = 0.00001; //Intervalo no qual procurar o zero

	xN = (funcKa(b) * a - funcKa(a) * b) / (funcKa(b) - funcKa(a));
 
	comp = b - a;

	while (comp > Error)
	{
		if (funcKa(a) * funcKa(xN) < 0) {
			a = a;
			b = xN;
		}
		else {
			a = xN;
			b = b;
		}

		N++;
		comp = abs(b - a);
		xN = (funcKa(b) * a - funcKa(a) * b) / (funcKa(b) - funcKa(a));
	}

	results.at(1).res = xN;
	results.at(1).numIt = N;

	//3 - Método de Newton

	N = 0;
	double xi = 1.3 * pow(10, -6); //Valor plausível para o zero da função (Observação do gráfico no Maxima)

	xN = xi - funcKa(xi) / diffFuncKa(xi);

	comp = abs(xN - xi);

	while (comp > Error)
	{
		xi = xN;
		xN = xi - funcKa(xi) / diffFuncKa(xi);

		N++;
		comp = abs(xN - xi);
	}

	results.at(2).res = xN;
	results.at(2).numIt = N;


	//4 - Método de Picard Peano

	N = 0;
	xi = 0.1; //Valor plausível para o zero da função

	xN = picardPeanoKa(xi);
	comp = abs(xN - xi);

	while (comp > Error)
	{
		//fiz uma alteração meia estranha para parar quando der infinito
		//cout << xN << endl;

		N++;

		xi = xN;
		xN = picardPeanoKa(xi);

		if (isinf(abs(xN)))
			xN = xi; break;

		comp = abs(xN - xi);

	
		//cout << "Comp > error : " << (comp > Error) << endl;
	}

	results.at(3).res = xN;
	results.at(3).numIt = N;

	return results;
}

//Definição da expressão de D(t) e cálculo dos conjuntos de pontos (t, mi) e (t, mp)
double Ka = 0.0;

//time in minutes
double D(double t)
{

	//taken from https://pubchem.ncbi.nlm.nih.gov/compound/chloramphenicol#section=LC-MS
	double retention_time = 6.853 / 60;		//in minutes
	double take_time = 24;

	if (t >= 3 * take_time) {
		return 0;
	}

	while (t >= take_time) {
		t -= take_time;
	}

	if (t <= retention_time) {
		return 0;
	}
	else if (t > retention_time && t < t_max) {
		//return (t - retention_time) * 0.2221075900271471;
		return (double)5 * (t - retention_time) / (double)24;
	}
	else if (t >= t_max && t < take_time) {
		//return  -0.019030582145507832 * (t - t_max) + 24000 / 52547;
		return (double)5 / (double)11 - (double)5 * (t - t_max) / (double)264;
	}

	return 0;
}

//equação diferencial 1 (dmi/dt)
double diff1(double t, double mi)
{
	return D(t)-ka*mi;
}

//equação diferencial 2 (dmp/dt)
double diff2(double mi, double mp)
{
	return ka * mi - ke * mp;
}

//euler method for the differential equation 1
//x is t
//y is mi 
//z is mp
vector<vector<double>> eulerDiff(double x0, double y0, double z0, double xf, int steps) {

	//vectors of points
	vector<vector<double>> points;

	//get a ka value
	double ka1 = kaResults[0].res;

	//solve 1st eq
	double current_x, current_y, current_z, d_x;

	current_x = x0;
	current_y = y0;
	current_z = z0;
	d_x = (xf - x0) / steps;

	while (current_x < xf) {

		int y_save = current_y;
		current_y += diff1(current_x, current_y) * d_x;
		current_z += diff2(y_save, current_z) * d_x;
		current_x += d_x;
		
		//save the current point
		points.push_back({ current_x, current_y, current_z });
	}

	return points;
}

//runge kutta for solving the system
//x is t
//y is mi 
//z is mp
vector<vector<double>> rungeKutta2Diff(double x0, double y0, double z0, double xf, int steps) {

	//vectors of points
	vector<vector<double>> points;

	//get a ka value
	double ka1 = kaResults[0].res;

	double h = (xf - x0) / steps;

	for (int it = 0; it < steps; it++) {

		double dy1_n = diff1(x0, y0);
		double dz2_n = diff2(y0, z0);

		double dy1_a = diff1(x0 + h / 2, y0 + h / 2 * dy1_n);
		double dz2_a = diff2(y0 + h / 2, z0 + h / 2 * dz2_n);

		x0 += h;
		y0 += dy1_a * h;
		z0 += dz2_a * h;

		points.push_back({x0, y0, z0});

	}

	return points;
	
}

vector<vector<double>> rungeKutta4Diff(double x0, double y0, double z0, double xf, int steps) {

	//vectors of points
	vector<vector<double>> points;

	//get a ka value
	double ka1 = kaResults[0].res;

	double del1A, del1B;
	double del2A, del2B;
	double del3A, del3B;
	double del4A, del4B;
	double del5A, del5B;
	double dy, dz, h;

	h = (xf - x0) / steps;

	for (int i = 0; i < steps; i++) {

		//calculate delta 1 for func1 and func 2
		del1A = h * diff1(x0, y0);
		del1B = h * diff2(y0, z0);

		del2A = h * diff1(x0 + h / 2, y0 + del1A / 2);
		del2B = h * diff2(y0 + del1A / 2, z0 + del1B / 2);

		del3A = h * diff1(x0 + h / 2, y0 + del2A / 2);
		del3B = h * diff2(y0 + del2A / 2, z0 + del2B / 2);

		del4A = h * diff1(x0 + h / 2, y0 + del3A / 2);
		del4B = h * diff2(y0 + del3A / 2, z0 + del3B / 2);

		dy = del1A / 6 + del2A / 3 + del3A / 3 + del4A / 6;
		dz = del1B / 6 + del2B / 3 + del3B / 3 + del4B / 6;

		x0 += h;
		y0 += dy;
		z0 += dz;

		points.push_back({ x0, y0, z0 });
	}

	return points;
}

/*
vector<DataSis> sistemaDt()
{
	vector<DataSis> res(3); //um elemento para cada tipo de resolução
	double Error = pow(10, -8); //0.00000001
	int N = 0;

	//Completar isto
	double x0, y0, xf, steps;

	//2 - RK2

	//3 - RK4

	return res;
}*/

