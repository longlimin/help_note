

angular.module('com.common')



.directive('qrcodeImg', ['CcssoService', function(CcssoService ){
    return {
        restrict: 'E',
        link: function (scope, element, attr) {
            var url = CcssoService.getQrcodeUrl();
            element.attr("src", url);

            scope.$on('$ReloadQrcode', function () {
                url = CcssoService.getQrcodeUrl();
                element.attr("src", url);
            });
        }
    }
}])

.directive('previewDirective', ['$document','$window', function ($document,$window) {
    return {
        restrict: "EA",
        templateUrl: "common/template/previewImage.html",
        scope: {
            imageList: "=",
            current: "=",
            config: "="
        },
        link: function (scope, element, attr) {

            scope.download = function (event,url) {
                if(url){
                    $window.open(url);
                }
            }

            function changeImage(event) {
                switch (event.keyCode) {
                    case 38:
                    case 37:
                        scope.actions.prev();
                        break;
                    case 40:
                    case 39:
                        scope.actions.next();
                        break;
                    case 27:
                        scope.actions.close()
                }
                scope.$digest(), event.preventDefault(), event.stopPropagation();
            }

            function scaleSize(e) {
                var t, o;
                if (e.scale) t = e.scale, o = {
                    x: .5,
                    y: .5
                };
                else {
                    var n = e.delta;
                    o = e.posRatio || {
                        x: .5,
                        y: .5
                    }, t = y.scale, t = n > 0 ? t + S : t - S
                }
                t = t > w ? w : 1 / w > t ? 1 / w : t;
                var r = {
                    width: Math.round(M.width * t),
                    height: Math.round(M.height * t),
                    scale: t
                };
                r.top = Math.round(y.top - o.y * (r.height - y.height)), r.left = Math.round(y.left - o.x * (r.width - y.width)), y = r, imgDom.css(r)
            }

            function extend(e) {
                angular.extend(y, e), imgDom.css(e)
            }

            function l(e) {
                extend({
                    top: e.clientY - C.y + v.top,
                    left: e.clientX - C.x + v.left
                }), e.preventDefault();
            }

            function scaleImage(e) {
                switch (e.keyCode) {
                    case 107:
                    case 187:
                        scaleSize({
                            delta: 1
                        });
                        break;
                    case 109:
                    case 189:
                        scaleSize({
                            delta: -1
                        })
                }
                e.preventDefault(), e.stopPropagation();
            }

            function move() {
                imgDom.on("mousedown", function (e) {
                    return N ? void n.actions.close() : (C = {
                        x: e.clientX,
                        y: e.clientY
                    }, v = {
                        top: y.top,
                        left: y.left
                    }, imgOprContainer.css("display", "none"), imgDom.on("mousemove", l), void e.stopPropagation());
                }).on("mouseup", function () {
                    imgDom.off("mousemove", l), imgOprContainer.css("display", "block")
                }).on(P, function (e) {
                    var t, o = e.originalEvent;
                    ("mousewheel" == o.type || "DOMMouseScroll" == o.type) && (t = o.wheelDelta ? o.wheelDelta / 120 : -(o.detail || 0) / 3), void 0 !== t && (scaleSize(N ? {
                        delta: t
                    } : {
                        delta: t,
                        posRatio: {
                            x: o.offsetX / y.width,
                            y: o.offsetY / y.height
                        }
                    }), e.preventDefault(), e.stopPropagation());
                }), $document.keydown(scaleImage);
            }

            function uploadImage() {
                var srcUrl;
                var imgUrl = scope.imageList[scope.current];
                var t = new Image;

                scope.currentImageUrl = imgUrl; 
                scope.isLoaded = !1, scope.rotateDeg = 0, imgUrl && (scope.containerStyle = {
                    // background: "url(" + imgUrl + ") no-repeat center center",
                    "background-size": "auto"
                });
                t.onload = function () {
                    t.onload = null, M = {
                        width: t.width,
                        height: t.height
                    }, y = {
                        width: M.width,
                        height: M.height,
                        top: (height - M.height) / 2,
                        left: (documentWidth - M.width) / 2,
                        scale: 1
                    };
                    var e = T / t.height,
                        o = b / t.width;
                    1 > e && 1 > o ? scaleSize({
                        scale: o > e ? e : o
                    }) : 1 > e ? scaleSize({
                        scale: e
                    }) : 1 > o ? scaleSize({
                        scale: o
                    }) : imgDom.css(y), angular.extend(E, y), imgPreview[0].src = t.src, scope.isLoaded = !0, scope.containerStyle = null, scope.$digest();
                }, t.onerror = function () {
                    t.onerror = null;
                },
                    t.src = srcUrl;
            }

            var imgDom = element.find("#img_dom"),
                imgOprContainer = element.find("#img_opr_container"),
                imgPreview = imgDom.find("#img_preview"),
                documentWidth = document.documentElement.clientWidth,
                height = document.documentElement.clientHeight - parseInt(imgOprContainer.css("bottom")) - parseInt(imgOprContainer.height());
            scope.isLoaded = !1, scope.rotateDeg = 0, scope.actions = {
                next: function (event) {
                    scope.current < scope.imageList.length - 1 && (scope.current++, uploadImage());
                    if (event) {
                        event.stopPropagation();
                    }
                },
                prev: function (event) {
                    scope.current > 0 && (scope.current--, uploadImage());
                    if (event) {
                        event.stopPropagation();
                    }
                },
                rotate: function (event) {
                    scope.rotateDeg = (scope.rotateDeg + 90) % 360, scope.reflowFlag = !scope.reflowFlag;
                    event.stopPropagation();
                },
                close: function () {
                    element.remove(), scope.$destroy();
                }
            }, scope.$on("$destroy", function () {
                $document.unbind("keyup", changeImage), $document.unbind("keydown", scaleImage)
            }), $document.keyup(changeImage);
            var M, y, C, v, w = 5,
                S = .1,
                b = .8 * documentWidth,
                T = .8 * height,
                E = {},
                N = void 0 !== document.mozHidden,
                P = N ? "DOMMouseScroll" : "mousewheel";
            imgDom.bind("click", function (event) {
                event.stopPropagation();
            });
            imgOprContainer.bind("click", function (event) {
                event.stopPropagation();
            });
            $("#preview_container").on("click", function () {
                scope.actions.close()
            });
            uploadImage(), move();
        }
    };
}])

.directive('myvideo', ['baseService', function(baseService ){
    return {
        restrict: 'E',
        templateUrl: "common/template/myvideo.html",
        replace: true,
        transclude: true,
        scope: {},
        link: function (scope, element, attr) {
            info('myvideo link');
            

            scope.src = '/resource/video/mv.ogv';


            // var player = videojs('myvideo', { }, function () {
            //     console.log('Good to go!');
            //     //this.play(); // if you don't trust autoplay for some reason
            // });
            // player.on('play', function () {
            //     console.log('开始/恢复播放');
            // });
            // player.on('pause', function () {
            //     console.log('暂停播放');
            // });
            // player.on('ended', function () {
            //     console.log('结束播放');
            // });
            // player.on('timeupdate', function() {
            //     console.log(player.currentTime());
            //     // 如果 currentTime() === duration()，则视频已播放完毕
            //     if (player.duration() != 0 && player.currentTime() === player.duration()) {
            //             // 播放结束
            //     }
            // });
            
        }
    }
}])









