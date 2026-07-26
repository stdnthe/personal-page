#!/usr/bin/env python3
"""
Burn the English i18n dictionary directly into every HTML file,
then strip out the data-i18n attributes and site.js script tag.
"""

import re
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EN = {
    "navWork": "Project",
    "navWriting": "Blogs",
    "heroEyebrow": "Growth Analytics / AI Product Analytics / LLM Evaluation",
    "heroTitle": "About Me",
    "heroLede": "I'm Jiaqi He, an AI Product Data Scientist focused on LLM Evaluation, Agent Products, and Growth Analytics. I have also completed the Certificate in Quantitative Finance (CQF), which strengthened my foundation in quantitative modeling, machine learning, and financial applications.",
    "skillsKicker": "Core Skills",
    "homeBioOne": "I focus on turning growth, product, and business questions into verifiable data judgment, then shaping that judgment into more reliable AI analytics products.",
    "homeBioTwo": "My interests sit across Growth Analytics, AI Product Analytics, and LLM Evaluation: not just whether a model is capable, but whether it creates stable value in real tasks.",
    "backgroundKicker": "Personal Background",
    "aboutDetailTitle": "Work, education, and CQF",
    "backgroundOneLabel": "Industry",
    "backgroundOneTitle": "AI Data Analyst",
    "backgroundOneBody": "Currently working as an AI Data Analyst, with focus areas including Large Language Models, AI Evals, and data analysis for real business and product decisions.",
    "backgroundTwoLabel": "Education",
    "backgroundTwoTitle": "China University of Mining and Technology, Beijing",
    "backgroundTwoBody": "Bachelor of Engineering in Data Science, with hands-on foundations in SQL, Python, machine learning, and applied data analysis.",
    "backgroundThreeLabel": "Quant Finance",
    "backgroundThreeTitle": "CQF / Quantitative Finance",
    "backgroundThreeBody": "Completed the Certificate in Quantitative Finance, strengthening practical understanding of quantitative modeling, risk management, machine learning, and deep reinforcement learning.",
    "homeSelectedBlogsTitle": "Blogs",
    "homeSelectedBlogsIntro": "I often share my experience building AI products. Below is a selection of my long-form writing.",
    "postSixDate": "2026-06",
    "writingSixTitle": "Growth Data Agent Product Design",
    "postSixTopic": "Data Agent",
    "postFiveDate": "2026-05",
    "writingFiveTitle": "How do we know whether a model is strong?",
    "postFiveTopic": "LLM Evaluation",
    "postFourDate": "2026-05",
    "writingFourTitle": "How LLMs are trained: from data to dialogue",
    "postFourTopic": "LLM Training",
    "postThreeDate": "2026-05",
    "writingThreeTitle": "Transformer Block: the building block of LLMs",
    "postThreeTopic": "Transformer",
    "postTwoDate": "2026-05",
    "writingTwoTitle": "Attention: how does a model decide where to look?",
    "postTwoTopic": "Transformer",
    "postOneDate": "2026-05",
    "writingOneTitle": "What problem did the Transformer actually solve?",
    "postOneTopic": "Transformer",
    "contactTitle": "Follow Me",
    "contactBody": "If you are interested in AI evaluation, agent products, or data science workflows, feel free to reach out.",
    # blogs.html
    "writingKicker": "Blogs",
    "writingTitle": "Featured Blogs",
    "blogsIntro": "Notes and article series on AI evaluation, data products, and LLM fundamentals.",
    "seriesHomeKicker": "Blog Series",
    "seriesHomeTitle": "Start with these series",
    "seriesOneLabel": "Series 01",
    "seriesOneTitle": "LLM Explainer Series",
    "seriesOneBody": "A learning path from Transformers and attention to training and evaluation.",
    "seriesTwoLabel": "Coming next",
    "seriesTwoTitle": "AI Evals Notes",
    "seriesTwoBody": "Notes on task design, model evaluation, failure attribution, and real-world validation.",
    "seriesThreeLabel": "Product Doc",
    "seriesThreeTitle": "Data Product Practice",
    "seriesThreeBody": "Product-minded design notes on analytics, growth questions, and AI workflows.",
    "recentPostsTitle": "Recent / Featured Posts",
    # projects.html
    "workKicker": "Projects",
    "workTitle": "Selected Projects",
    "projectsIntro": "Selected projects around analytics, model evaluation, and visual explainers.",
    "projectFourLabel": "Data Product",
    "projectFourTitle": "Growth Data Agent Product Design",
    "projectFourBody": "A product design note for a growth analytics agent, covering business questions, data foundations, agent workflows, AI evals, and rollout planning.",
    "projectDocLink": "View doc",
    "projectOneLabel": "Evaluation System",
    "projectOneTitle": "Data Science Agent Evaluation",
    "projectOneBody": "A framework for testing whether models can complete realistic analytical tasks: understand the business question, process data, write SQL or Python, produce insights, and explain failures.",
    "projectOneStatus": "Building",
    "projectThreeLabel": "Prototype",
    "projectThreeTitle": "Model mechanism visualizer",
    "projectThreeBody": "Interactive explainers that turn papers and technical notes into visual pages for understanding complex model structures.",
    "projectThreeStatus": "Prototype",
    "projectTwoLabel": "Writing System",
    "projectTwoTitle": "LLM explainer series",
    "projectTwoBody": "Plain-language notes that explain Transformer basics, LLM training, and model evaluation.",
    "projectLink": "View series",
    # articles/index.html
    "seriesKicker": "LLM Explainer Series",
    "seriesTitle": "LLM Explainer Series",
    "seriesIntro": "A plain-language series unpacking why modern models use Transformers, what attention does, how LLMs are trained, and how we should evaluate them.",
    "seriesNoteTitle": "Suggested order",
    "seriesNoteBody": "Start with model structure, move into training, then finish with evaluation. Each article can stand alone or become a draft for future notes.",
    "seriesPhaseOne": "Phase 1 · Transformer fundamentals",
    "articleOneTitle": "What problem did the Transformer actually solve?",
    "articleOneBody": "From the sequential limits of RNNs to attention and parallel training.",
    "readTimeSix": "6 min read",
    "articleTwoTitle": "Attention: how does a model decide where to look?",
    "articleTwoBody": "An intuitive explanation of Query, Key, Value, and attention weights.",
    "readTimeSeven": "7 min read",
    "articleThreeTitle": "Transformer Block: the building block of LLMs",
    "articleThreeBody": "Multi-Head Attention, FFN, residual connections, and LayerNorm — what each component actually does.",
    "readTimeTen": "10 min read",
    "seriesPhaseTwo": "Phase 2 · LLM training",
    "articleFourTitle": "How LLMs are trained: from data to dialogue",
    "articleFourBody": "Pretraining, instruction tuning, preference alignment, and what each stage is for.",
    "readTimeEight": "8 min read",
    "seriesPhaseThree": "Phase 3 · Model evaluation",
    "articleFiveTitle": "How do we know whether a model is strong?",
    "articleFiveBody": "A map of benchmarks, human preference, real tasks, and agent evaluation.",
    # article pages - series progress
    "progressOne": "Article 1 / 5",
    "progressTwo": "Article 2 / 5",
    "progressThree": "Article 3 / 5",
    "progressFour": "Article 4 / 5",
    "progressFive": "Article 5 / 5",
    "readEstimateSix": "6 min read",
    "readEstimateSeven": "7 min read",
    "readEstimateEight": "8 min read",
    "readEstimateTen": "10 min read",
    # article nav
    "navBackSeries": "Back to series",
    "navPrevious": "Previous",
    "navNext": "Next",
    # transformer.html article body
    "transformerSummary": "The Transformer was not just a way to make models smarter. It made long-range relationships in text much easier to model efficiently.",
    # attention.html article body
    "attentionSummary": "Attention is a kind of relevance search: the current token asks a question, other tokens offer clues, and the model decides what to reference.",
    "attentionIntro": "When a model reads a sentence, each word should not be understood in isolation. If a sentence says ‘it works well,’ the model needs earlier context to know what ‘it’ refers to. Attention performs that search.",
    "attentionNodeOneBody": "The current token asks: what information do I need right now?",
    "attentionNodeTwoBody": "Other tokens provide an index: what clues do I contain?",
    "attentionNodeThreeBody": "The actual information passed along when a token is judged relevant.",
    "attentionHeadingOne": "What are attention weights?",
    "attentionBodyOne": "The model compares the Query with each Key. The better they match, the higher the weight; the higher the weight, the more that Value influences the current representation.",
    "attentionBodyTwo": "These relationships are not hand-written rules. They are learned from large amounts of text, where the model discovers which words tend to explain, limit, or complete each other.",
    "attentionHeadingTwo": "Why use multiple heads?",
    "attentionBodyThree": "A sentence can contain many relationships at once: subject-verb links, references, time, cause and effect. Multi-head attention lets the model inspect the same sentence from several angles.",
    "attentionHeadingThree": "One-sentence takeaway",
    "attentionBodyFour": "Attention lets a model do more than read in order. It dynamically decides where the current understanding should look for support.",
    # transformer-block.html
    "transformerBlockSummary": "A Transformer Block is more than a wrapper around attention. It is a set of clearly divided computation units: attention for cross-token exchange, FFN for per-token processing, residuals to preserve the signal highway, and LayerNorm to keep values stable.",
    # llm-training.html
    "trainingKicker": "LLM Training",
    "trainingSummary": "An LLM does not start out as a chat assistant. It first learns language patterns, then learns to follow instructions, then learns which answers people tend to prefer.",
    "trainingIntro": "You can think of training as three layers of ability: first continue text, then follow instructions, then give answers that are more helpful.",
    "trainingNodeOneTitle": "Pretraining",
    "trainingNodeOneBody": "Learning language structure, factual associations, and common patterns from massive text.",
    "trainingNodeTwoTitle": "Instruction tuning",
    "trainingNodeTwoBody": "Teaching the model that users may ask it to answer, summarize, rewrite, classify, or reason.",
    "trainingNodeThreeTitle": "Preference alignment",
    "trainingNodeThreeBody": "Using human preference signals to tune helpfulness, style, and safety boundaries.",
    "trainingHeadingOne": "Pretraining: learning the language world",
    "trainingBodyOne": "A common pretraining objective is next-token prediction. The task looks simple, but with enough data and model capacity it forces the model to learn grammar, knowledge, reasoning traces, and domain patterns.",
    "trainingHeadingTwo": "Instruction tuning: from continuation to assistant",
    "trainingBodyTwo": "A model trained only with pretraining behaves more like a text completer. Instruction tuning gives it examples of Q&A, summarization, classification, code, and reasoning so it learns to complete tasks.",
    "trainingHeadingThree": "Preference alignment: useful answers, not just plausible ones",
    "trainingBodyThree": "The same question can have many possible answers. Preference alignment teaches the model which responses are clearer, safer, and more useful. RLHF and DPO are two representative methods.",
    "trainingHeadingFour": "One-sentence takeaway",
    "trainingBodyFour": "LLM training is not a single magic step. It is a sequence from language modeling, to task following, to alignment with human preferences.",
    # model-evaluation.html
    "evaluationKicker": "AI Evaluation",
    "evaluationSummary": "A model’s strength is not just a leaderboard score. What matters is whether it is stable, controllable, and explainable in your task.",
    "evaluationIntro": "The easiest mistake in model evaluation is treating one score as the whole answer. Scores are useful, but they usually illuminate only one small part of the capability map.",
    "evaluationNodeOneTitle": "Benchmark",
    "evaluationNodeOneBody": "Useful for quick comparison, but often far from real business tasks.",
    "evaluationNodeTwoTitle": "Human preference",
    "evaluationNodeTwoBody": "Measures whether answers feel natural, clear, and helpful, but costs more.",
    "evaluationNodeThreeTitle": "Real tasks",
    "evaluationNodeThreeBody": "Closest to product value, but requires clear data, constraints, and success criteria.",
    "evaluationHeadingOne": "Leaderboard scores are a starting point",
    "evaluationBodyOne": "Benchmarks help us compare knowledge, math, code, and reasoning. But a high score does not guarantee that a model fits your actual workflow.",
    "evaluationHeadingTwo": "Real-task evaluation is closer to product judgment",
    "evaluationBodyTwo": "For a data analysis agent, the question is not only whether the answer is correct. It also needs to understand the business question, choose data, write runnable code, explain results, and notice anomalies.",
    "evaluationHeadingThree": "Good evaluation must be reproducible",
    "evaluationBodyThree": "The test set, scoring rules, failure categories, and example records all need to be explicit. Otherwise a model may look better or worse simply because the test changed.",
    "evaluationHeadingFour": "One-sentence takeaway",
    "evaluationBodyFour": "To judge a model, combine general scores, human experience, and real-task results. In product work, reliably solving the target task matters more than chasing one high score.",
}

