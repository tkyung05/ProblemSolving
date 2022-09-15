function solution(s) {
  const str = s.split(' ');
  const answer = str.map(x => x.charAt(0).toUpperCase() + x.slice(1).toLowerCase());
  
  return answer.join(' ');
}