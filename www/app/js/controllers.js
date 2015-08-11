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

    $scope.hasExercises = function hasExercises() {
      return !_.isEmpty($scope.models.exercises);
    };

    $scope.isSelectedExercise = function isSelectedExercise(exercise) {
      return $scope.models.selectedExercise === exercise;
    };

    $scope.getSelectedExercise = function getSelectedExercise() {
      return $scope.models.selectedExercise;
    };

    $scope.setSelectedExercise = function setSelectedExercise(value) {
      return $scope.models.selectedExercise = value;
    };

    function init() {
      $scope.getExercises();
    }

    init();
  }

  angular.module("app")
    .controller("MainController", ["$scope", MainController])
    .controller("HomeController", ["$scope", HomeController])
    .controller("ExerciseController", ["$scope", "ExerciseFactory", "exerciseService", ExerciseController]);

})(window, window.angular);