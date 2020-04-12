#include <bits/stdc++.h>
using namespace std;

int table[200][200];

int gcd(int a , int b)
{
   if(b==0) return a;
   a %= b;
   return gcd(b,a);
}

int main(void) {
    int k;
    cin >> k;

    for(int i = 0; i < 200; i++) {
        for(int j = 0; j < 200; j++) {
            table[i][j] = gcd(i + 1, j + 1);
        }
    }

    int x = 0;
    for(int a = 1; a <= k; a++) {
        for(int b = 1; b <= k; b++) {
            int y = table[a - 1][b - 1];
            for(int c= 1; c <= k; c++) {
                x += table[y - 1][c - 1];
            }
        }
    }
    cout << x << endl;
    return 0;
}