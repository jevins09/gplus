/**
 * Created by jevin on 8/10/2017.
 */

(function () {
    'use strict';

    angular
        .module('thinkster.authentication.controllers')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$location', '$scope', 'Authentication'];

    function LoginController($location, $scope, Authentication) {
        var vm = this;
        vm.login = login;

        activate();

    function login() {
        Authentication.login(vm.email, vm.password);
        }
    }
})();