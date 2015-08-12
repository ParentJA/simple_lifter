(function (window, angular, undefined) {
  "use strict";

  function MainController($scope) {}

  function HomeController($scope) {}

  function ExerciseController($scope, ExerciseFactory, exerciseService) {
    $scope.models = {
      exercises: undefined,
      selectedExercise: undefined
    };

    $scope.getExercises = function getExercises() {
      exerciseService.list().then(function (response) {
        $scope.models.exercises = new ExerciseFactory(response.data);
        $scope.models.selectedExercise = _.first($scope.models.exercises);
      });
    };

    function init() {
      $scope.getExercises();
    }

    init();
  }

  function ExerciseListController($scope) {
    $scope.isSelectedExercise = function isSelectedExercise(exercise) {
      return $scope.selectedExercise === exercise;
    };

    $scope.setSelectedExercise = function setSelectedExercise(value) {
      return $scope.selectedExercise = value;
    };

    $scope.hasExercises = function hasExercises() {
      return !_.isEmpty($scope.exercises);
    };
  }

  function ExerciseDetailController($scope) {}

  angular.module("app")
    .controller("MainController", ["$scope", MainController])
    .controller("HomeController", ["$scope", HomeController])
    .controller("ExerciseController", ["$scope", "ExerciseFactory", "exerciseService", ExerciseController])
    .controller("ExerciseListController", ["$scope", ExerciseListController])
    .controller("ExerciseDetailController", ["$scope", ExerciseDetailController]);

})(window, window.angular);