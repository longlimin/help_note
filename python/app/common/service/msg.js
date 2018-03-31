








var SOCKET_MSG = "socket:msg"; //普通消息
var SOCKET_MV = "socket:mv";  //socket图片流
var SOCKET_SYSTEM= "socket:system";  //system控制


var _socketKeyName = "socket_key";


function SocketMake(key){
    var res = {};
    res[_socketKeyName] = key;
    return res;
}

//取出data消息中的 key 消息类型 操作编码
function SocketGetKey(data){
    return data[_socketKeyName];
}













