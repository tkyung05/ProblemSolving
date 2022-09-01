function solution(absolutes, signs) {
  let answer = [];
  
  for (let i = 0; i < absolutes.length; i++) {
    answer.push(signs[i] ? absolutes[i] : -1 * absolutes[i]);
  }
  return answer.reduce((a, b) => a + b, 0);
}