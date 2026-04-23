#!/usr/bin/env python3
"""
MyNotes Summary Generator
用于自动生成和更新MyNotes项目的summary
"""

import os
import re
import datetime
import json

class SummaryGenerator:
    def __init__(self, project_root):
        # 确保project_root是项目根目录
        self.project_root = project_root
        # SUMMARY.md应该在项目根目录
        self.summary_file = os.path.join(project_root, 'SUMMARY.md')
        self.exclude_dirs = ['.git', '.idea', '.vscode', '.github', '.trae']
        self.exclude_files = ['SUMMARY.md', '.gitignore']
        # 定义目录分类映射，用于整理和归类
        self.category_mapping = {
            # 编程语言
            'C#': 'Programming Languages',
            'C++': 'Programming Languages',
            'python': 'Programming Languages',
            'typeScript': 'Programming Languages',
            'ES6': 'Programming Languages',
            
            # 前端技术
            'Vuejs': 'Frontend',
            'react': 'Frontend',
            'CSS': 'Frontend',
            'H5&C3': 'Frontend',
            'Aurelia': 'Frontend',
            'ag-grid': 'Frontend',
            'canvas': 'Frontend',
            'svg&VML&D3&Echarts': 'Frontend',
            'D3': 'Frontend',
            'GoJS': 'Frontend',
            'ui框架': 'Frontend',
            'darkTheme': 'Frontend',
            
            # 后端技术
            'node': 'Backend',
            'koa': 'Backend',
            'ASP.Net': 'Backend',
            'asp': 'Backend',
            'sql': 'Backend',
            'mongodb': 'Backend',
            'redis': 'Backend',
            'docker': 'Backend',
            
            # 工具和框架
            'toos': 'Tools & Frameworks',
            'json-server': 'Tools & Frameworks',
            'iscroll&hammer': 'Tools & Frameworks',
            'apiCloud': 'Tools & Frameworks',
            'Less': 'Tools & Frameworks',
            'GraphQL': 'Tools & Frameworks',
            'Extension API': 'Tools & Frameworks',
            
            # AI和机器学习
            'AI': 'AI & Machine Learning',
            
            # 移动开发
            'weChat': 'Mobile Development',
            'uniapp': 'Mobile Development',
            
            # 操作系统和环境
            'Linux': 'Operating Systems',
            'Vim': 'Operating Systems',
            
            # 项目管理和架构
            'Project Management': 'Project Management',
            '架构': 'Architecture',
            
            # 学习资源
            'Books': 'Learning Resources',
            'English': 'Learning Resources',
            '慕课副业': 'Learning Resources',
            '面试积累': 'Learning Resources',
            '设计模式': 'Learning Resources',
            
            # 其他
            'movie-web': 'Other',
            'mysite': 'Other',
            'ProductApi': 'Other',
            'share': 'Other',
            'we大师课': 'Other',
            '低代码平台开发记录': 'Other',
            '红薯': 'Other',
            '按键精灵': 'Other',
            '搜索引擎小技巧': 'Other'
        }
    
    def generate_summary(self):
        """生成完整的summary"""
        # 收集所有Markdown文件
        markdown_files = self._collect_markdown_files()
        
        # 按目录组织文件
        organized_files = self._organize_by_directory(markdown_files)
        
        # 生成summary内容
        summary_content = self._generate_summary_content(organized_files)
        
        # 写入文件
        with open(self.summary_file, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        print(f"Summary generated successfully at {self.summary_file}")
        return True
    
    def _collect_markdown_files(self):
        """收集所有Markdown文件"""
        markdown_files = []
        
        for root, dirs, files in os.walk(self.project_root):
            # 排除不需要的目录
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
            
            for file in files:
                if file.endswith('.md') and file not in self.exclude_files:
                    relative_path = os.path.relpath(os.path.join(root, file), self.project_root)
                    markdown_files.append(relative_path)
        
        return markdown_files
    
    def _organize_by_directory(self, files):
        """按目录组织文件"""
        organized = {}
        
        for file_path in files:
            parts = file_path.split(os.sep)
            if len(parts) == 1:
                # 根目录文件
                if 'root' not in organized:
                    organized['root'] = []
                organized['root'].append(file_path)
            else:
                # 子目录文件
                dir_name = parts[0]
                # 根据分类映射确定类别
                category = self.category_mapping.get(dir_name, 'Other')
                
                if category not in organized:
                    organized[category] = {}
                
                if dir_name not in organized[category]:
                    organized[category][dir_name] = []
                
                organized[category][dir_name].append(file_path)
        
        return organized
    
    def _generate_summary_content(self, organized_files):
        """生成summary内容"""
        content = []
        content.append('# MyNotes Summary')
        content.append('')
        content.append(f'Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        content.append('')
        content.append('## 目录结构')
        content.append('')
        
        # 添加根目录文件
        if 'root' in organized_files:
            content.append('### 根目录')
            content.append('')
            for file in sorted(organized_files['root']):
                content.append(f'- [{os.path.basename(file)}]({file})')
            content.append('')
        
        # 添加分类和子目录文件
        for category, dirs in sorted(organized_files.items()):
            if category == 'root':
                continue
            
            content.append(f'## {category}')
            content.append('')
            
            for dir_name, files in sorted(dirs.items()):
                content.append(f'### {dir_name}')
                content.append('')
                for file in sorted(files):
                    file_name = os.path.basename(file)
                    content.append(f'- [{file_name}]({file})')
                content.append('')
        
        content.append('## 内容摘要')
        content.append('')
        
        # 为根目录文件生成摘要
        if 'root' in organized_files:
            for file in sorted(organized_files['root']):
                file_path = os.path.join(self.project_root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                    
                    # 提取标题
                    title = self._extract_title(file_content)
                    if not title:
                        title = os.path.basename(file)
                    
                    # 提取摘要
                    summary = self._extract_summary(file_content)
                    
                    content.append(f'### [{title}]({file})')
                    content.append('')
                    if summary:
                        content.append(f'> {summary}')
                        content.append('')
                except Exception as e:
                    print(f"Error processing {file}: {e}")
        
        # 为分类和子目录文件生成摘要
        for category, dirs in sorted(organized_files.items()):
            if category == 'root':
                continue
            
            content.append(f'## {category}')
            content.append('')
            
            for dir_name, files in sorted(dirs.items()):
                for file in sorted(files):
                    file_path = os.path.join(self.project_root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            file_content = f.read()
                        
                        # 提取标题
                        title = self._extract_title(file_content)
                        if not title:
                            title = os.path.basename(file)
                        
                        # 提取摘要
                        summary = self._extract_summary(file_content)
                        
                        content.append(f'### [{title}]({file})')
                        content.append('')
                        if summary:
                            content.append(f'> {summary}')
                            content.append('')
                    except Exception as e:
                        print(f"Error processing {file}: {e}")
        
        return '\n'.join(content)
    
    def _extract_title(self, content):
        """从Markdown内容中提取标题"""
        match = re.search(r'^#\s+(.*)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        return None
    
    def _extract_summary(self, content):
        """从Markdown内容中提取摘要"""
        # 移除代码块
        content = re.sub(r'```[\s\S]*?```', '', content)
        # 移除标题
        content = re.sub(r'^#\s+.*$', '', content, flags=re.MULTILINE)
        # 移除空行
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        # 取前3行作为摘要
        if lines:
            summary = ' '.join(lines[:3])
            # 限制摘要长度
            if len(summary) > 150:
                summary = summary[:150] + '...'
            return summary
        return None
    
    def check_for_updates(self):
        """检查是否需要更新summary"""
        # 检查summary文件是否存在
        if not os.path.exists(self.summary_file):
            return True
        
        # 检查文件修改时间
        summary_mtime = os.path.getmtime(self.summary_file)
        
        # 检查所有Markdown文件的修改时间
        for root, dirs, files in os.walk(self.project_root):
            dirs[:] = [d for d in dirs if d not in self.exclude_dirs]
            
            for file in files:
                if file.endswith('.md') and file not in self.exclude_files:
                    file_path = os.path.join(root, file)
                    file_mtime = os.path.getmtime(file_path)
                    if file_mtime > summary_mtime:
                        return True
        
        return False
    
    def update_summary(self):
        """更新summary"""
        if self.check_for_updates():
            return self.generate_summary()
        else:
            print("No updates needed for summary")
            return False

if __name__ == '__main__':
    # 运行示例
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 确定项目根目录（脚本所在目录的父目录的父目录）
    project_root = os.path.dirname(os.path.dirname(script_dir))
    # 确保项目根目录是MyNotes
    if os.path.basename(project_root) != 'MyNotes':
        # 如果不是，尝试找到MyNotes目录
        import glob
        mynotes_dir = glob.glob(os.path.join(os.path.dirname(project_root), 'MyNotes'))
        if mynotes_dir:
            project_root = mynotes_dir[0]
    print(f"Using project root: {project_root}")
    generator = SummaryGenerator(project_root)
    generator.generate_summary()
