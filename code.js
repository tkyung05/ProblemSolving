const LIMIT = 60001
const DIV_NUM = 1000000007

function solution(n) {
    let answer = Array.from({lenght: LIMIT}, () => 0);
    answer[1] = 1;
    answer[2] = 2;
    
    for (let i = 3; i < LIMIT; i++) {
        answer[i] = (answer[i - 1] + answer[i - 2]) % DIV_NUM;
    }
    
    return answer[n];
}