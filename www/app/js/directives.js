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

  function workoutList() {
    return {
      restrict: "A",
      scope: {
        workouts: "=",
        selectedWorkout: "="
      },
      templateUrl: "/static/views/workout_list.html",
      controller: "WorkoutListController"
    };
  }

  function workoutDetail() {
    return {
      restrict: "A",
      scope: {
        selectedWorkout: "="
      },
      templateUrl: "/static/views/workout_detail.html",
      controller: "WorkoutDetailController"
    };
  }

  angular.module("app")
    .directive("exerciseList", [exerciseList])
    .directive("exerciseDetail", [exerciseDetail])
    .directive("workoutList", [workoutList])
    .directive("workoutDetail", [workoutDetail]);

})(window, window.angular);