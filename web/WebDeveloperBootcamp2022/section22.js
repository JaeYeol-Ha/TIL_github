// 221. forEach
let numbers = [1, 2, 3, 4, 5];

numbers.forEach(function (el) {
  console.log(el);
});
// for of 문이 생겨서 대체가능하다
for (let el of numbers) {
  console.log(el);
}

const movies = [
  {
    title: "alien",
    score: 90,
  },
  {
    title: "stand by me",
    score: 95,
  },
];

movies.forEach(function (movie) {
  console.log(`${movie.title} - ${movie.score}/100`);
});

// 222. map
// 기존 배열을 새로운 배열로 매핑(forEach + return arr)

numbers = [1, 2, 3, 4, 5];
const double = numbers.map(function (num) {
  return num * 2;
});
console.log(double);

const titles = movies.map(function (movie) {
  return movie.title.toUpperCase();
});

console.log(titles);

// 223. arrow function

const add = (x, y) => {
  return x + y;
};

const square = (x) => {
  return x * x;
};

const rollDie = () => {
  return Math.floor(Math.random() * 6) + 1;
};
