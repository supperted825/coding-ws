import sys


def main():
    adj = {}
    for line_idx, line in enumerate(sys.stdin):
        u, v = map(int, line.strip().split(" "))
        if line_idx == 0:
            N, M = u, v
            continue
        if u == v:
            continue
        if u not in adj:
            adj[u] = set()
        if v not in adj:
            adj[v] = set()
        adj[u].add(v)
        adj[v].add(u)

    stack = [1]
    visited = set()

    while stack:
        curr_node = stack.pop()
        if curr_node in visited:
            continue
        visited.add(curr_node)

        for node in adj[curr_node]:
            stack.append(node)

    unconnected = [u for u in range(1, N + 1) if u not in visited]

    if not unconnected:
        print("All connected")
        return

    for u in unconnected:
        print(u)


if __name__ == "__main__":
    main()
