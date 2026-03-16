import * as THREE from "three";

export class Terrain extends THREE.Mesh {
  constructor(width, height) {
    super();
    this.width = width;
    this.height = height;
    this.geometry = new THREE.PlaneGeometry(width, height); // Mặt phẳng
    this.material = new THREE.MeshBasicMaterial({ color: 0x50a000 });

    this.rotation.x = -Math.PI / 2;
  }
}
