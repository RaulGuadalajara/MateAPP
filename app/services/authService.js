
angular.module('mathApp')
.factory('AuthService', function() {
  const userData = { username: 'admin', password: '1234' };

  return {
    login: function(user) {
      return user.username === userData.username && user.password === userData.password;
    }
  };
});
