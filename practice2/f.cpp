#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int main(void)
{
    int i;
    int n, m;
    cin >> n >> m;

    vector<int> a(n);
    vector<int> b(m);
    for(i = 0; i < n; i++)
        cin >> a[i];
    for(i = 0; i < m; i++)
        cin >> b[i];
    
    auto c = convolution(a, b);
    for(auto cc : c) {
        cout << cc << " ";
    }
    cout << endl;
    
    return 0;
}