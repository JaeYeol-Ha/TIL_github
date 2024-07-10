// 함수표현식(FunctionExpressions)
// 아래 두개는 같은 표현임

// 1. 함수를 저장
function add(x, y) {
  return x + y;
}
console.log(add(1, 2));

// 2. annanymous 함수를 객체로 저장
const add2 = function (x, y) {
  return x + y;
};
console.log(add2(1, 2));

const square = function (x) {
  return Math.pow(x, 2);
};

console.log(square(4));

// 215. 반환함수
function makeMysteryFunc() {
  const rand = Math.random();
  if (rand > 0.5) {
    return function () {
      console.log("GOOD!");
    };
  } else {
    return function () {
      console.log("BAD!");
    };
  }
}

const mystery = makeMysteryFunc();

// 216. 메서드 정의하기
// 객체에 함수를 정의하면 메서드라고 함
const myMath = {
  PI: 3.141592,
  // define function
  square: function (num) {
    return num * num;
  },
  // define function (shorthand)
  cube(num) {
    return num ** 3;
  },
};

myMath.square(2); // 4
