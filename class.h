#ifndef CLASS_H
#define CLASS_H

extern int X;
extern int Y;
extern int Z;
extern int delta2[3];
extern int delta3[4];


extern "C"
{
    int Xret();
    int Yret();
    int Zret();
    void Krammer2(int inp[2][3]);
    void Krammer3(int inp[3][4]);
    void Gauss3(int inp[3][4]);
    int threeDelta0ret();
    int threeDelta1ret();
    int threeDelta2ret();
    int threeDelta3ret();
    int twoDelta0ret();
    int twoDelta1ret();
    int twoDelta2ret();
}

#endif