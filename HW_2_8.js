/*С помощью рекурсии организовать функцию возведения числа в степень.
 Формат: function power(val, pow), где val – заданное число, pow – степень. */
"use strict";
function power(val, pow) {
    if (pow == 0) {
        return 1
    }
    return val * power(val, pow - 1);
}
var val = +prompt('Введите число: ');
var pow = +prompt('Введите степень: ');
alert('Результат: ' + power(val, pow));

/* */