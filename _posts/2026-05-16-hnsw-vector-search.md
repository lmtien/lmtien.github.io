---
title: "HNSW: The Graph Behind Fast Vector Search"
categories:
  - Software-Development
tags:
  - graph
  - hnsw
  - vector search
  - software development
---

I found a small Vietnamese post about HNSW and semantic search. It is not a famous article. It has the feeling of something written for engineers who are trying to ship RAG or semantic search and suddenly realize that "just store embeddings" is not the whole story.

That is a good graph topic.

HNSW stands for Hierarchical Navigable Small World. The name is a mouthful, but the idea is surprisingly physical: build a graph of vectors, then search by walking through that graph toward better and better neighbors.

![HNSW vector search graph](/assets/images/post/2026-05-16-hnsw-vector-search.svg){: .align-center}

## Why vector search needs an index

Embeddings turn text, images, or other data into vectors. Once everything is a vector, search becomes a nearest-neighbor problem:

```text
Given a query vector, find the stored vectors closest to it.
```

The simplest solution is brute force. Compare the query against every vector, sort the distances, return the top results.

That is perfect for correctness and terrible for scale.

If you have 5,000 vectors, brute force is fine. If you have 5 million vectors and users expect answers in milliseconds, the cost becomes painful. This is why vector databases use approximate nearest neighbor indexes. They trade a little exactness for a lot of speed.

HNSW is one of the most useful of those indexes because it is a graph.

## The graph idea

Each vector becomes a node. Edges connect that vector to nearby vectors.

If the graph is built well, nearby vectors are not only close in the mathematical space, they are also reachable by short paths in the graph. Search becomes a walk:

1. Start from an entry point.
2. Look at neighbors.
3. Move to the neighbor closer to the query.
4. Repeat until moving no longer improves the distance.

This already sounds useful, but a single dense graph can still waste time. HNSW adds hierarchy.

## Why the hierarchy matters

Think about a city map.

If you are going across the city, you do not start by checking every small alley. You first use highways and large roads to get near the destination. Then you switch to local roads. Only near the end do you care about the exact street.

HNSW does something similar:

- Upper layers are sparse.
- Lower layers are denser.
- The bottom layer contains all points.

Search begins at the top. The algorithm greedily moves toward a closer node. Then it drops down a layer and refines the position. By the time it reaches the bottom layer, it is already in the right neighborhood, so it can search locally instead of scanning the whole dataset.

This is the part I like: HNSW does not make search fast by hiding the graph. It makes search fast because the graph is the index.

## The knobs engineers actually touch

When you use HNSW in a library like FAISS, Qdrant, Weaviate, Milvus, or hnswlib, you usually meet a few parameters.

`M` controls how many neighbors a node tries to keep. A larger `M` gives the graph more roads. Recall often improves, but memory usage also grows.

`efConstruction` controls how much effort the index spends while building the graph. Higher values usually produce a better graph, but indexing takes longer.

`efSearch` controls how many candidate nodes the search explores at query time. Higher values usually improve recall, but queries become slower.

The trade-off is not mysterious:

```text
more graph edges + more candidates = better recall, more memory, more latency
fewer graph edges + fewer candidates = faster search, lower recall
```

This is why benchmarks without parameters are not very useful. HNSW is not one speed. It is a dial.

## A small FAISS example

Here is the shape of a basic HNSW index in Python:

```python
import faiss
import numpy as np

dimension = 768
neighbors_per_node = 32

index = faiss.IndexHNSWFlat(dimension, neighbors_per_node)
index.hnsw.efConstruction = 200
index.hnsw.efSearch = 64

vectors = np.asarray(vectors, dtype="float32")
query = np.asarray([query_vector], dtype="float32")

index.add(vectors)
distances, ids = index.search(query, k=5)
```

For cosine similarity, normalize vectors before adding and querying:

```python
faiss.normalize_L2(vectors)
faiss.normalize_L2(query)
```

Then inner product or L2 behavior becomes easier to reason about, depending on how the index is configured.

## What the Vietnamese post gets right

The useful point from the Vietnamese article is that HNSW is not just a vector database feature. It is the retrieval engine inside many modern semantic search systems.

In a RAG pipeline, the flow usually looks like this:

```text
question -> embedding -> vector index -> top-k chunks -> LLM answer
```

If retrieval is slow, the whole product feels slow.

If retrieval misses the right chunks, the LLM may answer confidently with the wrong context.

That means HNSW tuning is not an academic detail. It affects user experience, infrastructure cost, and answer quality.

## Where I would be careful

It is tempting to say "HNSW is O(log N)" or "HNSW gives 95% recall." You will see claims like that in many blog posts.

I would phrase it more carefully.

HNSW is designed to make nearest-neighbor search very fast in practice, and the original paper shows strong performance across benchmarks. But recall and latency depend on the dataset, vector dimension, distance metric, insertion order, hardware, and parameters like `M`, `efConstruction`, and `efSearch`.

So the honest engineering answer is:

```text
HNSW is usually a very strong default, but you still need to measure it on your data.
```

That sentence is less exciting, but it is more useful.

## A practical tuning loop

If I were adding HNSW to a production search system, I would tune it like this:

1. Build a small labeled evaluation set.
2. Run a brute-force flat index as the quality baseline.
3. Try HNSW with conservative parameters.
4. Increase `efSearch` until recall is good enough.
5. Adjust `M` and `efConstruction` if recall is still weak.
6. Measure memory, indexing time, p95 latency, and recall together.

Do not optimize latency alone. A search system that returns fast but wrong results is just a fast disappointment.

## When HNSW is a good fit

HNSW is a strong choice when:

- You need low-latency semantic search.
- Your dataset fits comfortably in memory.
- You can accept approximate results.
- You care about high recall without scanning everything.
- You want a practical index for RAG, recommendations, deduplication, or similarity search.

It is less comfortable when:

- Memory is extremely tight.
- The dataset is enormous and needs heavy compression.
- You need exact nearest neighbors.
- Updates and deletes dominate the workload.

This does not make HNSW bad. It means it has a shape. Good engineering starts by noticing that shape.

## Final thought

What I like about HNSW is that it turns "search in high-dimensional space" into something almost visual.

There are nodes. There are edges. There are sparse roads and dense local streets. A query does not scan the world. It travels through the graph.

That is why graph thinking keeps showing up in software engineering. Sometimes the graph is your business domain. Sometimes it is your dependency tree. And sometimes, as with HNSW, the graph is the thing making your search fast enough to feel intelligent.

## Sources

- [Vietnamese source: Hieu va ung dung HNSW trong tim kiem ngu nghia voi embedding](https://viblo.asia/p/hieu-va-ung-dung-hnsw-trong-tim-kiem-ngu-nghia-voi-embedding-bNVQGGXRJvR)
- [Original HNSW paper: Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs](https://arxiv.org/abs/1603.09320)
- [FAISS index documentation](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes)
