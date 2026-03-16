#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int findColumnWithMostPrimes(const vector<vector<int>>& A) {
    if (A.empty()) return -1;
    
    int M = A.size();       
    int N = A[0].size();  
    
    int max_primes = -1;   
    int best_col_index = -1;

    for (int j = 0; j < N; j++) {
        int count = 0;
        
        // Duyệt qua từng dòng (i) của cột j
        for (int i = 0; i < M; i++) {
            if (isPrime(A[i][j])) {
                count++;
            }
        }

        if (count >= max_primes) {
            max_primes = count;
            best_col_index = j;
        }
    }

    return best_col_index;
}

int main() {
    vector<vector<int>> A = {
        {1,  2,  3,  4},
        {6,  7,  8,  5},  
        {10, 11, 12, 13}  
    };
  
    int result = findColumnWithMostPrimes(A);
    cout << "Cot co nhieu so nguyen to nhat (uu tien index lon) la: " << result << endl;

    return 0;
}