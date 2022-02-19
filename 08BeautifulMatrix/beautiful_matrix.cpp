#include <bits/stdc++.h>

using namespace std;

int main()
{

    int matrix[5][5] = {
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 1},
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0}};

    int k, m;

    for (int i = 0; i < 5; i++)
    {
        bool found = false;
        for (int j = 0; j < 5; j++)
        {
            if (matrix[i][j] == 1)
            {
                k = i;
                m = j;
                found = true;
                break;
            }
        }

        if (found)
            break;
    }

    int result = 0;
    if (k > 2)
    {
        if (m > 2)
        {
            result = k - 2 + m - 2;
        }
        else
        {
            result = k - 2 + 2 - m;
        }
    }
    else if (k < 2)
    {
        if (m > 2)
        {
            result = 2 - k + m - 2;
        }
        else
        {
            result = 2 - k + 2 - m;
        }
    }
    else if (k == 2)
    {
        if (m > 2)
        {
            result = m - 2;
        }
        else
            result = 2 - m;
    }
    else if (k == 2 && m == 2)
    {
        result = 0;
    }

    cout << result << endl;

    return 0;
}