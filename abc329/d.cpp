#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n, m;
    cin >> n >> m;

    int maxcnt = 0;
    map<int, int> cnt;
    map<int, set<int>> chars;
    for(int i = 0; i < m; i++) {
        int a, c = 0;
        cin >> a;
        if(cnt.find(a) != cnt.end()) {
            c = cnt[a];
            chars[c].erase(a);
        }
        c++;
        chars[c].insert(a);
        maxcnt = max(maxcnt, c);
        cnt[a]++;
        cout << *chars[maxcnt].begin() << endl;
    }

    return 0;
}