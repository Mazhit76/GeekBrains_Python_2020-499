/*6. Реализовать функцию с тремя параметрами:
function mathOperation(arg1, arg2, operation),
где arg1, arg2 – значения аргументов,
operation – строка с названием операции.
В зависимости от переданного значения операции
 выполнить одну из арифметических операций
 (использовать функции из пункта 3)
 и вернуть полученное значение (использовать switch).
*/
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
function mathOperation(arg1, arg2, operation) {
    switch (operation) {
        case '+': return summary(arg1, arg2);
        case '-': return difference(arg1, arg2);
        case '*': return composition(arg1, arg2);
        case '/': return divison(arg1, arg2);
    }
}
var x = parseFloat(prompt('Введите 1 аргумент:'));
var y = parseFloat(prompt('Введите 2 аргумент:'));
var operation = prompt('Введите опреацию:');
alert(x + ' ' + operation + ' ' + y + ' получится ' + mathOperation(x, y, operation));


/* 7. Сравнить null и 0. Попробуйте объяснить результат. */

alert(0 == null);

/**Сравнить null и 0. Попробуйте объяснить результат. Ответ -будет "false" т.к. null – ключевое слово, как признак
обычного или вполне ожидаемого отсутствия значения, нельзя сравнить и сказать что 0 -это отсутствие значения. Это зачение равное 0
(Хотя в обиходе мы знаем, что 0 это есть отсутсвие чего либо).
Похоже на тавтологию. Но как то так. */