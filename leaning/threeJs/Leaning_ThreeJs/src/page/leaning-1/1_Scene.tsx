import { Canvas } from "@react-three/fiber";

export default function SceneDemo() {
    return (
        <div style={{ width: "100vw", height: "100vh" }}>
            <Canvas>
                <ambientLight intensity={0.5}   />
                {/* <directionalLight position={[10, 10, 5]} intensity={1} /> */}

                <mesh
                    onClick={(e) => console.log("click")}
                    onContextMenu={(e) => console.log("context menu")}
                    onDoubleClick={(e) => console.log("double click")}
                    onWheel={(e) => console.log("wheel spins")}
                    onPointerUp={(e) => console.log("up")}
                    onPointerDown={(e) => console.log("down")}
                    onPointerOver={(e) => console.log("over")}
                    onPointerOut={(e) => console.log("out")}
                    onPointerEnter={(e) => console.log("enter")}
                    onPointerLeave={(e) => console.log("leave")}
                    onPointerMove={(e) => console.log("move")}
                    onPointerMissed={() => console.log("missed")}
                    onUpdate={(self) => console.log("props have been updated")}
                >
                    <boxGeometry args={[2, 2, 2]} />
                    <meshPhongMaterial color="royalblue" />
                </mesh>
            </Canvas>
        </div>
    );
}
