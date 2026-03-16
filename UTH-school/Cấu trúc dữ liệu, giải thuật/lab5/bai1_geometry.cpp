#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

const double PI = acos(-1.0);
const double EPS = 1e-9;

// ===================== STRUCT DEFINITIONS =====================

struct Point {
    double x, y;
};

struct Segment {
    Point A, B;
};

// ax + by + c = 0
struct Line {
    double a, b, c;
};

// y = ax^2 + bx + c
struct Parabol {
    double a, b, c;
};

struct Vector2D {
    Point source, target;
    double dx() const { return target.x - source.x; }
    double dy() const { return target.y - source.y; }
};

struct Triangle {
    Point A, B, C;
};

struct Rectangle {
    Point A, B, C, D;
};

struct Circle {
    Point center;
    double radius;
};

struct ConvexPoly {
    int n;
    Point* points;
};

// ===================== INPUT FUNCTIONS =====================

void inputPoint(Point &p, const char* name = "") {
    cout << "Nhap toa do " << name << " (x y): ";
    cin >> p.x >> p.y;
}

void inputSegment(Segment &s) {
    cout << "--- Nhap doan thang ---\n";
    inputPoint(s.A, "A");
    inputPoint(s.B, "B");
}

void inputLine(Line &l) {
    cout << "--- Nhap duong thang ax + by + c = 0 ---\n";
    cout << "Nhap a, b, c: ";
    cin >> l.a >> l.b >> l.c;
}

void inputParabol(Parabol &p) {
    cout << "--- Nhap parabol y = ax^2 + bx + c ---\n";
    cout << "Nhap a, b, c: ";
    cin >> p.a >> p.b >> p.c;
}

void inputVector(Vector2D &v) {
    cout << "--- Nhap vector ---\n";
    inputPoint(v.source, "goc");
    inputPoint(v.target, "ngon");
}

// Kiem tra 3 diem co tao thanh tam giac khong
bool isTriangle(Point A, Point B, Point C) {
    double cross = (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x);
    return fabs(cross) > EPS;
}

void inputTriangle(Triangle &t) {
    cout << "--- Nhap tam giac ---\n";
    while (true) {
        inputPoint(t.A, "A");
        inputPoint(t.B, "B");
        inputPoint(t.C, "C");
        if (isTriangle(t.A, t.B, t.C)) break;
        cout << "3 diem thang hang, khong tao thanh tam giac. Nhap lai!\n";
    }
}

void inputRectangle(Rectangle &r) {
    cout << "--- Nhap hinh chu nhat (4 dinh theo thu tu) ---\n";
    inputPoint(r.A, "A");
    inputPoint(r.B, "B");
    inputPoint(r.C, "C");
    inputPoint(r.D, "D");
}

void inputCircle(Circle &c) {
    cout << "--- Nhap duong tron ---\n";
    inputPoint(c.center, "tam");
    cout << "Nhap ban kinh: ";
    cin >> c.radius;
}

// Tich co huong
double cross(Point O, Point A, Point B) {
    return (A.x - O.x) * (B.y - O.y) - (A.y - O.y) * (B.x - O.x);
}

// Kiem tra da giac loi
bool isConvex(Point* pts, int n) {
    if (n < 3) return false;
    bool hasPos = false, hasNeg = false;
    for (int i = 0; i < n; i++) {
        double d = cross(pts[i], pts[(i + 1) % n], pts[(i + 2) % n]);
        if (d > EPS) hasPos = true;
        if (d < -EPS) hasNeg = true;
        if (hasPos && hasNeg) return false;
    }
    return true;
}

void inputConvexPoly(ConvexPoly &poly) {
    cout << "--- Nhap da giac loi ---\n";
    while (true) {
        cout << "Nhap so dinh (n >= 3): ";
        cin >> poly.n;
        if (poly.n < 3) {
            cout << "So dinh phai >= 3. Nhap lai!\n";
            continue;
        }
        poly.points = new Point[poly.n];
        for (int i = 0; i < poly.n; i++) {
            char name[20];
            sprintf(name, "dinh %d", i + 1);
            inputPoint(poly.points[i], name);
        }
        if (isConvex(poly.points, poly.n)) break;
        cout << "Da giac lom! Nhap lai!\n";
        delete[] poly.points;
    }
}

// ===================== TINH TOAN =====================

// Do dai segment
double segmentLength(Segment s) {
    double dx = s.B.x - s.A.x;
    double dy = s.B.y - s.A.y;
    return sqrt(dx * dx + dy * dy);
}

