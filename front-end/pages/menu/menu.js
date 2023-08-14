// pages/form/form.js
Page({
    data: {
        menuId: 0,
        menuUrl: ''
    },
    onLoad: function(options) {
      // 生命周期函数--监听页面加载
      this.setData({
        menuId: options.menuId,
        menuUrl: decodeURIComponent(options.menuUrl)
      })
      console.log(this.data)

    }
  
})