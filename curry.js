function add(...orice) {
  let res = 0;
  for (const x of orice) res += x;
  return res;
}

function summ(...args) {
  if (args.length == 1) return args[0];
  var partial = add(...args);
  return function(...rest) {
    return summ(partial, ...rest);
  }
}

sum = summ(0, 0);

console.log(sum(1,2,3)());
console.log(sum(1,2)(3)(4)(5,6)());
console.log(sum(1)(2)(3)(4)(5)(6)());
console.log(sum(1,2,3)(4,5)(4,5)(4,5)(5,5,5,5,5,5,5)(1)(1)());
