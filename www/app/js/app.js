(function (window, angular, undefined) {
  "use strict";

  var ExerciseDTD = {
    id: undefined,
    name: undefined,
    _utility: {
      id: undefined,
      description: undefined
    },
    _mechanics: {
      id: undefined,
      description: undefined
    },
    _force: {
      id: undefined,
      description: undefined
    },
    _muscle: {
      id: undefined,
      description: undefined
    },
    preparation: undefined,
    execution: undefined
  };

  function HttpConfig($httpProvider) {
    $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
    $httpProvider.defaults.xsrfCookieName = "csrftoken";
  }

  function UiRouterConfig($stateProvider, $urlRouterProvider) {
    $stateProvider
      .state("home", {
        url: "/",
        templateUrl: "/static/views/home.html",
        controller: "HomeController"
      });

    //Default state...
    $urlRouterProvider.otherwise("/");
  }

  function UiRunner($rootScope, $state) {
    $rootScope.$state = $state;
  }

  angular.module("app", ["ui.router"])
    .constant("BASE_URL", "/api/v1/")
    .constant("ExerciseDTD", ExerciseDTD)
    .config(["$httpProvider", HttpConfig])
    .config(["$stateProvider", "$urlRouterProvider", UiRouterConfig])
    .run(["$rootScope", "$state", UiRunner]);

})(window, window.angular);