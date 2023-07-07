# ACM-Xmake-Template

本项目是一个模版项目，适用于不同的平台，用于快速创建一个基于 [xmake](https://github.com/xmake-io/xmake) 的 C/C++ 项目，用于完成 ACM 竞赛题目的编写、测试。

## TodoLists

- [x] 基于模版创建项目
- [x] 从文件重定向输入输出流
- [x] 支持多文件测试用例
- [x] 支持多文件编译
- [ ] 支持调试功能
- [ ] 支持对拍功能
- [ ] 支持提交代码功能

## Requirements

本项目需要以下环境才能正常运行：

- C/C++编译环境，包括但不限于：gcc、clang、msvc
- [xmake](https://github.com/xmake-io/xmake)
- [xmake-vscode 插件](https://github.com/xmake-io/xmake-vscode)
- [codelldb 插件](https://github.com/vadimcn/codelldb)
- [clangd 插件](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.vscode-clangd)
- Python 运行环境，用于运行一些功能脚本，只需要包含Python标准库即可

> 注意⚠️：不要使用C/C++ vscode插件，它会给你的使用带来很大的困扰。

## Usage

### 1. 运行示例项目

项目中已经包含一个简单的示例项目：`luogu/p1001`.

```shell
➜ tree luogu/p1001
luogu/p1001
├── ans
│   ├── 1.ans
│   └── 2.ans
├── in
│   ├── 1.in
│   └── 2.in
├── out
│   ├── 1.out
│   └── 2.out
├── src
│   └── main.cpp
└── xmake.lua
```

从他的目录结构可以看出，`p1001` 是一个典型的 ACM 题目，包含了输入输出文件、源代码文件、xmake.lua 文件。

在项目根目录下，运行 `xmake` 命令，即可编译该项目。

运行 `xmake run luogu/p1001` 命令，即可运行该项目。

当然，你也可以使用`xmake-vscode`提供的可视化菜单来完成这些操作。

### 2. 创建新项目

为了方便创建新项目，避免不必要的重复劳动，本项目提供了一个xmake插件来完成这个操作。

```shell
Usage: $xmake spawn [options]

Create new projects by the template projects.
```

例如你需要创建一个新的项目，名为 `luogu/p1002`，那么你可以运行以下命令：

```shell
xmake spawn luogu/p1002
```

如果你想修改模版内容，请修改`template`目录内的内容。

### 3. 项目配置

本项目设置为C++17标准，如果你想更改，需要修改两个地方：
根目录的`xmake.lua`文件；vscode的clangd配置文件，参考配置项如下：

```json
{
    "clangd.fallbackFlags": [
        "-std=c++17",
    ]
}
```

本项目默认只从`luogu`目录中搜索子项目，如果需要其他目录，直接修改根目录的`xmake.lua`文件即可。

```lua
add_subdirs("other/*")
```

> 本项目在macOS下编写，在Windows上未经测试。
