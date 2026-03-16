interface co_the_bay {
    fly(): void;
}

interface co_the_boi {
    swim(): void;
}

abstract class Animal {
    protected name: string;
    protected species: string;

    constructor(name: string, species: string) {
        this.name = name;
        this.species = species;
    }

    abstract tieng_kieu(): void;

    eat(food: string): void {
        console.log(`${this.name} (${this.species}) đang ăn ${food}`);
    }

    getDetails(): string {
        return `Tên ${this.name}, Loài: ${this.species}`;
    }
}

class Chim_Canh_Cut extends Animal implements co_the_boi {
    constructor(name: string) {
        super(name, "Chim cánh cụt");
    }

    tieng_kieu(): void {
        console.log("Pingu Pingu!");
    }

    // Bắt buộc phải có hàm này vì đã implements co_the_boi
    swim(): void {
        console.log(`${this.name} đang lặn xuống nước băng giá.`);
    }
}
