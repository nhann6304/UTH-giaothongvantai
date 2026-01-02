import Navbar from "./component/Navbar";
import HeroSection from "./component/selection/HeroSelection";
import { ThemeProvider } from "./context/ThemeContext";

export default function App() {
  return (
    <>
      <ThemeProvider>
        <div>
          <Navbar />
          <HeroSection />
        </div>
      </ThemeProvider>
    </>
  );
}
