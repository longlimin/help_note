


angular.module('com.common')


.filter("videoUrl", ['$sce', '$ADDR_LOCAL', function ($sce, $ADDR_LOCAL) {
    return function (recordingUrl) {
        recordingUrl = $ADDR_LOCAL + '/' + recordingUrl;
        return $sce.trustAsResourceUrl(recordingUrl);
    };
}])

//list map cols决定顺序 列求和 生成list<string> [0, 998]
.filter('getSumsList', [function() {
    return function(httplist, cols){
        var sums = []; 
        
        if(httplist){
            for(var key in cols){
                sums.push(0) ;
            }
            for(var i = 0; i < httplist.length; i++){
                var item = httplist[i];
                var j = 0;
                for(var key in cols){
                    sums[j] = toInt(sums[j]) + toInt(item[key]);
                    j++;
                }
            }
        }
        return sums;
    };
}])
//list map 列求和 生成map {'key1sum':0, 'key2sum':998}
.filter('getSumsMap', [function() {
    return function(httplist){
        var sums = {}; 
    
        if(httplist)
            angular.forEach(httplist, function(item){
                for(var key in item){
                    sums[key] = toInt(sums[key]) + toInt(item[key]) ;
                };
            });

        return sums;
    };
}])
//list<map>  map筛选
.filter('mapSearch', function(){
    return function(list, search){
        if(! isNotNull(search)) 
            return list;

        var res = [];
        for(var i = 0; i < list.length; i++){
            var flag = true;
            for(var key in search){
                if(search[key] && list[i][key] && list[i][key].indexOf(search[key]) < 0 ){//都不为null 且不包含 则一票否决
                    flag = false;
                    break;
                } 
            }   
            if(flag){
                res.push(list[i]);
            } 
        }
        
        return res;
    };

})

.filter('getNameFirstUpperChar', [function() {
    return function(str){
        var res = '-';
        if(str){
            res = str.substr(0, 1);
        }
        return res.toUpperCase();
    };
}])
//显示多长时间之前
.filter('timeAgo',function(){
    return function (time_ago, accuracy, time_now) {
        var timeAgo = {
            execute: function (time_ago, accuracy, time_now) {
                var difference, grouped_difference;
                // Validation
                if (time_ago === undefined || time_ago === null) {
                    return null;
                }
                if (accuracy < 1) {
                    return null;
                }
                // Default values
                var type = typeof(time_ago);
                if (type == 'string') {
                    time_ago = time_ago.substring(0, 19);
                    time_ago = new Date(time_ago.replace(/-/g, "/"));
                } else {
                    time_ago = new Date(time_ago);
                }
                if (accuracy === undefined || accuracy === null) {
                    accuracy = 1;
                }
                if (time_now === undefined || time_now === null) {
                    time_now = new Date();
                } else {
                    time_now = new Date(time_now);
                }
                // Calculation
                difference = this.calculateDifference(time_now, time_ago);
                if (difference === 0) {
                    return '刚刚';
                }
                grouped_difference = this.groupDifference(difference);
                grouped_difference = this.applyAccuracy(grouped_difference, accuracy);
                return this.toString(grouped_difference, (time_ago > time_now));

            },
            calculateDifference: function (now, ago) {
                return Math.abs(Math.round((now - ago) / 1000));
            },
            groupDifference: function (difference) {
                var grouped_difference = [],
                    second_groups = {
                        "年": 365 * 24 * 60 * 60,
                        "月": 31 * 24 * 60 * 60,
                        "周": 7 * 24 * 60 * 60,
                        "天": 24 * 60 * 60,
                        "小时": 60 * 60,
                        "分钟": 60,
                        "秒": 1
                    },
                    group,
                    group_seconds,
                    group_count,
                    group_string;
                // Iterate through and build an array of preformatted strings
                for (group in second_groups) {
                    group_seconds = second_groups[group];
                    group_count = Math.floor(difference / group_seconds);
                    group_string = this.formatGroup(group_count, group);
                    // Add the null values after the first group
                    // so that the accuracy is for all groups, and not only the
                    // groups with a value
                    if (group_string !== null || grouped_difference.length > 0) {
                        grouped_difference.push(group_string);
                    }
                    difference -= group_count * group_seconds;
                }
                return grouped_difference;
            },
            formatGroup: function (quantity, group_name) {
                if (quantity < 1) {
                    return null;
                }
                //var plural = (quantity > 1) ? 's' : '';
                return quantity + ' ' + group_name;
            },
            applyAccuracy: function (grouped_difference, accuracy) {
                grouped_difference.length = Math.min(grouped_difference.length, accuracy);
                return grouped_difference;

            },
            toString: function (grouped_difference, in_future) {
                var string;
                grouped_difference = this.removeNullValues(grouped_difference);
                string = this.joinArray(grouped_difference);
                return (in_future) ? 'in ' + string : string + '前';
            },
            removeNullValues: function (array) {
                var i, clean_array = [];
                for (i = 0; i !== array.length; i++) {

                    if (array[i] !== null) {
                        clean_array.push(array[i]);
                    }
                }
                return clean_array;
            },
            joinArray: function (array) {
                if (array.length === 1) {
                    return array[0];
                }
                return array.slice(0, -1).join(' ') + ' and ' + array[array.length - 1];
            }
        };
        return timeAgo.execute(time_ago, accuracy, time_now);
    };
}) 







