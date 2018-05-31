(function() {
    'use strict';

    angular.module('qingye',['ui-router'])
        .config(stateConfig);

    stateConfig.$inject = ['$stateProvider','$UrlRouterProvider'];

    function stateConfig($stateProvider,$UrlRouterProvider) {
    	$UrlRouterProvider.otherwise('/home');
        $stateProvider.state('home', {
            url: '/home',
            data: {
                authorities: []
            },
            views: {
                'content@': {
                    templateUrl: 'home/home.html',
                    controller: 'HomeController',
                    controllerAs: 'vm'
                }
            }
        });
        $stateProvider.state('comprehension',{
        	url:'/comprehension',
        	data:{
        		authorities:[]
        		},
        	views:{
        		'content@':{
        			templateUrl:'comprehension/comprehension.html',
        			controller:'ComprehensionController',
        			controllerAs:'vm'
        		}
        	}
        });
    }
})();
