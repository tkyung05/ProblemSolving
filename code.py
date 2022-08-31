def solution(record):
    answer = []
    
    cmd_get = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    uid_get = {}
    logs = []
    
    for re in record:
        cmd = list(map(str, (re.split())))

        if cmd[0] == 'Enter':
            uid_get[cmd[1]] = cmd[2] 
            logs.append((cmd[0], cmd[1]))
        elif cmd[0] == 'Leave':
            logs.append((cmd[0], cmd[1]))
        elif cmd[0] == 'Change':
            uid_get[cmd[1]] = cmd[2]
            
    for cmd, uid in logs:
        answer.append(uid_get[uid] + cmd_get[cmd])

    return answer