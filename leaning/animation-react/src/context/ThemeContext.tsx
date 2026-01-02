import {
    createContext,
    useContext,
    useEffect,
    useState,
    type ReactNode,
} from "react";

export enum ETheme {
    LIGHT = "light",
    DARK = "dark",
}

interface ThemeContextType {
    isDarkMode: boolean;
    toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export const ThemeProvider = ({ children }: { children: ReactNode }) => {
    const [isDarkMode, setIsDarkMode] = useState<boolean>(() => {
        if (typeof window !== "undefined") {
            return localStorage.getItem("theme") === ETheme.DARK;
        }
        return false;
    });

    useEffect(() => {
        const root = document.documentElement;
        root.classList.toggle(ETheme.DARK, isDarkMode);
        localStorage.setItem("theme", isDarkMode ? ETheme.DARK : ETheme.LIGHT);
    }, [isDarkMode]);

    const toggleTheme = () => setIsDarkMode((prev) => !prev);

    return (
        <ThemeContext.Provider value={{ isDarkMode, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
};
// Hook
export const useTheme = () => {
    const context = useContext(ThemeContext);
    if (!context) throw new Error("useTheme must be used within ThemeProvider");
    return context;
};
