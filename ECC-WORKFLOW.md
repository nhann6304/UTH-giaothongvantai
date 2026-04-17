# Workflow áp dụng ECC vào dự án có sẵn

## 🚀 Quick Start (5 phút)

```bash
# 1. Cài ECC vào project
cd /your/project
git clone https://github.com/affaan-m/everything-claude-code.git ecc
cd ecc && npm install && ./install.sh --profile typescript

# 2. Tạo CLAUDE.md
# Copy template từ CLAUDE-PROJECT-TEMPLATE.md

# 3. Setup rules
cp -r ecc/rules/common ~/.claude/rules/
cp -r ecc/rules/typescript ~/.claude/rules/

# 4. Test ECC
/plan "Review existing authentication system"
```

## 📋 Checklist áp dụng ECC

### Phase 1: Setup (1-2 hours)

- [ ] Clone ECC vào project
- [ ] Cài đặt dependencies
- [ ] Tạo CLAUDE.md config
- [ ] Copy rules phù hợp
- [ ] Test basic commands

### Phase 2: Audit existing code (2-4 hours)

- [ ] `/code-review` trên các file chính
- [ ] `/security-reviewer` cho auth/API
- [ ] `/typescript-reviewer` cho TypeScript files
- [ ] `/performance-optimizer` cho pages chậm
- [ ] Tạo action items list

### Phase 3: Apply improvements (1-2 weeks)

- [ ] Fix high-priority security issues
- [ ] Add TypeScript types
- [ ] Improve error handling
- [ ] Add tests cho critical functions
- [ ] Update documentation

## 🔄 Daily Workflow

### Khi làm feature mới:

```
1. /plan "Feature X implementation"
2. /tdd (nếu phức tạp)
3. Viết code
4. /typescript-reviewer
5. /security-reviewer (nếu cần)
6. /test-coverage check
7. Manual test
8. Commit
```

### Khi fix bug:

```
1. /build-error-resolver "Bug description"
2. Fix code
3. /code-review
4. Test lại
5. Commit
```

### Khi review PR:

```
1. /code-review trên changed files
2. /security-reviewer cho sensitive changes
3. /test-coverage check
4. Approve/request changes
```

## 🎯 Priority Matrix

### High Priority (Làm ngay)

- Security vulnerabilities
- Type errors
- Critical bugs
- Performance issues

### Medium Priority (Trong tuần)

- Add missing tests
- Improve error handling
- Code organization
- Documentation

### Low Priority (Khi có thời gian)

- Refactor old code
- Add new patterns
- Optimize bundle size
- Improve DX

## 📊 Measuring Success

### Metrics to track:

- **Code Quality**: Số lỗi TypeScript giảm
- **Security**: Số vulnerabilities giảm
- **Test Coverage**: Tăng từ X% → 80%+
- **Performance**: Page load time giảm
- **Developer Experience**: Time onboarding giảm

### Weekly review:

```
/learn "Review本周 improvements"
/evolve "Cluster patterns into skills"
/skill-stocktake "Audit available skills"
```

## 🛠️ Common Scenarios

### Scenario 1: Legacy TypeScript project

```
/typescript-reviewer "Review entire codebase"
/plan "Migrate to strict TypeScript"
/tdd "Add tests for critical functions"
```

### Scenario 2: React project không có types

```
/plan "Add TypeScript to React project"
/typescript-reviewer "Review component types"
/coding-standards "Set up TypeScript standards"
```

### Scenario 3: API security issues

```
/security-reviewer "Audit all API endpoints"
/plan "Implement security improvements"
/build-error-resolver "Fix security vulnerabilities"
```

### Scenario 4: Performance issues

```
/performance-optimizer "Analyze bundle size"
/plan "Implement lazy loading"
/coding-standards "Performance guidelines"
```

## 🚀 Advanced Usage

### Custom Skills cho project:

```
/skill-create "Create project-specific patterns"
/evolve "Evolve instincts into skills"
/learn "Extract patterns from codebase"
```

### Multi-team coordination:

```
/orchestrate "Coordinate frontend/backend teams"
/multi-plan "Break down large feature"
/multi-execute "Execute parallel tasks"
```

### Continuous improvement:

```
/instinct-status "Check learned patterns"
/instinct-export "Export team knowledge"
/instinct-import "Import best practices"
```

## 💡 Tips & Tricks

### Start small:

- Chọn 1-2 modules để test ECC
- Áp dụng với new code trước
- Gradually migrate old code

### Team adoption:

- Demo ECC trong team meeting
- Create team-specific CLAUDE.md
- Pair programming với ECC

### Avoid overwhelm:

- Không cần áp dụng tất cả cùng lúc
- Focus on high-impact changes
- Measure ROI của mỗi improvement

## 🔧 Troubleshooting

### Common issues:

1. **Rules không load**: Check ~/.claude/rules/ path
2. **Commands không work**: Verify plugin installation
3. **Type errors**: Check tsconfig.json setup
4. **Test failures**: Update jest configuration

### Get help:

```
/troubleshooting "ECC setup issues"
/docs-lookup "Find ECC documentation"
/learn "Extract error patterns"
```
