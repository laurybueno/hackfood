var app = angular.module('HackfoodFront', ['ngResource']).factory('Busca', function($resource) {
  return $resource("http://localhost:8000/api/receitas/busca/:ingredientes/",
                    {'query': { method: 'GET' }});
});

app.config(['$resourceProvider', function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);

app.controller('SearchIngredients', function($scope, Busca){

	$scope.pesquisarReceitas = function(){
    $scope.searching = true;
		Busca.query({ ingredientes: $scope.ingredient }, function(busca){
			console.log(busca);
		});
    $scope.searching = false;
	};

	$scope.hello = 'Hello, world!';

});
