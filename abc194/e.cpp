#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    int i;
    map<int, int> tb;

    int n, m;
    cin >> n >> m;
    
    vector<int> a(n, 0);
    for(i = 0; i < n; i++) {
        cin >> a[i];
    }

    int ans = 0;
    for(i = 0; i < m; i++) {
        tb[a[i]]++;
        while(tb[ans] > 0) {
            ans++;
        }
    }

    int aans = ans;
    for(i = 1; i <= n - m; i++) {
        int rm = a[i - 1];
        tb[rm]--;
        tb[a[i + m - 1]]++;
        if(tb[rm] == 0 && ans > tb[rm]) {
            ans = rm;
        }
        while(tb[ans] > 0) {
            ans++;
        }
        aans = min(aans, ans);
    }
    cout << aans << endl;
    return 0;
}