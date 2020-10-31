/*Реализовать основные 4 арифметические операции в виде
функций с двумя параметрами.
Обязательно использовать оператор return. */
"use strict";
function summary(x, y) {
    return x + y;
}
function difference(x, y) {
    return x - y;
}
function composition(x, y) {
    return x * y;
}
function divison(x, y) {
    return x / y;
}
var x = 10, y = 5;
alert('x=10,y=5');
alert('Сумма: ' + summary(x, y));
alert('Разница: ' + difference(x, y));
alert('Произведение: ' + composition(x, y));
alert('Деление: ' + divison(x, y));
/* */