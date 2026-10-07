"""工具函数：存盘和读盘"""
import json



def load(filename="todos.json"):
    try:
        with open(filename, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save(tasks, filename="todos.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


