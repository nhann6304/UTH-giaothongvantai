#include <iostream>
#include <cstdlib>

using namespace std;

struct TapHop {
    int* elements;
    int size;
};

// Tao tap hop moi
TapHop createSet() {
    TapHop s;
    cout << "Nhap so luong phan tu: ";
    cin >> s.size;
    s.elements = new int[s.size];
    cout << "Nhap cac phan tu:\n";
    for (int i = 0; i < s.size; i++) {
        cout << "  Phan tu " << i + 1 << ": ";
        cin >> s.elements[i];
    }
    // Loai bo phan tu trung lap
    int newSize = 0;
    int* temp = new int[s.size];
    for (int i = 0; i < s.size; i++) {
        bool found = false;
        for (int j = 0; j < newSize; j++) {
            if (temp[j] == s.elements[i]) {
                found = true;
                break;
            }
        }
        if (!found) {
            temp[newSize++] = s.elements[i];
        }
    }
    delete[] s.elements;
    s.elements = temp;
    s.size = newSize;
    return s;
}

// Hien thi tap hop
void displaySet(TapHop s, const char* name = "") {
    cout << name << " = { ";
    for (int i = 0; i < s.size; i++) {
        cout << s.elements[i];
        if (i < s.size - 1) cout << ", ";
    }
    cout << " }" << endl;
}

// Kiem tra phan tu co trong tap hop khong
bool contains(TapHop s, int val) {
    for (int i = 0; i < s.size; i++) {
        if (s.elements[i] == val) return true;
    }
    return false;
}

// Them phan tu vao tap hop
TapHop addElement(TapHop s, int val) {
    if (contains(s, val)) return s;
    int* newArr = new int[s.size + 1];
    for (int i = 0; i < s.size; i++) newArr[i] = s.elements[i];
    newArr[s.size] = val;
    delete[] s.elements;
    s.elements = newArr;
    s.size++;
    return s;
}

// Xoa phan tu khoi tap hop
TapHop removeElement(TapHop s, int val) {
    int idx = -1;
    for (int i = 0; i < s.size; i++) {
        if (s.elements[i] == val) { idx = i; break; }
    }
    if (idx == -1) return s;
    int* newArr = new int[s.size - 1];
    int j = 0;
    for (int i = 0; i < s.size; i++) {
        if (i != idx) newArr[j++] = s.elements[i];
    }
    delete[] s.elements;
    s.elements = newArr;
    s.size--;
    return s;
}

// Hop (Union) A ∪ B
TapHop unionSet(TapHop a, TapHop b) {
    TapHop result;
    result.elements = new int[a.size + b.size];
    result.size = 0;
    for (int i = 0; i < a.size; i++) {
        result.elements[result.size++] = a.elements[i];
    }
    for (int i = 0; i < b.size; i++) {
        if (!contains(result, b.elements[i])) {
            result.elements[result.size++] = b.elements[i];
        }
    }
    return result;
}

// Giao (Intersection) A ∩ B
TapHop intersectionSet(TapHop a, TapHop b) {
    TapHop result;
    result.elements = new int[min(a.size, b.size)];
    result.size = 0;
    for (int i = 0; i < a.size; i++) {
        if (contains(b, a.elements[i])) {
            result.elements[result.size++] = a.elements[i];
        }
    }
    return result;
}

// Hieu (Difference) A \ B
TapHop differenceSet(TapHop a, TapHop b) {
    TapHop result;
    result.elements = new int[a.size];
    result.size = 0;
    for (int i = 0; i < a.size; i++) {
        if (!contains(b, a.elements[i])) {
            result.elements[result.size++] = a.elements[i];
        }
    }
    return result;
}

// Hieu doi xung (Symmetric Difference) A Δ B
TapHop symmetricDifference(TapHop a, TapHop b) {
    TapHop ab = differenceSet(a, b);
    TapHop ba = differenceSet(b, a);
    TapHop result = unionSet(ab, ba);
    delete[] ab.elements;
    delete[] ba.elements;
    return result;
}

