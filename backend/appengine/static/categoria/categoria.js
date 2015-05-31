/**
 * Created by Karen on 27/05/2015.
 */
var categoriaModulo=angular.module('categoriaModulo',['rest']);

categoriaModulo.directive('categoriaform', function(){
    return{
        restrict: 'E',
        replace:true,
        templateUrl:'/static/categoria/html/categoria_form.html',
        scope:{
            categoria2: '=',
            nomeLabel: '@',
            imagemLabel: '@',
            saveComplete: '&'
        },
        controller:function($scope,CategoriaApi){
            $scope.salvandoFlag=false;
            $scope.salvar=function(){
                $scope.salvandoFlag=true;
                $scope.errors={};
                var promessa = CategoriaApi.salvar($scope.categoria2);
                promessa.success(function(categoria2){
                    console.log(categoria2);
                    $scope.categoria2.nome="";
                    $scope.categoria2.imagem="";
                    $scope.salvandoFlag=false;
                    if ($scope.saveComplete != undefined){
                        $scope.saveComplete({'categoria': categoria2});
                    }
                })
                promessa.error(function(erros){
                    $scope.errors=errors;
                    console.log(errors);
                    $scope.salvandoFlag=false;
                })
            }
        }
    };
});


categoriaModulo.directive('categorialinha', function(){
    return{
        replace:true,
        templateUrl:'/static/categoria/html/categoria_linha_tabela.html',
        scope:{
            categoria2: '=',
            deleteComplete:'&'
        },
        controller:function($scope,CategoriaApi){
            $scope.ajaxFlag=false;
            $scope.editingFlag=false;
            $scope.categoriaEdicao={};
            $scope.deletar=function(){
                $scope.ajaxFlag=true;
                CategoriaApi.deletar($scope.categoria2.id).success(function(){
                   $scope.deleteComplete({'categoria': $scope.categoria2});
                }).error(function(){
                    console.log('erro');
                });
            }

            $scope.editar=function(){
                $scope.editingFlag=true;
                $scope.categoriaEdicao.id=$scope.categoria2.id;
                $scope.categoriaEdicao.nome=$scope.categoria2.nome;
                $scope.categoriaEdicao.imagem=$scope.categoria2.imagem;
            }

            $scope.cancel=function(){
                $scope.editingFlag=false;
            }

        }
    };
});
