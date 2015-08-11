(function (window, angular, undefined) {
  "use strict";

  function ExerciseFactory() {
    return function (data) {
      _.forEach(data.exercises, function (exercise) {
        // Extract utility data...
        exercise._utility = _.findWhere(data.utilities, {id: exercise.utility});

        // Extract mechanics data...
        exercise._mechanics = _.findWhere(data.mechanics, {id: exercise.mechanics});

        // Extract force data...
        exercise._force = _.findWhere(data.forces, {id: exercise.force});

        // Extract muscle data...
        exercise._muscle = _.findWhere(data.muscles, {id: exercise.muscle});
      });

      return data.exercises;
    };
  }

  function exerciseService($http, BASE_URL) {
    this.list = function list() {
      return $http.get(BASE_URL + "exercises/");
    };

    this.retrieve = function retrieve(id) {
      return $http.get(BASE_URL + "exercises/" + id + "/");
    };
  }

  angular.module("app")
    .factory("ExerciseFactory", [ExerciseFactory])
    .service("exerciseService", ["$http", "BASE_URL", exerciseService]);

})(window, window.angular);