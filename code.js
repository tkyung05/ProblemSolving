const LIMIT = 10001;

function solution(n) {
    let answer = 0;
    
    for (let i = 1; i <= LIMIT; i++) {
        let sumNum = i;
        
        if (sumNum > n) {
            break;
        }
        
        for (let j = i + 1; j <= LIMIT; j++) {
            if (sumNum > n) {
                break;
            } 
            else if (sumNum == n) {
                answer++;
            }
            
            sumNum += j
        }
    }
    
    return answer;
}