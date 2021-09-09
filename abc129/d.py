#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;

int aa[2000][2000];
string s[2000];

int main(void) {
    int i, x, y;
    int h, w;
    scanf("%d", &h);
    scanf("%d", &w);

    for(i = 0; i < h; ++i) {
        cin >> s[i];
    }

    for(y = 0; y < h; ++y) {
        int l = 0;
        for(x = 0; x < w; ++x) {
            if(s[y][x] == '#') {
                for(i = l; i < x; ++i) {
                    aa[y][i] = x - l;
                }
                l = x + 1;
            }
        }
        for(i = l; i < w; ++i) {
            aa[y][i] = w - l;
        }
    }

    int ans = 0;
    for(x = 0; x < w; ++x) {
        int t = 0;
        for(y = 0; y < h; ++y) {
            if(s[y][x] == '#') {
                for(i = t; i < y; ++i) {
                    aa[i][x] += y - t;
                    ans = max(ans, aa[i][x]);
                }
                t = y + 1;
            }
        }
        for(i = t; i < h; ++i) {
            aa[i][x] += h - t;
            ans = max(ans, aa[i][x]);
        }
    }
    printf("%d\n", ans - 1);
    return 0;
}
