(function (window, angular, undefined) {
  "use strict";

  function exerciseService($http, BASE_URL) {

  }

  angular.module("app")
    .service("exerciseService", ["$http", "BASE_URL", exerciseService]);

})(window, window.angular);