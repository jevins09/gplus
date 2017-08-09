/**
 * Created by jevin on 8/9/2017.
 */
(function () {
    'use strict';

    angular
        .module('thinkster.config')
        .config(config);

    config.$inject = ['$locationProvider'];

    function config($locationProvider) {
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');
    }
})();