angular.module('mathApp')
.controller('LoginController', function($scope, $location) {
  $scope.user = { username: '', password: '' };
  $scope.error = '';

  $scope.login = function() {
    fetch('http://localhost/7A/AS/parcial3/proyectoMatematicas/appServidor/login.php', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify($scope.user)
    })
    .then(res => res.json())
    .then(data => {
      if (data.status === "ok") {
        $location.path('/inicio');
        $scope.$apply();
      } else {
        $scope.error = data.message;
        $scope.$apply();
      }
    })
    .catch(err => {
      $scope.error = "Error de conexión con el servidor.";
      $scope.$apply();
    });
  };
});
