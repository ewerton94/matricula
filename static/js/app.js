var MyApp = angular.module('MyApp');

MyApp.config(['$routeProvider','urls','$locationProvider',
    function($routeProvider,urls,$locationProvider){
        $routeProvider.
            when('/cadastro', {
                templateUrl : urls.cadastro,
                controller : 'CadastroCtrl'
            }).
            when('/', {
                templateUrl : urls.home,
                controller : 'HomeCtrl'
            }).
            when('/sair', {
                templateUrl : urls.home,
                controller : 'SairCtrl'
            }).
            when('/situacao', {
                templateUrl : urls.situacao,
                controller : 'SituacaoCtrl',
            }).
            when('/matricula', {
                templateUrl : urls.matricula,
                controller : 'MatriculaCtrl'
            }).
            when('/login', {
                templateUrl : urls.login,
                controller : 'LoginCtrl'
            }).
            when('/reseta_senha', {
                templateUrl : urls.senha_reseta,
                controller : 'ResetaSenhaCtrl'
            }).
            when('/reajuste', {
                templateUrl : urls.reajuste,
                controller : 'ReajusteCtrl'
            }).
            otherwise({
                redirectTo: '/'
            });
        /*$locationProvider.html5Mode(true);*/
        
    }]);



MyApp.config(['$httpProvider',function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

}]);



MyApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

MyApp.service('ServeHorarios', function() {
    var myData = null;
    return {
        setData: function (data) {
            myData = data;
        },
        doStuff: function () {
            return myData.getSomeData();
        }
    };
});
MyApp.factory('PostLoginServer',function($http,urls) {

    var postData = function(in_data) {

        // Angular $http() and then() both return promises themselves 
        errors=[];

        $http.post('/auth/login', in_data)
            .then(function(out_data) {
            
            return out_data
        }, function(data) {
            $window.scrollTo(0, 0);
            

            errors.push("Erro!");
        //some error
        errors.push(data.data.detail);
            return errors
        })};
    
    return { postData: postData };
    });
function login_function($scope, PostLoginServer,in_data,$window) {
    
    var myDataPromise = PostLoginServer.postData(in_data); 
    myDataPromise.then(function(out_data) {
            
            $window.location.href = urls.base+'/#!situacao';
            $window.location.reload();
        }, function(data) {
            $window.scrollTo(0, 0);
            

            $scope.errors.push("Erro!");
        //some error
        $scope.errors.push(data.data.detail);
        }); 
    console.log("This will get printed before data.name inside then. And I don't want that."); 
 };



    

