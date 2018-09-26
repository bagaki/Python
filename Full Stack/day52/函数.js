// function foo(a, b) {
//     console.log("a",a);
//     console.log("b",b);
//     return a+b
// }

// 匿名函数
// var func = function (a, b) {
//     console.log("a",a);
//     console.log("b",b);
//     return a+b
// };


// 立即执行函数
// (function (a, b) {
//     console.log('立即执行函数');
//     console.log(a+b);
// })(12, 22);

// var ret = foo(11, 22);
// console.log("a+b=", ret);
//
// var ret1 = func(12, 23);
// console.log("a+b=", ret1);


// arguments
// function foo1(a, b) {
//     // console.log("a",a);
//     // console.log("b",b);
//     console.log(arguments.length);
//     var ret = 0;
//     for (var i = 0; i < arguments.length; i++){
//         ret += arguments[i]
//     }
//     return ret;
// }

// console.log("arguments: ", foo1(11, 22));

// var city = "Beijing";
// function Bar(){
//     console.log(city);
// }
//
// function f() {
//     var city = "Shanghai";
//     return Bar
// }
//
// var ret = f()
// ret()

// // 闭包
// var city = "Beijing";
// function f() {
//     var city = "Shanghai";
//     function inner(){
//         console.log(city);
//     }
//     return inner;
// }
// var ret = f();
// ret();


// JS中的词法分析
// var age = 18;
// function func3() {
//     console.log(age);
//     var age = 22;
//     console.log(age);
// }
//
//
// func3();


var age = 18;
function foo() {
    console.log("kakaka")
    var age = 22;
    console.log(age)
    function age() {
        console.log("hahah")
    }
    console.log(age)
}


foo();
