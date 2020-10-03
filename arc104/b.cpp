#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int n;
    string s;
    cin >> n >> s;

    int ans = 0;
    for(int i = 0; i < n; i++) {
        map<char, int> ctr;
        for(int j = i; j < n; j++) {
            ctr[s[j]]++;
            if(ctr['A'] == ctr['T'] && ctr['C'] == ctr['G']) {
                ans++;
            }
        }
    }
    cout << ans << endl;
    return 0;
}