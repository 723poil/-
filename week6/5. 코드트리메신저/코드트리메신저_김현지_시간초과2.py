def makeReceivers(N, active, authority, parents):
    receivers = [[] for _ in range(N+1)]
    for start in range(1, N+1):
        current = start
        steps = 0
        while current != 0 and active[current] and steps <= authority[start]:
            if current != start:
                receivers[current].append(start)
            current = parents[current]
            steps += 1
    return receivers

def main():
    # N: 채팅방의 수, Q: 명령의 수
    N, Q = map(int, input().split())
    commands = list(map(int, input().split()))

    parents = [0] * (N+1)
    authority = [0] * (N+1)
    active = [True] * (N+1)

    for i in range(1, N+1):
        parents[i] = commands[i]

    for i in range(N+1, 2*N+1):
        authority[i-N] = commands[i]

    for _ in range(Q-1):
        commands = list(map(int, input().split()))
        command = commands[0]
        if command == 200:
            c = commands[1]
            active[c] = not active[c]
        elif command == 300:
            c, power = commands[1], commands[2]
            authority[c] = power
        elif command == 400:
            c1, c2 = commands[1], commands[2]
            parents[c1], parents[c2] = parents[c2], parents[c1]
        elif command == 500:
            receivers = makeReceivers(N, active, authority, parents)
            c = commands[1]
            print(len(receivers[c]))


if __name__ == "__main__":
    main()