#include <iostream>
#include <string>
#include <vector>

#include "utilFuncs.h"

using namespace std;

//double ka = 0.093; what is this?
double ke = 0.093;
double t_max = 2;
double ka;

vector<Data> kaResults;
vector<vector<double>> eulerPoints;
vector<vector<double>> rk2Points;
vector<vector<double>> rk4Points;

int main()
{
    cout << "\n------------------------------- Projeto de Metodos Numericos -------------------------------\n";
    
    //Obtenção do Valor de Ka - 4 Métodos (bissecçao, corda, newton, picard peano)
    kaResults = eqConstAbsorb();

    cout << "\n----- Resultados para Ka na eqConstAbsorb -----\n";
    for (int i = 0; i < kaResults.size(); i++)
    {
        if (i == 0)
        {
            cout << "\n    Bissecao : \n";
            //ka = kaResults.at(i).res; //definição da global Ka
        }
        else if (i == 1)
        {
            cout << "\n    Corda : \n";
            //ka = kaResults.at(i).res; //definição da global Ka
        }
        else if (i == 2)
        {
            cout << "\n    Newton : \n";
            ka = kaResults.at(i).res; //definição da global Ka
        }
        else
        {
            cout << "\n    Pecard Peano : \n";
            //ka = kaResults.at(i).res; //definição da global Ka
        }
        cout << "\tEstimativa de Ka = " << kaResults.at(i).res << endl;;
        cout << "\tNumero de iteracoes: " << kaResults.at(i).numIt;

        cout << endl;
    }
    
    cout << endl;
    cout << "\n-------------------------------------------------------------------------------\n";
    cout << "\tProvalvelmente o melhor metodo para achar Ka e o de Newton\n";
    cout << "   (pelo numero de Iteracoes). Agora temos de calcular o erro associado tambem!";
    cout << "\n-------------------------------------------------------------------------------\n";

    //Se tivermos tempo adicionar ao Cálculo do Ka o cálculo de e

    cout << endl;

    //Definição da expressão de D(t) e cálculo dos conjuntos de pontos (t, mi) e (t, mp)
    //Usando metodo de sistema de equacoes diferenciais (rk2, rk4, euler)

    //vector<DataSis> resultsS = sistemaDt();

    /*
    cout << "\n----------------- Resultados para os pontos no sistemaDt -----------------\n";
    for (int i = 0; i < resultsS.size(); i++)
    {
        if (i == 0)
        {
            cout << "\n    Euler : \n";
        }
        else if (i == 1)
        {
            cout << "\n    RK2 : \n";
        }
        else
        {
            cout << "\n    RK4 : \n";
        }

        cout << "\tEstimativa de Solucao dos pontos : i = (" << resultsS.at(i).xi << ", " << resultsS.at(i).yi << ")";
        cout << " p = (" << resultsS.at(i).xp << ", " << resultsS.at(i).yp << ")" << endl;
        cout << "\tNumero de iteracoes: " << resultsS.at(i).numIt;

        cout << endl;
    }*/

    int steps = 2000;

    cout << "\n----------------- Resultados para os pontos no sistemaDt segundo o método de euler -----------------\n";
    eulerPoints = eulerDiff(0, 0, 0, 72, steps);

    for (int i = 0; i < eulerPoints.size(); i++) {
        cout << "(x,y,z) = (" << eulerPoints[i][0] << ", " << eulerPoints[i][1] << ", " << eulerPoints[i][2] << ")\n";
    }

    cout << endl;
    

    cout << "\n----------------- Resultados para os pontos no sistemaDt segundo o método de rk2 -----------------\n";
    rk2Points = rungeKutta2Diff(0, 0, 0, 72, steps);

    for (int i = 0; i < rk2Points.size(); i++) {
        cout << "(x,y,z) = (" << rk2Points[i][0] << ", " << rk2Points[i][1] << ", " << rk2Points[i][2] << ")\n";
    }

    cout << endl;



    cout << "\n----------------- Resultados para os pontos no sistemaDt segundo o método de rk4 -----------------\n";
    rk4Points = rungeKutta4Diff(0, 0, 0, 72, steps);

    for (int i = 0; i < rk4Points.size(); i++) {
        cout << "(x,y,z) = (" << rk4Points[i][0] << ", " << rk4Points[i][1] << ", " << rk4Points[i][2] << ")\n";
    }

    cout << endl;


    cout << "\n----------------- Valores de Qc no rk4 -----------------\n";
    int s1 = steps * 2;
    int s2 = steps * 4;
    vector<vector<double>> rk4Points1 = rungeKutta4Diff(0, 0, 0, 72, s1);
    vector<vector<double>> rk4Points2 = rungeKutta4Diff(0, 0, 0, 72, s2);

    vector<double> QC;

    for (int i = 0; i < steps; i++) {
        double s, ds, dds;
        s = rk4Points[i][2];
        ds = rk4Points1[2 * i][2];
        dds = rk4Points2[4 * i][2];

        double current_QC = (ds - s) / (dds - ds);

        QC.push_back(current_QC);
    }

    for (int i = 0; i < steps; i++) {
        cout << "QC = " << QC[i] << "\n";
    }

    cout << endl;

    return 0;
}
