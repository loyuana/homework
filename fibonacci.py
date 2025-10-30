"""斐波那契数列计算模块。

提供三种计算单个斐波那契数的方法：
- fib_iterative(n): 迭代法（推荐，时间复杂度 O(n)）
- fib_recursive(n): 朴素递归（仅用于教学，指数时间）
- fib_memo(n): 带缓存的递归（动态规划/记忆化）

还提供 fib_sequence(n) 生成器来按序产生前 n 项。
"""
from typing import Iterator, List, Optional


def _validate_n(n: int) -> None:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")


def fib_iterative(n: int) -> int:
    """使用迭代法返回第 n 个斐波那契数，fib(0) = 0, fib(1) = 1."""
    _validate_n(n)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_recursive(n: int) -> int:
    """朴素递归（指数时间），仅用于教学和小 n 的对比测试。"""
    _validate_n(n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memo(n: int, _cache: Optional[dict] = None) -> int:
    """带缓存的递归，时间复杂度 O(n)。

    参数 _cache 为内部使用，外部调用无需传入。
    """
    _validate_n(n)
    if _cache is None:
        _cache = {0: 0, 1: 1}
    if n in _cache:
        return _cache[n]
    _cache[n] = fib_memo(n - 1, _cache) + fib_memo(n - 2, _cache)
    return _cache[n]


def fib_sequence(n: int) -> Iterator[int]:
    """生成前 n 项斐波那契数（长度为 n），按序产出 fib(0), fib(1), ..."""
    _validate_n(n)
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


__all__ = [
    "fib_iterative",
    "fib_recursive",
    "fib_memo",
    "fib_sequence",
]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="计算第 n 个斐波那契数（fib(0)=0）")
    parser.add_argument("n", type=int, help="要计算的 n（非负整数）")
    parser.add_argument(
        "-m",
        "--method",
        choices=("iter", "rec", "memo"),
        default="iter",
        help="计算方法：iter(迭代)、rec(递归)、memo(记忆化递归)，默认 iter",
    )

    args = parser.parse_args()
    n = args.n
    method = args.method

    if method == "iter":
        res = fib_iterative(n)
    elif method == "rec":
        res = fib_recursive(n)
    else:
        res = fib_memo(n)

    print(res)
