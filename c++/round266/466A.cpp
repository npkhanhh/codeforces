#include <math.h>

#include <iostream>
using namespace std;

int main() {
  int n, m, a, b;
  cin >> n >> m >> a >> b;
  int res;
  double cost_per_ride = double(b) / m;
  if (cost_per_ride >= a) {
    res = n * a;
  } else {
    int min_multi = floor(double(n) / m);
    int left = n % m;
    res = min((min_multi + 1) * b, min_multi * b + left * a);
  }
  cout << res;
  return 0;
}
