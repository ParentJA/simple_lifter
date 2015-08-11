(function (window, angular, undefined) {
  "use strict";

  function MainController($scope) {

  }

  function HomeController($scope, ExerciseDTD, exerciseService) {
    $scope.models = {
      exercises: [ExerciseDTD],
      selectedExercise: ExerciseDTD
    };

    $scope.getExercises = function getExercises() {
      exerciseService.list().then(onLoadSuccess);

      function onLoadSuccess(response) {
        $scope.models.exercises = response.data;
      }
    };

    $scope.getExercise = function getExercise(id) {
      exerciseService.retrieve(id).then(onLoadSuccess);

      function onLoadSuccess(response) {
        $scope.models.selectedExercise = response.data;
      }
    };

    $scope.hasExercises = function hasExercises() {
      return !_.isEmpty($scope.models.exercises);
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
    .controller("HomeController", ["$scope", "ExerciseDTD", "exerciseService", HomeController]);

})(window, window.angular);