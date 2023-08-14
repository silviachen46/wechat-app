// pages/form/form.js
Page({
    data: {
        food_id:"",
        food_name: "",
        date_till:"",
        mass:"",
        
      },
    bindDateChange: function(e) {
        this.setData({
          date_till: e.detail.value,
        });
      },
    onTitleInput: function(e) {
        this.setData({
          food_name: e.detail.value
        });
      },  
      
    onDescInput: function(e) {
        var val1 = e.detail.value;
        this.setData({
          mass: val1
        });
      },  
    save(e) {
        wx.request({
            url: 'http://localhost:5000/food',
            data: {
                ...this.data
            },
            header:{'Content-Type':'application/json;charset=utf-8'},
            method: 'POST',
            success: (res) => {
                console.log(res)
            }
        })
        wx.showToast({
            title:"提交成功!",
            icon:"success",
            duration:1500
        })
            
    },

    Delete(e) {
      wx.request({
          url: 'http://localhost:5000/food',
          //header:{'Content-Type':'application/json;charset=utf-8'},
          
          method: 'DELETE',
          success: (res) => {
              console.log(res)
          }
      })
      wx.showToast({
          title:"删除成功!",
          icon:"success",
          duration:1500
      })
          
  },
    
})