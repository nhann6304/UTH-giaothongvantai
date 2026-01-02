import React, { useEffect, useRef } from "react";
import * as THREE from "three";

/**
 * 🎬 BÀI 1: SCENE (Cảnh) - Khái niệm cơ bản nhất trong Three.js
 *
 * SCENE LÀ GÌ?
 * - Scene giống như một "sân khấu" hoặc "không gian 3D"
 * - Tất cả mọi thứ bạn muốn hiển thị (objects, lights, camera) đều phải thêm vào Scene
 * - Giống như một cái hộp chứa tất cả đồ vật trong thế giới 3D của bạn
 *
 * CÁC THUỘC TÍNH QUAN TRỌNG CỦA SCENE:
 * 1. background - Màu nền của scene
 * 2. fog - Sương mù (làm mờ object ở xa)
 * 3. add() - Thêm object vào scene
 * 4. remove() - Xóa object khỏi scene
 */

const SceneDemo2: React.FC = () => {
    const containerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (!containerRef.current) return;
        const container = containerRef.current;

        // ========================================
        // 🎬 TẠO SCENE
        // ========================================
        const scene = new THREE.Scene();

        // 🎨 Đặt màu nền cho scene (màu xanh dương nhạt)
        scene.background = new THREE.Color(0x87ceeb);

        // 📝 In ra console để xem scene có gì
        console.log("Scene đã tạo:", scene);
        console.log("Màu nền của scene:", scene.background);

        // ========================================
        // 📷 TẠO CAMERA (cần thiết để nhìn thấy scene)
        // ========================================
        const camera = new THREE.PerspectiveCamera(
            75, // Góc nhìn
            window.innerWidth / window.innerHeight, // Tỷ lệ
            0.1, // Near
            1000 // Far
        );
        camera.position.z = 5; // Đặt camera cách scene 5 đơn vị

        // ========================================
        // 🖼️ TẠO RENDERER (cần thiết để vẽ scene)
        // ========================================
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        container.appendChild(renderer.domElement);

        // ========================================
        // 🎨 RENDER SCENE (Vẽ scene lên màn hình)
        // ========================================
        // Hiện tại scene chỉ có background thôi, chưa có object nào
        renderer.render(scene, camera);

        // 📝 In thông tin
        console.log("Scene hiện có bao nhiêu object?", scene.children.length);
        console.log("Danh sách object trong scene:", scene.children);

        // ========================================
        // 🧹 CLEANUP
        // ========================================
        return () => {
            if (
                container &&
                renderer.domElement &&
                container.contains(renderer.domElement)
            ) {
                container.removeChild(renderer.domElement);
            }
            renderer.dispose();
        };
    }, []);

    return (
        <div className="relative w-full h-screen">
            {/* Canvas container */}
            <div ref={containerRef} className="w-full h-full" />

            {/* Giải thích */}
            <div className="absolute top-8 left-8 bg-white bg-opacity-95 p-6 rounded-lg shadow-xl max-w-md">
                <h2 className="text-2xl font-bold mb-4 text-gray-800">
                    🎬 Bài 2: SCENE
                </h2>

                <div className="space-y-4 text-sm text-gray-700">
                    <div>
                        <h3 className="font-bold text-base mb-2">Scene là gì?</h3>
                        <p className="leading-relaxed">
                            <strong>Scene</strong> giống như một{" "}
                            <span className="text-blue-600">sân khấu 3D</span> - là không gian
                            chứa tất cả mọi thứ bạn muốn hiển thị.
                        </p>
                    </div>

                    <div className="border-t pt-3">
                        <h3 className="font-bold text-base mb-2">Code cơ bản:</h3>
                        <pre className="bg-gray-100 p-3 rounded text-xs overflow-x-auto">
                            {`const scene = new THREE.Scene();

// Đặt màu nền
scene.background = new THREE.Color(0x87CEEB);`}
                        </pre>
                    </div>

                    <div className="border-t pt-3">
                        <h3 className="font-bold text-base mb-2">Bạn đang thấy gì?</h3>
                        <ul className="space-y-2">
                            <li className="flex items-start gap-2">
                                <span className="text-blue-500 font-bold">•</span>
                                <span>
                                    Một <strong>Scene rỗng</strong> với màu nền xanh dương nhạt
                                </span>
                            </li>
                            <li className="flex items-start gap-2">
                                <span className="text-blue-500 font-bold">•</span>
                                <span>
                                    Chưa có object nào (cube, sphere...) vì chưa add vào scene
                                </span>
                            </li>
                            <li className="flex items-start gap-2">
                                <span className="text-blue-500 font-bold">•</span>
                                <span>
                                    Mở <strong>Console</strong> (F12) để xem thông tin scene
                                </span>
                            </li>
                        </ul>
                    </div>

                    <div className="border-t pt-3">
                        <h3 className="font-bold text-base mb-2">
                            ⚡ Các thuộc tính quan trọng:
                        </h3>
                        <ul className="space-y-1 text-xs">
                            <li>
                                <code className="bg-gray-200 px-1 rounded">
                                    scene.background
                                </code>{" "}
                                - Màu nền
                            </li>
                            <li>
                                <code className="bg-gray-200 px-1 rounded">
                                    scene.add(object)
                                </code>{" "}
                                - Thêm object
                            </li>
                            <li>
                                <code className="bg-gray-200 px-1 rounded">
                                    scene.remove(object)
                                </code>{" "}
                                - Xóa object
                            </li>
                            <li>
                                <code className="bg-gray-200 px-1 rounded">scene.children</code>{" "}
                                - Danh sách objects
                            </li>
                        </ul>
                    </div>

                    <div className="bg-yellow-50 border border-yellow-200 rounded p-3">
                        <p className="text-xs">
                            💡 <strong>Lưu ý:</strong> Scene chỉ là "container" thôi. Để nhìn
                            thấy được, bạn cần thêm <strong>Camera</strong> và{" "}
                            <strong>Renderer</strong>.
                        </p>
                    </div>
                </div>
            </div>

            {/* Gợi ý tiếp theo */}
            <div className="absolute bottom-8 right-8 bg-green-500 text-white p-4 rounded-lg shadow-lg">
                <p className="text-sm font-semibold">✅ Hiểu về Scene rồi?</p>
                <p className="text-xs mt-1">Bài tiếp theo: Thêm Object vào Scene! 🎁</p>
            </div>
        </div>
    );
};

export default SceneDemo2;
