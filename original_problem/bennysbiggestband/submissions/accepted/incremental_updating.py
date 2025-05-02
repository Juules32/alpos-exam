from collections import defaultdict


def dfs(curr, t, graph, seen, path):
    if curr == t:
        return path

    seen.add(curr)
    for k, v in graph[curr].items():
        if k not in seen and v > 0:
            limit = min(path[0], v)
            path[1].append(k)
            p = dfs(k, t, graph, seen, (limit, path[1]))
            if p:
                return p
            path[1].pop()

    return None


def flow(s, t, G, range_graph_indices):
    residual = defaultdict(lambda: defaultdict(int))

    for k, v in G.items():
        for g, u in v.items():
            residual[k][g] = u
            residual[g][k] = 0

    flow = 0
    while True:
        # maintain balance; when r flow is found allow more flow from each range
        if flow % len(range_graph_indices) == 0:
            for val in range_graph_indices:
                residual[val][t] = 1

        path = dfs(s, t, residual, set(), (float("inf"), [s]))
        if path:
            flow += path[0]
            nodes = path[1]
            for i in range(len(nodes) - 1):
                residual[nodes[i]][nodes[i + 1]] -= path[0]
                residual[nodes[i + 1]][nodes[i]] += path[0]
        else:
            return flow, residual


m, i, r = map(int, input().split())
G = defaultdict(lambda: defaultdict(int))

musicians = []
for _ in range(m):
    musicians.append(input().split())

instruments = {}
for j in range(i):
    instrument = input().split()
    # e.g. instrument["flute"] = [0, 2, [3]]
    instruments[instrument[0]] = [j, int(instrument[1]), list(map(int, instrument[2:]))]

for j in range(len(musicians)):
    G[0][j + 1] = 1
    curr_musician = musicians[j]
    for k in range(len(curr_musician) - 1):
        instID = instruments[curr_musician[k + 1]][0]
        G[j + 1][instID + m + 1] = 1

for instrument in instruments.values():
    graph_index = m + 1 + instrument[0]
    graph_index_out = -1 * graph_index
    G[graph_index][graph_index_out] = instrument[1]
    for val in instrument[2]:
        range_graph_index = m + i + 2 + val
        G[graph_index_out][range_graph_index] = instrument[1]

sink_index = m + i + r + 3
range_graph_indices = set()
for j in range(r):
    range_graph_index = m + i + 2 + j
    G[range_graph_index][sink_index] = 0
    range_graph_indices.add(range_graph_index)

f, _ = flow(0, sink_index, G, range_graph_indices)
print((f // r) * r)

# Graph indices (up to and including):
# Source: 0
# Musicians: 1..m
# Instruments: m + 1..m + i + 1
# Instruments out: instruments * -1
# Ranges: m + i + 2..m + i + r + 2
# Sink: m + i + r + 3

