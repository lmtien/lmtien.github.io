---
title: "0-1 BFS: The Small Graph Trick Between BFS and Dijkstra"
categories:
  - Software-Development
tags:
  - graph
  - algorithms
  - bfs
  - software development
---

I found a Vietnamese article on Viblo about `0-1 BFS` that felt worth bringing into English. It is not one of the famous global algorithm posts that everyone has already seen. It is a local Vietnamese write-up, practical and quietly good, especially in the way it explains the jump from normal BFS to a shortest-path algorithm for edges that cost only `0` or `1`.

Here is my retelling of the idea, with a small engineering lens.

## The problem with normal BFS

Normal BFS is beautiful because it is honest. In an unweighted graph, every edge has the same cost, so BFS can visit nodes layer by layer and the first time it reaches a node, that path is shortest.

But that promise breaks as soon as some moves are free.

Imagine a graph where every edge has one of two costs:

- `0`: this move is free.
- `1`: this move costs one unit.

Now a path with five edges can be cheaper than a path with two edges. BFS only counts layers. It does not understand that some edges should not move us to the next cost level.

The usual answer is Dijkstra. That works, but it is a little heavier than necessary. If weights are only `0` and `1`, we can use a `deque` and get the same shortest-path result in linear time.

That is `0-1 BFS`.

![0-1 BFS with a deque](/assets/images/post/2026-05-15-zero-one-bfs.svg){: .align-center}

## The whole trick

In normal BFS, we use a queue:

```text
push new nodes to the back
pop from the front
```

In `0-1 BFS`, we use a double-ended queue, or `deque`:

```text
if edge cost is 0: push the neighbor to the front
if edge cost is 1: push the neighbor to the back
```

That is almost the whole algorithm.

A free move should be handled immediately because it does not increase the current distance. A cost-1 move can wait behind everything else with the same current cost.

It feels like a tiny priority queue with only two lanes.

## Why it works

The key invariant is that nodes inside the deque are always ordered by distance. More specifically, while processing distance `d`, the deque contains only nodes with distance `d` or `d + 1`.

So when we pop from the front, we are taking a node with the smallest known distance, just like Dijkstra would.

If we relax an edge with cost `0`, the neighbor still has distance `d`, so it belongs at the front.

If we relax an edge with cost `1`, the neighbor has distance `d + 1`, so it belongs at the back.

Because the weights are only `0` and `1`, there is no need for a heap. The deque is enough to preserve the processing order.

## A TypeScript version

Here is a compact implementation. It assumes nodes are numbered from `0` to `n - 1`, and each edge is represented as `[to, weight]`.

```typescript
type Edge = [to: number, weight: 0 | 1];

function zeroOneBfs(graph: Edge[][], start: number): number[] {
  const inf = Number.MAX_SAFE_INTEGER;
  const dist = Array(graph.length).fill(inf);
  const deque: number[] = [];

  dist[start] = 0;
  deque.push(start);

  while (deque.length > 0) {
    const node = deque.shift()!;

    for (const [next, weight] of graph[node]) {
      const candidate = dist[node] + weight;

      if (candidate >= dist[next]) {
        continue;
      }

      dist[next] = candidate;

      if (weight === 0) {
        deque.unshift(next);
      } else {
        deque.push(next);
      }
    }
  }

  return dist;
}
```

In production JavaScript, `shift()` and `unshift()` can be expensive on large arrays. For serious input sizes, use a real deque implementation or a ring buffer. The algorithmic idea is still the same.

## A small example

Suppose we have this graph:

```text
A --0--> B
A --1--> C
B --1--> D
C --0--> D
```

Starting from `A`:

- `B` gets distance `0`, so it goes to the front.
- `C` gets distance `1`, so it goes to the back.
- From `B`, `D` gets distance `1`.
- From `C`, going to `D` also costs `1`, so it does not improve anything.

The final distances are:

```text
A = 0
B = 0
C = 1
D = 1
```

This is exactly what we want: free edges stay in the same wave, cost-1 edges move to the next wave.

## Where this shows up

The most useful part of `0-1 BFS` is not the code. It is the modeling habit.

Many problems do not say "this is a graph with edge weights 0 and 1." They describe a system:

- Following the current direction is free, reversing direction costs `1`.
- Walking on an empty cell is free, breaking a wall costs `1`.
- Keeping the current mode is free, switching mode costs `1`.
- Moving along a preferred route is free, taking a detour costs `1`.

Once you can turn that into a graph, `0-1 BFS` becomes the natural tool.

## BFS, 0-1 BFS, and Dijkstra

Here is the simple decision table:

| Problem shape | Best fit |
| --- | --- |
| Every edge has the same cost | BFS |
| Every edge costs `0` or `1` | 0-1 BFS |
| Edges have non-negative general weights | Dijkstra |
| Edges may have negative weights | Bellman-Ford or another specialized approach |

This is why `0-1 BFS` is satisfying. It is not a brand-new universe. It is the small missing bridge between BFS and Dijkstra.

## Complexity

For a graph with `V` vertices and `E` edges:

```text
Time:  O(V + E)
Space: O(V + E)
```

Each successful relaxation puts a node into the deque, and every edge is considered through the adjacency list. The important win is that deque operations are constant time, while Dijkstra's heap operations are usually `O(log V)`.

## Final thought

I like this algorithm because it rewards noticing the shape of the problem.

If the graph is unweighted, use BFS. If the graph is weighted, many of us jump straight to Dijkstra. But when the weights are only `0` and `1`, there is a more precise tool.

It is still BFS at heart. It just learned one small kind of priority.

## Source

- [Vietnamese source: Tìm Đường Đi Ngắn Nhất Trên Đồ Thị Có Trọng Số 0-1 Với 0-1 BFS](https://viblo.asia/p/tim-duong-di-ngan-nhat-tren-do-thi-co-trong-so-0-1-voi-0-1-bfs-ZoJjeNOO4Y7)
