#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int main(void)
{
    string s;
    cin >> s;

    auto sa = suffix_array(s);
    long long ans = s.length() * (s.length() + 1) / 2;
    for(auto x : lcp_array(s, sa)) {
        ans -= x;
    }
    
    cout << ans << endl;
    return 0;
}