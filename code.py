def solution(skill, skill_trees):
    answer = 0
    my_skill = {s: 1 for s in skill}

    for skt in skill_trees:
        cur = 0
        impossible_skill = False

        for s in skt:
            if s in my_skill:
                if skill[cur] == s:
                    cur += 1
                else:
                    impossible_skill = True
                    break

        answer += 0 if impossible_skill else 1

    return answer