// Khoang cach tu diem den duong thang
double distPointToLine(Point p, Line l) {
    return fabs(l.a * p.x + l.b * p.y + l.c) / sqrt(l.a * l.a + l.b * l.b);
}

// Do dai vector
double vectorLength(Vector2D v) {
    return sqrt(v.dx() * v.dx() + v.dy() * v.dy());
}

// Goc giua 2 vector (radian -> do)
double angleBetweenVectors(Vector2D v1, Vector2D v2) {
    double dot = v1.dx() * v2.dx() + v1.dy() * v2.dy();
    double len1 = vectorLength(v1);
    double len2 = vectorLength(v2);
    if (len1 < EPS || len2 < EPS) return 0;
    double cosAngle = dot / (len1 * len2);
    // Clamp to [-1, 1]
    cosAngle = max(-1.0, min(1.0, cosAngle));
    return acos(cosAngle) * 180.0 / PI;
}

// Khoang cach giua 2 diem
double dist(Point a, Point b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

// ===================== TAM GIAC =====================

void classifyTriangle(Triangle t) {
    double a = dist(t.B, t.C);
    double b = dist(t.A, t.C);
    double c = dist(t.A, t.B);

    cout << "Cac canh: a=" << a << " b=" << b << " c=" << c << endl;

    bool isIsosceles = (fabs(a - b) < EPS || fabs(b - c) < EPS || fabs(a - c) < EPS);
    bool isEquilateral = (fabs(a - b) < EPS && fabs(b - c) < EPS);

    double a2 = a * a, b2 = b * b, c2 = c * c;
    // Sap xep
    double sides[3] = {a2, b2, c2};
    sort(sides, sides + 3);

    if (isEquilateral) {
        cout << "Tam giac DEU\n";
    } else if (fabs(sides[2] - sides[0] - sides[1]) < EPS) {
        if (isIsosceles)
            cout << "Tam giac VUONG CAN\n";
        else
            cout << "Tam giac VUONG\n";
    } else if (sides[2] > sides[0] + sides[1]) {
        if (isIsosceles)
            cout << "Tam giac TU CAN\n";
        else
            cout << "Tam giac TU\n";
    } else {
        if (isIsosceles)
            cout << "Tam giac NHON CAN\n";
        else
            cout << "Tam giac NHON\n";
    }
}

double trianglePerimeter(Triangle t) {
    return dist(t.A, t.B) + dist(t.B, t.C) + dist(t.A, t.C);
}

double triangleArea(Triangle t) {
    return fabs(cross(t.A, t.B, t.C)) / 2.0;
}

// ===================== HINH CHU NHAT =====================

double rectanglePerimeter(Rectangle r) {
    return dist(r.A, r.B) + dist(r.B, r.C) + dist(r.C, r.D) + dist(r.D, r.A);
}

double rectangleArea(Rectangle r) {
    // Dien tich = |AB x AD|
    double dx1 = r.B.x - r.A.x, dy1 = r.B.y - r.A.y;
    double dx2 = r.D.x - r.A.x, dy2 = r.D.y - r.A.y;
    return fabs(dx1 * dy2 - dy1 * dx2);
}

// ===================== DUONG TRON =====================

double circlePerimeter(Circle c) {
    return 2.0 * PI * c.radius;
}

double circleArea(Circle c) {
    return PI * c.radius * c.radius;
}

// ===================== DA GIAC LOI =====================

double convexPolyPerimeter(ConvexPoly poly) {
    double p = 0;
    for (int i = 0; i < poly.n; i++)
        p += dist(poly.points[i], poly.points[(i + 1) % poly.n]);
    return p;
}

double convexPolyArea(ConvexPoly poly) {
    double area = 0;
    for (int i = 0; i < poly.n; i++) {
        area += poly.points[i].x * poly.points[(i + 1) % poly.n].y;
        area -= poly.points[(i + 1) % poly.n].x * poly.points[i].y;
    }
    return fabs(area) / 2.0;
}

// ===================== KIEM TRA GIAO NHAU =====================

// Diem nam trong tam giac
bool pointInTriangle(Point p, Triangle t) {
    double d1 = cross(t.A, t.B, p);
    double d2 = cross(t.B, t.C, p);
    double d3 = cross(t.C, t.A, p);
    bool hasNeg = (d1 < 0) || (d2 < 0) || (d3 < 0);
    bool hasPos = (d1 > 0) || (d2 > 0) || (d3 > 0);
    return !(hasNeg && hasPos);
}

// Diem nam trong duong tron
bool pointInCircle(Point p, Circle c) {
    return dist(p, c.center) <= c.radius + EPS;
}

// Diem nam trong da giac loi
bool pointInConvexPoly(Point p, ConvexPoly poly) {
    for (int i = 0; i < poly.n; i++) {
        double d = cross(poly.points[i], poly.points[(i + 1) % poly.n], p);
        if (d < -EPS) return false;
    }
    return true;
}

// Kiem tra 2 doan thang giao nhau
bool onSegment(Point p, Point q, Point r) {
    return q.x <= max(p.x, r.x) && q.x >= min(p.x, r.x) &&
           q.y <= max(p.y, r.y) && q.y >= min(p.y, r.y);
}

int orientation(Point p, Point q, Point r) {
    double val = cross(p, q, r);
    if (fabs(val) < EPS) return 0;
    return (val > 0) ? 1 : 2;
}

bool segmentsIntersect(Segment s1, Segment s2) {
    int o1 = orientation(s1.A, s1.B, s2.A);
    int o2 = orientation(s1.A, s1.B, s2.B);
    int o3 = orientation(s2.A, s2.B, s1.A);
    int o4 = orientation(s2.A, s2.B, s1.B);

    if (o1 != o2 && o3 != o4) return true;
    if (o1 == 0 && onSegment(s1.A, s2.A, s1.B)) return true;
    if (o2 == 0 && onSegment(s1.A, s2.B, s1.B)) return true;
    if (o3 == 0 && onSegment(s2.A, s1.A, s2.B)) return true;
    if (o4 == 0 && onSegment(s2.A, s1.B, s2.B)) return true;
    return false;
}

// 2 duong tron: giao, trong, ngoai
void checkTwoCircles(Circle c1, Circle c2) {
    double d = dist(c1.center, c2.center);
    double r1 = c1.radius, r2 = c2.radius;

    if (d > r1 + r2 + EPS) {
        cout << "Hai duong tron nam NGOAI nhau\n";
    } else if (d + min(r1, r2) < max(r1, r2) - EPS) {
        cout << "Mot duong tron nam TRONG duong tron kia\n";
    } else {
        cout << "Hai duong tron GIAO nhau\n";
    }
}

// Tam giac vs duong tron
void checkTriangleCircle(Triangle t, Circle c) {
    bool allInside = pointInCircle(t.A, c) && pointInCircle(t.B, c) && pointInCircle(t.C, c);
    if (allInside) {
        cout << "Tam giac nam TRONG duong tron\n";
        return;
    }

    // Kiem tra dinh duong tron co trong tam giac khong
    bool centerInTri = pointInTriangle(c.center, t);

    // Kiem tra canh tam giac co cat duong tron khong
    Segment sides[3] = {{t.A, t.B}, {t.B, t.C}, {t.C, t.A}};
    bool hasIntersection = false;
    for (int i = 0; i < 3; i++) {
        // Khoang cach tu tam duong tron den canh
        Line l;
        l.a = sides[i].B.y - sides[i].A.y;
        l.b = sides[i].A.x - sides[i].B.x;
        l.c = -(l.a * sides[i].A.x + l.b * sides[i].A.y);
        double d = distPointToLine(c.center, l);
        if (d <= c.radius + EPS) {
            hasIntersection = true;
            break;
        }
    }

    if (!hasIntersection && !centerInTri) {
        cout << "Tam giac va duong tron nam NGOAI nhau\n";
    } else {
        cout << "Tam giac va duong tron GIAO nhau\n";
    }
}

// ===================== DISPLAY =====================

void displayPoint(Point p) {
    cout << "(" << p.x << ", " << p.y << ")";
}

void displaySegment(Segment s) {
    cout << "Doan thang: "; displayPoint(s.A); cout << " -> "; displayPoint(s.B); cout << endl;
}

void displayTriangle(Triangle t) {
    cout << "Tam giac: "; displayPoint(t.A); cout << ", "; displayPoint(t.B); cout << ", "; displayPoint(t.C); cout << endl;
}

void displayCircle(Circle c) {
    cout << "Duong tron tam "; displayPoint(c.center); cout << " ban kinh " << c.radius << endl;
}

// ===================== MENU =====================

int main() {
    cout << fixed << setprecision(4);
    int choice;

    do {
        cout << "\n============= MENU HINH HOC 2D =============\n";
        cout << "1.  Nhap va hien thi diem\n";
        cout << "2.  Tinh do dai doan thang\n";
        cout << "3.  Khoang cach tu diem den duong thang\n";
        cout << "4.  Goc giua 2 vector\n";
        cout << "5.  Phan loai tam giac\n";
        cout << "6.  Dien tich & chu vi tam giac\n";
        cout << "7.  Dien tich & chu vi hinh chu nhat\n";
        cout << "8.  Dien tich & chu vi duong tron\n";
        cout << "9.  Dien tich & chu vi da giac loi\n";
        cout << "10. Kiem tra 2 duong tron giao nhau\n";
        cout << "11. Kiem tra tam giac va duong tron\n";
        cout << "12. Kiem tra 2 doan thang giao nhau\n";
        cout << "13. Nhap parabol\n";
        cout << "0.  Thoat\n";
        cout << "Lua chon: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                Point p;
                inputPoint(p, "P");
                cout << "Diem P = "; displayPoint(p); cout << endl;
                break;
            }
            case 2: {
                Segment s;
                inputSegment(s);
                displaySegment(s);
                cout << "Do dai: " << segmentLength(s) << endl;
                break;
            }
            case 3: {
                Point p; Line l;
                inputPoint(p, "P");
                inputLine(l);
                cout << "Khoang cach: " << distPointToLine(p, l) << endl;
                break;
            }
            case 4: {
                Vector2D v1, v2;
                cout << "Vector 1:\n";
                inputVector(v1);
                cout << "Vector 2:\n";
                inputVector(v2);
                cout << "Goc giua 2 vector: " << angleBetweenVectors(v1, v2) << " do\n";
                break;
            }
            case 5: {
                Triangle t;
                inputTriangle(t);
                classifyTriangle(t);
                break;
            }
            case 6: {
                Triangle t;
                inputTriangle(t);
                displayTriangle(t);
                cout << "Chu vi: " << trianglePerimeter(t) << endl;
                cout << "Dien tich: " << triangleArea(t) << endl;
                break;
            }
            case 7: {
                Rectangle r;
                inputRectangle(r);
                cout << "Chu vi: " << rectanglePerimeter(r) << endl;
                cout << "Dien tich: " << rectangleArea(r) << endl;
                break;
            }
            case 8: {
                Circle c;
                inputCircle(c);
                displayCircle(c);
                cout << "Chu vi: " << circlePerimeter(c) << endl;
                cout << "Dien tich: " << circleArea(c) << endl;
                break;
            }
            case 9: {
                ConvexPoly poly;
                inputConvexPoly(poly);
                cout << "Chu vi: " << convexPolyPerimeter(poly) << endl;
                cout << "Dien tich: " << convexPolyArea(poly) << endl;
                delete[] poly.points;
                break;
            }
            case 10: {
                Circle c1, c2;
                cout << "Duong tron 1:\n"; inputCircle(c1);
                cout << "Duong tron 2:\n"; inputCircle(c2);
                checkTwoCircles(c1, c2);
                break;
            }
            case 11: {
                Triangle t; Circle c;
                inputTriangle(t);
                inputCircle(c);
                checkTriangleCircle(t, c);
                break;
            }
            case 12: {
                Segment s1, s2;
                cout << "Doan thang 1:\n"; inputSegment(s1);
                cout << "Doan thang 2:\n"; inputSegment(s2);
                if (segmentsIntersect(s1, s2))
                    cout << "Hai doan thang GIAO nhau\n";
                else
                    cout << "Hai doan thang KHONG giao nhau\n";
                break;
            }
            case 13: {
                Parabol p;
                inputParabol(p);
                cout << "Parabol: y = " << p.a << "x^2 + " << p.b << "x + " << p.c << endl;
                double delta = p.b * p.b - 4 * p.a * p.c;
                double xv = -p.b / (2 * p.a);
                double yv = p.a * xv * xv + p.b * xv + p.c;
                cout << "Dinh parabol: (" << xv << ", " << yv << ")\n";
                if (delta > EPS) cout << "Cat truc Ox tai 2 diem\n";
                else if (fabs(delta) < EPS) cout << "Tiep xuc truc Ox\n";
                else cout << "Khong cat truc Ox\n";
                break;
            }
            case 0:
                cout << "Thoat chuong trinh.\n";
                break;
            default:
                cout << "Lua chon khong hop le!\n";
        }
    } while (choice != 0);

    return 0;
}
