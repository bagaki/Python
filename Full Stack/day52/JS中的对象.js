// JS中自定义对象
//
// var person = {"name":"小强","age":18}; // JS的对象中，键（属性）默认不加引号，并且自动把单引号变成双引号
// console.log(person);
//
// // 单独取对象的属性
// console.log("name:"+person.name);
// console.log("age:" +person.age);
//
// // 遍历对象的属性
// for (var i in person){
//     console.log(person[i]);
// }


// Date对象
// var d1 = new Date();
// console.log(d1);
// console.log(typeof d1);
// console.log(d1.toLocaleString());
// console.log(typeof d1.toLocaleString());
//
// // 生成指定时间的date对象
// var d2 = new Date("2014/3/22 11:22:33");
// console.log(d2.toLocaleString());  // 转成字符串格式的本地时间
// console.log(d2.toUTCString());


// JSON对象
 var s = '{"name":"小强","age":18}';
// 把字符串转换程JS内部的对象
var ret = JSON.parse(s);
console.log(ret);
// 把JS内部的对象转换程字符串
var s1 = JSON.stringify(ret);
console.log(s1);
console.log(typeof s1);


// RegExp对象 --> Python re模块
// 生产 RegExp对象
var reg1 = new RegExp("^[a-zA-Z][a-zA-Z0-9_]{5,11}$");
var regexpRet1 = reg1.test("xiaoqiang");
console.log(regexpRet1);

var regexpRet2 = reg1.test("1xiaoqiang");
console.log(regexpRet2);

console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test("1xiaoqiang"));

// 坑1（正则表达式中间一定不可以有空格）

// 坑2 test()不传值相当于传了一个undefined进去，然后test()就把这个undefined当成字符串来判断


// JS正则的两种模式
// 1.g 表示全局
// 2.i 忽略大小写
var ss = "bagaki";
var s3 = ss.replace(/a/, "kakaka");
console.log(s3);

// 坑3
// 当正则表达式使用了全局模式（g）的时候，并且还让它检测一个字符串，此时会引出一个lastIndex
// lastIndex会记住上一次匹配成功的位置，并把下一次要开始校验的位置记住