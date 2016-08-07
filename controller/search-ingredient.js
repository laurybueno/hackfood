var app = angular.module('HackfoodFront', []);

app.controller('SearchIngredients', function($scope){
	$scope.ingredients = function($scope, $http){
		$http.get('').success(function(data){
			return data;
		});
	};
	$scope.pesquisarReceitas = function(){
		$http.get("#").then(function (response) {
			if(response.data.sucesso == true){//se tem receitas
				$scope.receitas = response.data.receitas;
			}
			else{
				$scope.receitas = -1;
			}
  	});
	}

	$scope.hello = 'Hello, world!';

});
