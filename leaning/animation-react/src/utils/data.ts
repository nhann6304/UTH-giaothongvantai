import {
    Cloud,
    Code2,
    Database,
    Server,
    Heart,
    Coffee,
    Music,
    Book,
    Mail,
    Phone,
    MapPin,
} from "lucide-react";
import { FiGithub, FiLinkedin, FiTwitter } from "react-icons/fi";

interface ISkill {
    name: string;
    level: number;
    color: string;
}

export interface ISkillCategory {
    title: string;
    icon: any;
    description: string;
    skills: ISkill[];
}

export interface IStats {
    number: string;
    label: string;
}

export interface IProject {
    id: string;
    title: string;
    description: string;
    image: string;
    liveUrl: string;
    gitUrl: string;
    Featured: boolean;
    category: string;
}

export interface IJourneySteps {
    year: string;
    title: string;
    description: string;
    icon: any;
    color: string;
}

export interface IPassions {
    icon: any;
    title: string;
    description: string;
}

export interface ISocialLinks {
    name: string;
    icon: any;
    url: string;
    color: string;
    bgColor: string; // Fixed typo: bgbColor -> bgColor
}

export interface IContactInfo {
    icon: any;
    label: string;
    value: string;
}

export const SKILLS_CATEGORY: ISkillCategory[] = [
    {
        title: "Frontend",
        icon: Code2,
        description: "Crafting beautiful, responsive user interfaces",
        skills: [
            {
                name: "React",
                level: 95,
                color: "bg-blue-500",
            },
            {
                name: "TypeScript",
                level: 95,
                color: "bg-blue-600",
            },
            {
                name: "Next.js",
                level: 95,
                color: "bg-gray-800",
            },
            {
                name: "Tailwind CSS",
                level: 95,
                color: "bg-cyan-500",
            },
            {
                name: "Framer Motion",
                level: 95,
                color: "bg-pink-500",
            },
        ],
    },
    {
        title: "Backend",
        icon: Server,
        description: "Building robust server-side solutions",
        skills: [
            {
                name: "Node.js",
                level: 95,
                color: "bg-green-500",
            },
            {
                name: "Express.js",
                level: 95,
                color: "bg-gray-700",
            },
            {
                name: "NestJS",
                level: 95,
                color: "bg-pink-600",
            },
            {
                name: "REST APIs",
                level: 95,
                color: "bg-orange-500",
            },
            {
                name: "GraphQL",
                level: 95,
                color: "bg-purple-500",
            },
        ],
    },
    {
        title: "Database",
        icon: Database,
        description: "Managing and optimizing databases",
        skills: [
            {
                name: "MongoDB",
                level: 95,
                color: "bg-green-600",
            },
            {
                name: "PostgreSQL",
                level: 95,
                color: "bg-blue-700",
            },
            {
                name: "MySQL",
                level: 95,
                color: "bg-red-500",
            },
            {
                name: "Redis",
                level: 95,
                color: "bg-indigo-600",
            },
            {
                name: "Prisma",
                level: 95,
                color: "bg-yellow-600",
            },
        ],
    },
    {
        title: "DevOps",
        icon: Cloud,
        description: "Deploying and maintaining cloud infrastructure",
        skills: [
            {
                name: "Docker",
                level: 95,
                color: "bg-blue-600",
            },
            {
                name: "AWS",
                level: 95,
                color: "bg-orange-600",
            },
            {
                name: "Vercel",
                level: 95,
                color: "bg-gray-900",
            },
            {
                name: "Git",
                level: 95,
                color: "bg-orange-700",
            },
            {
                name: "CI/CD",
                level: 95,
                color: "bg-purple-600",
            },
        ],
    },
];

export const TECH_STACK = [
    "JavaScript",
    "TypeScript",
    "HTML5",
    "CSS3",
    "Sass",
    "Vite",
    "Figma",
    "Git",
    "GitHub",
    "GitLab",
];