# Per-file title / description overrides
FILE_META = {
    "index.html": {
        "desc": "Data scientist and AI analyst focused on model evaluation, growth analytics, and practical AI products.",
    },
    "blogs.html": {
        "desc": "Notes and articles on AI evaluation, data products, and LLM fundamentals.",
    },
    "projects.html": {
        "desc": "Selected projects in AI evaluation, data analytics, and model visualization.",
    },
    "articles/index.html": {
        "title": "LLM Explainer Series | Jiaqi He",
        "desc": "An explainer series on Transformers, attention, LLM training, and model evaluation.",
    },
    "articles/transformer.html": {
        "title": "What problem did the Transformer actually solve? | Jiaqi He",
        "desc": "From RNN limitations to Transformers, attention, and parallel training.",
    },
    "articles/attention.html": {
        "title": "Attention: how does a model decide where to look? | Jiaqi He",
        "desc": "An intuitive explanation of Query, Key, Value, and attention weights.",
    },
    "articles/transformer-block.html": {
        "title": "Transformer Block: the building block of LLMs | Jiaqi He",
        "desc": "Unpacking Multi-Head Attention, FFN, residual connections, and LayerNorm.",
    },
    "articles/llm-training.html": {
        "title": "How LLMs are trained: from data to dialogue | Jiaqi He",
        "desc": "Pretraining, instruction tuning, preference alignment, and what each stage is for.",
    },
    "articles/model-evaluation.html": {
        "title": "How do we know whether a model is strong? | Jiaqi He",
        "desc": "A map of benchmarks, human preference, real tasks, and agent evaluation.",
    },
    "articles/data-agent-product-design.html": {
        "title": "Growth Data Agent Product Design | Jiaqi He",
        "desc": "A product design note for a growth analytics agent covering business questions, agent workflows, AI evals, and rollout planning.",
    },
}

