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

  function WorkoutFactory() {
    return function (data) {
      _.forEach(data.workouts, function (workout) {
        // Extract workout exercise data...
        workout._workout_exercises = _.filter(data.workout_exercises, {workout: workout.id});

        _.forEach(workout._workout_exercises, function (workout_exercise) {
          // Extract exercise data...
          workout_exercise._exercise = _.findWhere(data.exercises, {id: workout_exercise.exercise});

          // Extract utility data...
          workout_exercise._exercise._utility = _.findWhere(data.utilities, {id: workout_exercise._exercise.utility});

          // Extract mechanics data...
          workout_exercise._exercise._mechanics = _.findWhere(data.mechanics, {id: workout_exercise._exercise.mechanics});

          // Extract force data...
          workout_exercise._exercise._force = _.findWhere(data.forces, {id: workout_exercise._exercise.force});

          // Extract muscle data...
          workout_exercise._exercise._muscle = _.findWhere(data.muscles, {id: workout_exercise._exercise.muscle});
        });
      });

      return data.workouts;
    };
  }

  function workoutService($http, BASE_URL) {
    this.list = function list() {
      return $http.get(BASE_URL + "workouts/");
    };

    this.retrieve = function retrieve(id) {
      return $http.get(BASE_URL + "workouts/" + id + "/");
    };
  }

  angular.module("app")
    .factory("ExerciseFactory", [ExerciseFactory])
    .service("exerciseService", ["$http", "BASE_URL", exerciseService])
    .factory("WorkoutFactory", [WorkoutFactory])
    .service("workoutService", ["$http", "BASE_URL", workoutService]);

})(window, window.angular);