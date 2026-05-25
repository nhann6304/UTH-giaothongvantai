import { Injectable } from '@nestjs/common';
import { USERS, FILTER_SCHEMA, UserRow } from './users.mock';

export interface FilterState {
  position?: string[];
  statusUser?: string[];
  gender?: string[];
  hasPermission?: string[];
  department?: string[];
  team?: string[];
  role?: string[];
  createdBy?: string[];
  createdAtStart?: string;
  createdAtEnd?: string;
}

export interface BugReport {
  id: number;
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
  title: string;
  steps: string[];
  expected: string;
  actual: string;
  createdAt: string;
}

@Injectable()
export class FilterService {
  private currentFilter: FilterState = {};
  private bugs: BugReport[] = [];

  getSchema() {
    return FILTER_SCHEMA;
  }

  getOptions(field: keyof typeof FILTER_SCHEMA): string[] {
    const meta: any = FILTER_SCHEMA[field];
    return meta?.options || [];
  }

  getState(): FilterState {
    return { ...this.currentFilter };
  }

  reset() {
    this.currentFilter = {};
  }

  applyFilter(input: FilterState): FilterState {
    this.currentFilter = { ...input };
    return this.getState();
  }

  // ====================================================================
  // FILTER LOGIC — CỐ Ý CHÈN 3 BUG ĐỂ AI PHÁT HIỆN
  //
  //   Bug 1: filter `hasPermission` bị "quên" implement → trả về full list
  //   Bug 2: filter `team` so sánh case-sensitive nhưng data trộn lẫn case
  //          (mock data ổn case, nhưng nếu user gửi lowercase sẽ miss)
  //   Bug 3: `createdAtEnd` dùng "<" thay vì "<=" → mất row đúng ngày end
  //   Bug 4: KHÔNG validate Start > End → trả về 0 row mà không báo lỗi
  // ====================================================================
  getResults(): { rows: UserRow[]; total: number } {
    let rows = [...USERS];
    const f = this.currentFilter;

    if (f.position?.length) rows = rows.filter((u) => f.position!.includes(u.position));
    if (f.statusUser?.length) rows = rows.filter((u) => f.statusUser!.includes(u.statusUser));
    if (f.gender?.length) rows = rows.filter((u) => f.gender!.includes(u.gender));

    // BUG 1: hasPermission bị bỏ quên — không filter
    // (đáng lẽ phải có: if (f.hasPermission?.length) rows = rows.filter(...))

    if (f.department?.length) rows = rows.filter((u) => f.department!.includes(u.department));

    // BUG 2: team filter strict equality nhưng so sánh case-sensitive
    if (f.team?.length) rows = rows.filter((u) => f.team!.includes(u.team));

    if (f.role?.length) rows = rows.filter((u) => f.role!.includes(u.role));
    if (f.createdBy?.length) rows = rows.filter((u) => f.createdBy!.includes(u.createdBy));

    if (f.createdAtStart) {
      const s = new Date(f.createdAtStart).getTime();
      rows = rows.filter((u) => new Date(u.createdAt).getTime() >= s);
    }
    if (f.createdAtEnd) {
      const e = new Date(f.createdAtEnd).getTime();
      // BUG 3: phải là <= nhưng đang dùng <
      rows = rows.filter((u) => new Date(u.createdAt).getTime() < e);
    }

    // BUG 4: không có validation khi start > end

    return { rows, total: rows.length };
  }

  // ====================================================================
  // VERIFICATION: so sánh kết quả thật vs kỳ vọng dựa trên filter
  // Trả về danh sách row không match filter (= AI có thể dùng để báo bug)
  // ====================================================================
  verify(): {
    matched: number;
    mismatched: Array<{ id: number; reason: string }>;
    filterApplied: FilterState;
  } {
    const { rows } = this.getResults();
    const f = this.currentFilter;
    const mismatched: Array<{ id: number; reason: string }> = [];

    for (const u of rows) {
      const reasons: string[] = [];
      if (f.position?.length && !f.position.includes(u.position))
        reasons.push(`position=${u.position} not in [${f.position.join(',')}]`);
      if (f.statusUser?.length && !f.statusUser.includes(u.statusUser))
        reasons.push(`statusUser=${u.statusUser} not in [${f.statusUser.join(',')}]`);
      if (f.gender?.length && !f.gender.includes(u.gender))
        reasons.push(`gender=${u.gender} not in [${f.gender.join(',')}]`);
      if (f.hasPermission?.length && !f.hasPermission.includes(u.hasPermission))
        reasons.push(`hasPermission=${u.hasPermission} not in [${f.hasPermission.join(',')}]`);
      if (f.department?.length && !f.department.includes(u.department))
        reasons.push(`department=${u.department} not in [${f.department.join(',')}]`);
      if (f.team?.length && !f.team.includes(u.team))
        reasons.push(`team=${u.team} not in [${f.team.join(',')}]`);
      if (f.role?.length && !f.role.includes(u.role))
        reasons.push(`role=${u.role} not in [${f.role.join(',')}]`);
      if (reasons.length) mismatched.push({ id: u.id, reason: reasons.join(' | ') });
    }

    return {
      matched: rows.length - mismatched.length,
      mismatched,
      filterApplied: this.getState(),
    };
  }

  reportBug(b: Omit<BugReport, 'id' | 'createdAt'>): BugReport {
    const bug: BugReport = {
      ...b,
      id: this.bugs.length + 1,
      createdAt: new Date().toISOString(),
    };
    this.bugs.unshift(bug);
    return bug;
  }

  getBugs(): BugReport[] {
    return [...this.bugs];
  }

  clearBugs() {
    this.bugs = [];
  }
}
