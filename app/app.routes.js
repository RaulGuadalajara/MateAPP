angular.module('mathApp')
.config(function($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'app/views/login.html',
      controller: 'LoginController'
    })
    .when('/inicio', {
      templateUrl: 'app/views/home.html',
      controller: 'HomeController'
    })
    .otherwise({
      redirectTo: '/'
    });
});
