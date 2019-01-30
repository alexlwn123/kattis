#include <iostream>
#include <cstring>

using namespace std;

using ll = long long;
using ld = long double;

constexpr int MAXN = 22;
constexpr int MAXB = 15;
constexpr ll INF = 0x3f3f3f3f3f3f3f3f;
int b;
int p[MAXB][2];     //beeper locations
ll dp[1 << MAXB][MAXB];

void read() {
    int n, m;
    scanf("%d %d", &n, &m); //board dimensions
    scanf("%d %d", &p[0][0], &p[0][1]); //start
    scanf("%d", &b); //num of beeps
    ++b;
    for (int i = 1; i < b; i++) {  //reading in beeper loci
        scanf("%d %d", &p[i][0], &p[i][1]);
    }
}

inline ll dist(int i, int j) {
    return abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1]); //dist traveling legally
}

void solve() {  
    memset(dp, 0x3f, sizeof(dp)); //fill with '?'
    dp[1][0] = 0;  //represent each beeper as bit  
    for (int mask = 1; mask < (1 << b); ++mask) { //stop after going through all bits
        for(int i = 0; i < b; ++i) {
            if (dp[mask][i] == INF or (mask & (1 << i)) == 0) { //if the spot doesn't exist or specific beeper has been found
                continue;
            }
        
        
            for(int j = 0; j < b; ++j) { 
                if ((mask & (1 << j)) != 0) { //if beeper is still there, continue
                    continue;
                }
                
                int new_mask = mask | (1 << j);  //add current beeper to existing mask 
                ll cost = dp[mask][i] + dist(i, j); //determine cost of getting here
                dp[new_mask][j] = min(dp[new_mask][j], cost); //save cost in dp if more efficient way of getting here

            }
        }
    }
    
    int final_mask = (1 << b) - 1;
    ll ans = INF;
    for (int i = 1; i < b; i++) {
        ans = min(ans, dp[final_mask][i] + dist(i, 0));
    }

    printf("%lld\n", ans);


}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int T;
    scanf("%d", &T);
    while (T-- > 0) {
        read();
        solve();
    }
    return 0;
}
