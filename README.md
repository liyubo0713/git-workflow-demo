# Git Workflow Demo

用于练习 Git 远程仓库、分支、Pull Request、代码评审和合并流程的小项目。

## 参与角色

- A（仓库所有者、评审者）：liyubo0713
- B（贡献者）：Rhys-Maya
- 本项目由一人使用两个账号完成。

## 当前功能

- 加法：`add(a, b)`
- 减法：`subtract(a, b)`
- 除法：`divide(a, b)`

## 运行方式

需要 Python 3，无需安装第三方依赖。

```powershell
python calculator.py
```

预期输出：

```text
2 + 3 = 5
5 - 3 = 2
6 / 2 = 3.0
```

## 除法的异常行为

`divide(a, b)` 支持正数和负数除法。除数 `b` 为 `0` 时，函数会抛出
Python 的 `ZeroDivisionError`，由调用方根据需要捕获处理。

## 运行测试

在项目根目录执行：

```powershell
python -m unittest -v
```

测试使用 Python 标准库 `unittest`，无需安装第三方依赖。
三个测试分别覆盖正常除法、负数除法，以及除数为 `0` 时抛出
`ZeroDivisionError` 的行为。测试通过时，末尾显示 `Ran 3 tests` 和 `OK`。
