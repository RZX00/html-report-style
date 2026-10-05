# Output ladder and controlled prose

Read this before choosing an output form or writing report body text. It refines `SKILL.md`; the visual contract, offline delivery and Chinese-first default stay unchanged.

## The ladder and this skill's rung

Andrej Karpathy's post of 2026-10-02 (https://x.com/karpathy/status/2105819303471976479) ranks formats that make model output easier to understand. Each rung is "even better" than the one before: writing in ASD-STE100, sometimes softened to "80% of the way"; diagrams; HTML web pages; bespoke explainer videos. His summary is that human work rises into oversight and understanding, and that cheap code makes "large, custom, discardable software artifacts" worth making.

| Rung | What it adds | This skill |
| --- | --- | --- |
| Controlled writing | Text that reads correctly the first time | The prose contract below, in every report |
| Diagrams | Structure at a glance | Tables, ASCII, Mermaid, SVG and plots; see `visualization-guide.md` |
| Web page | Layout, navigation, interaction | The container: one offline static report. Interaction only for a part the reader must operate |
| Explainer video | Paced, narrated explanation | Out of scope. A video skill would be separate |

This skill makes documents that people review, decide on and keep. A reviewer must find, quote and check each claim, in a review folder, a file previewer, on paper or on a phone. Static text does this best: it is searchable, quotable and printable, and it stays readable with scripts blocked or years later offline. Interaction can hide a result behind a state; video is linear and hard to cite. A report is a record to keep, not a discardable artifact. Each rung up costs more to make and to verify, so climb only when the reader's task needs it.

## Choose the output

Ask in this order:

1. Did the user name a format? Use it. Video and full web apps stay out of scope.
2. Is it an ordinary question, a status check or a yes/no answer? Reply in chat; create no file.
3. Does the reader need a conclusion, a review draft or questions to answer? Create the offline report. This is the default.
4. Must the reader operate something to understand it? Add interaction to that part of the report only, under the rules below.
5. Is it a request for an explainer video? Say it is outside this skill and offer a report with diagrams.

Do not create an HTML file when:

- A few paragraphs in chat answer the question, for example what a parameter means.
- The answer is a status, a yes/no decision or a single command.
- The user asked for Markdown, another document format or slides.
- The result needs live data, login, a server or shared editing. That is an app, not a report.
- The deliverable is a video, a narration or an animation.

### Interaction rules

Interaction is justified when the reader's own input decides the result and a table cannot list the cases: what-if inputs, filtering many rows, exploring a large map, stepping through states.

- Write the conclusion, key numbers and the representative case in static HTML first. A control explores around them; it never holds the only copy of a result.
- Pair each control with a static table or figure of the main cases, and open in the representative state.
- Without JavaScript, hide or disable the controls and keep all content visible, as the figure viewer and file explorer already do.
- Inline all code and data. Add no CDN, network request, external font or analytics.
- Reuse the template's tokens and components; add no new visual style. Support keyboard use and reduced motion.

Do not add interaction for decoration: animation, tabs that hide required text, or a slider over three values that a table shows at once.

## Controlled prose: about 80% of ASD-STE100

ASD-STE100 Simplified Technical English is a controlled language first developed for aerospace maintenance documentation. Its current edition (January 2025) has 53 writing rules and an approved English dictionary of about 900 words. Reports here are Chinese, so this skill borrows the writing rules and drops the dictionary and English grammar rules. In an English report, use STE's own word counts as the length signal. Never describe a report as STE-compliant. Paraphrases below follow public summaries such as https://en.wikipedia.org/wiki/Simplified_Technical_English; the specification is the authority.

The same rules apply to figure captions, table notes and callouts.

### Kept: the 80%

| STE rule (paraphrased) | In Chinese reports |
| --- | --- |
| One instruction per sentence | This skill extends it to every sentence: one sentence, up to 。, carries one fact, action or judgement. End it when the topic changes instead of chaining clauses with commas. Two attributes of the same subject may share a sentence. |
| At most 20 words per procedural sentence and 25 per descriptive sentence | Treat length as a signal. A statement over about 50 characters or a step over about 30, not counting code and paths, usually carries two topics. These numbers are this skill's rough conversion, not STE's. |
| One word, one meaning; technical names are allowed | Define a term at first use: the Chinese name, the code name in `code`, and one sentence of meaning if the reader may not know it. Then use only that name. Expand abbreviations at first use. Do not coin a label without defining it. |
| No noun cluster longer than three words | Keep at most two 的 in one modifier chain and at most three stacked nouns. Split the phrase into a sentence or a table, or define a term for it. |
| Active voice; do not omit parts of a sentence (verb, subject, article) to make it shorter | Name who or what acts: a role, a service, a script. Avoid 被 and subjectless sentences when the actor is known. A short sentence still keeps its subject and verb. Use the verb itself: 修改配置, not 对配置进行修改. |
| One topic per paragraph, at most six sentences | Open each paragraph with its claim, then support it. Start a new paragraph when the claim changes. |
| Procedures in the imperative; vertical lists for complex text | Number the steps. Give one action per step and put the condition first (如果……，……). |
| A warning starts with a clear command or condition, then explains the risk | Place the warning before its step: the command first, then the specific risk. |

