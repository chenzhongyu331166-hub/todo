import json
import sys
import sys
from utils import load_tasks, save_tasks

def main():
    tasks = load_tasks()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"

    if cmd == "add":
        text = sys.argv[2]
        tasks.append({"text": text, "done": False})
        save_tasks(tasks)
        print("已添加:", text)
    elif cmd == "list":
        if not tasks:
            print("还没有任务")
        for i, t in enumerate(tasks, 1):
            mark = "x" if t["done"] else " "
            print(f"[{mark}] {i}. {t['text']}")

if __name__ == "__main__":
    main()