#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, k;
    int count = 0;
    cin >> n >> k;
    int arr[n];
    for (int i = 0; i < sizeof(arr) / 4; i++)
        cin >> arr[i];

    for (int i = 0; i < sizeof(arr) / 4; i++)
    {
        if (arr[i] > 0 && arr[i] >= arr[k - 1])
        {
            count++;
        }
    }

    cout << count;
    return 0;
}