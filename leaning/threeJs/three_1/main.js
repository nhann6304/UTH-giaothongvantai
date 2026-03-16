import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import Stats from "three/addons/libs/stats.module.js";
const scene = new THREE.Scene(); // tạo cảnh
import { GUI } from "three/addons/libs/lil-gui.module.min.js";
import { Terrain } from "./src/components/terrian";
const camera = new THREE.PerspectiveCamera(
  90, // góc nhìn nếu 90 là góc nhìn người thật
  window.innerWidth / window.innerHeight, // tỷ lệ khung hình
  0.1,
  1000,
);

// Bảng điều khiển
const gui = new GUI();

const terrain = new Terrain(10, 10);
scene.add(terrain);

const renderer = new THREE.WebGLRenderer(); // Vẽ hình ảnh 3D lên trình duyệt
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setAnimationLoop(animate); // FPS
document.body.appendChild(renderer.domElement);

// tạo khối xanh
// Các loại geometry khác:
// new THREE.SphereGeometry(1, 32, 32);     // Cầu
// new THREE.ConeGeometry(1, 2, 32);       // Nón
// new THREE.CylinderGeometry(1, 1, 2, 32); // Hình trụ
// new THREE.PlaneGeometry(1, 1);          // Mặt phẳng
// new THREE.TorusGeometry(1, 0.4, 16, 100); // Hình xuyến

const geometry = new THREE.BoxGeometry(1, 1, 1); // Cube đơn vị  (Rộng, Cao, Sâu)

const material = new THREE.MeshStandardMaterial({
  // MeshBasicMaterial
  color: 0x00ff00, // Xanh lá cây
  // wireframe: false, // Hiển thị đầy đủ
  // transparent: true, // Cho phép trong suốt
  // opacity: 0.5, // Độ trong suốt 50%
  // side: THREE.DoubleSide, // Hiển thị cả 2 mặt
});
// Điều kiển camera
const controls = new OrbitControls(camera, renderer.domElement);

// Stats - hiển thị FPS thông tin trang hiệu năng
const start = new Stats();
document.body.appendChild(start.domElement);

const cube = new THREE.Mesh(geometry, material);
scene.add(cube);
// sun

// // Thêm ánh sáng môi trường để cube không bao giờ tối hoàn toàn
// const ambientLight = new THREE.AmbientLight(0x404040, 0.5); // Màu xám, cường độ 0.5
// scene.add(ambientLight);

const sun = new THREE.DirectionalLight(0xffffff, 1); // Màu trắng, cường độ 1
// Test để thấy sự khác biệt:
// sun.position.set(0, 0, 1); // Từ sau vào - sẽ tối mặt sau
// sun.position.set(0, 0, -1); // Từ trước vào - sẽ tối mặt trước
// sun.position.set(1, 0, 0);  // Từ phải qua - sáng mặt phải
// sun.position.set(0, 1, 0);  // Từ trên xuống - sáng mặt trên

sun.position.set(1, 2, 3); // Ánh sáng từ sau ra trước
scene.add(sun);
//

camera.position.z = 5;

function animate() {
  // cube.rotation.x += 0.01;
  // cube.rotation.y += 0.01;
  // cube.rotation.z += 0.01;
  controls.update();
  renderer.render(scene, camera);
  start.update();
}

window.addEventListener("resize", () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

const folder = gui.addFolder("Cube");

folder.add(cube.position, "x", -2, 2, 0.1).name("X Position");
folder.addColor(cube.material, "color");
