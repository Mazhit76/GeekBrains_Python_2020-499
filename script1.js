"use strict";
var inputUser = prompt('Введите температуру в градусах Цельсия:');
if (inputUser != null) {
    var tempCelsia = parseFloat(inputUser);
    if (isNaN(tempCelsia)) {
        alert('Вы ввели не число!!!!');
    } else {
        var tempFarengeit = (9 / 5) * tempCelsia + 32;
        alert('Введенная температура по Фаренгейту:' + tempFarengeit);
    }
}
let admin = '';
let name = 'Василий';
admin = name;
alert(admin);
alert(1000 + "108");//Будет 1000108, так при сложение ищет в строки и если хоть в одном
                    // аргументе не чило, то рассматривает выражение, как строку.
//async	Порядок загрузки(кто загрузится первым, тот и сработает).
        //Не имеет значения.Может загрузиться и выполниться до того,
        // как страница полностью загрузится.Такое случается, 
        //если скрипты маленькие или хранятся в кеше, а документ достаточно большой.
//defer	Порядок документа(как расположены в документе).Выполняется после того,
    // как документ загружен и обработан(ждёт), непосредственно перед DOMContentLoaded.
    //Пользователь может знакомиться с содержимым страницы, читать её, 
    //но графические компоненты пока отключены.