/*Предположим, есть сущность корзины. Нужно реализовать функционал подсчета стоимости корзины в зависимости
 от находящихся в ней товаров. Товары в корзине хранятся в массиве. Задачи:
a) Организовать такой массив для хранения товаров в корзине;
b) Организовать функцию countBasketPrice, которая будет считать стоимость корзины. */
"use strict";
var shopping_cart = [[2, 20]];
function countBasketPrice(shopping_cart) {
    var i = 0, shopping_cash = 0;
    while (i < shopping_cart.length) {
        shopping_cash += shopping_cart[i][0] * shopping_cart[i][1];
        i++;
    }
    return shopping_cash;
}
alert('Стоимость корзины: ' + countBasketPrice(shopping_cart));