#!/usr/bin/env python3
"""
MyNotes Summary Watcher
用于监控Markdown文件变化并自动更新summary
"""

import os
import time
import subprocess
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MarkdownChangeHandler(FileSystemEventHandler):
    def __init__(self, summary_generator_script):
        self.summary_generator_script = summary_generator_script
        self.last_update = 0
        self.update_interval = 2  # 避免频繁更新，设置2秒间隔
    
    def on_modified(self, event):
        """当文件被修改时触发"""
        if not event.is_directory and event.src_path.endswith('.md'):
            self._trigger_update()
    
    def on_created(self, event):
        """当文件被创建时触发"""
        if not event.is_directory and event.src_path.endswith('.md'):
            self._trigger_update()
    
    def on_deleted(self, event):
        """当文件被删除时触发"""
        if not event.is_directory and event.src_path.endswith('.md'):
            self._trigger_update()
    
    def _trigger_update(self):
        """触发summary更新"""
        current_time = time.time()
        if current_time - self.last_update > self.update_interval:
            print("Detected changes, updating summary...")
            try:
                subprocess.run([sys.executable, self.summary_generator_script], 
                             check=True, capture_output=True, text=True)
                print("Summary updated successfully")
            except subprocess.CalledProcessError as e:
                print(f"Error updating summary: {e}")
                print(f"Error output: {e.stderr}")
            self.last_update = current_time

def main():
    """主函数"""
    project_root = os.path.dirname(os.path.abspath(__file__))
    summary_generator_script = os.path.join(project_root, 'summary_generator.py')
    
    # 检查summary_generator.py是否存在
    if not os.path.exists(summary_generator_script):
        print(f"Error: {summary_generator_script} not found")
        return 1
    
    # 初始化事件处理器
    event_handler = MarkdownChangeHandler(summary_generator_script)
    
    # 初始化观察者
    observer = Observer()
    
    # 监控项目根目录
    observer.schedule(event_handler, project_root, recursive=True)
    
    # 启动观察者
    observer.start()
    print(f"Watching for changes in {project_root}...")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
    return 0

if __name__ == '__main__':
    sys.exit(main())
