const inputArrayNum: number[] = [10, 20, 30, 40, 50]; // Mảng số nguyên đầu vào
const inputN = 5; // Số phần tử trong mảng

function xuatmang1d(arr: number[], num: number): void {
    for (let i = 0; i < num; i++) {
        console.log("<<<I>>>", arr[i]);
    }
}

function nhapmang1d(arr: number[], num: number): void {
    for (let i = 0; i <= num; i++) {
        console.log("<<<I>>>", arr[i]);
    }
}

function main(): void {
    console.log(
        nhapmang1d(inputArrayNum, inputN),
        xuatmang1d(inputArrayNum, inputN)
    );
}

main();
