#include <iostream>
#include <algorithm>
#include "class.h"
extern "C"

int lcm(int a, int b)
{
    // maximum value between n1 and n2 is stored in max
    return (a / std::__gcd(a, b))*b;
}

void Krammer2(Krammer &krammer2)
{
    krammer2.delta2[0] = krammer2.inp2[0][0] * krammer2.inp2[1][1] - krammer2.inp2[0][1] * krammer2.inp2[1][0];
    krammer2.delta2[1] = krammer2.inp2[0][2] * krammer2.inp2[1][1] - krammer2.inp2[0][1] * krammer2.inp2[1][2];
    krammer2.delta2[2] = krammer2.inp2[0][0] * krammer2.inp2[1][2] - krammer2.inp2[1][0] * krammer2.inp2[0][2];
    krammer2.X = krammer2.delta2[1]/krammer2.delta2[0];
    krammer2.Y = krammer2.delta2[2]/krammer2.delta2[0];

}

void Krammer3(Krammer &krammer3)
{
    krammer3.delta3[0] = krammer3.inp3[0][0]*krammer3.inp3[1][1]*krammer3.inp3[2][2] + krammer3.inp3[0][1]*krammer3.inp3[1][2]*krammer3.inp3[2][0] + krammer3.inp3[0][2]*krammer3.inp3[2][1]*krammer3.inp3[1][0] - krammer3.inp3[2][2]*krammer3.inp3[1][0]*krammer3.inp3[0][1] - krammer3.inp3[2][1]*krammer3.inp3[1][2]*krammer3.inp3[0][0] - krammer3.inp3[2][0]*krammer3.inp3[1][1]*krammer3.inp3[0][2];
    krammer3.delta3[1] = krammer3.inp3[0][3]*krammer3.inp3[1][1]*krammer3.inp3[2][2] + krammer3.inp3[0][1]*krammer3.inp3[1][2]*krammer3.inp3[2][3] + krammer3.inp3[0][2]*krammer3.inp3[1][3]*krammer3.inp3[2][1] - krammer3.inp3[0][1]*krammer3.inp3[1][3]*krammer3.inp3[2][2] - krammer3.inp3[0][3]*krammer3.inp3[1][2]*krammer3.inp3[2][1] - krammer3.inp3[0][2]*krammer3.inp3[1][1]*krammer3.inp3[2][3];
    krammer3.delta3[2] = krammer3.inp3[0][0]*krammer3.inp3[1][3]*krammer3.inp3[2][2] + krammer3.inp3[0][3]*krammer3.inp3[1][2]*krammer3.inp3[2][0] + krammer3.inp3[0][2]*krammer3.inp3[1][0]*krammer3.inp3[2][3] - krammer3.inp3[0][3]*krammer3.inp3[1][0]*krammer3.inp3[2][2] - krammer3.inp3[0][0]*krammer3.inp3[1][2]*krammer3.inp3[2][3] - krammer3.inp3[0][2]*krammer3.inp3[1][3]*krammer3.inp3[2][0];
    krammer3.delta3[3] = krammer3.inp3[0][0]*krammer3.inp3[1][1]*krammer3.inp3[2][3] + krammer3.inp3[0][1]*krammer3.inp3[1][3]*krammer3.inp3[2][0] + krammer3.inp3[0][3]*krammer3.inp3[1][0]*krammer3.inp3[2][1] - krammer3.inp3[0][1]*krammer3.inp3[1][0]*krammer3.inp3[2][3] - krammer3.inp3[0][0]*krammer3.inp3[1][3]*krammer3.inp3[2][1] - krammer3.inp3[0][3]*krammer3.inp3[1][1]*krammer3.inp3[2][0];
    krammer3.X = krammer3.delta3[1]/krammer3.delta3[0];
    krammer3.Y = krammer3.delta3[2]/krammer3.delta3[0];
    krammer3.Z = krammer3.delta3[3]/krammer3.delta3[0];
}



void Gauss3(Krammer &gauss3)
{
    const int size = 3;
    int X[size], first[size+1], second[size], third[size], result[size-1];

    //sorting the krammer3.inp3(bubble sort):
    for(int i = 0; i < size-1; i++)
    {
        for(int j = 0; j < size-i-1; j++)
        {
            if(gauss3.inp3[j][0] > gauss3.inp3[j+1][0])
            {
                for(int n = 0; n <= size; n++)
                {
                    int temp = gauss3.inp3[j][n];
                    gauss3.inp3[j][n] = gauss3.inp3[j+1][n];
                    gauss3.inp3[j+1][n] = temp;
                }
            }
        }
    }
    for(int i = 0; i < size; i++)
    {
        X[i] = gauss3.inp3[i][0];
    }
    //putting gauss3.inp3[0] into first[size+1]:
    for(int i = 0; i <= size; i++)
    {
        first[i] = gauss3.inp3[0][i];
    }
       //find lcm of first and second:
    int mult = lcm(X[0], X[1]);
    for(int i = 0; i <= size; i++)
    {
        gauss3.inp3[0][i] *= (mult/X[0]);
        gauss3.inp3[1][i] *= (mult/X[1]);
    }
    //putting the result into second[size]:
    for(int i = 0; i < size; i++)
    {
        second[i] = gauss3.inp3[0][i+1] - gauss3.inp3[1][i+1];
    }
    //repeating the process with I and III and putting it into third[size]:
    mult = lcm(X[0], X[2]);
    for(int i = 0; i <= size; i++)
    {
        first[i] *= (mult/X[0]);
        gauss3.inp3[2][i] *= (mult/X[2]);
    }
    for(int i = 0; i < size; i++)
    {
        third[i] = first[i+1] - gauss3.inp3[2][i+1];
    }
    //repeating the process with II and III and finding Z:
    mult = lcm(second[0], third[0]);
    int Y[2] = {second[0], third[0]};
    for(int i = 0; i < size; i++)
    {
        second[i] *= (mult/Y[0]);
        third[i] *= (mult/Y[1]);
    }
    for(int i = 0; i < size - 1; i++)
    {
        result[i] = second[i+1] - third[i+1];
    }
    gauss3.Z = result[1]/result[0];
    gauss3.Y = (second[2] - second[1]*gauss3.Z)/second[0];
    gauss3.X = (first[3] - first[2]*gauss3.Z - first[1]*gauss3.Y)/first[0];
}

