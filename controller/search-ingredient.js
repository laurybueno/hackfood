var app = angular.module('HackfoodFront', ['ngResource']).factory('Busca', function($resource) {
  return $resource("http://hackfood.herokuapp.com/api/receitas/busca/:ingredientes/",
                    {'query': { method: 'GET' }});
});

app.config(['$resourceProvider', function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);

app.controller('SearchIngredients', function($scope, Busca){

	$scope.pesquisarReceitas = function(){
    $scope.searching = true;
		Busca.query({ ingredientes: $scope.ingrediente }, function(busca){
			console.log(busca);
      $scope.receitas_encontradas = busca;
      $scope.receitas_falha = false;
		}, function() {
		  $scope.receitas_falha = true;
		});
    $scope.searching = false;
	};

  $scope.escolher_receita = function(id) {
    $scope.receita_escolhida = $scope.receitas_encontradas[id];
  };

});