export const STATS: IStats[] = [
    { number: "50+", label: "Projects Completed" },
    { number: "3+", label: "Years Experience" },
    { number: "20+", label: "Technologies" },
    { number: "100%", label: "Client Satisfaction" },
];

export const PROJECTS: IProject[] = [
    {
        id: "1",
        title: "E-Commerce Platform",
        description:
            "Full-stack e-commerce solution with Next.js and NestJS backend",
        image: "https://surl.li/bagtgd",
        liveUrl: "https://project1.com",
        gitUrl: "https://github.com/project1",
        Featured: true,
        category: "Full Stack",
    },
    {
        id: "2",
        title: "Task Management System",
        description: "Collaborative task management app with real-time updates",
        image: "https://surl.li/ocpttl",
        liveUrl: "https://project2.com",
        gitUrl: "https://github.com/project2",
        Featured: true,
        category: "Full Stack",
    },
    {
        id: "3",
        title: "Social Media Dashboard",
        description: "Analytics dashboard for social media management",
        image: "https://surl.li/bagtgd",
        liveUrl: "https://project3.com",
        gitUrl: "https://github.com/project3",
        Featured: false,
        category: "Frontend",
    },
];

export const JOURNEY_STEPS: IJourneySteps[] = [
    {
        year: "2022",
        title: "Started Coding with HTML & CSS",
        description:
            "Began my web development journey learning the fundamentals of HTML and CSS",
        icon: Code2,
        color: "bg-blue-500",
    },
    {
        year: "2023",
        title: "Mastered JavaScript & React",
        description:
            "Dove deep into JavaScript and modern frontend frameworks like React",
        icon: Code2,
        color: "bg-green-500",
    },
    {
        year: "2024",
        title: "Full Stack Development",
        description:
            "Expanded skills to backend with Node.js, NestJS and database management",
        icon: Server,
        color: "bg-purple-500",
    },
    {
        year: "2025",
        title: "Senior Full Stack Developer",
        description:
            "Leading projects with Next.js, NestJS and cloud infrastructure",
        icon: Cloud,
        color: "bg-orange-500",
    },
];

export const PASSIONS: IPassions[] = [
    {
        icon: Code2,
        title: "Clean Code",
        description:
            "Writing maintainable, scalable, and efficient code that stands the test of time",
    },
    {
        icon: Heart,
        title: "Problem Solving",
        description:
            "Tackling complex challenges and creating innovative solutions",
    },
    {
        icon: Coffee,
        title: "Continuous Learning",
        description:
            "Always exploring new technologies and staying updated with industry trends",
    },
    {
        icon: Music,
        title: "UI/UX Design",
        description:
            "Creating beautiful and intuitive user experiences that delight users",
    },
];

export const SOCIAL_LINKS: ISocialLinks[] = [
    {
        name: "GitHub",
        icon: FiGithub,
        url: "https://github.com/yourusername",
        color: "text-gray-900",
        bgColor: "hover:bg-gray-800",
    },
    {
        name: "LinkedIn",
        icon: FiLinkedin,
        url: "https://linkedin.com/in/yourusername",
        color: "text-blue-600",
        bgColor: "hover:bg-blue-500/10",
    },
    {
        name: "Twitter",
        icon: FiTwitter,
        url: "https://twitter.com/yourusername",
        color: "text-sky-500",
        bgColor: "hover:bg-sky-500/10",
    },
    {
        name: "Email",
        icon: Mail,
        url: "mailto:your.email@example.com",
        color: "text-red-500",
        bgColor: "hover:bg-green-500/10",
    },
];

export const CONTACT_INFO: IContactInfo[] = [
    {
        icon: Mail,
        label: "Email",
        value: "your.email@example.com",
    },
    {
        icon: Phone,
        label: "Phone",
        value: "+84 123 456 789",
    },
    {
        icon: MapPin,
        label: "Location",
        value: "Ho Chi Minh City, Vietnam",
    },
];
