// pages/search/search.js
Page({
    data: {
        inputValue:"",
      },

    searchQuery: function(e) {
        var val3 = e.detail.value;
        this.setData({
          inputValue: val3,
        });
      },
    
    //this.data.inputValue
    searchClick: function (e) {
      queryString ="query="+this.data.inputValue
      url='http://localhost:5000/menu?'+queryString
      //console.log(url)
        wx.request({
            url: url,
            method: 'GET',
            success: (res) => {
				console.log(res)
            }
        })
    }
})

//http://localhost:5000/food?query=test&query=3

