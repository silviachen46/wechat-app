// index.js

Page({
  
      onClick() {
          wx.navigateTo({
            url: '../../pages/form/form',
          })
        }
      ,
      data: {
        list:[]
      },
    
      
      onClick2 (e) {
        
          wx.request({
              url: 'http://localhost:5000/food',
              //header:{'Content-Type':'application/json;charset=utf-8'},
              method: 'GET',
              success:(res)=>{
                this.setData({
                  list:res.data
                }) 
        
              },
            //   success:function(res){
            //     var datalist=res.data.datalist
            //     call_back(datalist)  
                
            //  }
          })
      },
      
      
  })
  
  
  // that.setData({
  //   food_name:res.data,
  //   mass:res.data,
  //   date_till:res.data
  // }) 

  //'../../pages/form/form'
