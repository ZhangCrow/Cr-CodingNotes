# Cr Git Commit Message Standards
## 修改自-原爱学iOS开发团队 Git 提交信息规范

> The Latest Edited Date: 2019/04/03 16:30
> 共同维护，探索最适用的提交规范。
> 参考链接：[知乎-Git commit message 规范](https://zhuanlan.zhihu.com/p/69989048)

[TOC]

### 规范细则
概览形式如下：
```
<type>(<scope>): <subject>
// 空行
<body>
// 空行
<footer>
```
Header是必需的，Body和Footer可以省略，Header不应超过50字符，Body和Footer每行都不应超过80字符。

#### Header
Header只有一行，包含三个字段，type（必须）、scope（可选）和subject（必须）
```
<type>(<scope>): <subject>
// 注: “:”为半角冒号，冒号后面有空格，“()”也应该是半角括号。
```
**另 在爱学项目中，因工程结构特殊，使用下面的提交格式**
```
<type>(scope)(subScope): <subject>

// Eg:🌰
update: (教师端)(积分)接口和模型调整
update: (家长端)(我的/我的孩子)人脸识别对接
update: (通知、任务、调查)列表、详情页删除
update: (BBKit)(TIM)登录调优
update: (ComKit)(TableVc基类)新增自动分割线

```

##### type
type用于说明commit的类别，约定只使用以下标识：

| 标识 | 场景 | 备注 | 
| :--- | :--------------- | :---: |
| feat | 新增模块/业务/逻辑/工程文件 | feature | 
| update | 已有业务/逻辑 需求变更或更新 | - | 
| fix | 修复bug | - | 
| track | 工程埋点的增/删/改 | - | 
| style | 导航/类名改动，代码空格/缩进/pragmaMark等改动（不影响代码运行的改动） | - | 
| docs | 文档的增/删/改 | documentation | 
| chore | 构建过程或辅助工具的变动 | - | 
| refactor | 新重构（即不是新增功能，也不是修改bug的代码变动） | - | 

有一种特殊情况，如果当前commit用于撤销以前的commit，则必须以`revert`开头，后面跟着被撤销的Commit的Header
```
revert: feat(pencil): add 'graphiteWidth' option
This reverts commit 667ecc1654a317a13331b17617d973392f415f02.
```

- - -
Q&A:
Q: Podfile的改动应该用什么标签？
A: chore

Q: 需求上的纯文案改动应该用什么标签？
A: update？ style？ 争议中待定...
- - -

##### scope
用于说明commit影响的范围，比如数据层、控制层、视图层等，视项目不同而不同

##### subject
是commit的简短描述，不超过50字符
Eg:
```
fix(login): array parsing issue when multiple spaces were contained in string.
```
* 义动词开头，使用第一人称现在时（change，而不是changed）
* 第一个字母小写
* 结尾不加句号(.)

* 若提交多模块或多业务相似正删改时，表述中中文语境统一使用“、”，英文语境统一使用“, ”（半角逗号后有空格）

#### Body
是对本次commit的详细描述，可以分成多行：
```
More detailed explanatory text, if necessary.  Wrap it to 
about 72 characters or so. 

Further paragraphs come after blank lines.

- Bullet points are okay, too
- Use a hanging indent
```
有两个注意点： 
1. 使用第一人称现在时 
2. 说明代码变动的动机，以及与以前行为的对比

#### Footer
只适用于两种情况

1. 不兼容变动
如果当前代码与上一个版本不兼容，则Footer部分以BREAKING CHANGE开头，后面是变动的描述以及变动理由和迁移方法

```
BREAKING CHANGE: isolate scope bindings definition has changed.

To migrate the code follow the example below:

Before:

scope: {
myAttr: 'attribute',
}

After:

scope: {
myAttr: '@',
}

The removed `inject` wasn't generaly useful for directives so there should be no code using it.
```

2. 关闭Issue
如果当前commit针对某个issue，那么可以在Footer部分关闭这个issue
```
Closes #123, #245, #992
```


