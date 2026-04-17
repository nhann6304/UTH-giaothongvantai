// Test file cho array.ts - Áp dụng TDD
import { xuatMang1D, nhapMang1D } from './array';

// Mock console.log để test
const mockConsoleLog = jest.fn();
const originalConsoleLog = console.log;

beforeEach(() => {
    console.log = mockConsoleLog;
    mockConsoleLog.mockClear();
});

afterEach(() => {
    console.log = originalConsoleLog;
});

describe('Test mảng 1 chiều', () => {
    test('xuatMang1D - mảng hợp lệ', () => {
        const testArray = [1, 2, 3];
        xuatMang1D(testArray, 3);
        
        expect(mockConsoleLog).toHaveBeenCalledWith("Các phần tử của mảng:");
        expect(mockConsoleLog).toHaveBeenCalledWith("Phần tử[0]: 1");
        expect(mockConsoleLog).toHaveBeenCalledWith("Phần tử[1]: 2");
        expect(mockConsoleLog).toHaveBeenCalledWith("Phần tử[2]: 3");
    });

    test('xuatMang1D - input không hợp lệ', () => {
        const testArray = [1, 2, 3];
        xuatMang1D(testArray, 5); // num > length
        
        expect(mockConsoleLog).toHaveBeenCalledWith("Input không hợp lệ");
    });

    test('nhapMang1D - mảng hợp lệ', () => {
        const testArray = [10, 20, 30];
        nhapMang1D(testArray, 3);
        
        expect(mockConsoleLog).toHaveBeenCalledWith("Nhập mảng (hiển thị các phần tử):");
        expect(mockConsoleLog).toHaveBeenCalledWith("arr[0] = 10");
        expect(mockConsoleLog).toHaveBeenCalledWith("arr[1] = 20");
        expect(mockConsoleLog).toHaveBeenCalledWith("arr[2] = 30");
    });

    test('nhapMang1D - input không hợp lệ', () => {
        const testArray = [1, 2, 3];
        nhapMang1D(testArray, -1); // num <= 0
        
        expect(mockConsoleLog).toHaveBeenCalledWith("Input không hợp lệ");
    });
});
