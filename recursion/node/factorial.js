function factorial(n) {
    if (n === 0) {
        return 1; 
    }
    return n * factorial(n-1);
}

res = factorial(5)
console.assert(res == 120, "factorial(5) should be 120")
console.log("PASSED")
