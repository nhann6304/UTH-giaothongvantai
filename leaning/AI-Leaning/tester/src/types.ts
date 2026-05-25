export interface TargetConfig {
  name: string;
  baseUrl: string;
  frontendUrl: string;
  auth: {
    type: 'cookie-jwt';
    loginPath: string;
    credentialsField: { email: string; password: string };
    cookieName: string;
  };
  responseShape: {
    metadataPath: string;
    itemsPath: string;
    totalPath: string;
  };
  modules: Record<string, ModuleConfig>;
}

export interface ModuleConfig {
  label: string;
  basePath: string;
  endpoints: {
    findMulti: string;
    findOverview: string;
    findFilterOptions: string;
  };
  filterFields: FilterFieldConfig[];
  verifyRules?: {
    rowFieldMapping?: Record<string, string>;
  };
}

export interface FilterFieldConfig {
  field: string;
  type: 'MULTI' | 'DATE_RANGE' | 'SINGLE';
  source?: 'enum' | 'api';
  enum?: string;
  values?: string[];
  optionKey?: string;
}

export interface SessionContext {
  cookies: string;
  baseUrl: string;
  module?: string;
  targetName: string;
}

export interface ToolCallLog {
  name: string;
  args: any;
  result: any;
  ts: number;
}

export interface BugReport {
  id: string;
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  title: string;
  steps: string[];
  expected: string;
  actual: string;
  field?: string;
  screenshotUrl?: string;
}
