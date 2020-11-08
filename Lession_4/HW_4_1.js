"use strict"
function countInuserInput(userCount) {
    let userString = '';
    userCount['Еденицы'] = [];
    userCount['Десятки'] = [];
    userCount['Сотни'] = [];
    while (userString !== 'exit') {
        userString = prompt('Введите число не более 999, exit-Выход:');
        if (userString.match(/^\d{1,3}$/)) {
            let lenUserstring = userString.length;
            userCount['Еденицы'].push(+userString.charAt(lenUserstring - 1));
            userCount['Десятки'].push(+userString.charAt(lenUserstring - 2));
            userCount['Сотни'].push(+userString.charAt(lenUserstring - 3));
        } else {
            userCount = {};
            console.log('Вы ввели не число!');
            return userCount;
        }
        for (var key in userCount) {
            console.log(key + ':' + userCount[key]);
        }
    }
}

var userCount = {};

countInuserInput(userCount);