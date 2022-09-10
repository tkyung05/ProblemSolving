def solution(s):
    answer = 0
    ran = len(s)
    brackets = {')': '(', '}': '{', ']': '['}

    for _ in range(ran):
        f, l = s[:1], s[1:]
        s = l + f

        stack = []
        bug = False

        for b in s:
            if b not in brackets:
                stack.append(b)
            else:
                if stack and stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    bug = True
                    break

        if not bug and len(stack) == 0:
            answer += 1

    return answer
