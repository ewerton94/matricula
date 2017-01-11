var matriculaControllers = angular.module('matriculaControllers',[]);

matriculaControllers.controller('CadastroCtrl', ['$scope', '$http', '$location','user','$window','urls','$timeout','situacao',
    function ($scope, $http, $location,user,$window,urls,$timeout,situacao) {
        $scope.situacao=situacao.ativa;
        $scope.dado={};
        $scope.dado.curso='1';
       var get_usuario_deslogado = function () {
        $scope.usuario={};
            
        $http.get(urls.base+'/matricula/get_usuario_deslogado').then(function (data) {
            $timeout(get_usuario_deslogado, 1000);
            
        }, function(data) {
            $window.location.reload();
            
            $window.location.href = urls.base+'/#!situacao/';
            
            
            
            
        })};
            get_usuario_deslogado();
        
        $scope.form = [];
        
        
        $scope.SendData = function () {
            $scope.errors=[];
            if ($scope.dado.senha1 != $scope.dado.senha2){
                $window.scrollTo(0, 0);
                $scope.errors.push("As senhas que você digitou não são iguais!");
            }else {
                
            
            var in_data = { dado: $scope.dado };
            $http.post(urls.base + '/matricula/cadastro', in_data)
                .then(function(out_data) {
                $window.location.href = urls.base + '/';
            }, function(data) {
                $window.scrollTo(0, 0);
                $scope.errors.push("Formulário Inválido");
            //some error
            $scope.errors.push(data.data.detail);
        });
            
        }};

        
    }]);

matriculaControllers.controller('ResetaSenhaCtrl', ['$scope', '$http', '$location','user','$window','urls','$timeout',
    function ($scope, $http, $location,user,$window,urls,$timeout) {
        
       var get_usuario = function () {
        $scope.usuario={};
            
        $http.get(urls.base+'/matricula/get_usuario_logado').then(function (data) {
            $scope.usuario=data.data;
            
            $timeout(get_usuario, 1000);
            
        }, function(data) {
            $window.location.reload();
            $window.location.href = urls.base+'/#!login/';
            
        })};
            get_usuario();
        $scope.SendData = function () {
            $scope.errors=[];
            if ($scope.dado.senha1 != $scope.dado.senha2){
                $window.scrollTo(0, 0);
                $scope.errors.push("As senhas que você digitou não são iguais!");
            }else {
                
            
            var in_data = { new_password: $scope.dado.senha1,current_password: $scope.dado.senha};
            $http.post(urls.base + '/auth/altera_senha/', in_data)
                .then(function(out_data) {
                $window.location.href = urls.base + '/';
            }, function(data) {
                $window.scrollTo(0, 0);
                $scope.errors.push("Formulário Inválido");
            //some error
            $scope.errors.push(data.data.detail);
        });
            
        }};

        
    }]);

matriculaControllers.controller('SairCtrl', ['$scope', '$http', '$location','user','$window','urls',
    function ($scope, $http, $location,user,$window,urls) {
        $http.get(urls.base + '/sair').then(function (data) {
            $window.location.reload();
            $window.location.href = urls.base+'/';
            
        }, function(data) {
            //some error
            $window.location.href = urls.base+'/';
        });
    }]);

matriculaControllers.controller('MatriculaCtrl', ['$scope', '$http', '$location','user','$window','$uibModal','urls','$timeout',
    function ($scope, $http, $location,user,$window,$uibModal,urls,$timeout) {
        var get_usuario = function () {
        $scope.usuario={};
            
        $http.get(urls.base+'/matricula/get_usuario_logado').then(function (data) {
            $scope.usuario=data.data;
            
            $timeout(get_usuario, 1000);
            
        }, function(data) {
            $window.location.reload();
            $window.location.href = urls.base+'/#!login/';
            
        })};
            get_usuario();
        
        $scope.disciplinas=[]
        $scope.disciplinas_escolhidas=[];
        $http.get(urls.base+'/matricula/disciplinas').then(function (data) {
            $scope.disciplinas=data.data;
            
        }, function(data) {
            $scope.errors=[];
        });
        $scope.disciplinas_matriculadas=[];
        $http.get(urls.base+'/matricula/disciplinas_matriculadas').then(function (data) {
            $scope.disciplinas_matriculadas=data.data;
            
        }, function(data) {
            $scope.errors=[];
        });
        
        
        $scope.SendData = function () {
            $scope.errors=[];
            
                
            
            var in_data = { disciplinas: $scope.disciplinas_escolhidas };
            
            $http.post(urls.base+'/matricula/nova', in_data)
                .then(function(out_data) {
                
                $window.location.href = urls.base+'#!situacao';
            }, function(data) {
                $window.scrollTo(0, 0);
                
                $scope.errors.push("Formulário Inválido");
            //some error
            $scope.errors.push(data.data.detail);
        });
                     
        };
        $scope.open = function () {

            var modalInstance =  $uibModal.open({
              templateUrl: urls.base+'/static/partials/modal.html',
              controller: 'ModalInstanceCtrl',
              
            });

            modalInstance.result.then(function () {
               $scope.SendData();
            }, function () {
              $log.info('Modal dismissed at: ' + new Date());
            });
    }}]);


