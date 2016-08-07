var app = angular.module('HackfoodFront', []);

app.controller('SearchIngredients', function($scope){
	$scope.ingredients = function($scope, $http){
		$http.get('').success(function(data){
			return data;
		});
	};
	
	$scope.ingredient = 'Pão';
	
	$scope.hello = 'Hello, world!';
	
});