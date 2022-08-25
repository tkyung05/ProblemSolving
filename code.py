import heapq

def solution(jobs):
    answer = []
    disk_count = len(jobs)
    
    heapq.heapify(jobs)
  
    total_time = 0

    while jobs:
      temp_disk = []
      only_one = False

      # 마지막으로 처리한 시간보다 작거나 같은 디스크를 넣어줌
      while jobs and jobs[0][0] <= total_time:
        ask_time, work_time = heapq.heappop(jobs)
        heapq.heappush(temp_disk, (work_time, ask_time))

      # 요청 시간이 total 보다 큰 경우
      if not temp_disk:
        ask_time, work_time = heapq.heappop(jobs)
        heapq.heappush(temp_disk, (work_time, ask_time))
        only_one = True

      now_work_time, now_ask_time = heapq.heappop(temp_disk)
      
      if only_one:
        answer.append(now_work_time)
        total_time = now_ask_time + now_work_time
      else:
        answer.append((total_time - now_ask_time) + now_work_time)
        total_time += now_work_time

      while temp_disk:
        work, ask = heapq.heappop(temp_disk)
        heapq.heappush(jobs, [ask, work])

    return sum(answer) // disk_count
