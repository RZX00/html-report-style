# Output choice and controlled prose

Read this before choosing an output form or writing report body text. It maps the understanding ladder discussed in Karpathy's October 2, 2026 post to this skill. The visual contract, offline delivery and Chinese-first default stay unchanged.

## Start with the reader's task

The formats answer different questions. A later format is not automatically better.

| Reader task | Output | First thing the reader must see | Additional requirement |
| --- | --- | --- | --- |
| Get a short answer | Conversation | The answer | Create no file unless the reader needs a durable artifact |
| Review, decide, approve or keep a record | Decision brief | Conclusion, scope and decision request | Evidence must be searchable and readable with JavaScript off |
| Understand a mechanism, relationship or change | Explanation brief | Static conclusion and the question the visual answers | Add a diagram, table or sequence only when it reduces explanation cost |
| Explore cases that cannot fit in a table | Interactive explanation | Static result and representative case | Keep controls local, keyboard usable and non-essential to the conclusion |
| Learn a complex idea through pacing or narration | Media handoff | Static explanation and claims | Deliver a scene or beat list to the separate media workflow; do not pretend this skill produced the video |

Use the lowest form that lets the reader complete the task. A report may combine two forms. Put the decision brief first and the explanation layer after it. This keeps the record useful when a reader prints it, quotes it, opens it years later or blocks scripts.

## Decision brief and explanation brief

### Decision brief

Use a decision brief for a review, a plan, an incident summary, an architecture choice or a request for approval.

The first screen states four things:

1. **Conclusion:** what the report says or recommends.
2. **Scope:** which system, time range, version or audience the conclusion covers.
3. **Decision request:** what the reader must approve, reject, answer or leave unchanged.
4. **Evidence state:** which claims are facts, inferences or unknowns.

Use this order when it fits the topic:

```text
Conclusion -> scope -> decision request
Facts -> inferences -> unknowns
Options or trade-offs
Next steps and owner
Sources
```

Do not make the reader infer the decision from a long background section. Background belongs after the decision request unless it is required to understand the scope.

### Explanation brief

Use an explanation brief when the reader must form a mental model. Start with the conclusion, then name the question that the visual answers.

Every important visual has four nearby parts:

- **Question:** what should the reader learn from this visual?
- **Reading instruction:** where should the reader look, and in what order?
- **Source:** which file, measurement, commit, system or date supports it?
- **Limitation:** what the visual does not prove?

Keep a searchable table or short paragraph beside a chart. Do not make color, animation or hover state the only carrier of a claim. Mark illustrative diagrams as illustrative, and do not use them as evidence about a real system.

## Interaction and media handoff

Interaction is justified only when the reader's own input changes the answer and a table cannot list the cases. Examples include what-if inputs, filtering many rows and exploring a genuinely large map.

- Write the conclusion, key numbers and representative case in static HTML first.
- Open the interaction in the representative state.
- Keep the main cases in a table or figure beside the control.
- With JavaScript disabled, show the conclusion and the static result. Hide or disable controls that cannot work.
- Inline code and data. Add no CDN, network request, external font or analytics.
- Reuse the template's tokens and components. Support keyboard use and reduced motion.

Do not add interaction for decoration. Do not hide required prose in tabs. Do not use a slider when a table can show the three values.

Video and narrated animation are outside this skill. When a reader asks for them, create a media handoff instead of a fake implementation:

```text
Static conclusion
Audience and learning goal
Scene or beat list
Claim and source for each scene
Unknowns and required review
Static fallback for print and no-JavaScript use
```

The handoff must not claim that the separate media workflow has rendered, checked or published the media.

## Controlled prose for Chinese reports

The host project's Chinese expression standard is the language authority when one exists. This reference does not replace that standard or copy its full rule set. It tells the report writer how to apply the standard to evidence and presentation.

The report writer should:

- define a technical term at first use, then keep one name for that thing;
- lead with the conclusion and its scope;
- state who acts when the actor is known;
- give each sentence one fact, action or judgement;
- keep causal connectives when they carry the reasoning;
- remove filler, invented labels and unsupported degree words;
- distinguish facts, inferences and unknowns when the distinction affects a decision;
- use a table for exact comparison, a diagram for structure or sequence, and prose for judgement;
- use numbered imperative steps for procedures, with warnings before risky actions.

Do not turn this into a rigid style costume. Do not use fixed Chinese character counts as a rule. A long sentence is a signal to check whether it contains more than one topic. Short fragments are also a problem when they remove the actor or the logical connection.

### Evidence labels

Use labels where a reader could otherwise mistake an interpretation for an observation:

- **事实：** something read, measured, executed or cited directly. Name the source and date when they matter.
- **推断：** a judgement derived from named facts. State the basis and the confidence that the evidence supports.
- **未知：** something not established. State what would resolve it, who checks it and whether it blocks the conclusion.

Do not label every sentence mechanically. Background facts can remain ordinary prose. Label the claims that the decision depends on.

## Before and after

### Choose the output

```text
Before: 这次问题需要一个更好的输出，最好做成可交互网页，最后再考虑视频。

After: 读者需要先决定是否合并。先出一份决策稿。决策稿之后再加图，解释改动范围。只有读者必须自己改变输入时，才加交互。视频交给单独的媒体流程。
```

Why: the revised version names the reader's task and assigns each form a job. It does not treat a more elaborate artifact as automatically better.

### Separate observation from explanation

```text
Before: 这次改动明显提高了理解效率，所以应该合并。

After: 事实：PR 修改了 skill 规则、reference 和离线测试。事实：模板布局没有变化。推断：读者更容易先看到结论，再判断是否需要图或交互。这个推断还没有用使用记录验证。建议：先合并规则改动，再观察三份真实报告。
```

Why: the revised version does not present an unmeasured effect as a fact. It also gives the reader an action that follows from the evidence.

### Describe a visual

```text
Before: 下面的图说明了整个流程。

After: 问题：请求在哪个服务边界内处理？阅读顺序：先看客户端到 API 的实线箭头，再看虚线框中的职责范围。来源：架构评审提交 abc123。限制：这张图表达职责关系，不代表请求量或性能。
```

Why: the reader knows what to inspect and what not to infer.

### Keep the sentence natural

```text
Too far: 网关超时。原因未知。执行检查。检查日志。采样率低。提高采样率。

Better: 网关晚高峰超时的初始原因还不清楚。现有日志采样率只有 1%，样本不足以定位。下一步把采样率提到 10%，收集一个晚高峰的数据后再判断。
```

Why: short sentences alone are not the goal. The better version keeps the subject, reason and next action.

## Publishing checklist

- The first screen states the conclusion, scope and decision or question.
- The output form matches the reader's task.
- A decision brief comes before an explanation layer.
- Each important visual states its question, reading instruction, source and limitation.
- Interactive controls do not contain the only copy of a conclusion or key number.
- A media request has a static explanation and a handoff checklist.
- Terms are defined once and keep one name.
- Decision-relevant claims separate facts, inferences and unknowns.
- Long sentences were checked as signals, not rejected by a fixed character limit.
- Procedures use one action per numbered step, with warnings before risky actions.
- With JavaScript off, the conclusion, key numbers, tables and figures remain readable.
