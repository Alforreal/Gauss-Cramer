#include<vector>
class Gauss
{
    public:
    vector<vector<int>> matrix;
    void input(int size);
    void solve();
};

void input(int size, Frontend frontend)
{
    matrix.resize(size);
    for (int i = 0; i < matrix.size(); i++) matrix[0].resize(size + 1);
}