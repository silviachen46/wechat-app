Upgrade:function(e){
    wx.request({
    url: 'http://localhost:5000/food',
    data: {
        food_name: 'test100'
    },
    method: 'POST',
    success: (res) => {
        console.log(res)
    }
})},