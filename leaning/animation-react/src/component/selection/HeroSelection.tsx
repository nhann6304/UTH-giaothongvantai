import {
    MotionConfig,
    useScroll,
    useTransform,
    type Variants,
} from "framer-motion";
import { useTheme } from "../../context/ThemeContext";
import { motion, AnimatePresence } from "framer-motion";
import { FiGithub, FiLinkedin } from "react-icons/fi";
import { ArrowDown } from "lucide-react";

export default function HeroSection() {
    const { isDarkMode } = useTheme();

    const { scrollY } = useScroll();
    const heroY = useTransform(scrollY, [0, 500], [0, -100]);

    console.log("ScrollY::", scrollY);
    console.log("heroY::", heroY);

    const scrollToSelection = (sectionId: string) => {
        const element = document.getElementById(sectionId);
        if (element) {
            element.scrollIntoView({
                behavior: "smooth",
            });
        }
    };

    const containerVariants: Variants = {
        hidden: { opacity: 0, y: 20 },
        visible: {
            opacity: 1,
            transition: {
                staggerChildren: 0.2,
                delayChildren: 0.3,
            },
        },
    };

    const itemVariants: Variants = {
        hidden: { opacity: 0, y: 30 },
        visible: {
            y: 0,
            opacity: 1,
            transition: {
                duration: 0.8,
                ease: "easeOut",
            },
        },
    };

    const textVariants: Variants = {
        hidden: { opacity: 0, y: 20 },
        visible: {
            y: 0,
            opacity: 1,
            transition: {
                duration: 0.6,
                ease: "easeOut",
            },
        },
    };

    const imageVariants: Variants = {
        hidden: { opacity: 0, x: 50 },
        visible: {
            x: 0,
            opacity: 1,
            transition: {
                duration: 1,
                ease: "easeOut",
                delay: 0.5,
            },
        },
    };

    return (
        <div
            className={`min-h-screen transition-all ${isDarkMode ? "bg-gray-900 text-white" : "bg-gray-50 text-gray-900"
                }`}
        >
            <motion.section
                id="home"
                style={{ y: heroY }}
                className="min-h-screen flex item-center justify-center relative px-6 pt-10"
            >
                <div className="absolute inset-0 overflow-hidden">
                    <motion.div
                        animate={{
                            scale: [1, 1.1, 1],
                            rotate: [0.18, 360],
                        }}
                        transition={{
                            duration: 20,
                            repeat: Infinity,
                            ease: "linear",
                        }}
                        className={`absolute bottom-20 left-20 w-48 h-48 rounded-full blur-3xl opacity-10 ${isDarkMode ? "bg-purple-500" : "bg-purple-400"
                            }`}
                    ></motion.div>
                </div>

                <div className="max-w-7xl mx-auto w-full z-10 mt-20">
                    <div className="block lg:hidden">
                        <motion.div variants={imageVariants} className="">
                            <div className="w-32 h-32 mx-auto relative">
                                <motion.div
                                    whileHover={{ scale: 1.05 }}
                                    className={`w-full h-32 rounded-2xl overflow-hidden border-4 shadow-2xl ${isDarkMode ? "border-gray-800" : "border-gray-300"
                                        }`}
                                >
                                    <img
                                        src={
                                            "https://cdn.xtmobile.vn/vnt_upload/news/06_2024/hinh-nen-anime-cho-may-tinh-1-xtmobile.jpg"
                                        }
                                        alt="Profile"
                                        className="w-full h-full object-cover"
                                    />
                                </motion.div>

                                {/*  */}

                                <motion.div
                                    animate={{ rotate: 360 }}
                                    transition={{
                                        duration: 20,
                                        repeat: Infinity,
                                        ease: "linear",
                                    }}
                                    className=""
                                ></motion.div>
                                {/* Content mobile textVariants*/}

                                <motion.div
                                    variants={textVariants}
                                    className={`text-sm uppercase tracking-wider mb-4 ${isDarkMode ? "text-gray-500" : "text-gray-600"
                                        }`}
                                >
                                    Full Stack Developer
                                </motion.div>

                                <motion.h1 variants={itemVariants} className="">
                                    <span
                                        className={`${isDarkMode ? "text-white" : "text-gray-900"}`}
                                    >
                                        Building digital
                                    </span>

                                    <span className="">experiences</span>

                                    <br />

                                    <span className={isDarkMode ? "text-white" : "text-gray-900"}>
                                        that matter
                                    </span>
                                </motion.h1>

                                <motion.p
                                    variants={itemVariants}
                                    className={`text-base md:text-lg ${isDarkMode ? "text-gray-400" : "text-gray-600"
                                        } mb-8 max-w-xl mx-auto font-light leading-relaxed`}
                                >
                                    I craft beautiful and functional web applications with modern
                                    technologies and thoughtful user experiences.
                                </motion.p>

                                {/*  */}

                                <motion.div variants={itemVariants} className="">
                                    <motion.button
                                        whileHover={{ y: -2 }}
                                        whileTap={{ scale: 0.98 }}
                                        onClick={() => scrollToSelection("work")}
                                        className=""
                                    >
                                        View Work
                                    </motion.button>
                                    {/*  */}

                                    <motion.button
                                        whileHover={{ y: -2 }}
                                        whileTap={{ scale: 0.98 }}
                                        onClick={() => scrollToSelection("contact")}
                                        className={`border ${isDarkMode
                                            ? "border-gray-700 hover:border-amber-600 text-gray-300"
                                            : "border-gray-300 hover:border-amber-500 text-gray-700"
                                            } px-8 py-3 rounded-full text-sm uppercase tracking-wider font-medium transition-all duration-300`}
                                    >
                                        Get in Touch
                                    </motion.button>
                                </motion.div>
                            </div>

                            <motion.div variants={itemVariants} className="">
                                {[
                                    { icon: FiGithub, href: "https://github.com/your-profile" },
                                    {
                                        icon: FiLinkedin,
                                        href: "https://linkedin.com/in/your-profile",
                                    },
                                    {
                                        icon: FiLinkedin,
                                        href: "https://linkedin.com/in/another-profile",
                                    },
                                ].map((social, index) => (
                                    <motion.a
                                        key={index} // ✅ Thêm key
                                        href={social.href}
                                        target="_blank"
                                        whileHover={{ y: -3, scale: 1.1 }} // Hiệu ứng hover
                                        className={`p-3 rounded-full transition-colors ${isDarkMode
                                            ? "bg-gray-400 hover:text-white hover:bg-gray-800"
                                            : "bg-gray600 hover:text-gray-900 hover:bg-gray-200"
                                            } `}
                                    >
                                        <social.icon />
                                    </motion.a>
                                ))}
                            </motion.div>

                            {/*  */}

                            <motion.div variants={itemVariants} className="">
                                <span
                                    className={isDarkMode ? "text-gray-600" : "text-gray-500"}
                                >
                                    React
                                </span>
                                <span
                                    className={isDarkMode ? "text-gray-700" : "text-gray-400"}
                                >
                                    .
                                </span>
                                v
                                <span
                                    className={isDarkMode ? "text-gray-600" : "text-gray-400"}
                                >
                                    Node.js
                                </span>
                                <span
                                    className={isDarkMode ? "text-gray-700" : "text-gray-400"}
                                >
                                    .
                                </span>
                                <span
                                    className={isDarkMode ? "text-gray-600" : "text-gray-500"}
                                >
                                    TypeScript
                                </span>
                                <span
                                    className={isDarkMode ? "text-gray-700" : "text-gray-400"}
                                >
                                    .
                                </span>
                                <span
                                    className={isDarkMode ? "text-gray-600" : "text-gray-500"}
                                >
                                    MongoDB
                                </span>
                            </motion.div>
                        </motion.div>
                    </div>
                </div>

                <motion.div
                    animate={{ y: [0, 8, 0] }}
                    transition={{ duration: 2, repeat: Infinity }}
                    className=""
                >
                    <ArrowDown
                        size={20}
                        className={isDarkMode ? "text-gray-600" : "text-gray-400"}
                    />
                </motion.div>
            </motion.section>

            {/* 31:45 */}
        </div>
    );
}
