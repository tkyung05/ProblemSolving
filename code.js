function solution(n, works) {
  while (n != 0 && works.reduce((a, b) => a + b, 0) > 0) {
    works[works.indexOf(Math.max(...works))] -= 1;
    n--;
  }

  const answer = works.map((x) => x ** 2).reduce((a, b) => a + b, 0);

  return answer;
}
