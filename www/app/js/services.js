(function (window, angular, undefined) {
  "use strict";

  function exerciseService($http, BASE_URL) {
    this.list = function list() {
      return $http.get(BASE_URL + "exercises/");
    };

    this.retrieve = function retrieve(id) {
      return $http.get(BASE_URL + "exercises/" + id + "/");
    };
  }

  angular.module("app")
    .service("exerciseService", ["$http", "BASE_URL", exerciseService]);

})(window, window.angular);