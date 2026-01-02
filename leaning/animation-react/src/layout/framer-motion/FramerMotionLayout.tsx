import { useEffect, useState } from "react";

export default function FramerMotionLayout() {
    const [count, setCount] = useState(0);
    const [effectCount, setEffectCount] = useState(0);

    useEffect(() => {
        const interval = setInterval(() => {
            setEffectCount((prev) => prev + 1);
        }, 1000);
        console.log("interval:::", interval);
        return () => clearInterval(interval);
    }, []);

    return (
        <div>
            <h1>Framer Motion Layout</h1>
            <button onClick={() => setCount(count + 1)}>Increment</button>
            <p>Count: {effectCount}</p>
        </div>
    );
}
