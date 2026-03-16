function daonguoc(num: number): number {
    let result = 0;

    for (let i = 0; i <= num.toString().length; i++) {
        console.log((result = result * 10 + (num % 10)));
        num = Math.floor(num / 10);
    }

    // while (num > 0) {
    //     result = result * 10 + (num % 10);
    //     num = Math.floor(num / 10);
    // }

    return result;
}

console.log(daonguoc(12345)); // 54321
