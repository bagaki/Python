// pages/details/details.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    showModalStatus: false,
    list: [
      {
        id: 0,
        name: "HTML基础",
        introduce: "简介：HTML语言是一种规范，通过标签告诉浏览器如何显示其中内容。",
        src: "https://static1.bcjiaoyu.com/c2.png",
        showModalStatus: false,
        catalog: [
          { section: "1.HTML介绍" }, { section: "2.标题" },
          { section: "3.分割线" }, { section: "4.文字段落" }, { section: "5.斜体字" }, { section: "6.粗体字" },
          { section: "7.下划线字" }, { section: "8.图片" },
          { section: "9.无序列表" }, { section: "10.有序列表" }, 
          { section: "11.表格" }, { section: "12.视频" },
          { section: "13.链接" }, { section: "14.HTML完整结构" }
        ]
      },
      {
        id: 1,
        name: "CSS 基础",
        introduce: "简介:CSS 层叠样式表。对网页中的元素排版进行精确控制，修饰网页。",
        src: 'https://static1.bcjiaoyu.com/c4.png',
        showModalStatus: false,
        catalog: [
          { section: "1. CSS介绍" },
          { section: "2. 字体颜色" },
          { section: "3. 元素宽高" },
          { section: "4. 背景颜色及字体大小" },
          { section: "5. 边框" },
          { section: "6. 边距" },
          { section: "7. 表格边框" }
        ]
      },
      {
        id: 2,
        name: "HTML+CSS 进阶",
        introduce: "简介:HTML+CSS的综合运用课程，讲解更多的样式效果。",
        src: 'https://static1.bcjiaoyu.com/c5.png',
        showModalStatus: false,
        catalog: [
          { section: "1. padding-top" },
          { section: "2. font-family" },
          { section: "3. text-align" },
          { section: "4. float" },
          { section: "5. position" },
          { section: "6. div" },
          { section: "7. 个人网页(一)" },
          { section: "8. 个人网页(二)" },
          { section: "9. 个人网页(三)" },
          { section: "10. 个人网页(四)" }
        ]
      },
      {
        id: 3,
        name: "HTML&CSS高级课程",
        introduce: "简介:HTML&CSS的高级课程",
        src: 'https://static1.bcjiaoyu.com/c2.png',
        showModalStatus: false,
        catalog: [
          { section: "暂无目录数据" }
        ]
      },
      {
        id: 4,
        name: "JavaScript 基础",
        introduce: "简介:JS是广泛用于客户端的脚本语言，用来给HTML网页增加动态功能。",
        src: 'https://static1.bcjiaoyu.com/c3.png',
        showModalStatus: false,
        catalog: [
          { section: "1. JavaScript介绍" },
          { section: "2. 变量和字符串" },
          { section: "3. JavaScript DOM" },
          { section: "4. 函数" },
          { section: "5. 事件" },
          { section: "6. 综合项目" }
        ]
      },
    ]
  },

  powerDrawer: function (e) {
    var currentStatu = e.currentTarget.dataset.statu;
    var index = e.currentTarget.id;

    // 关闭
    if (currentStatu == "close") {
      this.data.list[index].showModalStatus = false;
      this.setData({
        showModalStatus: false,
        list: this.data.list,
      });
    }

    // 显示
    if (currentStatu == "open"){
      this.data.list[index].showModalStatus = true;
      this.setData({
        showModalStatus: true,
        list: this.data.list,
      });
    }
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})