const copy = {
  zh: {
    navWork: "Projects",
    navWriting: "Writing",
    navContact: "Contact",
    heroEyebrow: "Data Science / LLM Evaluation / Agent Product",
    heroTitle: "我关心模型在真实任务中是否真的可靠",
    heroLede:
      "我用数据科学的方式观察大模型、Agent 和分析工作流：它们何时有效，何时失败，以及如何把这些判断变成可复用的产品能力。",
    chipOne: "Agent 评测",
    chipTwo: "数据工作流",
    chipThree: "AI 产品原型",
    heroPrimary: "看作品",
    heroSecondary: "读文章",
    photoCaption: "Snowboard, data, and models: all require feedback from reality.",
    statementKicker: "Positioning",
    statementTitle: "把抽象的模型能力，拆成可观察、可评估、可迭代的问题。",
    statementBody:
      "这里记录我对 Agent 产品、模型评测和数据工作流的持续观察与实践：从任务设计、错误归因，到把评测结果转化为更清晰的产品判断。",
    workKicker: "Projects",
    workTitle: "作品与实验",
    projectOneLabel: "Evaluation System",
    projectOneTitle: "数据科学 Agent 评测平台",
    projectOneBody:
      "评估模型是否能完成真实数据分析任务：理解业务问题、处理数据、编写 SQL/Python、生成洞察，并对错误进行归因。",
    projectOnePointOne: "任务完成度评分",
    projectOnePointTwo: "代码可运行性检查",
    projectOnePointThree: "结论是否被数据支持",
    projectOnePointFour: "失败原因归因报告",
    projectTwoLabel: "Writing System",
    projectTwoTitle: "大模型科普系列",
    projectTwoBody:
      "从 Transformer 原理、LLM 训练流程到大模型能力评估，把复杂概念写成更容易理解的文章和脚本。",
    projectThreeLabel: "Prototype",
    projectThreeTitle: "模型机制可视化解释器",
    projectThreeBody:
      "将论文和原理笔记转成可视化解释页面，用交互原型帮助自己把复杂模型结构讲清楚。",
    projectLink: "查看选题",
    projectLinkAlt: "查看项目",
    writingKicker: "Writing",
    writingTitle: "文章与视频选题",
    writingOneTitle: "Transformer 到底解决了什么问题？",
    writingOneBody: "从 RNN 的限制讲到 Attention 和并行训练的意义。",
    writingTwoTitle: "Attention 机制：模型如何决定该看哪里？",
    writingTwoBody: "解释 Query、Key、Value 和注意力权重的直觉。",
    writingThreeTitle: "LLM 训练过程：从数据到会对话的模型",
    writingThreeBody: "拆解预训练、指令微调、RLHF / DPO 和推理阶段。",
    writingFourTitle: "大模型能力评估：怎么判断一个模型强不强？",
    writingFourBody: "讨论 Benchmark、人类偏好、真实任务和 Agent 评估。",
    contactKicker: "Contact",
    contactTitle: "保持好奇，也保持可验证。",
    contactBody: "如果你也关注 AI 评测、Agent 产品或数据科学工作流，欢迎交流。",
  },
  en: {
    navWork: "Projects",
    navWriting: "Writing",
    navContact: "Contact",
    heroEyebrow: "Data Science / LLM Evaluation / Agent Product",
    heroTitle: "I care whether models hold up in real tasks",
    heroLede:
      "I study LLMs, agents, and analytical workflows through a data science lens: when they work, where they fail, and how those judgments can become reusable product capability.",
    chipOne: "Agent evaluation",
    chipTwo: "Data workflows",
    chipThree: "AI prototypes",
    heroPrimary: "See the work",
    heroSecondary: "Read notes",
    photoCaption: "Snowboard, data, and models: all require feedback from reality.",
    statementKicker: "Positioning",
    statementTitle: "Turning abstract model capability into observable, testable, iterative systems.",
    statementBody:
      "This site collects my notes and prototypes around agent products, model evaluation, and data workflows: from task design and failure analysis to clearer product judgment.",
    workKicker: "Projects",
    workTitle: "Work and experiments",
    projectOneLabel: "Evaluation System",
    projectOneTitle: "Data Science Agent Evaluation",
    projectOneBody:
      "A framework for testing whether models can complete realistic analytical tasks: understand the business question, process data, write SQL or Python, produce insights, and explain failures.",
    projectOnePointOne: "Task completion scoring",
    projectOnePointTwo: "Runnable code checks",
    projectOnePointThree: "Evidence-backed conclusions",
    projectOnePointFour: "Failure attribution reports",
    projectTwoLabel: "Writing System",
    projectTwoTitle: "LLM explainer series",
    projectTwoBody:
      "Notes and scripts that explain Transformer basics, LLM training, and model evaluation in plain language.",
    projectThreeLabel: "Prototype",
    projectThreeTitle: "Model mechanism visualizer",
    projectThreeBody:
      "Interactive explainers that turn papers and technical notes into visual pages for understanding complex model structures.",
    projectLink: "View topics",
    projectLinkAlt: "View project",
    writingKicker: "Writing",
    writingTitle: "Writing and video topics",
    writingOneTitle: "What problem did the Transformer actually solve?",
    writingOneBody: "From RNN limitations to attention and parallel training.",
    writingTwoTitle: "Attention: how does a model decide where to look?",
    writingTwoBody: "An intuitive explanation of Query, Key, Value, and attention weights.",
    writingThreeTitle: "How LLMs are trained: from data to dialogue",
    writingThreeBody: "Pretraining, instruction tuning, RLHF / DPO, and inference.",
    writingFourTitle: "How do we know whether a model is strong?",
    writingFourBody: "Benchmarks, human preference, real-world tasks, and agent evaluation.",
    contactKicker: "Contact",
    contactTitle: "Stay curious. Stay verifiable.",
    contactBody:
      "If you are interested in AI evaluation, agent products, or data science workflows, feel free to reach out.",
  },
};

const applyLanguage = (language) => {
  const dictionary = copy[language] || copy.zh;
  document.documentElement.lang = language === "zh" ? "zh-CN" : "en";
  document.body.dataset.lang = language;

  document.querySelectorAll("[data-i18n]").forEach((node) => {
    const key = node.dataset.i18n;
    if (dictionary[key]) {
      node.textContent = dictionary[key];
    }
  });

  document.querySelectorAll("[data-set-lang]").forEach((button) => {
    button.classList.toggle("active", button.dataset.setLang === language);
    button.setAttribute("aria-pressed", String(button.dataset.setLang === language));
  });

  localStorage.setItem("preferred-language", language);
};

document.querySelectorAll("[data-set-lang]").forEach((button) => {
  button.addEventListener("click", () => applyLanguage(button.dataset.setLang));
});

applyLanguage(localStorage.getItem("preferred-language") || "zh");
