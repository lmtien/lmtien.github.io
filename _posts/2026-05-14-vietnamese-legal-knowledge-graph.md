---
title: "Vietnam's Legal Knowledge Graph"
categories:
  - Software-Development
tags:
  - graph
  - knowledge graph
  - vietnam
  - computer science
---

I went looking for an interesting Vietnamese story about graphs, not just the usual "DFS and BFS" tutorial. The best one I found is about something very local: Vietnam's legal documents.

Vietnam has a growing public collection of judgments, case law, and legal documents. The problem is not only search. The problem is relationship. A court case may mention many laws. A law may appear across many cases. Two cases may look unrelated by keyword, but they may share the same court, legal domain, or legal basis.

That is exactly the kind of problem a graph is good at.

![Vietnam legal knowledge graph](/assets/images/post/2026-05-14-vietnam-legal-knowledge-graph.svg){: .align-center}

## Why a graph?

A normal search engine thinks mostly in documents and keywords. If you type "land dispute" or "marriage law", it can return pages that contain those words. That is useful, but it misses the structure hiding inside the legal system.

A graph thinks in entities and relationships:

- A court decides a case.
- A case belongs to a domain.
- A case is based on one or more laws.
- A law connects many cases together.

Once the data is represented like that, search becomes more than text matching. You can ask: show me cases decided by the same court, in the same domain, based on similar laws. You can move through the graph.

That movement is the interesting part.

## The Vietnam-specific part

This topic is not just "legal tech" in general. It is specific to Vietnam because the graph depends on Vietnamese legal structure, Vietnamese language, and Vietnamese court data.

In 2016, Vietnam's Supreme People's Court launched an official online case law portal at `anle.toaan.gov.vn`, described by Nhan Dan as the official source of information about case law from the Supreme People's Court. That matters because a graph needs reliable source data before it can become useful.

There is also a legal culture difference. Vietnam is closer to a civil-law tradition, where written law is central and case law has a more supplementary role. A Vietnamese legal article from Dan Chu & Phap Luat explains that Vietnamese case law is not the main source of law in the way common-law precedent is, but it helps guide courts toward more consistent application of written law.

So a Vietnamese legal graph has a special shape. It is not only connecting judgments to judgments. It is connecting judgments back to codes, laws, articles, courts, and domains.

## The research version

A paper by Vietnamese researchers, "Constructing a Knowledge Graph for Vietnamese Legal Cases with Heterogeneous Graphs", makes this more concrete.

Their graph contains several types of nodes:

- `Case`: the judgment or decision.
- `Court`: the court that heard the case.
- `Domain`: the legal area, such as civil, criminal, marriage and family, etc.
- `Law`: the law or code referenced by the case.

And it uses a few clear relationship types:

- `Court -> Case`: the court decided the case.
- `Case -> Domain`: the case belongs to a legal domain.
- `Case -> Law`: the case is based on a law or code.

That is a heterogeneous graph: different node types, different edge types, and different meanings for each path.

For example, if two cases follow this path:

```text
Case -> Domain -> Case
```

then they are related because they belong to the same legal domain.

If they follow this path:

```text
Case -> Law -> Case
```

then they are related because they rely on the same law.

These paths are not just database joins. They are signals. They tell us why two cases might be useful to compare.

## A small mental model

Imagine we have a new legal case and we want to know which laws may be relevant.

A simple text search can compare the new case directly with all law documents. But legal documents are long, formal, and sometimes written in ways that do not match the query words. The same concept may be expressed with different words.

The graph gives another route:

1. Find similar past cases.
2. Look at the laws those cases were based on.
3. Use shared domains or shared courts to reduce noisy matches.
4. Return likely laws with more context.

This is why graphs feel powerful. They do not replace text search; they give text search a memory of structure.

## The product version

I also found a Vietnamese article from CMC ATI about using AI for reviewing legal documents in Vietnam. The article describes a legal review assistant that uses NLP to compare legal clauses and knowledge graphs to connect relationships between documents and provisions.

That is the same core idea in a more product-oriented form: laws are not isolated pages. They are a network of references, amendments, conflicts, effective dates, and dependencies.

For anyone who has worked with regulations, that is immediately familiar. The hard part is rarely reading one document. The hard part is knowing what this document touches, what it overrides, and what else changes when it changes.

That is graph work.

## What I like about this

There is a very practical beauty here. Graph theory can sound abstract when we learn it through vertices, edges, BFS, DFS, shortest paths, and adjacency matrices. But the Vietnamese legal system gives us a real example:

- A case is a node.
- A law is a node.
- A court is a node.
- A legal relationship is an edge.

Then algorithms become useful questions:

- Which cases are close to this case?
- Which laws are central in this domain?
- Which courts produce many cases in a particular area?
- Which laws connect otherwise distant legal topics?
- Where are the isolated nodes that no case references?

The graph is not decoration. It is a way to make legal knowledge navigable.

## Engineering notes

If I were building a small version of this, I would not start with a complex AI model. I would start with a clean graph schema:

```text
(Court)-[:DECIDED]->(Case)
(Case)-[:BELONGS_TO]->(Domain)
(Case)-[:BASED_ON]->(Law)
(Law)-[:HAS_ARTICLE]->(Article)
```

Then I would add a text search layer beside it:

- BM25 or full-text search for initial candidate retrieval.
- Named entity extraction for courts, laws, article numbers, people, places, and dates.
- Graph traversal for expanding from one case to related cases.
- Ranking that combines text similarity and graph proximity.

This hybrid approach feels more maintainable than asking an LLM to understand everything directly. The LLM can summarize and explain, but the graph should carry the factual structure.

## Conclusion

The best graph problems are usually hiding inside messy real systems. Vietnam's legal documents are a good example: lots of text, many formal relationships, and a real need for better navigation.

What makes this interesting is not only that it uses a graph. It is that the graph respects the local shape of Vietnamese law. Courts, cases, domains, and laws are not just words in a database. They are connected parts of a living system.

And once we model those connections, the legal archive becomes less like a folder of PDFs and more like a map.

## Sources

- [CMC ATI article on AI for Vietnamese legal document review](https://cmcati.vn/cmc-ati-thanh-cong-ung-dung-ai-trong-ra-soat-van-ban-phap-luat/)
- [Constructing a Knowledge Graph for Vietnamese Legal Cases with Heterogeneous Graphs](https://arxiv.org/abs/2309.09069)
- [Readable HTML version of the paper](https://ar5iv.labs.arxiv.org/html/2309.09069)
- [Nhan Dan: Supreme People's Court launched the case law portal](https://nhandan.vn/tand-toi-cao-ra-mat-trang-tin-dien-tu-ve-an-le-post275627.html)
- [Dan Chu & Phap Luat article on Vietnamese case law and civil-law tradition](https://danchuphapluat.vn/nhung-van-de-co-ban-ve-an-le-theo-truyen-thong-dan-luat-va-kinh-nghiem-cho-viet-nam-4121.html)
