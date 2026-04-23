# MyNotes Summary Generator Tool

## 功能介绍

这是一个为MyNotes项目设计的自动summary生成工具，主要功能包括：

- **自动扫描**：扫描项目中的所有Markdown文件
- **按目录组织**：将文件按目录结构组织，生成清晰的目录树
- **自动更新**：通过Git pre-commit钩子，在每次提交时自动更新summary
- **时间戳**：在summary中包含生成时间，方便追踪更新

## 工具组成

1. **Generate-Summary.ps1** - 核心脚本，用于生成SUMMARY.md文件
2. **.git/hooks/pre-commit** - Git钩子，在提交时自动运行summary生成脚本

## 使用方法

### 手动生成Summary

在项目根目录运行以下命令：

```powershell
# Windows PowerShell
.enerate-Summary.ps1

# 或使用完整路径
powershell -ExecutionPolicy Bypass -File "D:\github\MyNotes\Generate-Summary.ps1"
```

### 自动更新（推荐）

Git pre-commit钩子已配置，当你执行`git commit`时，会自动：

1. 运行summary生成脚本
2. 如果SUMMARY.md有变化，将其添加到当前提交
3. 完成提交操作

### 查看生成的Summary

生成的SUMMARY.md文件位于项目根目录，包含：

- 生成时间
- 按目录组织的Markdown文件列表
- 每个文件的相对路径和链接

## 技术实现

### 工作原理

1. **文件扫描**：使用PowerShell的Get-ChildItem命令递归扫描项目目录
2. **文件过滤**：排除.git、.idea、.vscode等目录和非Markdown文件
3. **目录组织**：将文件按目录结构分组
4. **内容生成**：生成包含目录结构的Markdown格式内容
5. **文件写入**：将生成的内容写入SUMMARY.md文件

### 性能优化

- **按需更新**：Git钩子会在提交时检查是否需要更新
- **快速扫描**：使用PowerShell的高效文件系统操作
- **最小化输出**：只生成必要的目录结构，避免冗余信息

## 自定义配置

### 修改排除目录

编辑`Generate-Summary.ps1`文件中的`$ExcludeDirs`数组，添加或移除需要排除的目录：

```powershell
$ExcludeDirs = @(".git", ".idea", ".vscode")
```

### 修改排除文件

编辑`Generate-Summary.ps1`文件中的文件过滤逻辑，添加或移除需要排除的文件：

```powershell
if ($_.Extension -eq ".md" -and $_.Name -ne "SUMMARY.md" -and $_.Name -ne ".gitignore") {
    # 处理文件
}
```

## 常见问题

### 脚本无法运行

**问题**：PowerShell执行策略限制

**解决方法**：使用`-ExecutionPolicy Bypass`参数运行脚本：

```powershell
powershell -ExecutionPolicy Bypass -File "Generate-Summary.ps1"
```

### Git钩子不生效

**问题**：pre-commit钩子没有执行

**解决方法**：

1. 确保钩子文件有执行权限
2. 检查钩子文件路径是否正确：`.git/hooks/pre-commit`
3. 手动运行钩子测试：
   ```bash
   cd .git/hooks && ./pre-commit
   ```

### SUMMARY.md不更新

**问题**：运行脚本后SUMMARY.md没有更新

**解决方法**：

1. 检查是否有新的Markdown文件添加
2. 检查文件路径是否包含特殊字符
3. 查看脚本运行输出，是否有错误信息

## 注意事项

1. **文件编码**：确保Markdown文件使用UTF-8编码
2. **路径长度**：Windows系统下路径长度可能有限制，过长的路径可能导致脚本执行失败
3. **性能**：对于非常大的项目，扫描和生成过程可能需要较长时间

## 示例输出

生成的SUMMARY.md文件示例：

```markdown
# MyNotes Summary

Generated on: 2026-04-23 23:15:38

## Directory Structure

### Root Directory

- [interview.md](interview.md)
- [interviewQuestion.md](interviewQuestion.md)
- [plan.md](plan.md)

### Vuejs

- [readme.md](Vuejs/readme.md)
- [vue3.md](Vuejs/vue3.md)
- [vue-cli.md](Vuejs/vue-cli.md)

...
```

## 未来改进

- 添加内容摘要功能，提取每个Markdown文件的主要内容
- 支持自定义summary格式和样式
- 添加文件变化监控，实时更新summary
- 支持更多文件类型的处理

---

**作者**：AI Assistant
**版本**：1.0
**日期**：2026-04-23
