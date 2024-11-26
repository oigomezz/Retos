#include <iostream>
#include <vector>
#include <cstdlib>

int main() {
    int n, k, steps = 0;
    std::cin >> n; 
    std::vector<int> a(n), b(n);
    
    for(int i = 0; i < n; i++)
        std::cin >> a[i];
    for(int i = 0; i < n; i++)
        std::cin >> b[i];
    
    for(int i = 0; i < n - 1; i++) {
        if(a[i] < a[i + 1]) {
            k = a[i];
            a[i] = a[i + 1];
            a[i + 1] = k;
            k = b[i];
            b[i] = b[i + 1];
            b[i + 1] = k;
        }
    }
    
    for(int i = 0; i < n - 1; i++) {
        while(a[n - 1] != a[i]) {
            if(a[i] <= 0) {
                std::cout << "-1";
                exit(0);
            }
            if(a[n - 1] < a[i]) {
                a[i] = a[i] - b[i];
                steps++;
            }
            if(a[n - 1] > a[i]) {
                a[n - 1] = a[n - 1] - b[n - 1];
                steps++;
            }
        }
    }
    
    std::cout << steps;
    return 0;
}

