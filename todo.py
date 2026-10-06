# ▶ 题hw课后作业（Todo命令行工具）
# 要求：完整实现：todo.py 支持 add/done/del/list/自动存档，目标80行以上。自己敲，卡住先想10分钟再问AI。完成后传GitHub(D15正式教git，今天先用AI给的三条命令)。
# 期望：python todo.py add 学Python 后 list 显示 [ ] 1. 学Python
# 作业代码写在这行下面，写完点【交给AI老师批改】
import sys
from utils import load, save



def add(tasks, text):
    new_id=max((t['id'] for t in tasks),default=0 )+1
    tasks.append({"id": new_id, "text": text, "done": False})
    return (tasks,True,"任务已添加")

def done(tasks, tid):
    for t in tasks:
        if t["id"] == tid:
            if t["done"]==False:
                t["done"] = True
                return (tasks,True,"任务已标记完成")
            else:
                return (tasks,True,"提示：该任务已经处于完成状态，无需重复操作")
        
    return (tasks,False,"找不到此ID！")

def del_tasks(tasks, tid):
    new_tasks=[]
    found=False
    for t in tasks:
        if t["id"] != tid:
            new_tasks.append(t)
        else:
            found=True
    
    if found:
        return (new_tasks,True,"已删除此任务！")
    else:
        return (new_tasks,False,"找不到此ID！")
        


def list_tasks(tasks):
    return (tasks,True,"已列出任务")

def main():
    tasks=load()
    args=sys.argv
    if len(args)<2:
        print("用法示例：python todo.py add 任务内容")
        return
    op=args[1]
    if op=='add':

        if len(args)<3:
            print("缺少参数！示例：python todo.py add 任务内容")
            return
        text=" ".join(args[2:])
        tasks,ok,msg=add(tasks,text)
        print(msg)
        save(tasks)
    elif op=='done':
        if len(args)<3:
            print("缺少参数！示例：python todo.py add 任务内容")
            return
        tid=int(args[2])
        tasks,ok,msg=done(tasks, tid)
        print(msg)
        save(tasks)
    elif op=='del':
        if len(args)<3:
            print("缺少参数！示例：python todo.py add 任务内容")
            return
        tid=int(args[2])
        tasks,ok,msg=del_tasks(tasks, tid)
        print(msg)
        save(tasks)
    elif op=='list':
        tasks,ok,msg=list_tasks(tasks)
        print(msg)
        save(tasks)
        for t in tasks:
           if t["done"]==True:
               mark="[√]"
           else:
               mark="[x]"
           print(f"{mark} {t['id']}.{t['text']}")

if __name__=="__main__":
    main()



        
    

# ▶ END






