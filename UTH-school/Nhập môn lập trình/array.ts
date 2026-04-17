// Mảng số nguyên đầu vào
const inputArrayNum: number[] = [10, 20, 30, 40, 50];
const inputN = 5; // Số phần tử trong mảng

/**
 * Xuất mảng 1 chiều
 * @param arr - Mảng cần xuất
 * @param num - Số phần tử thực tế của mảng
 */
function xuatMang1D(arr: number[], num: number): void {
    // Validation: kiểm tra input
    if (!Array.isArray(arr) || num <= 0 || num > arr.length) {
        console.error("Input không hợp lệ");
        return;
    }

    console.log("Các phần tử của mảng:");
    for (let i = 0; i < num; i++) {
        console.log(`Phần tử[${i}]: ${arr[i]}`);
    }
}

/**
 * Nhập mảng 1 chiều (hiển thị các phần tử)
 * @param arr - Mảng cần hiển thị
 * @param num - Số phần tử thực tế của mảng
 */
function nhapMang1D(arr: number[], num: number): void {
    // Validation: kiểm tra input
    if (!Array.isArray(arr) || num <= 0 || num > arr.length) {
        console.error("Input không hợp lệ");
        return;
    }

    console.log("Nhập mảng (hiển thị các phần tử):");
    for (let i = 0; i < num; i++) {
        console.log(`arr[${i}] = ${arr[i]}`);
    }
}

/**
 * Hàm main để demo các chức năng
 */
function main(): void {
    console.log("=== BÀI TẬP MẢNG 1 CHIỀU ===");

    // Demo nhập mảng
    nhapMang1D(inputArrayNum, inputN);

    console.log(); // dòng trống

    // Demo xuất mảng
    xuatMang1D(inputArrayNum, inputN);
}

// Export functions để test
export { xuatMang1D, nhapMang1D };

// Chạy hàm main nếu chạy trực tiếp
if (require.main === module) {
    main();
}
