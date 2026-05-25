import type { BugReport, SessionContext, ToolCallLog } from './types';

export interface TargetOverride {
  target: string;
  baseUrl?: string;
  frontendUrl?: string;
  loginPath?: string;
}

interface SessionState {
  ctx: SessionContext | null;
  toolCalls: ToolCallLog[];
  bugs: BugReport[];
  baseline: { total: number } | null;
  startedAt: number;
  override: TargetOverride | null;
}

const state: SessionState = {
  ctx: null,
  toolCalls: [],
  bugs: [],
  baseline: null,
  startedAt: Date.now(),
  override: null,
};

export const session = {
  get(): SessionState {
    return state;
  },
  setCtx(ctx: SessionContext) {
    state.ctx = ctx;
  },
  pushTool(log: ToolCallLog) {
    state.toolCalls.push(log);
  },
  pushBug(bug: BugReport) {
    state.bugs.push(bug);
  },
  clearBugs() {
    state.bugs = [];
  },
  setOverride(o: TargetOverride | null) {
    state.override = o;
  },
  reset() {
    state.ctx = null;
    state.toolCalls = [];
    state.bugs = [];
    state.baseline = null;
    state.startedAt = Date.now();
    state.override = null;
  },
};
