new Vue({
    el:'#vuee',
    data:{
      login:false,
      view:false,
      transac:false,
      delet:false,
      update:false,
      updateForm:false
    },
    methods:{
      logrev:function(){
        this.login=!this.login;
        this.view=false;
        this.transac=false;
        this.delet=false;
        this.update=false;
        this.updateForm=false;
      },
      viewAll:function(){
        this.login=false;
        this.view=!this.view;
        this.transac=false;
        this.delet=false;
        this.update=false;
        this.updateForm=false;
      },
      transactionn:function(){
        this.login=false;
        this.view=false;
        this.transac=!this.transac;
        this.delet=false;
        this.update=false;
        this.updateForm=false;
      },
      deletControl:function(){
        this.login=false;
        this.view=false;
        this.transac=false;
        this.delet=!this.delet;
        this.update=false;
        this.updateForm=false;
      },
      
      deletee:function(inp){
        alert("Item has been "+inp+"!")
      }
    }
  })