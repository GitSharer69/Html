var num2 = prompt()
function isPrime(num) {
  
    if (num === 2) {
      return "true";
    } else if (num > 1) {
      for (var i = 2; i < num; i++) {
  
        if (num % i !== 0) {
          return true;
        } else if (num === i * i) {
          return false
        } else {
          return false;
        }
      }
    } else {
      return "not prime";
    }
  
  }

     alert(isPrime(num2));
