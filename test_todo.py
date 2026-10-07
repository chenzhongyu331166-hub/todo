import unittest
from todo import add, done, del_tasks, list_tasks

class TestTodo(unittest.TestCase):
    def test_add_normal(self):
        """测试：正常新增一条任务"""
        tasks = []
        res_tasks, ok, msg = add(tasks.copy(), "买牛奶")
        self.assertEqual(len(res_tasks), 1)
        self.assertEqual(res_tasks[0]["text"], "买牛奶")

    def test_done_normal(self):
        """测试：正常把任务标记为完成"""
        tasks = [{"id": 1, "text": "看书", "done": False}]
        res_tasks, ok, msg = done(tasks.copy(), 1)
        self.assertEqual(res_tasks[0]["done"], True)

    def test_done_not_found(self):
        """测试done：任务ID不存在，返回失败"""
        tasks = [{"id": 1, "text": "看书", "done": False}]
        res_tasks, ok, msg = done(tasks.copy(), 999)
        self.assertFalse(ok)
        self.assertEqual(len(res_tasks), 1)

    def test_del_normal(self):
        """测试：正常删除任务"""
        tasks = [{"id":1,"text":"看书","done":False},{"id":2,"text":"喝水","done":False}]
        res_tasks, ok, msg = del_tasks(tasks.copy(),1)
        self.assertEqual(len(res_tasks), 1)
        self.assertEqual(res_tasks[0]["id"],2)

    def test_del_not_found(self):
        """测试del：删除不存在id，返回失败"""
        tasks = [{"id": 1, "text": "看书", "done": False}]
        res_tasks, ok, msg = del_tasks(tasks.copy(), 888)
        self.assertFalse(ok)
        self.assertEqual(len(res_tasks),1)

def test_list_tasks(self):
    """测试list_tasks：原样返回任务，不修改数据"""
    input_tasks = [
        {"id":1,"text":"看书","done":False},
        {"id":2,"text":"喝水","done":True}
    ]
    res_tasks, ok, msg = list_tasks(input_tasks.copy())
    #断言操作成功
    self.assertTrue(ok)
    #返回的列表长度要和输入一模一样
    self.assertEqual(len(res_tasks), len(input_tasks))
    #逐条校验，数据完全没有改动
    self.assertEqual(res_tasks[0]["id"],1)
    self.assertEqual(res_tasks[0]["text"],"看书")
    self.assertEqual(res_tasks[0]["done"],False)
    self.assertEqual(res_tasks[1]["id"],2)
    self.assertEqual(res_tasks[1]["text"],"喝水")
    self.assertEqual(res_tasks[1]["done"],True)
import os
from utils import load, save

def test_save_load_io(self):
    temp_file = "_tmp_test.json"
    sample_data = [{"id": 1, "text": "IO测试任务", "done": False}]

    #写入临时文件
    save(sample_data, temp_file)
    #从临时文件读回
    result = load(temp_file)

    self.assertEqual(len(result), 1)
    self.assertEqual(result[0]["text"], "IO测试任务")

    #测试结束，把临时文件删掉，不留垃圾文件
    if os.path.exists(temp_file):
        os.remove(temp_file)


if __name__ == '__main__':
    unittest.main()
