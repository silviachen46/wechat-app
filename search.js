// pages/search/search.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        inputValue: "",
        scrollIndex: 0,
        totalNum: 4,
        startY: 0,
        startTime: 0,
        endY: 0,
        endTime: 0,
        critical: 80,
        maxTimeCritical: 300,
        minTimeCritical: 100,
        marginTop: 0,
        currentTarget: null,
        menus: [],
    },

    searchQuery: function(e) {
        this.setData({
            inputValue: e.detail.value
        })
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

    },
    menuClick: function(e){

        var menu = e.currentTarget.dataset.bean // e.currentTarget
        console.log(menu)
        if (menu){
            wx.navigateTo({
                url: '../../pages/menu/menu?menuId=' + menu.menu_id + '&menuUrl=' + encodeURIComponent(menu.url),
              })
    
        }
    },
    searchClick: function() {
        const parent = this
        wx.showLoading({
            title: "搜索中",
        })
        queryString = "query=" + this.data.inputValue,
        url = 'http://localhost:5000/menu?' + queryString
        console.log(url)
        wx.request({
            url: url,
            method: 'GET',
            success: function(res) {
                wx.hideLoading()
                parent.setData({
                    menus: res.data
                })
                console.log("返回成功的数据:" + parent.data.menus)
                console.log("返回成功的数据:" + JSON.stringify(res.data))
            },
            fail: function(fail) {

            },
            complete: function(arr) {

            }
        })
    }

})

// Component({
//     methods: {
        

//         scrollTouchStart: function (e) {
//             let py =  e.touches[0].pageY,
//             stamp =  e.timeStamp,
//             currentTarget = e.currentTarget.id;
//             console.log(py);
//             this.setData({
//                 startY:  py,
//                 startTime: stamp,
//                 currentTarget: currentTarget
//             })
//         },
            
//         scrollTouchMove(e) {
                
//         },
            
//         scrollTouchEnd: function (e) {
//             let py =  e.changedTouches[0].pageY,
//             stamp =  e.timeStamp,
//             d =  this.data,
//             timeStampdiffer = stamp - d.startTime;
//             this.setData({
//                 endY:  py,
//                 endTime:  stamp
//             })
//         },
//     },
// })