# homework

此目录包含一个用于计算斐波那契数列的简单 Python 实现与测试。

文件说明：
- `fibonacci.py`：实现了三种计算斐波那契数的方法（迭代、朴素递归、记忆化递归），以及生成器和命令行入口。

快速使用（PowerShell）：

```powershell
# 计算 fib(10) 使用默认的迭代方法
python .\fibonacci.py 10

# 使用记忆化方法
python .\fibonacci.py 30 -m memo

# 使用朴素递归（仅限小 n）
python .\fibonacci.py 10 -m rec
```

运行单元测试：

```powershell
python -m unittest discover -v
```

说明：如果想把 `fibonacci.py` 放到其他位置，请确保当前工作目录或 Python 路径包含该文件。
123软件
