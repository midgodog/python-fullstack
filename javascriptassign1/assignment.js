function print(text) {
  document.getElementById("output").textContent = text;
}

function problem1() {
  let a = parseFloat(prompt("Enter first number:"));
  let b = parseFloat(prompt("Enter second number:"));
  let out = "Addition: " + (a + b) + "\\n";
  out += "Subtraction: " + (a - b) + "\\n";
  out += "Multiplication: " + (a * b) + "\\n";
  out += "Division: " + (b !== 0 ? (a / b) : "Cannot divide by zero") + "\\n";
  out += "Modulus: " + (a % b);
  print(out);
}

function problem2() {
  let a = parseFloat(prompt("Enter first number:"));
  let b = parseFloat(prompt("Enter second number:"));
  let result = (a > b) ? "First number is greater" : (a < b ? "First number is smaller" : "Both are equal");
  print(result);
}

function problem3() {
  let x = 10;
  let out = "Initial x: " + x + "\\n";
  x += 5;
  out += "After +=5: " + x + "\\n";
  x *= 3;
  out += "After *=3: " + x + "\\n";
  x -= 10;
  out += "After -=10: " + x + "\\n";
  x /= 2;
  out += "After /=2: " + x + "\\n";
  x %= 3;
  out += "After %=3: " + x;
  print(out);
}

function problem4() {
  let num = parseInt(prompt("Enter a number:"));
  print(num % 2 === 0 ? "Even number" : "Odd number");
}

function problem5() {
  let num = parseInt(prompt("Enter a number:"));
  let sum = 0;
  do {
    sum += num % 10;
    num = Math.floor(num / 10);
  } while (num > 0);
  print("Sum of digits: " + sum);
}

function problem6() {
  let num = parseInt(prompt("Enter a number:"));
  let fact = 1, i = 1;
  while (i <= num) {
    fact *= i;
    i++;
  }
  print("Factorial: " + fact);
}

function problem7() {
  let str = prompt("Enter a string:");
  let ch = prompt("Enter a character:");
  let count = 0;
  for (let i = 0; i < str.length; i++) {
    if (str[i] === ch) count++;
  }
  print("'" + ch + "' occurred " + count + " times.");
}

function problem8() {
  let num = parseInt(prompt("Enter a number:"));
  let out = "";
  for (let i = 1; i <= 10; i++) {
    out += num + " x " + i + " = " + (num * i) + "\\n";
  }
  print(out);
}

function problem9() {
  let n = parseInt(prompt("Enter number of terms:"));
  let a = 0, b = 1, out = "";
  for (let i = 1; i <= n; i++) {
    out += a + "\\n";
    let temp = a + b;
    a = b;
    b = temp;
  }
  print(out);
}

function problem10() {
  let input = prompt("Enter array elements (space-separated):");
  let arr = input.trim().split(" ");
  let freq = {};
  for (let item of arr) {
    freq[item] = (freq[item] || 0) + 1;
  }
  let out = "";
  for (let key in freq) {
    out += key + ": " + freq[key] + "\\n";
  }
  print(out);
}