matriculaControllers.controller('LoginCtrl', ['$scope', '$http', '$location','user','$window','situacao','urls','$timeout','$q',
    function ($scope, $http, $location,user,$window,situacao,urls,$timeout,$q) {
        var get_usuario_deslogado = function () {
        $scope.usuario={};
            
        $http.get(urls.base+'/matricula/get_usuario_deslogado').then(function (data) {
            $timeout(get_usuario_deslogado, 1000);
            
        }, function(data) {
            $window.location.reload();
            
            $window.location.href = urls.base+'/#!situacao/';
            
            
            
            
        })};
            
        
        
        
        $scope.SendData = function () {
            $scope.errors=[];
            var in_data = { username: $scope.username,password:$scope.password };
        var login=$http.post(urls.base+'/auth/login', in_data);
        $q.all([login]).then(function(out_data) {
            
            $window.location.href = urls.base+'/#!situacao';
            $window.location.reload();
        }, function(data) {
            $window.scrollTo(0, 0);
            

            $scope.errors.push("Erro!");
        //some error
        $scope.errors.push(data[0].data.detail);
        });
                     
        };
        get_usuario_deslogado();
        
    }]);

matriculaControllers.controller('HomeCtrl', ['$scope', '$http', '$location','user','$window','situacao','urls','$timeout',
    function ($scope, $http, $location,user,$window,situacao,urls,$timeout) {
        $scope.dados = [];
        $scope.situacao=situacao.ativa;
        data1=new Date();
        data2=new Date("January 03, 2017 00:00:00");
        
        if (data1<data2){
            $scope.situacao=false;
        };
        var get_usuario_deslogado = function () {
        $scope.usuario={};
            
        $http.get(urls.base+'/matricula/get_usuario_deslogado').then(function (data) {
            $timeout(get_usuario_deslogado, 1000);
            
        }, function(data) {
            $window.location.reload();
            
            $window.location.href = urls.base+'/#!situacao/';
            
            
            
            
        })};
            get_usuario_deslogado();
        
        
        $scope.logado = user.autenticado;
        if ($scope.logado == 1){
            $window.location.href = urls.base+'#!situacao';
        }
        
    }]);



matriculaControllers.controller('SituacaoCtrl', ['$scope', '$http', '$location','user','$window','$uibModal','urls','ServeHorarios','$timeout',
    function ($scope, $http, $location,user,$window,$uibModal,urls,ServeHorarios,$timeout) {
        
            
        var get_usuario = function () {
        $scope.usuario={};
            $scope.errors=[]
            
        $http.get(urls.base+'/matricula/get_usuario_logado').then(function (data) {
            $scope.usuario=data.data;
            
            $timeout(get_usuario, 1000);
            
        }, function(data) {
            $window.location.reload();
            $scope.errors.push("Você se desconectou");
            
            $window.location.href = urls.base+'/#!login/';
            
        })};
            get_usuario();
            $scope.disciplinas=[];
        
        
        $http.get(urls.base+'/matricula/disciplinas_matriculadas').then(function (data) {
            $scope.disciplinas=data.data;
            
        }, function(data) {
            $scope.errors=[];
        });
        $scope.atividades=[];
            
        var get_horarios = function () {
        $http.get(urls.base+'/matricula/horarios').then(function (data) {
            $scope.atividades=data.data;
            if (!$scope.atividades.length){
                $window.location.reload();
                $window.location.href = urls.base+'/#!login/';
            }
            $timeout(get_horarios, 1000);
            
        }, function(data) {
            $scope.errors=[];
        })};
            
        get_horarios();
        
            
        
        
            
            
            
            
            
        $scope.DeletaDisciplina = function (id) {
            $scope.errors=[];
            
                
            
            var in_data = { disciplinas: $scope.disciplinas_escolhidas };
            
            $http.delete(urls.base+'/matricula/disciplinas_matriculadas/delete/' + id, in_data)
                .then(function(out_data) {
                
                $window.location.href = urls.base+'#!situacao';
            }, function(data) {
                $window.scrollTo(0, 0);
                
                $scope.errors.push("Formulário Inválido");
            //some error
            $scope.errors.push(data.data.detail);
        });
                     
        };
          $scope.botao_deletar = function (id) {

            var modalInstance =  $uibModal.open({
              templateUrl: urls.base+'/static/partials/modal.html',
              controller: 'ModalInstanceCtrl',
              
            });

            modalInstance.result.then(function () {
                $scope.DeletaDisciplina(id);
            }, function () {
              $log.info('Modal dismissed at: ' + new Date());
            });

        }}]);


matriculaControllers.controller('ModalDemoCtrl', function ($scope,  $uibModal, $log,$window,urls) {
    $scope.items = ['item1', 'item2', 'item3'];

  $scope.open = function () {

    var modalInstance =  $uibModal.open({
      templateUrl: urls.base+'/static/partials/modal.html',
      controller: 'ModalInstanceCtrl',
      resolve: {
        items: function () {
          return $scope.items;
        }
      }
    });

    modalInstance.result.then(function (selectedItem) {
      $scope.selected = selectedItem;
    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });
    
}});




matriculaControllers.controller('ModalInstanceCtrl', function ($scope,$uibModalInstance, $window) {

  $scope.ok = function () {
      $uibModalInstance.close();
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
});




