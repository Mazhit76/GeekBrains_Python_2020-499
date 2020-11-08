/*Предположим, есть сущность корзины. Нужно реализовать функционал подсчета стоимости корзины в зависимости
 от находящихся в ней товаров. Товары в корзине хранятся в массиве. Задачи:
a) Организовать такой массив для хранения товаров в корзине;
b) Организовать функцию countBasketPrice, которая будет считать стоимость корзины. 
3.1. В прошлом домашнем задании вы реализовали корзину на базе массивов. Какими объектами можно заменить их элементы?
3.2. Реализуйте такие объекты.
3.3. Перенести функционал подсчета корзины на объектно-ориентированную базу.*/
"use strict";
//var shopping_cart = [[2, 20]];
/*function countBasketPrice(shopping_cart) {
    var i = 0, shopping_cash = 0;
    while (i < shopping_cart.length) {
        shopping_cash += shopping_cart[i][0] * shopping_cart[i][1];
        i++;
    }
    return shopping_cash;
}
alert('Стоимость корзины: ' + countBasketPrice(shopping_cart));
*/

var basketPurcase = {
    userBye: [
        {
            id: 1,
            namePurcase: 'Рубашка',
            quantity: 2,
            price: 1500,
            totalPrice: 0,
        }
    ],
    countTotalPrice(i) {
        //return price1 * quan;
        //userBye.totalPrice = userBye.quantity * userBye.price;
        return this.userBye[i].totalPrice = this.userBye[i].quantity * this.userBye[i].price;

    },
}
//alert(basketPurcase.countTotalPrice(basketPurcase.userBye[0].price, basketPurcase.userBye[0].quantity));
alert(basketPurcase.countTotalPrice(0));
