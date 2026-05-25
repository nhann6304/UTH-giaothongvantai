// 50 mock user records. Trộn random theo seed cố định để dễ test.
// Dữ liệu này được dùng cho module Filter / Users.

export interface UserRow {
  id: number;
  fullName: string;
  position: string;
  statusUser: string;
  gender: string;
  hasPermission: string;
  department: string;
  team: string;
  role: string;
  createdBy: string;
  createdAt: string; // ISO date
  updatedAt: string;
}

const positions = ['Developer', 'Designer', 'Manager', 'QA', 'DevOps'];
const statuses = ['Active', 'Inactive', 'Pending'];
const genders = ['Male', 'Female'];
const yesNo = ['Yes', 'No'];
const departments = ['Engineering', 'Marketing', 'Sales', 'HR', 'Finance'];
const teams = ['Frontend', 'Backend', 'Mobile', 'Data', 'Infra'];
const roles = ['Admin', 'User', 'Guest'];
const creators = ['admin@corp', 'lead1@corp', 'lead2@corp'];

const firstNames = ['Nhân', 'Bình', 'Lan', 'Minh', 'Hoa', 'Phong', 'Anh', 'Linh', 'Quân', 'Trang'];
const middleNames = ['Văn', 'Thị', 'Huỳnh', 'Trần', 'Lê'];
const lastNames = ['Thành', 'Hùng', 'Mai', 'Tuấn', 'Hương', 'Đức', 'Tâm'];

// Pseudo-random với seed để mỗi lần restart server, data giống nhau.
function mulberry32(seed: number) {
  let a = seed;
  return () => {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const rand = mulberry32(42);
const pick = <T>(arr: T[]) => arr[Math.floor(rand() * arr.length)];

export const USERS: UserRow[] = Array.from({ length: 50 }, (_, i) => {
  const id = i + 1;
  const created = new Date(2025, Math.floor(rand() * 12), Math.floor(rand() * 28) + 1);
  const updated = new Date(created.getTime() + Math.floor(rand() * 1000 * 60 * 60 * 24 * 60));
  return {
    id,
    fullName: `${pick(firstNames)} ${pick(middleNames)} ${pick(lastNames)}`,
    position: pick(positions),
    statusUser: pick(statuses),
    gender: pick(genders),
    hasPermission: pick(yesNo),
    department: pick(departments),
    team: pick(teams),
    role: pick(roles),
    createdBy: pick(creators),
    createdAt: created.toISOString(),
    updatedAt: updated.toISOString(),
  };
});

// Metadata trả về cho AI / FE để biết schema filter
export const FILTER_SCHEMA = {
  position: { type: 'select', label: 'Position', options: positions },
  statusUser: { type: 'select', label: 'Status users', options: statuses },
  gender: { type: 'select', label: 'Gender', options: genders },
  hasPermission: { type: 'select', label: 'Has Permission', options: yesNo },
  department: { type: 'select', label: 'Department', options: departments },
  team: { type: 'select', label: 'Team', options: teams },
  role: { type: 'select', label: 'Roles', options: roles },
  createdBy: { type: 'select', label: 'Created By', options: creators },
  createdAtStart: { type: 'date', label: 'Created At — start' },
  createdAtEnd: { type: 'date', label: 'Created At — end' },
};
