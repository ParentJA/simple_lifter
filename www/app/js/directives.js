(function (window, angular, undefined) {
  "use strict";

  function exerciseList() {
    return {
      restrict: "A",
      scope: {
        exercises: "=",
        selectedExercise: "="
      },
      templateUrl: "/static/views/exercise_list.html",
      controller: "ExerciseListController"
    };
  }

  function exerciseDetail() {
    return {
      restrict: "A",
      scope: {
        selectedExercise: "="
      },
      templateUrl: "/static/views/exercise_detail.html",
      controller: "ExerciseDetailController"
    };
  }

  angular.module("app")
    .directive("exerciseList", [exerciseList])
    .directive("exerciseDetail", [exerciseDetail]);

})(window, window.angular);