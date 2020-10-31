"use strict";

let i = 1;
while (i <= 5) {
    document.write(i + '<br>');
    i = i + 1;

}
var answer = parseInt(Math.random() * 100);
var attempt = 1;
var attemptsCount = 7;

while (attempt <= attemptsCount) {
    var userAnswer = prompt("Угадайте число от 0 до 100, у вас 7 попыток. Попытка № " + attempt);
    userAnswer = parseInt(userAnswer);

    if (userAnswer > answer) {
        alert("Ваш ответ больше загаданного числа.");
    } else if (userAnswer < answer) {
        alert("Ваш ответ меньше загаданного числа.");
    } else if (userAnswer == answer) {
        alert("Вы угадали!");
        break;
    } else {
        alert("Необходимо ввести число!");
    }
    attempt++;
}

if (attempt > attemptsCount) {
    alert("К сожалению, вы не угадали. Было загадано число: " + answer);
} 