// Kiem tra tap con A ⊂ B
bool isSubset(TapHop a, TapHop b) {
    for (int i = 0; i < a.size; i++) {
        if (!contains(b, a.elements[i])) return false;
    }
    return true;
}

// Kiem tra 2 tap bang nhau
bool isEqual(TapHop a, TapHop b) {
    return isSubset(a, b) && isSubset(b, a);
}

// Kiem tra tap rong
bool isEmpty(TapHop s) {
    return s.size == 0;
}

// So phan tu
int cardinality(TapHop s) {
    return s.size;
}

// Giai phong bo nho
void freeSet(TapHop &s) {
    if (s.elements != nullptr) {
        delete[] s.elements;
        s.elements = nullptr;
        s.size = 0;
    }
}

int main() {
    TapHop A, B;
    A.elements = nullptr; A.size = 0;
    B.elements = nullptr; B.size = 0;

    int choice;
    do {
        cout << "\n========== MENU TAP HOP ==========\n";
        cout << "1.  Tao tap hop A\n";
        cout << "2.  Tao tap hop B\n";
        cout << "3.  Hien thi tap hop A va B\n";
        cout << "4.  Hop A U B\n";
        cout << "5.  Giao A n B\n";
        cout << "6.  Hieu A \\ B\n";
        cout << "7.  Hieu doi xung A delta B\n";
        cout << "8.  Kiem tra A la tap con cua B\n";
        cout << "9.  Kiem tra A bang B\n";
        cout << "10. Them phan tu vao A\n";
        cout << "11. Xoa phan tu khoi A\n";
        cout << "12. Kiem tra phan tu thuoc A\n";
        cout << "13. So phan tu cua A va B\n";
        cout << "0.  Thoat\n";
        cout << "Lua chon: ";
        cin >> choice;

        switch (choice) {
            case 1:
                freeSet(A);
                A = createSet();
                displaySet(A, "A");
                break;
            case 2:
                freeSet(B);
                B = createSet();
                displaySet(B, "B");
                break;
            case 3:
                displaySet(A, "A");
                displaySet(B, "B");
                break;
            case 4: {
                TapHop result = unionSet(A, B);
                displaySet(result, "A U B");
                freeSet(result);
                break;
            }
            case 5: {
                TapHop result = intersectionSet(A, B);
                displaySet(result, "A n B");
                freeSet(result);
                break;
            }
            case 6: {
                TapHop result = differenceSet(A, B);
                displaySet(result, "A \\ B");
                freeSet(result);
                break;
            }
            case 7: {
                TapHop result = symmetricDifference(A, B);
                displaySet(result, "A delta B");
                freeSet(result);
                break;
            }
            case 8:
                if (isSubset(A, B))
                    cout << "A la tap con cua B\n";
                else
                    cout << "A KHONG la tap con cua B\n";
                break;
            case 9:
                if (isEqual(A, B))
                    cout << "A bang B\n";
                else
                    cout << "A KHONG bang B\n";
                break;
            case 10: {
                int val;
                cout << "Nhap phan tu can them: ";
                cin >> val;
                A = addElement(A, val);
                displaySet(A, "A");
                break;
            }
            case 11: {
                int val;
                cout << "Nhap phan tu can xoa: ";
                cin >> val;
                A = removeElement(A, val);
                displaySet(A, "A");
                break;
            }
            case 12: {
                int val;
                cout << "Nhap phan tu can kiem tra: ";
                cin >> val;
                if (contains(A, val))
                    cout << val << " THUOC tap A\n";
                else
                    cout << val << " KHONG thuoc tap A\n";
                break;
            }
            case 13:
                cout << "|A| = " << cardinality(A) << endl;
                cout << "|B| = " << cardinality(B) << endl;
                break;
            case 0:
                cout << "Thoat chuong trinh.\n";
                break;
            default:
                cout << "Lua chon khong hop le!\n";
        }
    } while (choice != 0);

    freeSet(A);
    freeSet(B);
    return 0;
}
