angular.module('mathApp')
.controller('LoginController', function($scope, $location, AuthService) {
  $scope.user = { username: '', password: '' };
  $scope.error = '';

  $scope.login = function() {
    if (AuthService.login($scope.user)) {
      $location.path('/inicio');
    } else {
      $scope.error = 'Usuario o contraseña incorrectos.';
    }
  };
});