ARIA_MAP = {
    "回到首页": "Back to home",
    "主导航": "Main navigation",
    "系列进度": "Series progress",
    "页内目录": "Table of contents",
    "上一篇下一篇": "Article navigation",
    "系列说明": "Series note",
    "文章列表": "Article list",
    "QKV 直觉": "QKV intuition",
}

FILES = [
    "index.html",
    "blogs.html",
    "projects.html",
    "articles/index.html",
    "articles/transformer.html",
    "articles/attention.html",
    "articles/transformer-block.html",
    "articles/llm-training.html",
    "articles/model-evaluation.html",
    "articles/data-agent-product-design.html",
]


def process(content: str, meta: dict) -> str:
    # 1. Fix html lang attribute
    content = content.replace('lang="zh-CN"', 'lang="en"')

    # 2. Fix <title>
    if "title" in meta:
        content = re.sub(
            r"<title>[^<]+</title>",
            f'<title>{meta["title"]}</title>',
            content,
        )

    # 3. Fix meta description (handles both plain and data-i18n-content variants)
    if "desc" in meta:
        # Remove data-i18n-content attribute if present, and update content value
        content = re.sub(
            r'\s*data-i18n-content="[^"]*"',
            "",
            content,
        )
        content = re.sub(
            r'(<meta\s[^>]*name="description"[^>]*content=")[^"]*(")',
            lambda m: m.group(1) + meta["desc"] + m.group(2),
            content,
        )
    else:
        # Resolve data-i18n-content from dictionary if no explicit override
        def resolve_meta_content(m):
            key = m.group(1)
            existing = m.group(2)
            return f'content="{EN.get(key, existing)}"'

        content = re.sub(
            r'data-i18n-content="([^"]+)"\s+content="([^"]*)"',
            resolve_meta_content,
            content,
        )
        # Remove any leftover data-i18n-content attributes
        content = re.sub(r'\s*data-i18n-content="[^"]*"', "", content)

    # 4. Replace data-i18n text content, then remove the attribute
    def replace_text(m):
        key = m.group(1)
        val = EN.get(key, m.group(2).strip())
        return f">{val}<"

    content = re.sub(
        r'data-i18n="([^"]+)">\s*(.*?)\s*<',
        replace_text,
        content,
        flags=re.DOTALL,
    )
    content = re.sub(r'\s*data-i18n="[^"]*"', "", content)

    # 5. Remove body data-title-key and data-lang
    content = re.sub(r'\s*data-title-key="[^"]*"', "", content)
    content = re.sub(r'\s*data-lang="[^"]*"', "", content)

    # 6. Fix Chinese aria-labels
    for zh, en_val in ARIA_MAP.items():
        content = content.replace(f'aria-label="{zh}"', f'aria-label="{en_val}"')

    # 7. Fix hardcoded Chinese UI strings not covered by i18n
    content = content.replace(">本文目录<", ">Contents<")

    # 8. Remove site.js script tag
    content = re.sub(
        r"[ \t]*<script src=\"[^\"]*site\.js[^\"]*\"></script>\n?",
        "",
        content,
    )

    return content


def main():
    for rel_path in FILES:
        abs_path = os.path.join(BASE, rel_path)
        if not os.path.exists(abs_path):
            print(f"  SKIP (not found): {rel_path}")
            continue

        with open(abs_path, "r", encoding="utf-8") as fh:
            original = fh.read()

        meta = FILE_META.get(rel_path, {})
        result = process(original, meta)

        with open(abs_path, "w", encoding="utf-8") as fh:
            fh.write(result)

        changed = original != result
        print(f"  {'OK' if changed else 'unchanged'}: {rel_path}")


if __name__ == "__main__":
    main()
