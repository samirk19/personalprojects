let x = 4;
console.log(x)
const y = new Map();
y.set(1, "a");
y.set(2, "b");

for (var j = 1; j <= y.size; j++) {
    console.log(y.get(j));
}