### Facts, inferences and unknowns

This is not an STE rule. It is this skill's evidence discipline, and it depends on one-topic sentences: a sentence that mixes an observation with its explanation cannot carry one label.

- **事实**: read, measured, executed or cited directly. Give the source: file and line, log, commit, link or measurement date. State it without hedging.
- **推断**: reasoned from facts. Name the facts it rests on and how strong it is. One hedge word is enough (可能, 很可能); do not stack them.
- **未知**: not yet established. Say what would resolve it, who checks it, and whether it blocks the conclusion.

Label the claims a decision depends on: findings, causes, risks, recommendations. Background description needs no labels. Put the label at the start of a sentence or list item (事实：), in a subsection heading, or in a table column. A causal sentence may stand alone when the cause was verified, for example by reproduction. Otherwise split the observation (事实) from the explanation (推断).

### Dropped: the other 20%

- The approved dictionary. Use normal Chinese and the project's own terms.
- English-only grammar rules: verb forms, -ing words, article use, contractions.
- Hard length limits in descriptive text. Length stays a signal.
- STE's punctuation rules. Use standard Chinese punctuation; a chain of semicolons is usually several sentences, so split it.

### When to move closer to STE

Tighten toward full STE for runbooks and operation steps (deploy, migrate, roll back, recover), warnings before destructive or irreversible actions, checklists used for audit, and text that will be machine-translated or read by non-native readers. There, treat the length signals as limits and write every instruction in the imperative.

### Too far

Chasing short sentences alone produces telegraphic text: fragments, dropped subjects, missing connectives. STE itself forbids omitting parts of a sentence to make it shorter. Over-strict use also turns an explanation into a checklist: every sentence a command, numbered lists used for an argument, the same sentence frame repeated. Keep connectives such as 因为, 所以 and 但 when they carry the logic. Also remove phrases that carry no information, such as 值得注意的是 and 综上所述.

## Before and after

The examples are fictional and only show the writing.

**One topic per sentence**

> Before: 迁移脚本在预发环境执行成功，但由于生产库数据量大约是预发的四十倍并且存在历史遗留的空值，所以预计执行时间会明显变长，需要提前和 DBA 确认维护窗口。
>
> After: 迁移脚本已在预发环境执行成功。生产库数据量约为预发的 40 倍，并有历史遗留的空值。推断：生产执行时间会明显更长。发布前，发布负责人需与 DBA 确认维护窗口。

**Define the term, then keep it**

> Before: 本次改造主要涉及入口层。网关收到请求后先查限流配置，GW 侧命中规则就直接拒绝，接入层日志里能看到记录。
>
> After: 本文的“网关”指 `api-gateway` 服务，它接收所有外部请求。网关收到请求后先查限流配置。请求命中限流规则时，网关直接拒绝，并写一条拒绝日志。

**Conclusion first; facts, inferences and unknowns apart**

> Before: 我们对最近一周的超时问题做了比较全面的排查，从日志看晚高峰超时明显偏多，重试没有退避应该是放大了问题，另外采样率低也影响了判断，综上所述建议先改重试策略。
>
> After:
>
> 结论：先给网关重试加退避，暂不扩容。
>
> - 事实：9 月 28 日至 10 月 4 日，晚高峰超时率约 2%，其他时段低于 0.1%。来源：网关访问日志。
> - 事实：重试配置为失败后立即重试 3 次，没有退避。来源：`gateway.yaml` 的 `retry` 段。
> - 推断：立即重试会在高峰期叠加请求，很可能放大了超时。依据是上面两条事实，尚未压测验证。
> - 未知：超时的初始原因还没有确认。日志采样率只有 1%，提高到 10% 后复核。这一项不影响先加退避。

**Closer to STE: a procedure**

> Before: 回滚的时候要先确认一下当前版本号，然后把流量切走，等没有请求了以后执行回滚脚本，最好再看一眼监控有没有恢复。
>
> After:
>
> 警告：先切走流量，再执行回滚。回滚会中断进行中的写请求。
>
> 1. 记下当前版本号（`deploy status` 的输出）。
> 2. 把流量切到备用集群。
> 3. 等待活跃连接数降到 0。
> 4. 运行 `deploy rollback --to <版本号>`。
> 5. 观察错误率 5 分钟。
> 6. 如果错误率没有回到基线，通知值班负责人。

**Too far, then 80%**

> Too far: 网关超时。原因未知。执行检查。检查日志。采样率低。提高采样率。
>
> 80%: 网关晚高峰超时的初始原因还不清楚。现有日志采样率只有 1%，样本不足以定位。下一步把采样率提到 10%，收集一个晚高峰的数据后再判断。

## Check before publishing

- The first screen states the conclusion, its scope, and what the reader must decide or answer.
- Each section and paragraph opens with its claim.
- No sentence carries two topics; long sentences were checked.
- Each term is defined at first use and keeps one name.
- Claims that a decision depends on are labelled 事实, 推断 or 未知, with a source, a basis or the next check.
- Steps are numbered imperatives with one action each; warnings come before their steps.
- With JavaScript off, every conclusion and key number is still readable.
