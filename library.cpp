#include "class.h"
#include <algorithm>
#include <fstream>
int X;
int Y;
int Z;
int delta2[3];
int delta3[4];
extern "C"
{
    // int lcm(int a, int b);
    void Gauss3(int inp[3][4])
    {
        std::ofstream file;
        file.open("data.txt");
        const int size = 3;
        int x[size], first[size+1], second[size], third[size], result[size-1];
        for(int i = 0; i < size; i++)
        {
            x[i] = inp[i][0];
        }
        //putting inp[0] into first[size+1]:
        for(int i = 0; i <= size; i++)
        {
            first[i] = inp[0][i];
        }
        //find lcm of first and second:
        int mult = (x[0] / std::__gcd(x[0], x[1]))*x[1];
        for(int i = 0; i <= size; i++)
        {
            inp[0][i] *= (mult/x[0]);
            inp[1][i] *= (mult/x[1]);
        }
        file << mult/x[0] << "\n";
        file << mult/x[1] << "\n";
        //putting the result into second[size]:
        for(int i = 0; i < size; i++)
        {
            second[i] = inp[0][i+1] - inp[1][i+1];
            file << second[i] << "\n";
        }
        //repeating the process with I and III and putting it into third[size]:
        mult = (x[0] / std::__gcd(x[0], x[2]))*x[2];
        file << mult/x[0] << "\n";
        file << mult/x[2] << "\n";
        for(int i = 0; i <= size; i++)
        {
            first[i] *= (mult/x[0]);
            file << first[i] << "\n";
            inp[2][i] *= (mult/x[2]);
        }
        for(int i = 0; i < size; i++)
        {
            third[i] = first[i+1] - inp[2][i+1];
            file << third[i] << "\n";
            
        }
        //repeating the process with II and III and finding Z:
        mult = (second[0] / std::__gcd(second[0], third[0]))*third[0];
        int y[2] = {second[0], third[0]};
        for(int i = 0; i < size; i++)
        {
            second[i] *= (mult/y[0]);
            third[i] *= (mult/y[1]);
        }
        file << mult/y[0] << "\n";
        file << mult/y[1] << "\n";
        for(int i = 0; i < size - 1; i++)
        {
            result[i] = second[i+1] - third[i+1];
            file << result[i] << "\n";
        }
        Z = result[1]/result[0];
        Y = (second[2] - second[1]*Z)/second[0];
        X = (first[3] - first[2]*Z - first[1]*Y)/first[0];
    }
    void Krammer2(int inp[2][3])
    {
        delta2[0] = inp[0][0] * inp[1][1] - inp[0][1] * inp[1][0];
        delta2[1] = inp[0][2] * inp[1][1] - inp[0][1] * inp[1][2];
        delta2[2] = inp[0][0] * inp[1][2] - inp[1][0] * inp[0][2];
        X = delta2[1]/delta2[0];
        Y = delta2[2]/delta2[0];
    }
    void Krammer3(int inp[3][4])
    {
        delta3[0] = inp[0][0]*inp[1][1]*inp[2][2] + inp[0][1]*inp[1][2]*inp[2][0] + inp[0][2]*inp[2][1]*inp[1][0] - inp[2][2]*inp[1][0]*inp[0][1] - inp[2][1]*inp[1][2]*inp[0][0] - inp[2][0]*inp[1][1]*inp[0][2];
        delta3[1] = inp[0][3]*inp[1][1]*inp[2][2] + inp[0][1]*inp[1][2]*inp[2][3] + inp[0][2]*inp[1][3]*inp[2][1] - inp[0][1]*inp[1][3]*inp[2][2] - inp[0][3]*inp[1][2]*inp[2][1] - inp[0][2]*inp[1][1]*inp[2][3];
        delta3[2] = inp[0][0]*inp[1][3]*inp[2][2] + inp[0][3]*inp[1][2]*inp[2][0] + inp[0][2]*inp[1][0]*inp[2][3] - inp[0][3]*inp[1][0]*inp[2][2] - inp[0][0]*inp[1][2]*inp[2][3] - inp[0][2]*inp[1][3]*inp[2][0];
        delta3[3] = inp[0][0]*inp[1][1]*inp[2][3] + inp[0][1]*inp[1][3]*inp[2][0] + inp[0][3]*inp[1][0]*inp[2][1] - inp[0][1]*inp[1][0]*inp[2][3] - inp[0][0]*inp[1][3]*inp[2][1] - inp[0][3]*inp[1][1]*inp[2][0];
        X = delta3[1]/delta3[0];
        Y = delta3[2]/delta3[0];
        Z = delta3[3]/delta3[0];
    }
    int Xret()
    {
        return X;
    }
    int Yret()
    {
        return Y;
    }
    int Zret()
    {
        return Z;
    }
    int threeDelta0ret()
    {
        return delta3[0];
    }
    int threeDelta1ret()
    {
        return delta3[1];
    }
    int threeDelta2ret()
    {
        return delta3[2];
    }
    int threeDelta3ret()
    {
        return delta3[3];
    }
    int twoDelta0ret()
    {
        return delta2[0];
    }
    int twoDelta1ret()
    {
        return delta2[1];
    }
    int twoDelta2ret()
    {
        return delta2[2];
    }
}