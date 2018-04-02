/*
    angular.foreach(cons, function(con, index))
    自带闭包                    
    //(function(index, tmpCon){
    
      })(ind, con)



*/
/*常用js jQuery 工具类*/

//true : not null    false : null or map all key-value is null
function isNotNull(obj){
    if(!obj) return false;

    if(typeof(obj) === 'object'){
        for(key in obj){
            if(obj[key]){
                return true;
            }
        }
        return false;
    }

    return true;
}

function resOk(result){
    return result ? true:false;
}
function openUrl(url){
    window.open(url);
    // window.location.href="http://www.100sucai.com/";     //在同当前窗口中打开窗口
    // window.open("http://www.100sucai.com/");                 //在另外新建窗口中打开窗口
}

function info(str){
    console.info(str);
 }
 
function error(obj) {   
    info("操作失败.obj=" ); 
    info(obj); 

} 


function toStr(json){
    return JSON.stringify(json);
}


/*

AngularJS事件大集合

ng-click ( 适用标签 ：所有，触发事件：单击)；

ngDblclick（ 适用标签 ：所有，触发事件：双击）；

ngBlur（适用标签 : a,input,select,textarea，触发事件：失去焦点）；

ngFocus（适用标签 : a,input,select,textarea，触发事件：获取焦点）；

ngChange（适用标签 : a,input,select,textarea，触发事件：model更新）；

ngkeydown（适用标签 : 所有，触发事件：键盘按键按下，要把$event传过去）；

ngKeyup（适用标签 :大部分用在input、textarea， 但适用所有标签，触发事件：键盘按键按下并松开，但要把$event 传过去）；

ngKeypress（同上）；

ngMousedown（适用标签 : 所有，触发事件：鼠标按下，左右中间都会触发）；

ngMouseup（适用标签 : a,input,select,textarea，触发事件：鼠标按下弹起，左右中间都会触发）；

ngMouseenter（适用标签 :所有，触发事件：鼠标进入）；

ngMouseleave（适用标签 :所有，触发事件：鼠标离开）；

ngMousemove（适用标签 :所有，触发事件：鼠标移动）；

ngMouseover（适用标签 :所有，触发事件：鼠标进入）；

注意：

所有标签均为驼峰命名法，但是用的时候要用小写的。如： 
ngClick，ngMouseover要写成ng-click，ng-mouseover的形式。
*/



/*<!-- 
int eachPageNum = defaulteachPageNum;//每页数量
int nowPage = 1;    //当前页码
int pageNum = 0;    //总页数
String order;   //排序
String desc;    //倒序 
-->*/
//共13页，当前第11页 -> 2-3 4 5-6 
function calcPage(PAGE){
    var now = PAGE.nowPage;
    var max = PAGE.pageNum;
    var deta = 2; 
    var from = 1;
    var to = max;

    if(now <= deta){
        from = 1;
        to = from + deta * 2;
        if(to > max){
            to = max;
        }
    }else if(now + deta > max){
        to = max;
        from = max - deta * 2;
        if(from < 1){
            from = 1;
        }
    }else{
        to = now + deta;
        from = now - deta;
    }

    var res =  getSeq(from, to);
    //info(res);
    return res;

 }
function getSeq(from, to){
    var res = [];
    for(var i = from; i <= to; i++){
        res[i-from] = i;
    }
    return res;
}


//data.option = $.extend({"yAxis":{}}, data.option )


function toolSetChart(id, option){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById(id)); 
    // 使用刚指定的配置项和数据显示图表。
    //清空画布，防止缓存
    myChart.clear();
    myChart.setOption(option); 
}

// title: {
//     text: title
// }, 
// legend: {
//     data: lineNames
// },
// xAxis: {
//     data: xNames
// }, 
// series: [ 
//     {
//         name: lineName,
//         type: 'line',
//         data: lineValues,
//     },
//     {
//         name: "num",
//         type: "bar",
//         data: lineValues,
//     },
// ]  


/*

jdbc执行sql 取出map的列顺序 与 sql取列顺序无关
而与别名长度有关###########
在查询echart需要的列相关xy轴数据集时注意


*/


function daata() {
    var date = new Date();

    date.getYear(); //获取当前年份(2位)
    date.getFullYear(); //获取完整的年份(4位)
    date.getMonth(); //获取当前月份(0-11,0代表1月)
    date.getDate(); //获取当前日(1-31)
    date.getDay(); //获取当前星期X(0-6,0代表星期天)
    date.getTime(); //获取当前时间(从1970.1.1开始的毫秒数)
    date.getHours(); //获取当前小时数(0-23)
    date.getMinutes(); //获取当前分钟数(0-59)
    date.getSeconds(); //获取当前秒数(0-59)
    date.getMilliseconds(); //获取当前毫秒数(0-999)
    date.toLocaleDateString(); //获取当前日期
    var mytime = date.toLocaleTimeString(); //获取当前时间
    date.toLocaleString(); //获取日期与时间

}

/**************************************时间格式化处理************************************/
//yyyy-MM-dd hh:mm:ss
function toDate(fmt,date)
{
    var o = {
        "M+" : date.getMonth()+1,                 //月份
        "d+" : date.getDate(),                    //日
        "h+" : date.getHours(),                   //小时
        "m+" : date.getMinutes(),                 //分
        "s+" : date.getSeconds(),                 //秒
        "q+" : Math.floor((date.getMonth()+3)/3), //季度
        "S"  : date.getMilliseconds()             //毫秒
    };
    if(/(y+)/.test(fmt))
        fmt=fmt.replace(RegExp.$1, (date.getFullYear()+"").substr(4 - RegExp.$1.length));
    for(var k in o)
        if(new RegExp("("+ k +")").test(fmt))
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
    return fmt;
}
//偏移天数
function getTheDay(fmt, deta){
    deta = deta && !isNaN(deta) ? parseInt(deta) : 0;
    deta = parseInt(deta);
    return toDate(fmt, new Date( (new Date()).getTime() + deta * 24 * 3600 * 1000));
}
function getTheDate(fmt, deta){
    var date = new Date( (new Date()).getTime() + deta);
    return getDateByTime(fmt, date);
}
function getDate(fmt){
    var date = new Date();
    return getDateByTime(fmt, new Date());
}
function getDateByTime(fmt, date)
{
    var o = {
        "M+" : date.getMonth()+1,                 //月份
        "d+" : date.getDate(),                    //日
        "h+" : date.getHours(),                   //小时
        "m+" : date.getMinutes(),                 //分
        "s+" : date.getSeconds(),                 //秒
        "q+" : Math.floor((date.getMonth()+3)/3), //季度
        "S"  : date.getMilliseconds()             //毫秒
    };
    if(/(y+)/.test(fmt))
        fmt=fmt.replace(RegExp.$1, (date.getFullYear()+"").substr(4 - RegExp.$1.length));
    for(var k in o)
        if(new RegExp("("+ k +")").test(fmt))
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
    return fmt;
}


//列求和统计汇总
function listSums(httplist, cols){
        var sums = {};

        for(var j = 0; j < cols.length; j++){
            sums[cols[j]] = 0;
        }
        for(var i = 0; i < httplist.length; i++){
            var item = httplist[i];
            for(var j = 0; j < cols.length; j++){
                var key = cols[j];
                sums[key] = toInt(sums[key]) + toInt(item[key]) ;
            }
        }
        return sums;
};
function toInt(value){
    return value && !isNaN(value) ? parseInt(value) : 0;
}


