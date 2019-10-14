# [GoogleCodeJam 2016](https://code.google.com/codejam/contests.html) ![Language](https://img.shields.io/badge/language-Python-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md) ![Progress](https://img.shields.io/badge/progress-26%20%2F%2026-ff69b4.svg)

Python solutions of Google Code Jam 2016. Solution begins with `*` means it will get TLE in the largest data set (total computation amount > `10^8`, which is not friendly for Python to solve in 5 ~ 15 seconds). A `4-minute` timer is set for the small dataset and a `8-minute` timer is set for the large dataset this year.

* [Qualification Round](https://github.com/kamyu104/GoogleCodeJam-2016#qualification-round)
* [Round 1A](https://github.com/kamyu104/GoogleCodeJam-2016#round-1a)
* [Round 1B](https://github.com/kamyu104/GoogleCodeJam-2016#round-1b)
* [Round 1C](https://github.com/kamyu104/GoogleCodeJam-2016#round-1c)
* [Round 2](https://github.com/kamyu104/GoogleCodeJam-2016#round-2)
* [Round 3](https://github.com/kamyu104/GoogleCodeJam-2016#round-3)
* [World Finals](https://github.com/kamyu104/GoogleCodeJam-2016#world-finals)

## Qualification Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Counting Sheep](https://code.google.com/codejam/contest/6254486/dashboard#s=p0)| [Python](./Qualification%20Round/counting-sheep.py)| _O(NlogN)_ | _O(logN)_ | Easy | | Simulate |
|B| [Revenge of the Pancakes](https://code.google.com/codejam/contest/6254486/dashboard#s=p1)| [Python](./Qualification%20Round/revenge-of-the-pancakes.py)| _O(N)_ | _O(1)_ | Easy | | Math Analysis |
|C| [Coin Jam](https://code.google.com/codejam/contest/6254486/dashboard#s=p2)| [Python](./Qualification%20Round/coin-jam.py)| _O(N * J)_ | _O(N)_ | Medium | | Tricky Math |
|D| [Fractiles](https://code.google.com/codejam/contest/6254486/dashboard#s=p3)| [Python](./Qualification%20Round/fractiles.py)| _O(K)_ | _O(1)_ | Hard | | Logic, Math Induction |

## Round 1A
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [The Last Word](https://code.google.com/codejam/contest/4304486/dashboard#s=p0)| [Python](./Round%201A/the-last-word.py)| _O(L)_ | _O(L)_ | Easy | | Greedy |
|B| [Rank and File](https://code.google.com/codejam/contest/4304486/dashboard#s=p1)| [Python](./Round%201A/rank-and-file.py)| _O(N^2)_ | _O(N^2)_ | Easy | | Math Analysis |
|C| [BFFs](https://code.google.com/codejam/contest/4304486/dashboard#s=p2)| [Python](./Round%201A/bffs.py)| _O(N)_ | _O(N)_ | Hard | | Hash, Graph |

## Round 1B
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Getting the Digits](https://code.google.com/codejam/contest/11254486/dashboard#s=p0)| [Python](./Round%201B/getting-the-digits.py)| _O(N)_ | _O(1)_ | Easy | | Greedy |
|B| [Close Match](https://code.google.com/codejam/contest/11254486/dashboard#s=p1)| [Python](./Round%201B/close-match.py)| _O(N^2)_ | _O(N)_ | Medium | | Greedy |
|C| [Technobabble](https://code.google.com/codejam/contest/11254486/dashboard#s=p2)| [Python](./Round%201B/technobabble.py)| _O(N * sqrt(W))_ | _O(W)_ | Hard | | Graph, Bipartite Matching |

## Round 1C
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Senate Evacuation](https://code.google.com/codejam/contest/4314486/dashboard#s=p0)| [Python](./Round%201C/senate-evacuation.py)| _O(PlogP)_ | _O(P)_ | Easy | | Heap, Math Analysis |
|B| [Slides!](https://code.google.com/codejam/contest/4314486/dashboard#s=p1)| [Python](./Round%201C/slides.py)| _O(B^2)_ | _O(1)_ | Easy | | Math Analysis |
|C| [Fashion Police](https://code.google.com/codejam/contest/4314486/dashboard#s=p2)| [Python](./Round%201C/fashion-police.py)| _O(J * P * min(S, K))_ | _O(1)_ | Hard | | Math Analysis |

## Round 2
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Rather Perplexing Showdown](https://code.google.com/codejam/contest/10224486/dashboard#s=p0)| [Python](./Round%202/rather-perplexing-showdown.py)| _O(2^N)_ | _O(2^N)_ | Easy | | Math Analysis |
|B| [Red Tape Committee](https://code.google.com/codejam/contest/10224486/dashboard#s=p1)| [Python](./Round%202/red-tape-committee.py)| _O(NlogN + K^3)_ | _O(N)_ | Easy | | DP, Probability |
|C| [The Gardener of Seville](https://code.google.com/codejam/contest/10224486/dashboard#s=p2)| [Python](./Round%202/the-gardener-of-seville.py)| _O((R + C)log(R + C) + R * C)_ | _O(R * C)_ | Hard | | Simulate |
|D| [Freeform Factory](https://code.google.com/codejam/contest/10224486/dashboard#s=p3)| [Python](./Round%202/freeform-factory.py)| _O(N + C * C!)_ | _O(N + C * C!)_ | Hard | | Memoization, DFS |

## Round 3
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Teaching Assistant](https://code.google.com/codejam/contest/3224486/dashboard#s=p0)| [Python](./Round%203/teaching-assistant.py)| _O(S)_ | _O(S)_ | Easy | | Greedy |
|B| [Forest University](https://code.google.com/codejam/contest/3224486/dashboard#s=p1)| [Python](./Round%203/forest-university.py)| _O(T * N^2)_ | _O(N)_ | Medium | | Simulate |
|C| [Rebel Against The Empire](https://code.google.com/codejam/contest/3224486/dashboard#s=p2)| [C++](./Round%203/rebel-against-the-empire.cpp) [PyPy](./Round%203/rebel-against-the-empire.py) | _O(logN * (N^2 + H * N))_ | _O(N^2)_ | Hard | | Graph, BFS, Binary Search |
|D| [Go++](https://code.google.com/codejam/contest/3224486/dashboard#s=p3)| [Python](./Round%203/go++.py)| _O(L)_ | _O(L)_ | Medium | | Math Analysis |

## World Finals
You can relive the magic of the 2016 Code Jam World Finals by watching the [Live Stream Recording](https://www.youtube.com/watch?v=4diQ6JXY4cI) of the competition, problem explanations, interviews with Google and Code Jam engineers, and announcement of winners.

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Integeregex](https://code.google.com/codejam/contest/7234486/dashboard#s=p0)| [Python](./World%20Finals/integeregex.py) | _O(R^2 + RlogB)_  on average | _O(R)_ on average | Medium | | Automata, NFA, Thompson's Construction, DP |
|B| [Family Hotel](https://code.google.com/codejam/contest/7234486/dashboard#s=p1)| [Python](./World%20Finals/family-hotel.py) | _O(N)_ | _O(N)_ | Medium | | DP, Probability, Euler's Theorem |
|C| [Gallery of Pillars](https://code.google.com/codejam/contest/7234486/dashboard#s=p2)| [Python](./World%20Finals/gallery-of-pillars.py) | _O(NlogN)_ | _O(M)_ | Medium | | Inclusion-Exclusion Principle, Möbius Function, Sieve Of Eratosthenes, Math Analysis |
|D| [Map Reduce](https://code.google.com/codejam/contest/7234486/dashboard#s=p3)| [Python](./World%20Finals/map-reduce.py) [Python](./World%20Finals/map-reduce2.py) | _O((R * C) * log(R * C))_ | _O(R * C)_ | Hard | | BFS, Binary Search |
|E| [Radioactive Islands](https://code.google.com/codejam/contest/7234486/dashboard#s=p4)| [Python](./World%20Finals/radioactive-islands.py) | _O(P^2 *G^2)_ | _O(P * G)_ | Hard | | DP |
