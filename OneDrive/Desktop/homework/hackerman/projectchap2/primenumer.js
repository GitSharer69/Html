var n= prompt("enter number fo prime or not");

var stat = 0;
if (n == 1) console.log ("special boi");
for (var i = 2; i <= n-1; i++) {
    if (n % i == 0){
        stat =1;
        break;
    }
}

if (stat == 0) {
    console.log("prime")
}  else console.log("not prime")