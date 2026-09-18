# 种田短剧创作 · Farming Drama Writer

**让一季收成，长成一部值得追下去的短剧。**

一个面向中文种田题材的 Codex Skill：从参考阅读、选题和长篇故事开发，到分集剧本与制作交接。适用于农家经营、年代创业、灾后安居，以及由种田小说开发的连续短剧。

它把农事、有限资源与人物选择连在一起：一袋种子可以影响生计，一张订单可以改变家人的关系，一顿好饭可以兑现观众等待了几集的愿望。

> This Chinese-first Codex skill develops original rural-life stories into serialized short-drama scripts. It supports reference analysis, story development, episode writing, continuity tracking, and production handoff. It does not generate finished videos on its own.

## 可以做什么

| 阶段 | 工作内容 | 交付示例 |
|---|---|---|
| 参考学习 | 比较阅读吸引力和短剧改编潜力，记录实际阅读范围 | 阅读笔记、推荐方向 |
| 故事开发 | 建立人物目标、经营链、阶段回报和关系变化 | 项目简报、故事设定 |
| 短剧写作 | 将事件组织为可表演的场景、动作和对白 | 季纲、完整分集剧本 |
| 连续性管理 | 跟踪农时、钱粮、人物知情范围及未回收线索 | 连续性记录 |
| 制作交接 | 整理角色、地点、道具与镜头拆分所需信息 | 分镜制作交接文件 |

```mermaid
flowchart LR
    A[参考资料与创作需求] --> B[阅读比较与选题]
    B --> C[原创故事与人物]
    C --> D[季纲与分集剧本]
    D --> E[时长与连续性检查]
    E --> F[分镜制作交接]
    E --> D
```

## 安装

本仓库根目录就是技能目录，包含 `SKILL.md`、`agents/` 和 `references/`。

1. 下载仓库 ZIP 并解压，或使用本仓库 **Code** 菜单提供的地址克隆。
2. 将解压后的整个目录命名为 `farming-drama-writer`。
3. 将它放入个人技能目录：默认是 `~/.codex/skills/`；设置了 `CODEX_HOME` 时使用 `$CODEX_HOME/skills/`。

最终目录应为：

```text
~/.codex/skills/farming-drama-writer/SKILL.md
```

已有同名技能时，先备份再更新。不要把目录重复嵌套成 `farming-drama-writer/farming-drama-writer/`。

## 如何使用

在能发现此技能的 Codex 会话中明确调用 `$farming-drama-writer`，并提供素材位置或故事需求。

**先比较参考文**

```text
用 $farming-drama-writer 阅读我指定文件夹中的种田文。
选几部做连续阅读，分别判断哪个好读、哪个适合低成本短剧，
给出有具体依据的比较，不要把抽读说成通读。
```

**开发新短剧**

```text
用 $farming-drama-writer 开发一部原创种田短剧。
架空古代，女主经营育苗生意，家人有不同主张，不要空间金手指。
暂定 40 集，每集约 90 秒，先交付季纲和前三集完整剧本。
重点场景不超过五个，感情在合作和分歧中慢慢发展。
```

**继续已有项目**

```text
用 $farming-drama-writer 读取这个项目的设定、上一集和连续性记录，
完成第 4—6 集，承接已有集尾，不修改已经确定的钱粮和人物关系。
每集都要有具体动作与对白，不能只给剧情摘要。
```

用户明确的题材、篇幅和风格优先；40 集、90 秒只是无具体要求时可修改的工作假设，不是平台规则。

## 看一个例子

[《留一袋春天》第一集示例](examples/EP001.md) 展示了如何让“留种还是还债”成为一集约 90 秒的具体场景。它是原创格式演示，不代表完整季剧本或已制作视频。

更多可直接调整的输入见 [示例提示词](examples/prompts.md)。

## 创作原则

- **生产影响剧情**：成本、农时、运输、损耗和回款会改变决定。
- **配角也有生活**：家人可以相爱却不同意，合作双方也各有底线。
- **成功有过程**：试做、交易和回款分别存在问题，不靠一个秘方解决一切。
- **慢生活也能推进**：一次分饭、一件新衣可以承接此前积累的期待。
- **长故事不等于注水**：增加有效事件与后果，不重复误会或辱骂。
- **参考不等于复制**：研究叙事机制，不搬运原著文本、特色场景或人物关系链。

## 文件结构

```text
.
├── SKILL.md                         # 技能入口与工作模式
├── agents/openai.yaml               # 技能显示信息
├── references/
│   ├── reference-study.md           # 阅读范围与比较方法
│   ├── reading-lessons.md           # 有限样本形成的阅读经验
│   ├── story-development.md         # 长篇与人物开发
│   ├── screenwriting.md             # 分集、对白与时长
│   └── production-and-qa.md         # 制作交接与验收
├── examples/                        # 原创剧本及调用示例
└── scripts/validate.py              # 结构、引用与示例检查
```

## 检查与维护

核心技能是 Markdown 指令，不需要运行 Python。只有维护者执行仓库检查时需要 Python 3.9+ 和 PyYAML：

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
```

GitHub Actions 会执行同样的检查，包括技能标识、元数据、相对引用、遗留占位符、机器专属路径，以及示例场景时长加总。这些检查不证明剧情质量、农学准确性或实际成片时长；创作仍需阅读和排练审稿。

贡献内容时，请说明解决的实际写作问题，并给出前后示例。不要提交第三方小说全文、个人创作资料库、账号凭据或包含个人路径的输出文件。

## 制作边界

本技能交付文字内容与制作资料。分镜可接环境中已有的 `create-storyboard` 技能；它是可选衔接，不是本仓库捆绑的组件。图片、配音、视频与发布需要各自的工具及明确范围。

仓库中的阅读笔记来自有限片段分析，不是全书评测。农业、食品、历史等影响剧情的重要细节仍应核验。提及的作品仅作评论对象，其原文不随本仓库分发。
