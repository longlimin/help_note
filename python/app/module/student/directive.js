 //分页模板
 angular.module('com.student') 
.directive('pageDiv', [ function () {
    return {
        restrict: 'AE',
        replace: true,
        templateUrl: "module/student/template/pageDiv.html",
        scope: {
            page: "=",
            pageNum: "=",
            pageFunc: "&"     //点击页码的回调函数
        },
        link: function (scope, element, attrs) {
            var pageNum = scope.pageNum;
            var startPage = 1;
            var pageArr = [], allPages;
            scope.$watch(function () {
                if (scope.page) {
                    return scope.page.PAGES;
                }
                return null;
            }, function (pages) {
                if (pages) {
                    allPages = pages;
                    if (allPages > pageNum) {
                        pageArr = range(pageNum);
                    } else {
                        pageArr = range(allPages);
                    }
                    scope.pageArr = pageArr;
                    scope.currPage = 1;
                }
            });

            scope.currPage = 1;
            // 当前页码
            scope.clickNumData = function (curNum) {
                scope.currPage = curNum;
                if (pageArr.length < pageNum) {
                    // 根据curNum取数据

                } else {
                    startPage = curNum - 5;
                    if (startPage < 1) {
                        startPage = 1;
                    }
                    if (startPage + 9 > allPages) {
                        startPage = allPages - 9;
                    }
                    if (startPage != pageArr[0]) {
                        pageArr = [];
                        for (var i = 0; i < pageNum; i++) {
                            pageArr[i] = startPage + i;
                        }
                        scope.pageArr = pageArr;
                    }
                }
                scope.$eval(scope.pageFunc)(curNum);
            };

            //上一页
            scope.prevPage = function () {
                if (scope.currPage == 1) {
                    return;
                }
                scope.currPage--;
                scope.clickNumData(scope.currPage);
            };
            //下一页
            scope.nextPage = function () {
                if (scope.currPage == allPages) {
                    return;
                }
                scope.currPage++;
                scope.clickNumData(scope.currPage);
            };
            //跳页
            scope.goPageNum = "";
            scope.goPage = function (goPage) {
                //验证输入项是否合法
                if (isNaN(goPage)) {
                    info("请输入正确的页码", "warning");
                    return false;
                } else {
                    if (goPage < 1 || goPage > scope.page.PAGES) {
                        info("请输入正确的页码", "warning");
                        return false;
                    }
                }
                scope.page.NOWPAGE = goPage;
                scope.goPageNum = "";
                scope.clickNumData(goPage);
            };

            // 监听input的回车事件
            scope.enterClick = function (page, event) {
                if (event.keyCode == 13) {
                    scope.goPage(page);
                }
            };

            /**
             * 创建空数组使ng-repeat可以循环数字
             * @param length
             * @returns {Array}
             */
            function range(length) {
                var numLength = parseInt(length);
                var lengthArr = new Array(numLength);
                for (var i = 0; i < lengthArr.length; i++) {
                    lengthArr[i] = i + 1;
                }
                return lengthArr;
            }
        }

    }
}])