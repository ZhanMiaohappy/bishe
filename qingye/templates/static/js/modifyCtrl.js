(function () {
    'use strict';
    angular.module('modifyApp',[])
    .controller('modifyCtrl',function ($scope) {
      $scope.userdata={},

      $scope.submitForm=function(){
        console.log("$scope.userdata");
      }
    });
})();