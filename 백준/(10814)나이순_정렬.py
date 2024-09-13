import sys

N = int(sys.stdin.readline())
member = []

for _ in range(N):
    age, name = sys.stdin.readline().split()
    member.append((int(age), name))

member.sort(key=lambda x:x[0])

sys.stdout.write("\n".join(f"{age} {name}" for age, name in member) + "\n")