#include <iostream>
using namespace std;

int main() {
    char player1, player2;
    cout << "Nhap lua chon cua nguoi choi 1 (B=Bua, O=Bao, K=Keo): ";
    cin >> player1;
    cout << "Nhap lua chon cua nguoi choi 2 (B=Bua, O=Bao, K=Keo): ";
    cin >> player2;
    
    // Chuyển sang chữ hoa nếu nhập chữ thường
    if (player1 >= 'a' && player1 <= 'z') player1 = player1 - 32;
    if (player2 >= 'a' && player2 <= 'z') player2 = player2 - 32;
    
    if (player1 == player2) {
        cout << "Hoa!" << endl;
    } else if ((player1 == 'B' && player2 == 'K') || 
               (player1 == 'K' && player2 == 'O') || 
               (player1 == 'O' && player2 == 'B')) {
        cout << "Nguoi choi 1 thang!" << endl;
    } else {
        cout << "Nguoi choi 2 thang!" << endl;
    }
    
    return 0;
}
